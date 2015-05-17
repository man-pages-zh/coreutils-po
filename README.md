## GNU coreutils手册页翻译

master分支放的是`GNU coreutils 8.23`手册页的翻译。

### 任务分配
`coreutils`里面的命令是有分类的，建议按分类认领翻译。认领请在issue中告知。

功能 | 命令| 翻译 | 一校 | 状态
-----|-----|------|------|-----
输出整个文件 | cat tac `nl` `od` base64 | sadhen | |
格式化文件内容 | `fmt` `pr` `fold` | | |
输出文件一部分 | head `tail` `split` `csplite` | | |
文件摘要 | `wc` `sum` `cksum` `md5sum` `sha1sum` | | |
已排序文件上的操作 | `sort` `shuf` `uniq` `comm` `ptx` `tso` | | |
对域的操作 | `cut` `paste` `join` | | |
对字符的操作 | `tr` `expand` `unexpand` | | |
列目录 | `ls` `dir` `vdir` `dircolors` | | |
基本操作 | `cp` `dd` `install` `mv` `rm` `shred` | | |
打印文本 | `echo` `printf` yes | | |
条件 | false true `test` `expr` | sadhen | |

### 翻译
只要翻译`po`目录下面的文件就可以了。推荐使用专门的软件，比如`poedit`。在`KDE`平台下可以使用`Lokalize`。

翻译规范参考[wiki](https://github.com/man-pages-zh/wiki/wiki/%E7%BF%BB%E8%AF%91%E8%A7%84%E8%8C%83)。

### 维护
请先安装python3和po4a。

运行`python3 generate.py`可以：

1. 根据手册页的更新，更新pot和po
2. 根据po文件，生成翻译
