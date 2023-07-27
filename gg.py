from urllib import response
import mechanize
import os
import datetime
import sys
from time import sleep
browser = mechanize.Browser()
browser.set_handle_robots(False)
cookies = mechanize.CookieJar()
browser.set_cookiejar(cookies)
browser.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36')]
browser.set_handle_refresh(False)

url = 'https://m.facebook.com/login.php'

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        
def sp(stri):
    for letter in stri:
        print(letter, end = "")
        sys.stdout.flush()
        sleep(0.03)

def login():
    browser.open(url)
    browser.select_form(nr = 0)
    browser.form['email'] = USERNAME
    browser.form['pass'] = PASSWORD
    r = browser.submit()
    f = open("login.html", "wb")
    f.write(r.read())
    f.close()
    browser.select_form(nr = 0)
    print("\033[1;33;40m", end = "")
    sp("\nEnter the 2 factor code by google authenticator :\n")
    print("\033[1;37;40m")
    apr = str(input())
    try:
        browser.form['approvals_code'] = apr
    except mechanize._form_controls.ControlNotFoundError:
        print("Wrong password or some shit, check generated file")
        f = open("epage_" + str(USERNAME) + ".html", "wb")
        f.write(r.read())
        f.close()
        exit(1)
    r = browser.submit()
    browser.select_form(nr = 0)
    try:
        browser.form['name_action_selected'] = ['save_device']
    except mechanize._form_controls.ControlNotFoundError:
        print("Some shit gone down, check generated file")
        f = open("epage_" + str(USERNAME) + ".html", "wb")
        f.write(r.read())
        f.close()
        exit(1)
    r = browser.submit()
    f = open("full_login_" + str(USERNAME) + ".html", "wb")
    f.write(r.read())
    f.close()

def findtextchat(curl):
    r = browser.open(curl)
    x = browser.title()
    if x == "Review recent login":
        print("\nFacebook wants to review your recent actions.\nPlease fix that and then re run the program.")
        exit(1)
    if x == "Login approval needed":
        print("\nYour account is stuck on verification\nPlease do it and then re run the program.")
        exit(1)
    if x == "Epsilon":
        print("\nYour account got locked, recover it kindly and re run the script.")
        exit(1)

def sendtextconvo(comment):
    try:
        browser.select_form(nr = 1)
    except mechanize._mechanize.FormNotFoundError:
        print("Some error occured while finding text area, please check your account")
        exit(1)
    try:
        browser.form['body'] = comment
    except mechanize._form_controls.ControlNotFoundError:
        print("Some error occured while filling text, please check your account")
        exit(1)
    r = browser.submit()
    e = datetime.datetime.now()
    print("\033[1;32;40m", end = "")
    print (e.strftime("%d/%m/%Y   %I:%M:%S %p"))
    print(">>", line, "\n")

print("\033[1;33;40m", end = "")
sp("\nEnter your email :\n")
print()
print("\033[1;37;40m")
USERNAME = str(input())
print("\033[1;33;40m", end = "")
sp("\nEnter your password :\n")
print("\033[1;37;40m")
PASSWORD = str(input())
login()
print("\033[1;34;40m", end = "")
sp("Enter chat group or inbox id link :\n")
print("\033[1;37;40m")
cid = str(input())
curl = 'https://m.facebook.com/messages/t/' + str(cid)

print("\033[1;34;40m", end = "")
sp("Enter notepad file name :")
print("\033[1;37;40m")
np = str(input())
f = open(np, 'r')
lines = f.readlines()
f.close()
print("\033[1;33;40m", end = "")
sp("Enter the time delay in seconds :\n")
print("\033[1;37;40m")
t = int(input())

clear()

count = 0
while True:
    for line in lines:
        if len(line) > 3:
            if count != 0:
                sleep(t)
            findtextchat(curl)
            sendtextconvo(line)
            count += 1
            if count % 10 == 0:
                sleep(1)
                clear()
                print("\033[0;37;41m\n")
                _   _    _      _    _  _
