# -*- coding: utf-8 -*-
"""
LICENSE: MulanPSL2
AUTHOR:  cnhemiya@qq.com
DATE:    2021-11-13 15:35
"""

import os
import gtcmod.core as gtcc


MAP_GLADE_IDX = "glade"
MAP_CLASS_IDX = "class"
MAP_MOD_IDX = "mod"
GTC_FILE_HEADER = "GLADE TO CODE AUTO GENERATE"


class CodeObject:
    """
    转代码基类
    """

    def __init__(self):
        """
        初始化 CodeObject 类
        __parse: GladeParse 类
        """
        self.__gladeTxt = ""
        self.__gladeBaseName = ""
        self.__gladeParse = gtcc.GladeParse()

    def read(self, file_path):
        """
        读取 Glade 文件内容

        Args:
            file_path (str): Glade 文件路径
        """
        try:
            if not os.path.exists(file_path):
                print("文件不存在：%s" % file_path)
                return False
            else:
                f = open(file_path, "r", encoding="utf-8")
                self.__gladeTxt = f.read()
                f.close()
                self.__gladeParse.parse(file_path)
                basename = os.path.basename(file_path)
                self.__gladeBaseName = basename.split(".glade")[0]
                return True
        except Exception as e:
            print(e)
            return False

    def write(self, file_path):
        """
        写入生成的代码

        Args:
            file_path (str): 代码文件路径
        """
        try:
            f = open(file_path, "w", encoding="utf-8")
            f.write(self.makeCode())
            f.close()
            self.__printLog()
            return True
        except Exception as e:
            print(e)
            return False

    def makeCode(self):
        """
        生成代码，公有权限方便调试

        Returns:
            str: 生成的代码
        """
        raise Exception(self.__funcNotAchieved("makeCode"))

    def __printLog(self):
        print("无 ID class 列表")
        for i in self._gladeParse.classNoId:
            print(i)

    def __funcNotAchieved(self, func_name):
        """
        子类函数没有实现，加上子类名称和函数名称
        """
        return "子类函数没有实现: " + self.__class__.__name__ + "." + func_name

    @property
    def _gladeTxt(self):
        """
        获取 Glade 文件内容
        """
        return self.__gladeTxt

    @property
    def _gladeBaseName(self):
        """
        获取 Glade 文件名
        """
        return self.__gladeBaseName

    @property
    def _gladeParse(self):
        """
        获取 GladeParse 类
        """
        return self.__gladeParse

    def _gladeMapGtk(self, glade, map_list):
        """
        生成代码，Glade 文件中的 Gtk 对象
        """
        result = []
        for i in map_list:
            if i[MAP_GLADE_IDX] == glade:
                result.append(i[MAP_GLADE_IDX])
                result.append(i[MAP_CLASS_IDX])
                result.append(i[MAP_MOD_IDX])
                break
        return result

    def _modListCode(self, key_word, glade_map_gtk):
        """
        生成代码，模块列表
        """
        code = ""
        mod_list = []
        for i in self._gladeParse.classAndId:
            glade_map = self._gladeMapGtk(
                i[gtcc.XML_ATTRIB_CLASS], glade_map_gtk)
            if glade_map[2] not in mod_list:
                mod_list.append(glade_map[2])
        for i in mod_list:
            code += key_word + i + "\n"
        code += "\n"
        return code
