import pyautogui
from PIL import *
import time
import sys, string, os


def takecodeshot():
	pyautogui.click(1275,730)
	time.sleep(0.5)
	pyautogui.click(1020,360)
	time.sleep(0.5)
	im = pyautogui.screenshot("C:\\Users\\Sajjad\\Documents\\Instagram\\pytesser_v0.0.1\\image.png", region=(345,330, 155, 80))
	time.sleep(0.5)
	pyautogui.click(1275,730)
	time.sleep(0.5)
	pyautogui.click(250,230)
	time.sleep(0.5)
	
	os.chdir( 'C:\\Users\\Sajjad\\Documents\\Instagram\\pytesser_v0.0.1' )
	os.system("C:\\Users\\Sajjad\\Documents\\Instagram\\pytesser_v0.0.1\\fetchcode.py")
