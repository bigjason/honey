#!/usr/bin/env python

import sys
from os import path

from django.conf import settings

TEST_ROOT = path.dirname(__name__)

if not settings.configured:
    settings.configure(
        DATABASE_ENGINE='sqlite3',
        INSTALLED_APPS=[
            'honey.tests.testapp',
            'honey'
        ],
        TEMPLATE_LOADERS=(
            'honey.MakoFileSystemLoader',
            'honey.MakoAppDirLoader',
        ),
        TEMPLATE_DIRS = (
            path.join(TEST_ROOT, 'templates'),
        )
    )

from django.test.simple import run_tests

def _run_tests(*test_args):
    if not test_args:
        test_args = ['honey']
    parent = path.join(path.dirname(path.abspath(__file__)), "../../")
    sys.path.insert(0, parent)
    failures = run_tests(test_args, verbosity=1, interactive=True)
    sys.exit(failures)

if __name__ == '__main__':
    _run_tests(*sys.argv[1:])
