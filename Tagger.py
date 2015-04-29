#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# 形態素解析処理のラッパーモジュール
#

import sys
import MeCab

import Normalizer

class Tagger:
  def __init__(self):
    self.mode = 'mecabrc -u ./dic/userDic.dic'

    try:
      self.tagger = MeCab.Tagger(self.mode)
    except RuntimeError, e:
      print "RuntimeError:", e;

  def parse(self, str):
    # str 型じゃないと動作がおかしくなるので str 型に変換
    PARSE_TEXT_ENCODING = 'utf-8'
    text = str.encode(PARSE_TEXT_ENCODING)
    node = self.tagger.parseToNode(text)

    words = []
    nouns = []
    verbs = []
    adjs = []

    while node:
      pos = node.feature.split(",")[0]
      # unicode 型に戻す
      word = node.surface.decode("utf-8")
      if pos == "名詞":
        nouns.append(word)
      elif pos == "動詞":
        verbs.append(word)
      elif pos == "形容詞":
        adjs.append(word)
      words.append(word)
      node = node.next

    parsed_words_dict = {
      "all": words[1:-1], 
      "nouns": nouns,
      "verbs": verbs,
      "adjs": adjs
      }

    return parsed_words_dict

  def parseVecInterface(self, str):
    # str 型じゃないと動作がおかしくなるので str 型に変換
    PARSE_TEXT_ENCODING = 'utf-8'
    text = str.encode(PARSE_TEXT_ENCODING)
#    text = Normalizer.normalize(text)

    node = self.tagger.parseToNode(text)

    words = []
    nouns = []
    verbs = []
    adjs = []

    while node:
      pos = node.feature.split(",")[0]
      # unicode 型に戻す
      word = node.surface.decode("utf-8")
      if pos == "名詞":
        nouns.append(word)
      elif pos == "動詞":
        verbs.append(word)
      elif pos == "形容詞":
        adjs.append(word)
      words.append(word)
      node = node.next

    return words 
