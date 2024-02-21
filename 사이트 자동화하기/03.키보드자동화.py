import pyautogui
import pyperclip # pyautogui는 한글 적용이 안되어 있기 대문에 pyperclip 모듈을 통해서 한글을 복사 후 입력 가능


# pyautogui.write('hello world!') # 괄호 안의 문자를 타이핑합니다.
# pyautogui.write('hello world!', interval=0.25) # 각 문자를 0.25마다 타이핑합니다.

# pyperclip.copy("안녕하세요") # 클립보드에 텍스트 복사
# pyautogui.hotkey('command', 'v') # 붙여넣기(write 함수로는 shift나 cmd 등 문자가 아닌 키를 누를 수 없다.)

# pyautogui.press('shift') # shift키를 누릅니다.
# pyautogui.press('command') # cmd키를 누릅니다.

# pyautogui.keyDown('command') # cmd 키를 누른 상태를 유지합니다.
# pyautogui.press('c') # c 키를 입력합니다.
# pyautogui.keyUp('command') # cmd 키를 뗍니다.

# pyautogui.press(['left', 'left', 'left']) # 왼쪽 방향키를 세 번 입력합니다.
# pyautogui.press('left', presses=3) # 왼쪽 방향키를 세 번 입력합니다.
# pyautogui.press('enter', presses=3, interval=3) # enter 키를 3초에 한 번씩 3번 입력합니다.

pyautogui.hotkey('command', 'v') # cmd + c 키를 입력합니다. (여러 키를 동시에 입력해야 할 때 keyDown/Up은 불편합니다.)

