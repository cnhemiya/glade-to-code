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
GTC_FILE_HEADER = "GLADE TO CODE AUTO GENERATE\n"


class CodeObject:
    """
    转代码基类
    """

    def __init__(self):
        """
        初始化 CodeObject 类
        __gladeTxt: Glade 文件内容
        __parse: GladeParse 类
        """
        self.__gladeTxt = ""
        self.__parse = gtcc.GladeParse()

    def __readFile(self, file):
        """
        读取 Glade 文件内容

        Args:
            file (str): Glade 文件路径

        Raises:
            Exception: 文件不存在，抛出输入的文件路径
        """
        if not os.path.exists(file):
            raise Exception("文件不存在：%s" % file)
        else:
            f = open(file, "r", encoding="utf-8")
            self.__gladeTxt = f.read()
            f.close()

    def __writeFile(self, file, code_txt):
        """
        写入生成的代码

        Args:
            file (str): 代码文件路径
            code_txt (str): 生成的代码
        """
        f = open(file, "w", encoding="utf-8")
        f.write(code_txt)
        f.close()

    def read(self, file):
        try:
            self.__readFile(file)
            self.__parse(self.__gladeTxt)
            return True
        except Exception as e:
            print(e)
            return False

    def wirte(self, file):
        try:
            code_txt = self.__makeCode(file)
            self.__writeFile(file, code_txt)
            self.__printLog()
            return True
        except Exception as e:
            print(e)
            return False

    def __makeCode(self, file_name):
        code_txt = self._srcFileBegin(file_name)
        code_txt += self._srcModule()
        code_txt += self._srcCodeBegin()
        code_txt += self._srcCodeMain()
        code_txt += self._srcCodeEnd()
        code_txt += self._srcFileEnd(file_name)
        return code_txt

    def __printLog(self):
        print("__printLog no!!!")

    @property
    def _gladeTxt(self):
        return self.__gladeTxt

    @property
    def _parse(self):
        return self.__parse

    def __funcNotAchieved(self, func_name):
        """
        子类函数没有实现，加上子类名称和函数名称
        """
        return "子类函数没有实现: " + self.__class__.__name__ + "." + func_name

    def _srcFileBegin(self, file_name):
        """
        生成代码，文件开始
        """
        raise Exception(self.__funcNotAchieved("_srcFileBegin"))

    def _srcModule(self):
        """
        生成代码，模块
        """
        raise Exception(self.__funcNotAchieved("_srcModule"))

    def _srcCodeBegin(self):
        """
        生成代码，代码开始
        """
        raise Exception(self.__funcNotAchieved("_srcCodeBegin"))

    def _srcCodeMain(self):
        """
        生成代码，主代码
        """
        raise Exception(self.__funcNotAchieved("_srcCodeMain"))

    def _srcCodeEnd(self):
        """
        生成代码，代码结束
        """
        raise Exception(self.__funcNotAchieved("_srcCodeEnd"))

    def _srcFileEnd(self, file_name):
        """
        生成代码，文件结束
        """
        raise Exception(self.__funcNotAchieved("_srcFileEnd"))
