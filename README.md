# Glade To Code

## 简介
根据 [Glade](https://glade.gnome.org) 文件生成指定语言的 [GTK](https://www.gtk.org) 代码的工具

## 使用说明
python3 glade-to-code.py -l [语言类型] -i [输入 Glade 文件路径] -o [输出源代码文件路径]

## 提示
如果 Glade 文件中 GTK 组件的 ID 为空， 则不会生成对应的代码。

## 参数说明
    -l,  --lang=         语言类型，可选项："c++" 
    -i,  --in-file=      输入的 Glade 文件路径 
    -o,  --out-file=     输出的源代码文件路径 
