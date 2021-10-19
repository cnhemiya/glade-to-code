#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
LICENSE: MulanPSL2
AUTHOR:  cnhemiya@qq.com
DATE:    2021-10-08 20:01

提取 gxxmm-doc.txt 中的 class
"""

import sys
import xml.etree.ElementTree as et


def main(txt_file):
    class_names = []
    fin = open(txt_file, "r+")
    lines = fin.readlines()
    for i in lines:
        if i.find("class  	") > -1:
            s = i.split("\n")[0]
            class_names.append(s[8:])
    class_names.sort()
    for i in class_names:
        print(i)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print(__doc__)
