import requests
from bs4 import BeautifulSoup

##################################################
#댓글 추출
###################################################

#1.사이트에 요청 응답(html)을 받기  - requests
url = "https://movie.daum.net/moviedb/grade?movieId=139606"

#요청하기
response = requests.get(url);

html = response.text
#print(html)

#2.필요한 태그 추출하기 - BeautifulSoup4
soup = BeautifulSoup(html, "html.parser")

tags = soup.select(".cmt_info")   #* 전략을 잘 세워야 함
print(tags)