#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# MecabにUser Dictionaryを追加する。
#  不動産業界固有の単語を区切り過ぎないようにするために独自辞書を追加する。
#
# default dictionaries of Mecab
#  /usr/local/Cellar/mecab/0.996/lib/mecab/dic/ipadic
#
# command to add words to user dictionaries.
#  sudo /usr/local/Cellar/mecab/0.996/libexec/mecab/mecab-dict-index -f utf-8 -t utf-8
#
# /usr/local/Cellar/mecab/0.996/libexec/mecab/mecab-dict-index -d /usr/local/Cellar/mecab/0.996/lib/mecab/dic/ipadic -u userDic.dic -f utf-8 -t utf-8 ./userDic.csv

/usr/local/Cellar/mecab/0.996/libexec/mecab/mecab-dict-index -d /usr/local/Cellar/mecab/0.996/lib/mecab/dic/ipadic -u ./dic/userDic.dic -f utf-8 -t utf-8 ./dic/userDic.csv
