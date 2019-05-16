#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Steps before creating templates"""

from __future__ import print_function
import os
from time import gmtime, strftime


def main():
    """Main function"""
    if not os.path.exists(".backups/"):
        os.mkdir(".backups/")

    backup_dir = ".backups/" + strftime("%Y.%m.%d-%H.%M.%S", gmtime())
    backup_cmd = "rsync -avz --exclude='*.backups/*' --exclude='*.backups/' --exclude='.git/' . " + backup_dir
    os.mkdir(backup_dir)

    os.system(backup_cmd)


if __name__ == "__main__":
    main()
