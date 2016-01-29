import pyautogui
import time

def copyVerCode():
	pyautogui.click(1275,730)
	time.sleep(1)
	pyautogui.click(820,370)
	time.sleep(1)
	pyautogui.click(500,150)
	time.sleep(1)
	pyautogui.mouseDown(500, 150, button='left')
	time.sleep(1.5)
	pyautogui.mouseUp(500, 150, button='left')
	time.sleep(1)
	pyautogui.click(500,390)
	time.sleep(1)
	pyautogui.click(500,680)
	time.sleep(1)
	pyautogui.hotkey('ctrl', 'v')
	time.sleep(1)
	pyautogui.doubleClick(500,680)
	time.sleep(1)
	pyautogui.click(520,710)
	pyautogui.dragTo(540, 715, duration=0.5)

copyVerCode()


