#!/usr/bin/env python
# coding=utf-8

import sys

import nzbToMedia

section = 'HeadPhones'
result = nzbToMedia.main(sys.argv, section)
sys.exit(result)
