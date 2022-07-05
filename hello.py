import requests
from bs4 import BeautifulSoup

# MongoDB 사용하기
from pymongo import MongoClient
#                                  아이디 비밀번호
client = MongoClient('mongodb+srv://test:sparta@cluster0.epsmx.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

# 크롤링 : 프로그램이 웹 사이트를 정기적으로 돌며 정보를 추출하는 것
# 1) request를 통해 html 가져오기
# => 변수 =  request.get()을 통해 가져옴
# 2) beautifulSoup 사용해서 원하는 데이터 피싱
# beautifulSoup을 사용하는 방법
# 원하는 값에서 검사-> copy -> copy selector
# 변수 = soup.select_one('여기에 붙여넣기')

# headers => 우리가 코드에서 콜을 날린 걸 마치 우리가 브라우저에서 콜을 날린 것처럼 해주려고 씀
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20210829',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')
# title = soup.select_one('#old_content > table > tbody > tr:nth-child(2) > td.title > div > a')
# print(title)
# print(title['href'])
# print(title.text)

movies = soup.select('#old_content > table > tbody > tr')

for movie in movies :
    a = movie.select_one('td.title > div > a')
    b = movie.select_one('td:nth-child(1) > img')
    c =  movie.select_one('td.point')
    if a is not None :
        title = a.text
        rank = b['alt']
        star = c.text
        doc = {
            'title' : title,
            'rank' : rank,
            'star' : star

        }
        #db로 보내기
        db.movies.insert_one(doc)






