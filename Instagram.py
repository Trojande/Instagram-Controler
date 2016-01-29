import random
from faker import *
import pyautogui
import time
from faker import *
import random
import os
faker = Faker()
telnum = "2028448091"
emailsFile = open("emails.text", "r")
emailList = emailsFile.readlines()



def scroll(nclick):
	for i in range(nclick):
		pyautogui.scroll(-10)


def FullnameGen():
	FullNmae = faker.name()
	return FullNmae

def UserNmaeGen():
	#FullNmae = FullnameGen()
	FullNmaeLower = FullNmae.lower()
	UserName = FullNmaeLower.replace(" ","")
	return UserName

def passwordGen():
	alphabet = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()-=+"
	passwordLenght = 12
	Password = ""
	for i in range(passwordLenght):
		next = random.randrange(len(alphabet))
		Password = Password + alphabet[next]
	return Password

def follow():
	#pyautogui.moveTo(500,320)
	#pyautogui.click(500,320)
	pyautogui.click(1275,730)
	time.sleep(1)
	pyautogui.click(225,110)
	time.sleep(1)
	pyautogui.click(1050,175)
	time.sleep(4)
	pyautogui.click(680,150)
	time.sleep(3)
	#wait = input("countinue? ")
	pyautogui.click(480,650) # open image
	time.sleep(0.5)
	pyautogui.click(580,250)
	pyautogui.doubleClick(580,250)
	pyautogui.click(410,50) # back
	time.sleep(0.2)
	pyautogui.click(410,50) #back
	time.sleep(0.5)
	#pyautogui.click(600,600)
	#pyautogui.doubleClick(600,600)
	#time.sleep(0.5)


def followRandomPeople():
	pyautogui.click(550,730)
	time.sleep(8)
	#n = input("countinue: ")
	#pyautogui.moveTo(550,600)
	#scroll(12)
	time.sleep(0.5)
	pyautogui.click(480,150)
	time.sleep(0.5)
	pyautogui.click(810,100) # Follow key
	time.sleep(2)
	pyautogui.click(420,60)  #back Key
	time.sleep(0.5)
	pyautogui.click(580,150)
	time.sleep(0.5)
	pyautogui.click(810,100) # follow
	time.sleep(2)
	pyautogui.click(420,60) #back
	time.sleep(0.5)
	pyautogui.click(780,150)
	time.sleep(0.5)
	pyautogui.click(810,100) # follow
	time.sleep(2)
	pyautogui.click(420,60) #back
	time.sleep(0.5)
	pyautogui.click(480,350)
	time.sleep(0.5)
	pyautogui.click(810,100) # follow
	time.sleep(2)
	pyautogui.click(420,60) #back
	time.sleep(0.5)
	pyautogui.click(580,350)
	time.sleep(0.5)
	pyautogui.click(810,100) # follow
	time.sleep(2)
	pyautogui.click(420,60) #back
	time.sleep(0.5)
	pyautogui.click(780,350)
	time.sleep(0.5)
	pyautogui.click(810,100) # follow
	time.sleep(2)
	pyautogui.click(420,60) #back
	time.sleep(0.5)
	pyautogui.click(480,450)
	time.sleep(0.5)
	pyautogui.click(810,100) # follow
	time.sleep(2)
	pyautogui.click(420,60) #back
	time.sleep(0.5)
	pyautogui.click(580,450)
	time.sleep(0.5)
	pyautogui.click(810,100) # follow
	time.sleep(2)
	pyautogui.click(420,60) #back
	time.sleep(0.5)
	pyautogui.click(780,450)
	time.sleep(0.5)
	pyautogui.click(810,100) # follow
	time.sleep(2)
	pyautogui.click(420,60) #back
	time.sleep(0.5)

def logout():
	
	pyautogui.click(820,730)
	time.sleep(0.5)
	pyautogui.click(830,50)
	time.sleep(0.5)
	pyautogui.moveTo(820,600)
	for i in range(15):
		pyautogui.scroll(-10)
	pyautogui.click(820,680)
	time.sleep(0.5)
	pyautogui.click(700,420)
	time.sleep(5)

def androidIdChanger():
	pyautogui.click(1275,730)
	time.sleep(0.5)
	pyautogui.click(630,380)
	time.sleep(0.5)
	pyautogui.click(1190,80)
	time.sleep(0.5)
	pyautogui.click(1190,230)
	time.sleep(0.5)
	pyautogui.click(1275,730)
	time.sleep(0.5)
	pyautogui.click(250,230)
	time.sleep(1)

