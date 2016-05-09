import jieba, operator
import pandas as pd

haizi = open('haizi.txt','r',encoding="utf-8").read()
beidao = open('beidao.txt','r',encoding="utf-8").read()

blacklist = [u'，',u' ',u'。',u'\n',u'“',u'”',u'？',u'：',u'！',u'（',u'）',u'、',u'―',u'；',u'-']

output = {'haizi_word':[],
          'haizi_count':[],
          'beidao_word':[],
          'beidao_count':[]}

words_haizi = {}
for word in jieba.cut(haizi):
    if word in blacklist or len(word) == 1:
        continue
    words_haizi[word] = words_haizi.get(word, 0) + 1
sort_words_haizi =sorted(words_haizi.items(), key=operator.itemgetter(1), reverse=True)

for pair in sort_words_haizi[:100]:
    output['haizi_word'].append(list(pair)[0])
    output['haizi_count'].append(list(pair)[1])

words_beidao = {}
for word in jieba.cut(beidao):
    if word in blacklist or len(word) == 1:
        continue
    words_beidao[word] = words_beidao.get(word, 0) + 1
sort_words_beidao =sorted(words_beidao.items(), key=operator.itemgetter(1), reverse=True)

for pair in sort_words_beidao[:100]:
    output['beidao_word'].append(list(pair)[0])
    output['beidao_count'].append(list(pair)[1])


file = pd.DataFrame(output, columns=['haizi_word','haizi_count','beidao_word','beidao_count'])
file.to_csv('poets.csv',encoding="utf-8")
