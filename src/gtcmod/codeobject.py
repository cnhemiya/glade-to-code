# -*- coding: utf-8 -*-
"""
LICENSE: MulanPSL2
AUTHOR:  cnhemiya@qq.com
DATE:    2021-11-13 15:35
"""

import os


MAP_GLADE_IDX = "glade"
MAP_CLASS_IDX = "class"
MAP_MOD_IDX = "mod"


class CodeObject:
    """
    转代码基类
    """    
    def __init__(self):
        """
        glade 文件内容
        """
        self.__gladeTxt = ""

    def _readFile(self, file):
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

    def _writeFile(self, file, code_txt):
        """
        写入生成的代码

        Args:
            file (str): 代码文件路径
            code_txt (str): 生成的代码
        """        
        f = open(file, "w", encoding="utf-8")
        f.write(code_txt)
        f.close()

    @property
    def _gladeTxt(self):
        return self.__gladeTxt
