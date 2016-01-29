import time
import pyautogui

def login():

	pyautogui.moveTo(500,320)
	pyautogui.click(500,320)
	#time.sleep(0.5)
	pyautogui.doubleClick(450.320)
	pyautogui.typewrite(['backspace'])
	time.sleep(1)
	pyautogui.typewrite("sajjad_a_2", interval=0.1)
	time.sleep(0.75)
	pyautogui.click(500,370)
	pyautogui.typewrite("@S5233585a",interval=0.1)
	pyautogui.click(500,420)
	time.sleep(0.5)
