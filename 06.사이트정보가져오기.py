import requests


# URL 요청하기 - get
# status_code는 응답코드를 가져옵니다. text에는 HTML 코드가 담겨 있습니다.
response = requests.get('https://www.naver.com')

print(response.status_code)
print(response.text)

# 파라미터를 전달하는 방법
url = 'https://section.blog.naver.com/Search/Post.nhn?pageNo=1&rangeType=ALL&orderBy=sim&keyword=%ED%8C%8C%EC%9D%B4%EC%8D%AC'

params = {
    'pageNo' : 1,
    'rangeType' : 'ALL',
    'orderBy' : 'sim',
    'keyword' : '파이썬'
}

response = requests.get('https://section.blog.naver.com/Search/Post.nhn', params=params)

print(response.status_code)
print(response.url)