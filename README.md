## GNU coreutils手册页翻译

master分支放的是`GNU coreutils 8.23`手册页的翻译。

### 任务分配
`coreutils`里面的命令是有分类的，建议按分类认领翻译。认领请在issue中告知。

分类                      | 翻译   | 一校  | 状态 
--------------------------|--------|-------|------
`cat` `tac` nl od base64  | sadhen |       |
fmt pr fold               |        |       |

### 翻译
只要翻译`po`目录下面的文件就可以了。推荐使用专门的软件，比如`poedit`。在`KDE`平台下可以使用`Lokalize`。

翻译规范参考[wiki](https://github.com/man-pages-zh/wiki/wiki/%E7%BF%BB%E8%AF%91%E8%A7%84%E8%8C%83)。

### 维护
请先安装python3和po4a。

运行`python3 generate.py`可以：

1. 根据手册页的更新，更新pot和po
2. 根据po文件，生成翻译
