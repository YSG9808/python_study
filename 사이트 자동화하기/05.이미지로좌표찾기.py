import pyautogui as pg


# locate 함수 : 저장해놓은 이미지와 같은 이미지가 있는 좌표를 알려준다(ex. Box(left=1295, top=540, width=38, height=32)) 
imageLocation = pg.locateOnScreen('저장해놓은_이미지.png')
print(imageLocation)

# center 함수 : 출력결과(ex. Point(x=1314, y=556))
imageLocation = pg.locationOnScreen('저장해놓은_이미지.png')
point = pg.center(imageLocation) # Box 객체의 중앙 좌표를 리턴합니다.
print(point)
