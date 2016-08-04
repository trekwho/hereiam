import jieba, operator, re
import pandas as pd

text = open('weibo_text.txt','r',encoding="utf-8").read()
regex = re.compile("[?!^a-zA-Z0-9></='_;.!&-:，！]")
text = regex.sub(' ',text)

blacklist = [u'"',u'没有',u'别的',u'星星',u'半星',u'##',u'痴情',u'轩轩']
jieba.suggest_freq(('戴立忍'),True)
jieba.suggest_freq(('水原希子'),True)

output = {'word':[],
          'count':[]}

words={}
for word in jieba.cut(text):
    if word in blacklist or len(word) == 1:
        continue
    words[word] = words.get(word,0) + 1
sort_words = sorted(words.items(), key=operator.itemgetter(1), reverse=True)

for pair in sort_words[:191]:
    output['word'].append(list(pair)[0])
    output['count'].append(list(pair)[1])
    
file = pd.DataFrame(output, columns=['word','count'])
file.to_csv('weibo_word.csv',encoding="utf-8")