| \ | |  / \  / ___||  _ \    / \|_   _|
|  \| | / _ \ \___ \| |_) |  / _ \ | |
| |\  |/ _ \ _) |  _ <  / ___ \| |
|_| \_/_/   \_\____/|_| \_\/_/   \_\_|   
\x1b[1;97m🔹🔸🔹🔸🔹🔸🔹🔸🔹🔸🔹🔸🔹🔹🔸🔹🔸🔹🔸🔹🔸🔹🔸🔹🔸🔹🔹🔸🔹🔸🔹🔸🔹🔸🔹🔸🔹🔸🔹
\033[1;31m         HACEKR Loy Rayess kabul 💛👈 \33[0m
\x1b[1;97m🔹🔸🔹🔸🔹🔸🔹🔸🔹🔸🔹🔸🔹🔹🔸🔹🔸🔹🔸🔹🔸🔹🔸🔹🔸🔹🔸🔹🔸🔹🔸🔹🔸🔹🔸🔹🔸🔹🔹
\033[1;32m[+] 𝗔𝗨𝗧𝗛𝗢𝗥 | NASRAT
\033[1;33m[+] 𝗙𝗔𝗖𝗘𝗕𝗢𝗢𝗞 | Loy Rayess kabul
\033[1;34m[+] 𝗚𝗜𝗧𝗛𝗨𝗕  | Nasrat99845 
\033[1;35m[+] 𝗧𝗘𝗔𝗠   |   \33[1;42  Afghan Hacker \33[0m
\033[1;36m[+] 𝗩𝗘𝗥𝗦𝗜𝗢𝗡 |\x1b[1;97m    .0.1💓   \x1b[1;97m          
\x1b[1;97m🔹🔸🔹🔸🔹🔸🔹🔸🔹🔸🔹🔸🔹🔹🔸🔹🔸🔹🔸🔹🔸🔹🔸🔹🔸🔹🔹🔸🔹🔸🔹🔸🔹🔸🔹🔸🔹🔸🔹
"""


class Main:
	def __init__(self):
		self.id = []
		self.ok = []
		self.cp = []
		self.loop = 0
		os.system("clear")
		print(logo)
		print("")
		print("★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★")
		print("\033[1;37m𝗡𝗢𝗧𝗘 : 𝗔𝗽𝗽𝗿𝗼𝘃𝗮𝗹  𝗙ollow My Facebook Account ")
		print("★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★")
os.system("clear ")
print(logo)
print("")
print("\033[1;37m [1] 𝗙𝗶𝗿𝘀𝘁 Follow My Facebook Account ")
print("\033[1;37m [2] 𝗘𝘅𝗶𝘁")
print("")
Baloch = input("\n\033[1;37m  Choose : \033[1;32m")
if Baloch in ["", " "]:
	exit()
elif Baloch in ["2", "02"]:
	print("    Thanks♥️")
	exit() 
elif Baloch in ["1", "01"]:
	os.system("xdg-open https://www.facebook.com/profile.php?id=100041248659496")
print("")
time.sleep(3.0)
print("\033[1;37m    𝗖𝗛𝗘𝗖𝗞𝗜𝗡𝗚 𝗔𝗣𝗣𝗥𝗢𝗩𝗔𝗟 ")
print("")
input("\n\033[1;37m TYᑭᗴ Tᕼᗴ Oᗯᑎᗴᖇ ᖴᗩᑕᗴᗷOOK ᗩᑕᑕOᑌᑎT ᑎᗩᗰᗴ \033[1;37m")
time.sleep(3.1)
print("")
print("\033[1;32m ᗯᗴᒪᑕOᗰᗴ TO ••RAYEES NASRAT•• ᗷᖇᗩᑎᗪ TOOᒪՏ")
time.sleep(3.0)
os.system("clear")
print(logo)
print(" [+]𝗠𝗘𝗡𝗨  𝗠𝗘𝗧𝗛𝗢𝗗")
print("\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - -")

def riaz():
	os.system('clear')
	print(logo)
	print('[1] Pak Random Cloning menu')
	print('[2] Bangladish Random Cloning')
	print('[3] Create File dumping')
	print('[4] Follow me on Facebook')
	print('\x1b[1;91m[5] Exit Main menu')
	print('\33[1;37m----------------------------------------------')
	riaz1 = input('[•] Select option  : ')
	if riaz1 =='1':
		annu()
	if riaz1 =='5':
		riaz()
	if riaz1 =='3':
		os.system('xdg-open https://youtube.com/@sajjadhelpzone6744')
	if riaz1 =='4':
		os.system('xdg-open https://www.facebook.com/profile.php?id=100055742216218&mibextid=ZbWKwL');riaz()
	if riaz1 =='2':
		bangla()
	else:
		print('\n\033[1;31mChoose valid option\033[0;97m')
		riaz()
