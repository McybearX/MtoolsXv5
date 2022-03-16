import os,time,random
from gtts import gTTS
from googletrans import Translator
try:
	os.system("mkdir $HOME/storage/shared/MtoolsX")
	os.system("mkdir $HOME/storage/shared/MtoolsX/MttsX")
#	os.mkdir("Save_File")
except:
	pass
m = "\x1b[1;91m"
h = "\x1b[1;92m"
k = "\x1b[1;93m"
b = "\x1b[1;94m"
u = "\x1b[1;95m"
l = "\x1b[1;96m"
p = "\x1b[1;97m"
def iklan():
	iklan = os.system("cd ../../bin && python3 McybearX.py")
def tiks(teks,bahasa):
	try:
		hasil=Translator().translate(teks, dest=bahasa)
	except ValueError:
		emil(" Bahasa Tidak Suport untuk di Translite !!!");time.sleep(2)
		__emil__()
	print (p+" Text : "+hasil.text)
	try:
		print (p+" Read : "+hasil.pronunciation)
	except:
		pass
	tts(hasil.text,bahasa)
McybearX="the best of hacker"
sup = "\x1b[4;95m               \x1b[0;95m/\x1b[3;91mM\x1b[1;95mcybear\x1b[1;91mX\x1b[0;90m"
emil=print
mx = u+"ʕ"+m+" x"+u+"_"+m+"×"+u+"ʔ"
def logo():
	os.system("clear")
	print ("""
\x1b[1;91m     __  ___ \x1b[1;95m__   __       \x1b[1;91m _  __
\x1b[1;91m    /  |/  /\x1b[1;95m/ /_ / /_ _____\x1b[1;91m| |/ /
\x1b[1;91m   / /|_/ /\x1b[1;95m/ __// __// ___/\x1b[1;91m|   /
\x1b[1;91m  / /  / /\x1b[1;97m/ /_ / /_ (__  )\x1b[1;91m/   |
\x1b[1;91m /_/  /_/ \x1b[1;97m\__/ \__//____/\x1b[1;91m/_/|_|
""")
def tts(teks,bahasa):
	global suara
	try:
		suara=gTTS(text=teks,lang=bahasa).save("your.mp3")
		os.system("mv your.mp3 $HOME/storage/shared/MtoolsX/MttsX/your.mp3")
		os.system(f"play-audio $HOME/storage/shared/MtoolsX/MttsX/your.mp3")
		save()
	except ValueError:
		emil(" Bahasa Tidak Suport untuk di Translite Suara !!!");time.sleep(2)
		save()
def save():
	hihi=input(mx+p+" PutarLagi/Save/JanganSave "+k+"("+p+"P"+k+"/"+p+"S"+k+"/"+p+"J"+k+")"+p+" : ")
	if hihi=="s" or hihi=="S":
		haha=input(mx+p+" Name File : ")
		os.system(f"mv $HOME/storage/shared/MtoolsX/MttsX/your.mp3 $HOME/storage/shared/MtoolsX/MttsX/{haha}.mp3")
		emil(h+f" File tersimpan di /storage/MtoolsX/MttsX/{haha}.mp3");time.sleep(3)
		__emil__()
	elif hihi=="j" or hihi=="J":
		os.system("rm -rf $HOME/storage/shared/MtoolsX/MttsX/your.mp3")
		__emil__()
	elif hihi=="P" or hihi=="p":
		os.system(f"play-audio $HOME/storage/shared/MtoolsX/MttsX/your.mp3")
		save()
	else:
		__emil__()
def __emil__():
	logo()
	emil(k+" NOTE :"+p+" Pastikan Kamu Sudah Terhubung Dengan Internet!!!\n")
	emil(u+" ["+m+"o1"+u+"]"+p+" Indonesia")
	emil(u+" ["+m+"o2"+u+"]"+p+" English")
	emil(u+" ["+m+"o3"+u+"]"+p+" Japanese")
	emil(u+" ["+m+"o4"+u+"]"+p+" Korea")
	emil(u+" ["+m+"o5"+u+"]"+p+" Thailand")
	emil(u+" ["+m+"o6"+u+"]"+p+" Malaysia")
	emil(u+" ["+m+"o7"+u+"]"+p+" Arab")
	emil("")
	bahas=input(mx+p+" Bahasa : ")
	if bahas=="1":
		teks=input(mx+p+" Masukan Teks : ")
		bahasa="id"
	elif bahas=="2":
		teks=input(mx+p+" Masukan Teks : ")
		bahasa="en"
	elif bahas=="3":
		teks=input(mx+p+" Masukan Teks : ")
		bahasa="ja"
	elif bahas=="4":
		teks=input(mx+p+" Masukan Teks : ")
		bahasa="ko"
	elif bahas=="5":
		teks=input(mx+p+" Masukan Teks : ")
		bahasa="th"
	elif bahas=="6":
		teks=input(mx+p+" Masukan Teks : ")
		bahasa="ms"
	elif bahas=="7":
		teks=input(mx+p+" Masukan Teks : ")
		bahasa="ar"
	else:
		teks=input(mx+p+" Masukan Teks : ")
		bahasa=bahas
	tiks(teks,bahasa)
if McybearX=="the best of hacker":
	__emil__()
