# -*- coding: utf-8 -*-
"""
LICENSE: MulanPSL2
AUTHOR:  cnhemiya@qq.com
DATE:    2021-10-07 12:58
"""

import xml.etree.ElementTree as etree

XML_NODE_TAG = "object"
XML_ATTRIB_CLASS = "class"
XML_ATTRIB_ID = "id"

def replaceStringByDict(string_, str_dict):
    """
    根据 strDict 提供的字符串字典替换 string_ 文本，
    strDict={ "str_old1":"str_new1", "str_old2":"str_new2"}
    """
    for key in str_dict:
        string_ = string_.replace(key, str_dict[key])
    return string_


class GladeParse:
    """
    GladeParse 类，用于解析 glade 文件
    """

    def __init__(self):
        """
        初始化 GladeParse 类

        __nodeAttrib: 节点属性列表, {"class": "", "id": ""}
        """
        self.__nodeAttrib = []
        self.__classAndId = []
        self.__classNoId = []

    def parse(self, file_path):
        self.__parseNodeAttrib(file_path)

    def __parseNodeAttrib(self, file_path):
        tree = etree.ElementTree(file=file_path)
        for node in tree.iter(tag = XML_NODE_TAG):
            node_attrib = {XML_ATTRIB_CLASS: "", XML_ATTRIB_ID: ""}
            node_attrib[XML_ATTRIB_CLASS] = node.attrib[XML_ATTRIB_CLASS]
            if XML_ATTRIB_ID in node.attrib:
                node_attrib[XML_ATTRIB_ID] = node.attrib[XML_ATTRIB_ID]
                self.__classAndId.append(node_attrib)
            else:
                node_attrib[XML_ATTRIB_ID] = ""
                self.__classNoId = node.attrib[XML_ATTRIB_CLASS]
            self.__nodeAttrib.append(node_attrib)

    @property
    def nodeAttrib(self):
        return self.__nodeAttrib

    @property
    def classAndId(self):
        return self.__classAndId

    @property
    def classNoId(self):
        return self.__classNoId





