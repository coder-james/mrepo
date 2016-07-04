#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
MRepo

Usage:
  mrepo ( init | i )
  mrepo ( download | d ) [-d <directory>]
  mrepo ( generate | g )
  mrepo -H | --help
  mrepo -V | --version

Subcommands:
  init | i               Init Local Repository
  download | d           Download RPM Packages by "yum"
  generate | g           Generate .repo File

Options:
  -H, --help          Help information
  -V, --version       Show version
  -d <directory>      Specify the directory
"""

import os
from docopt import docopt
from mrepo import __version__

def main(args=None):
    if not args:
        args = docopt(__doc__, version="mrepo {0}".format(__version__))
    if args["init"] or args["i"]:
        pass
    elif args["download"] or args["d"]:
        if args["-d"] != None:
            pass
        else:
            print "you need designated a directory for download rpm packages"
    elif args["generate"] or args["g"]:
        pass
    else:
        pass


if __name__ == '__main__':
    main()