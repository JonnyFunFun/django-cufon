#!/usr/bin/env python

import os, sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'test_django_cufon'
parent = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))))

sys.path.insert(0, parent)

from django.test.simple import DjangoTestSuiteRunner

def runtests():
    DjangoTestSuiteRunner(failfast=False).run_tests([
        'cufon.TestHeadTags',
        'cufon.TestCufonTags',
    ])

if __name__ == '__main__':
    runtests()