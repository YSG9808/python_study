# BeautifulSoup 라이브러리의 한계 -> 자바스크립트로 동적으로 생성된 정보는 가져올 수 없다.
# Ajax(비동기 통신)형태로 서버와 데이터를 주고 받아 화면에 뿌려주는 사이트가 많아 졌다. 
# 이러한 형식으로 데이터를 주고 받으면 url 변경이나 새로고침 없이 데이터를 가져오게 되면 BeautifulSoup로 가져올 수 없다.
# Selenium 라이브러리를 사용하는 이유
# 1. 자바스크립트가 동적으로 만든 데이터를 크롤링 하기 위해
# 2. 사이트의 다양한 HTML 요소에 클릭, 키보드 입력 등 이벤트를 주기 위해
# Selenium 라이브러리를 잘 활용하면 다음과 같은 업무들을 자동화할 수 있다.
# 1. 자동으로 로그인하기
# 2. 메일보내기 자동화
# 3. 블로그 이웃새글 자동좋아요 누르기
# 4. 인스타그램 자동으로 좋아요, 댓글 작성하기
# 5. 등등 정말 많은 다양한 일

# https://chromedriver.chromium.org/downloads/version-selection에서 현재 사용중인 크롬버전과 같은 버전의 크롬드라이버 다운로드

from selenium import webdriver
# 다운받은 driver 경로가 다른 곳에 있는 경우 -> driver = webdriver.Chrome('driver 경로')
driver = webdriver.Chrome()
url = 'https://www.google.com'
driver.get(url)
