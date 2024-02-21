import pyautogui as pg


# alert() 함수 : 간단한 메세지 박스 표시, 버튼을 누르면 버튼의 텍스트가 리턴
a = pg.alert(text = '내용입니다', title = '제목입니다', button = 'OK')
print(a)

# confirm() 함수 : OK와 Cancel 버튼이 있는 메세지 박스 표시, 클릭한 버튼의 값을 리턴
a = pg.confirm(text='내용입니다', title = '제목입니다', buttons=['OK', 'Cancel'])
print(a)

# prompt() 함수 : 입력창이 있는 메세지 박스 표시, 입력한 텍스트 리턴, Cancel을 누르면 None 값이 리턴
a = pg.prompt(text = '내용입니다', title = '제목입니다', default = '입력하세요')
print(a)

# password() 함수 : '*'로 마스킹된 입력창이 표시, 입력한 텍스트 리턴, Cancel을 누르면 None 값이 리턴
a = pg.password(text = '내용입니다', title = '제목입니다', default = '입력하세요', mask = '*')
print(a)