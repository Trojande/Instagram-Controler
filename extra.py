faker = Faker()
emailsFile = open("emails.text", "r")
emailList = emailsFile.readlines()
emailNum = 0
	
def FetchEmail():
	global emailList
	global emailNum
	while True:
		emailNum = emailNum + 1
		print(emailList[emailNum])
		if emailNum == len(emailList)-1:
			break


def passwordGen():
	alphabet = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()-=+"
	passwordLenght = 12
	Password = ""
	for i in range(passwordLenght):
		next = random.randrange(len(alphabet))
		Password = Password + alphabet[next]
	print(Password)

def FullnameGen():
	FullNmae = faker.name()
	return FullNmae


def UserNmaeGen():
	FullNmae = FullnameGen()
	FullNmaeLower = FullNmae.lower()
	UserName = FullNmaeLower.replace(" ","")
	return UserNa