def takecodeshot():
	pyautogui.click(1275,730)
	time.sleep(1)
	pyautogui.click(1020,360)
	time.sleep(1)
	im = pyautogui.screenshot("C:\\Users\\Sajjad\\Documents\\Instagram\\pytesser_v0.0.1\\image.png", region=(345,330, 155, 80))
	time.sleep(1)
	pyautogui.click(1275,730)
	time.sleep(1)
	pyautogui.click(250,230)
	time.sleep(1)
	
	os.chdir( 'C:\\Users\\Sajjad\\Documents\\Instagram\\pytesser_v0.0.1' )
	os.system("C:\\Users\\Sajjad\\Documents\\Instagram\\pytesser_v0.0.1\\fetchcode.py")
	time.sleep(2)
	codefile = open("C:\\Users\\Sajjad\\Documents\\Instagram\\pytesser_v0.0.1\\code.text", "r")
	return codefile.readline()

def signup(email, usern, fname, pwd):
	pyautogui.click(690, 740)
	time.sleep(0.25)
	pyautogui.click(690,610)
	time.sleep(0.25)
	pyautogui.click(450,360)
	time.sleep(0.25)
	pyautogui.typewrite(email, interval=0.2)
	time.sleep(0.5)
	pyautogui.click(550,420)
	time.sleep(8)
	pyautogui.click(490,230)
	pyautogui.typewrite(fname, interval=0.2)
	time.sleep(0.5)
	pyautogui.click(490,290)
	pyautogui.typewrite(usern, interval=0.2)
	time.sleep(0.5)
	pyautogui.click(590,320)
	time.sleep(0.5)
	pyautogui.typewrite(pwd, interval=0.2)
	time.sleep(0.5)
	pyautogui.click(635,357)
	time.sleep(0.5)
	pyautogui.click(635,357)
	time.sleep(8)
	pyautogui.click(630,730)
	time.sleep(0.5)
	pyautogui.click(570,430)
	time.sleep(0.5)
	pyautogui.click(630,730)
	time.sleep(0.5)
	pyautogui.click(570,430)
	time.sleep(0.5)
	pyautogui.click(850,60)
	time.sleep(0.5)

def signUpByTel(fname, usern, pwd, telnum):
	pyautogui.click(690, 740)
	time.sleep(0.25)
	pyautogui.click(690,610)
	time.sleep(0.25)
	pyautogui.click(660,317)
	time.sleep(0.25)
	pyautogui.click(660,470)
	time.sleep(0.25)
	pyautogui.typewrite(telnum, interval=0.1)	
	time.sleep(0.25)
	pyautogui.click(660,520)
	time.sleep(1.5)
	pyautogui.click(660,520)
	time.sleep(1.5)
	pyautogui.click(660,415)
	time.sleep(1)
	pyautogui.click(660,470)
	time.sleep(15)
	codeVer = takecodeshot()
	pyautogui.typewrite(codeVer, interval=0.1)
	time.sleep(0.25)
	pyautogui.click(660,520)
	time.sleep(1)
	pyautogui.click(490,230)
	pyautogui.typewrite(fname, interval=0.2)
	time.sleep(0.5)
	pyautogui.click(490,290)
	pyautogui.typewrite(usern, interval=0.2)
	time.sleep(0.5)
	pyautogui.click(590,320)
	time.sleep(0.5)
	pyautogui.typewrite(pwd, interval=0.2)
	time.sleep(0.5)
	pyautogui.click(635,357)
	time.sleep(0.5)
	pyautogui.click(635,357)
	time.sleep(8)
	pyautogui.click(630,730)
	time.sleep(0.5)
	pyautogui.click(570,430)
	time.sleep(0.5)
	pyautogui.click(630,730)
	time.sleep(0.5)
	pyautogui.click(570,430)
	time.sleep(0.5)
	pyautogui.click(850,60)
	time.sleep(0.5)

counter = 0
for i in range(50):
	FullNmae = FullnameGen()
	PASSWORD = passwordGen()
	user_name = UserNmaeGen()
	#femail = i + "@gmail.com"
	data = open("data.text", "a")
	#data.write(femail+"\n")
	data.write(FullNmae+"\n")
	data.write(user_name+"\n")
	data.write(PASSWORD+"\n")
	data.write("\n")
	data.close()
	
	signUpByTel(FullNmae, user_name, PASSWORD, telnum)
	followRandomPeople()
	follow()
	logout()
	counter = counter + 1
	if counter == 9:
		androidIdChanger()
		counter = 0
	print(counter)
