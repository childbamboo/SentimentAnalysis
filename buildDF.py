#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# sort count.txt | uniq -c | sed -e 's/^  *//g' | sed -e 's/ /	/g' > count_sort.txt
# sort count.txt | uniq -c | sed -e 's/^  *//g' | sed -e 's/ /	/g' | sort -t " " -k 1 -n | nl | sed -e 's/^  *//g' > count_sort.txt
#

import unicodecsv
import sys
import Tagger
import Normalizer

import numpy
import scipy
import gensim
from gensim import corpora

def main():

  tagger = Tagger.Tagger()

  # initialize file reader
  spamReader = unicodecsv.reader(open('./comments/comments.tsv', 'rb'), delimiter='\t', encoding='utf-8')

  # gensim
  docWords = []

  # read each line
  for row in spamReader:
    sample_u = Normalizer.normalize(row[0])
    words_dict = tagger.parse(sample_u)
    # add words in document list
    docWords.append(words_dict['all'])

  # write df dictionary
  #   http://qiita.com/yasunori/items/31a23eb259482e4824e2 
  dictionary = corpora.Dictionary(docWords)
  dictionary.filter_extremes(no_above=0.2)
  dictionary.save_as_text('./dic/df.tsv')

if __name__ == "__main__":
  main()
