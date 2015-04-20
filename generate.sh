#!/bin/bash

ronn --roff ronn/*.ronn

if ! [ -e ~/.local/man/zh_CN/man1 ]; then
    mkdir -p ~/.local/man/zh_CN/man1;
fi

mv -u ronn/*.1 ~/.local/man/zh_CN/man1/
