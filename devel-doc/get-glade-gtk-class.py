#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
LICENSE: MulanPSL2
AUTHOR:  cnhemiya@qq.com
DATE:    2021-10-08 17:25

ζε gtk+.xml δΈ­η glade-widget-class-ref
"""

import sys
import xml.etree.ElementTree as et


def main(xml_file):
    class_names = []
    tree = et.ElementTree(file=xml_file)
    for elem in tree.iter():
        if elem.tag == "glade-widget-class-ref":
            class_names.append(elem.attrib["name"])
    class_names.sort()
    for i in class_names:
        print(i)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print(__doc__)
