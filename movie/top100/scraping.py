import requests,csv
from bs4 import BeautifulSoup

with open('ranks.csv','w',newline='',encoding='utf-8') as file:
    rankwriter = csv.writer(file)
    rankwriter.writerow(['rank','title','rating','box','date','type'])
    
    urls = ['https://www.douban.com/doulist/1295618/','https://www.douban.com/doulist/1295618/?start=25&sort=seq&sub_type=','https://www.douban.com/doulist/1295618/?start=50&sort=seq&sub_type=','https://www.douban.com/doulist/1295618/?start=75&sort=seq&sub_type=']
    for url in urls:
        page = requests.get(url)
        soup = BeautifulSoup(page.text)
        items = soup.find_all('div',class_='doulist-item')

        for item in items :
            rank = item.find('span',class_='pos')
            title = item.find('div',class_='title')
            rating = item.find('span',class_='rating_nums')
            comment = item.find('div',class_='comment-item content')
            comment_list = comment.text.strip().split('|')
            #print(rank.text.strip(),'\t',title.text.strip(),'\t',rating.text.strip(),'\t',comment.text.strip())
            content = [rank.text.strip(),title.text.strip(),rating.text.strip()]+comment_list
            rankwriter.writerow(content)
