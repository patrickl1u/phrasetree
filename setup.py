#!/usr/bin/env python
#
# Setup script for the Natural Language Toolkit
#
# Copyright (C) 2001-2020 NLTK Project
# Author: Steven Bird <stevenbird1@gmail.com>
#         Edward Loper <edloper@gmail.com>
#         Ewan Klein <ewan@inf.ed.ac.uk>
# URL: <http://nltk.org/>
# For license information, see LICENSE.TXT

# Work around mbcs bug in distutils.
# http://bugs.python.org/issue10945

# setuptools
from setuptools import setup, find_packages

_project_homepage = "http://nltk.org/"

setup(
    name="phrasetree",
    description="Phrase Tree from Natural Language Toolkit",
    version='0.0.9',
    url=_project_homepage,
    project_urls={
        "Documentation": _project_homepage,
    },
    long_description="""\
The phrase tree module from Natural Language Toolkit (NLTK)
Modifications:
- Keep phrase tree only
- Removed PCFG
- Dropped py2 support
""",
    license="Apache License, Version 2.0",
    keywords=[
        "NLP",
        "CL",
        "natural language processing",
        "computational linguistics",
        "parsing",
        "tagging",
        "tokenizing",
        "syntax",
        "linguistics",
        "language",
        "natural language",
        "text analytics",
    ],
    # maintainer="Steven Bird",
    # maintainer_email="stevenbird1@gmail.com",
    author="Steven Bird",
    author_email="stevenbird1@gmail.com",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Human Machine Interfaces",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Text Processing",
        "Topic :: Text Processing :: Filters",
        "Topic :: Text Processing :: General",
        "Topic :: Text Processing :: Indexing",
        "Topic :: Text Processing :: Linguistic",
    ],
    packages=find_packages(),
    zip_safe=False,  # since normal files will be present too?
)
