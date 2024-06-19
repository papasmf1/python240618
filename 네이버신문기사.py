import requests
from bs4 import BeautifulSoup

# URL 설정
url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%B0%98%EB%8F%84%EC%B2%B4'

# HTTP GET 요청
response = requests.get(url)

# 응답이 성공적일 경우
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # 기사 제목을 담고 있는 태그 찾기
    # 네이버의 구조에 따라 기사 제목이 포함된 태그와 클래스명을 수정해야 할 수 있음
    titles = soup.find_all('a', class_='news_tit')
    
    # 각 제목 출력
    for title in titles:
        print(title.get_text())

else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
