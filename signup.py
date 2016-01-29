import pyautogui
import time
from faker import *
import random
faker = Faker()

def FullnameGen():
	FullNmae = faker.name()
	return FullNmae

FullNmae = FullnameGen()

def UserNmaeGen():
	FullNmae = FullnameGen()
	FullNmaeLower = FullNmae.lower()
	UserName = FullNmaeLower.replace(" ","")
	return UserNa


def passwordGen():
	alphabet = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()-=+"
	passwordLenght = 12
	Password = ""
	for i in range(passwordLenght):
		next = random.randrange(len(alphabet))
		Password = Password + alphabet[next]
	return Password

PASSWORD = passwordGen()
def signup():
	pyautogui.click(690, 740)
	pyautogui.click(690,610)
	pyautogui.click(450,360)
	pyautogui.typewrite('sajjad_a_h@hotmail.com', interval=0.1)
	#time.sleep(2)
	pyautogui.click(550,420)
	time.sleep(2)
	pyautogui.click(490,230)
	pyautogui.typewrite(FullNmae, interval=0.1)
	pyautogui.click(490,270)
	time.sleep(1)
	pyautogui.click(590,320)
	time.sleep(0.5)
	pyautogui.typewrite(PASSWORD, interval=0.2)
	time.sleep(0.25)
	pyautogui.click(635,357)
	time.sleep(0.25)
	pyautogui.click(630,730)
	time.sleep(0.25)
	pyautogui.click(570,430)
	time.sleep(0.25)
	pyautogui.click(630,730)
	time.sleep(0.25)
	pyautogui.click(570,430)
	time.sleep(0.25)
	pyautogui.click(850,60)
