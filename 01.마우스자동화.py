import time
import pyautogui


# 화면 크기 출력
print(pyautogui.size())

time.sleep(1)

# 마우스 현재 위치 출력
print(pyautogui.position())

# 마우스 이동
pyautogui.moveTo(100, 200) # x -> 100, y -> 200 위치로 바로 이동
time.sleep(1)
pyautogui.moveTo(100, 200, 2) # x -> 100, y -> 200 위치로 2초동안 이동

# 마우스 클릭
pyautogui.click()
pyautogui.click(button='right')
pyautogui.doubleClick()
pyautogui.click(clicks=3, interval=1) # 1초에 1번씩 3번 클릭

# 마우스 드래그
pyautogui.moveTo(337, 92, 2)
pyautogui.dragTo(485, 86, button='left', duration=2)

