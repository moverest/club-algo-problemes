#/usr/bin/env python3

MAX_WORKERS = 10
TIMEOUT = 10

import sys
import requests
from lxml import html
import collections

import time

import atexit
import concurrent
from concurrent.futures import ThreadPoolExecutor
from requests_futures.sessions import FuturesSession


def get_article_future(session, article):
    return session.get(
        "https://fr.wikipedia.org/wiki/%s" % article, timeout=TIMEOUT)


def get_article_links(article_future):
    root = html.fromstring(article_future.result().text)
    links = root.xpath('//div[@class="mw-parser-output"]/p//a')
    return map(
        lambda l: l.lstrip('/wiki/'),
        filter(lambda l: l.startswith('/wiki/'),
               map(lambda l: l.attrib.get('href', ''), links)))


ArticleVisit = collections.namedtuple("VisitedArticle",
                                      ["src", "name", "future", "depth"])


def find_shorted_path(from_article, dest_article):
    executor = ThreadPoolExecutor(max_workers=MAX_WORKERS)
    atexit.unregister(concurrent.futures.thread._python_exit)
    executor.shutdown = lambda: None
    with FuturesSession(executor=executor) as session:
        def make_article_visit(from_article, article):
            return ArticleVisit(
                src=from_article,
                name=article,
                future=get_article_future(session, article),
                depth=(0 if from_article is None else from_article.depth + 1))

        start_time = time.time()
        found = set()
        to_visit = [make_article_visit(None, from_article)]
        count = 0

        def visit_article(article):
            nonlocal to_visit
            nonlocal count

            def print_progress():
                sys.stderr.write(
                    "\r\x1b[K[\x1b[31m{depth}\x1b[0m:\x1b[32m{count}\x1b[0m(\x1b[34m{buffer_size}\x1b[0m)\x1b[0m {speed:.0f} articles/s] \x1b[33m{article:.40s}\x1b[0m"
                    .format(
                        depth=article.depth,
                        count=count,
                        buffer_size=len(to_visit),
                        article=article.name,
                        speed=count / (time.time() - start_time)))

            count += 1
            print_progress()

            links = get_article_links(article.future)
            for link in links:
                if link in found:
                    continue

                article_visit = make_article_visit(article, link)
                if link == dest_article:
                    return article_visit

                found.add(link)
                to_visit.append(article_visit)

        def get_path(article):
            def browse_article(article):
                while not article.src is None:
                    yield article.name
                    article = article.src

                yield article.name

            return reversed(list(browse_article(article)))

        def clear_current_line():
            sys.stderr.write('\r\x1b[K')

        while len(to_visit) > 0:
            article_to_visit = to_visit[0]
            del to_visit[0]

            visit_result = visit_article(article_to_visit)
            if not visit_result is None:
                clear_current_line()
                duration = time.time() - start_time
                print(
                    "\x1b[33m{count} articles fetched in {duration:.2f}s ({speed:.2f} articles/s) with a depth of {depth}.\x1b[0m"
                    .format(
                        count=count,
                        duration=duration,
                        speed=count / duration,
                        depth=visit_result.depth),
                    file=sys.stderr)

                return get_path(visit_result)



if __name__ == '__main__':
    if len(sys.argv) < 3:
        print(
            "Usage: %s <start article> <end article>" % sys.argv[0],
            file=sys.stderr)
        exit(1)

    article, article_to_found = sys.argv[1:3]
    for article in find_shorted_path(article, article_to_found):
        print(article)
