## GNU coreutils手册页翻译

master分支放的是`GNU coreutils 8.23`手册页的翻译。

### 任务分配
表格中没有加`特效`的命令表示已经翻译校对过一遍了。

只要一个类别中所有的命令都翻译校对过一遍，我们就把它提交到`manpages-zh`中。

功能 | 命令| 提交
-----|-----|------|------|-----
输出整个文件 | cat tac `nl` `od` base64 |
格式化文件内容 | `fmt` `pr` `fold` |
输出文件一部分 | head `tail` `split` `csplite` |
文件摘要 | wc sum `cksum` `md5sum` `sha1sum` `sha224sum` `sha256sum` `sha384sum` `sha512sum` |
已排序文件上的操作 | `sort` `shuf` uniq `comm` `ptx` `tso` |
对域的操作 | `cut` paste `join` |
对字符的操作 | `tr` expand unexpand |
列目录 | `ls` `dir` `vdir` `dircolors` |
基本操作 | `cp` `dd` `install` `mv` `rm` `shred` |
特殊文件类型 | `mkdir` rmdir `unlink` `mkfifo` `mknod` `ln` link `readlink` |
改变文件属性 | `chgrp` `chmod` `chown` `touch` |
磁盘使用情况 | `df` `du` `stat` sync `truncate` |
打印文本 | echo `printf` yes |
条件 | false true test expr |
重定向 | tee |
文件名操作 | dirname basename `pathchk` `mktemp` `realpath` |
工作环境 | pwd `stty` printenv tty |
用户信息 | `id` logname whoami `groups` users who |
系统环境 | `date` arch `nproc` uname hostid|
SELinux环境 | `chcon` `runcon` |
修改环境 | `chroot` env nice nohup `stdbuf` `timeout` |
暂停 | sleep |
数值操作 | factor `seq` | | | 


### 翻译和维护
请先安装python3和po4a。

只要翻译`po`目录下面的文件就可以了。推荐使用专门的软件，比如`lokalize`。翻译好之后，请务必预览你翻译好的命令。
使用`./preview command`就可以预览。

**注意**：
1. 如果coreutils.po和manpages-zh已经有相应的翻译，请沿用已有的翻译。当然，可以在原有的基础上改进。
2. 对于不了解的内容，请**不要**翻译。对于coreutils，手册页的描述其实非常简略，模棱两可的地方一定弄明白（看info或者源代码）再翻译。否则请**不要**翻译。

翻译规范参考[wiki](https://github.com/man-pages-zh/wiki/wiki/%E7%BF%BB%E8%AF%91%E8%A7%84%E8%8C%83)。

### 维护
请先安装python3、[man2html](https://github.com/man-pages-zh/man2html)和po4a。

运行`./generate`可以：

1. 根据手册页的更新，更新pot和po
2. 根据po文件，生成翻译
3. 生成相应的html文件
