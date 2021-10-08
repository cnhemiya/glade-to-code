#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
LICENSE: MulanPSL2
AUTHOR:  cnhemiya@qq.com
DATE:    2021-10-08 17:25

提取 gtk+.xml 中的 glade-widget-class-ref
"""

import sys
import xml.etree.ElementTree as et


def main(xml_file):
    tree = et.ElementTree(file=xml_file)
    for elem in tree.iter():
        if elem.tag == "glade-widget-class-ref":
            print(elem.attrib["name"])


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
