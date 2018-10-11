#!/usr/bin/env python3
"""Problem specification and solver"""
from scraper import Scraper
from breadth_first_search import breadth_first_search
# from problem import Problem
import argparse
import time


class Problem(object):
    """Specification of our problem for generalised breadth first search."""

    def __init__(self, start_url, goal_url):
        """Saving two urls to link."""
        super(Problem, self).__init__()
        self.start_url = start_url
        self.goal_url = goal_url
        self.scraper = Scraper()
        self.base_url = 'https://fr.wikipedia.org'

    def get_root(self, side='left'):
        """Return the root node aka starting url."""
        if side == 'left':
            return self.start_url
        if side == 'right':
            return self.stop_url

    def is_goal(self, url):
        """Return true if the given url is same as goal_url."""
        return url == self.goal_url

    def get_successors(self, subtree_root):
        """Return list of successors for given address."""
        return self.scraper.scrap(subtree_root)

    def solve(self):
        """Return path between given links."""
        return breadth_first_search(self) + [self.goal_url]

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='beaconSystem'
                                     'plotting and Saving')
    parser.add_argument('url1', type=str, help='first url')
    parser.add_argument('url2', type=str, help='second url')
    args = parser.parse_args()
    pb = Problem(args.url1, args.url2)
    print('Searching links between {} and {}.'.format(args.url1, args.url2))
    start = time.time()
    url_list = pb.solve()
    end = time.time()
    print(url_list)
    print(len(url_list))
    print(end - start)
