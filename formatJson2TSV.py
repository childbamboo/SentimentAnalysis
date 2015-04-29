#coding:utf-8
import json

#
# jsonからコメント文のみ取得してtsvファイルに保存
#

f = open('./comments/comments.json', 'r')

jsonData = json.load(f)
# print json.dumps(jsonData, sort_keys = True, indent = 4 ,ensure_ascii=False)

count = jsonData['count']
#print count

collection = jsonData['results']['collection1']
# print len(collection)

i = 0
for comment in collection[0:] :
  text = comment['comment']['text']
  code = '\r\n'

  items = text.split('\n')
  text = "".join(items)
  print text.encode('utf-8')

f.close()
