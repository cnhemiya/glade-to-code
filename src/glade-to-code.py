#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
LICENSE: MulanPSL2
AUTHOR:  cnhemiya@qq.com
DATE:    2021-11-29 22:39
文档说明： 主程序
"""

import sys
import getopt
import gtcmod.tocpp

VERSION = "V0.1.0"

SUPPOT_LANG = ["c++"]

HELP_DOC = """\
Glade To Code %s

简介：
    Glade To Code 根据 Glade 文件生成指定语言的 GTK 代码的工具。

使用说明：
    python3 glade-to-code.py -l [语言类型] -i [输入 Glade 文件路径] -o [输出源代码文件路径]

提示：
    如果 Glade 文件中 GTK 组件的 ID 为空， 则不会生成对应的代码。

参数说明：
    -l,  --lang=         语言类型，可选项："c++"
    -i,  --in-file=      输入的 Glade 文件路径
    -o,  --out-file=     输出的源代码文件路径\
""" % VERSION

def toCode(lang, in_file, out_file):
    """
    将 glade 文件转换为指定语言的代码文件
    Args:
        lang (str): 语言类型，可选值："c++"
        in_file (str): 输入 Glade 文件路径
        out_file (str): 输出代码文件路径
    """
    try:
        to_code = None
        lang = lang.lower()
        if lang == "c++":
            to_code = gtcmod.tocpp.ToCpp()
        if to_code is not None:
            to_code.read(in_file)
            to_code.write(out_file)
    except Exception as e:
        print(e)


def argsParse():
    """
    解析命令行参数
    """
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hl:i:o:", [
                                   "help", "lang=", "in-file=", "out-file="])
        arg_lang = ""
        arg_in_file = ""
        arg_out_file = ""
        for opt, arg in opts:
            if opt in ("-h", "--help"):
                print(HELP_DOC)
                sys.exit()
            elif opt in ("-l", "--lang"):
                arg_lang = arg
            elif opt in ("-i", "--in-file"):
                arg_in_file = arg
            elif opt in ("-o", "--out-file"):
                arg_out_file = arg
            else:
                print(HELP_DOC)
                sys.exit()
        if arg_lang in SUPPOT_LANG and arg_in_file != "" and arg_out_file != "":
            toCode(arg_lang, arg_in_file, arg_out_file)
        else:
            print(HELP_DOC)
    except getopt.GetoptError as err:
        print(HELP_DOC)
        sys.exit(2)


def main():
    if len(sys.argv) > 3:
        argsParse()
    else:
        print(HELP_DOC)


if __name__ == '__main__':
    main()
