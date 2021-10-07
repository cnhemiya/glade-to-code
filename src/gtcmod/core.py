# -*- coding: utf-8 -*-
"""
LICENSE: MulanPSL2
AUTHOR:  cnhemiya@qq.com
DATE:    2021-10-07 12:58
"""

def replaceStringByDict(string_, strDict):
    """根据 strDict 提供的字符串字典替换 string_ 文本，
    strDict={ "str_old1":"str_new1", "str_old2":"str_new2"}"""
    for key in strDict:
        string_ = string_.replace(key, strDict[key])
    return string_
