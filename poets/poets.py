import jieba, operator
import pandas as pd

haizi = open('haizi.txt','r',encoding="utf-8").read()
beidao = open('beidao.txt','r',encoding="utf-8").read()

blacklist = [u'，',u' ',u'。',u'\n',u'“',u'”',u'？',u'：',u'！',u'（',u'）',u'、',u'―',u'；',u'-']

output = {'haizi_word':[],
          'haizi_count':[],
          'beidao_word':[],
          'beidao_count':[]}

def find_words(poet):
    global words_poet, sort_words_poet
    words={}
    for word in jieba.cut(poet):
        if word in blacklist or len(word) == 1:
            continue
        words[word] = words.get(word,0) + 1
    sort_words = sorted(words.items(), key=operator.itemgetter(1), reverse=True)
    return sort_words


sort_haizi = find_words(haizi)
sort_beidao = find_words(beidao)
    
for pair in sort_haizi[:100]:
    output['haizi_word'].append(list(pair)[0])
    output['haizi_count'].append(list(pair)[1])

for pair in sort_beidao[:100]:
    output['beidao_word'].append(list(pair)[0])
    output['beidao_count'].append(list(pair)[1])


file = pd.DataFrame(output, columns=['haizi_word','haizi_count','beidao_word','beidao_count'])
file.to_csv('poets.csv',encoding="utf-8")
