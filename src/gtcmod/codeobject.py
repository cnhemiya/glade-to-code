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
        __parse: GladeParse 类
        """
        self.__parse = gtcc.GladeParse()

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
                txt = f.read()
                f.close()
                self.__parse(self.__readFile(file_path))
                return True
        except Exception as e:
            print(e)
            return False

    def wirte(self, file_path):
        """
        写入生成的代码

        Args:
            file_path (str): 代码文件路径
        """
        try:
            f = open(file_path, "w", encoding="utf-8")
            f.write(self.__makeCode(file_path))
            f.close()
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
