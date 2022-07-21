import requests
from bs4 import BeautifulSoup

#import bs4  beautifulsoup4의 모듈이름


# 랭킹추출!!!
#1. 사이트에 요청, 응답을 받기
url = "https://movie.naver.com/movie/sdb/rank/rmovie.naver"

# 요청하기
response = requests.get(url);


# 응답확인
print(response.status_code)     #상태코드
html = response.text
# print(html)


#2. 필요한 태그 추출하기 - BeautifulSoup4
soup = BeautifulSoup(html, "html.parser")

# tag = soup.select_one(".tit3>a")    #select_one은 하나만~
# print(tag)


tags = soup.select(".tit3>a")  #select는 리스트로
# print(tags[0].text)

'''
for tag in tags:
    title = tag.text
    print(title)
'''


for index, tag in enumerate(tags):
    rank = index + 1    #index는 0번부터 주니까, +1
    title = tag.text
    print(rank, title)




