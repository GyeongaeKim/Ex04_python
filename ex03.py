import requests
from bs4 import BeautifulSoup

import util     #직접 만든거 가져오기
#랭킹추출
#1. 사이트에 요청, 응답을 받기
url = "https://movie.naver.com/movie/sdb/rank/rmovie.naver"

# 요청하기
response = requests.get(url);
html = response.text
# print(html)


#2. 필요한 태그 추출하기 BeautifulSoup4
soup = BeautifulSoup(html, "html.parser")
tags = soup.select(".tit3>a")   #뭘 가져올것인지 전략을 잘 세워야 한다

for index, tag in enumerate(tags):
    #순위
    rank = index + 1
    
    #영화제목
    title = tag.text
    
    #포스터 이미지
    sub_page_url = tag["href"]
    sub_url = "https://movie.naver.com/" + sub_page_url
    filePath = util.imgDown(sub_url)    #서브페이지에서 포스터를 수집


    print(rank, title, filePath)



