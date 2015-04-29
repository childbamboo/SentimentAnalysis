#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# sudo pip install gensim
# then, I got error message about nympy. so recompile it by following command.
# easy_install --upgrade numpy
#

import unicodecsv
import sys
import Tagger
import Normalizer

import numpy
import scipy
import gensim
from gensim import corpora
import math

import pickle
import os
from sklearn.feature_extraction.text import TfidfVectorizer

def is_bigger_than_min_tfidf(term, terms, tfidfs):
  '''
  [term for term in terms if is_bigger_than_min_tfidf(term, terms, tfidfs)]で使う
  list化した、語たちのtfidfの値のなかから、順番に当てる関数。
  tfidfの値がMIN_TFIDFよりも大きければTrueを返す
  '''
#  if tfidfs[terms.index(term)] > constants.MIN_TFIDF:
#    return True
#  return False

def main():

  # check command options
  argvs = sys.argv
  opt = ""
  if 1 < len(argvs):
    opt = argvs[1]

  # load dictionary
  dictionary = corpora.Dictionary.load_from_text('./dic/df.tsv')

  # initialize file reader
  spamReader = unicodecsv.reader(open('./comments/comments.tsv', 'rb'), delimiter='\t', encoding='utf-8')

  tagger = Tagger.Tagger()
  vectorizer = TfidfVectorizer(analyzer=tagger.parseVecInterface, min_df=1, max_df=50)

  corpus = [row[0] for row in spamReader]
  x = vectorizer.fit_transform(corpus)

  terms = vectorizer.get_feature_names()
  tfidfs = x.toarray()[0]
  for term in terms:
    print "+++++++++++++++"
    print term
    print terms.index(term)
    print tfidfs[terms.index(term)]

  print('合計%i種類の単語がページから見つかりました。' % (len(terms)))

  return

if __name__ == "__main__":
  main()
