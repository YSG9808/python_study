import requests
from bs4 import BeautifulSoup

# # BeautifulSoup 사용법 
# url = 'https://kin.naver.com/search/list.nhn?query=%ED%8C%8C%EC%9D%B4%EC%8D%AC'

# response = requests.get(url)

# if response.status_code == 200:
#     html = response.text
#     soup = BeautifulSoup(html, 'html.parser')
    
#     # copy selector한 css 선택자를 select_one 함수의 인자로 넣는다
#     title = soup.select_one('#s_content > div.section > ul') 
#     print(title)
#     # print(title.get_text) # 텍스트만 뽑아오기
# else : 
#     print(response.status_code)


# 제목 여러개 뽑기
url = 'https://kin.naver.com/search/list.nhn?query=%ED%8C%8C%EC%9D%B4%EC%8D%AC'

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    ul = soup.select_one('ul.basic1')           # select_one은 찾은 html 중 가장 첫번째 html을 가져온다
    titles = ul.select('li > dl > dt > a')      # select는 찾은 모든 html을 리스트 형태로 반환한다
    for title in titles:
        print(title.get_text())
else : 
    print(response.status_code)
