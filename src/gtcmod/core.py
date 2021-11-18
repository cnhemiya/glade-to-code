# -*- coding: utf-8 -*-
"""
LICENSE: MulanPSL2
AUTHOR:  cnhemiya@qq.com
DATE:    2021-10-07 12:58
"""

import xml.etree.ElementTree as etree

NODE_TAG = "object"
ATTRIB_CLASS = "class"
ATTRIB_ID = "id"

def replaceStringByDict(string_, strDict):
    """
    根据 strDict 提供的字符串字典替换 string_ 文本，
    strDict={ "str_old1":"str_new1", "str_old2":"str_new2"}
    """
    for key in strDict:
        string_ = string_.replace(key, strDict[key])
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
        for node in tree.iter(tag = NODE_TAG):
            node_attrib = {ATTRIB_CLASS: "", ATTRIB_ID: ""}
            node_attrib[ATTRIB_CLASS] = node.attrib[ATTRIB_CLASS]
            if ATTRIB_ID in node.attrib:
                node_attrib[ATTRIB_ID] = node.attrib[ATTRIB_ID]
                self.__classAndId.append(node_attrib)
            else:
                node_attrib[ATTRIB_ID] = ""
                self.__classNoId = node.attrib[ATTRIB_CLASS]
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





