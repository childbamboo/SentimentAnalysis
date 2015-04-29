#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# 形態素解析の精度を向上するためのノーマライズモジュール
#
# dictionaries of Mecab
#  /usr/local/Cellar/mecab/0.996/lib/mecab/dic/ipadic
#
# add words to user dictionaries.
#  sudo /usr/local/Cellar/mecab/0.996/libexec/mecab/mecab-dict-index -f utf-8 -t utf-8
#
# /usr/local/Cellar/mecab/0.996/libexec/mecab/mecab-dict-index -d /usr/local/Cellar/mecab/0.996/lib/mecab/dic/ipadic -u userDic.dic -f utf-8 -t utf-8 ./userDic.csv

import unicodecsv
import unicodedata

def unicode_ignore_invalid_char(text):
  if isinstance(text, str):
    return text.decode('utf-8', 'ignore')
  return text

def normalize(text, form='NFKC'):
  assert(form in ('NFC', 'NFKC', 'NFD', 'NFKD'))
  unicode_text = unicode_ignore_invalid_char(text)
  normalized_text = unicodedata.normalize(form, unicode_text)
  return normalized_text
