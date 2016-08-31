import json
import matplotlib.pyplot as plt

with open('weibo.json') as file:
    data= json.load(file)
    file.close()

male = 0
female = 0

fans_list = []
allre_list = []

text=""

for item in data:
    #print("------------------new item---------------")
    for i in item["cards"][0]["card_group"]:
        text += i["mblog"]["text"]+"\n"
        time = i["mblog"]["created_at"]
        fans = i["mblog"]["user"]["fansNum"]
        repo = i["mblog"]["reposts_count"]
        comm = i["mblog"]["comments_count"]
        like = i["mblog"]["attitudes_count"]
        allre = repo+comm+like
        fans_list.append(fans)
        allre_list.append(allre)
        print("time: "+time+"; fans: "+str(fans)+"; repo: "+str(repo)+"; comm: "+str(comm)+"; like: "+str(like))
        
        
        if i["mblog"]["user"]["gender"] == "m":
            male += 1
        elif i["mblog"]["user"]["gender"] == "f":
            female += 1
        else:
            print(i["mblog"]["user"]["gender"])
        
##        try:
##            for j in i["mblog"]["comment_summary"]["comment_list"]:
##                if j["user"]["gender"] == "m":
##                    male += 1
##                elif j["user"]["gender"] == "f":
##                    female += 1
##        except KeyError:
##            pass

print("m: "+str(male)+"; f: "+str(female))

fig = plt.figure()
plt.scatter(fans_list,allre_list)
plt.show()      

##with open ("weibo_text.txt","w") as afile:
##    afile.write(text)


