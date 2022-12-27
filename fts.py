import csv
import requests
from bs4 import BeautifulSoup
  
fields = ['id', 'Name', 'audience' , 'countLearner' , 'difficult' , 'category' , 'subcategory' , 'url']  
url = 'https://futureskill.co/fs-content-api/courses/public?where=%7B%7D&sort=%7B%22createdAt%22:-1%7D&page=1&limit=177'
data = requests.get(url)

target_audience = ['นักเรียน', 'นักศึกษา', 'พนักงาน', 'บุคคลทั่วไป', 'Influencers'] 
items = data.json()['data']['items']
course_data = []

with open('datas.csv', 'w' , encoding="utf-8" , newline="") as f :
        fw = csv.writer(f)
        fw.writerow(fields) 

    
for i in items:
    audience = ''
    description = i['description']
    for t in target_audience:
            if description.find(t) != -1:
                if audience == '':
                    audience += t
                else:
                    audience += ", " + t 
      

    course_data.append([i["id"], i["name"], audience , i["countLearner"], i["difficult"]["name"], i['category']["name"], i['subcategory']["name"], i["thumbnailUrl"]])      


with open('datas.csv', 'a' , encoding="utf-8" , newline="") as f :
        fw = csv.writer(f)
        fw.writerows(course_data)















