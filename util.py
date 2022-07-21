import requests
from bs4 import BeautifulSoup
import uuid

#필요한 메소드 만들기
def imgDown():
    sub_page_url = "https://movie.naver.com/movie/bi/mi/basic.naver?code=187347"

    # sub_page_url 요청하면  --> 응답(html)
    # 요청하기
    response = requests.get(sub_page_url)
    html = response.text
    # print(html)

    # 필요한 img_url 추출
    soup = BeautifulSoup(html, "html.parser")
    tag = soup.select_one(".poster>a>img")
    # print(tag)
    poster_url = tag["src"]      #진짜 이미지 경로
    # print(poster_url)

    # img_url 요청 --> 응답(1212344531203234873201123)
    # 파일이름
    saveName = str(uuid.uuid4())

    # 저장위치 + 파일이름
    filePath = "C:\\javaStudy\\upload\\movie\\" +saveName+".jpg"

    #요청
    img_response = requests.get(poster_url)

    # C:\javaStudy\upload\movie 경로에 저장
    file = open(filePath, "wb")
    file.write(img_response.content)
    file.close()

    # 파일경로 리턴
    return filePath

'''
result = imgDown()
print(result)
'''