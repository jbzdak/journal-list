#!/usr/bin/env python

# -*- coding: utf-8 -*-
__author__ = 'jb'
import sys
import subprocess

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--pip-path", default="pip")

opts = parser.parse_args()

modules = (
    ('Django', 'django'),
    ('psycopg2', 'psycopg2'),
    ('south', 'south'),
    ('python-stdnum', 'stdnum'),
#    ('docutils', 'docutils')
    #    ('python-openid', 'bar'),
    )

#try:
#    subprocess.check_call(['easy_install', '--help'])
#except subprocess.CalledProcessError:
#    subprocess.check_call(['apt-get','install', 'python-setuptools'])

for mod in modules:
    print mod
    try:
        __import__(mod[1])
        print 'already installed'
    except ImportError:
        subprocess.check_call([opts.pip_path, 'install', mod[0]])




