import requests
import uuid



# 이미지 추출!!!
img_url = "https://movie-phinf.pstatic.net/20220708_75/16572722362230AyHS_JPEG/movie_image.jpg"


# 저장위치 + 파일이름
saveName = uuid.uuid4()     #.uuid4() 시간과 관련하여...
print(saveName, type(saveName))

filePath = "C:\\javaStudy\\upload\\movie\\" +saveName+".jpg"


img_response = requests.get(img_url)
# print(img_response.text)

file = open(filePath, "wb")
file.write(img_response.content)    #이동 경로로 write
file.close()

