## GNU coreutils手册页翻译

使用po方案翻译。master分支放的是`GNU coreutils 8.23`手册页的翻译。

### 翻译
只要翻译`po`目录下面的文件就可以了。推荐使用专门的软件，比如`poedit`。在`KDE`平台下可以使用`Lokalize`。

### 维护
请先安装python3，pandoc，po4a和[改进过的man2html](https://github.com/man-pages-zh/man2html)。

运行`python3 generate.py`可以：
1. 根据更新过的手册页更新po文件
2. 根据po文件，生成翻译好的md文件，放在`doc/zh_CN`下面

注：只有po文件中80%以上已翻译，才能生成翻译好的md文件。
