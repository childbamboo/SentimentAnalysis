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

  i = 1
  tagger = Tagger.Tagger()

  # gensim
  docWords = []

  # read each line
  for row in spamReader:

    # normalize & tagging
    sample_u = Normalizer.normalize(row[0])
    words_dict = tagger.parse(sample_u)

    vec = dictionary.doc2bow(words_dict['all'])
    corpora.SvmLightCorpus.serialize
#    print vec

    norm = 0
    for feature in vec:
      a, b = feature
      norm += b ** 2
    norm = math.sqrt(norm)

    featureStr = ""
    for feature in vec:
      a, b = feature
      featureStr += str(a + 1) + ":" + str(b / norm) + " "

    # print features
    if "-d" == opt:
#      print featureStr + "#" + str(i) + " " + ",".join(wordDictUnique).encode('utf-8') + " ORG->", row[0].encode('utf-8')
      print featureStr + "#" + str(i) + " " + " ORG->", row[0].encode('utf-8')
      print "Nouns:", ",".join(words_dict['nouns']).encode('utf-8')
      print "Verbs:", ",".join(words_dict['verbs']).encode('utf-8')
      print "Adjs:", ",".join(words_dict['adjs']).encode('utf-8')
    else:
      print featureStr
    
    i += 1

if __name__ == "__main__":
  main()
