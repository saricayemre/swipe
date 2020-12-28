#!/usr/bin/python3

import os
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True) 

def banner(): # başlık metodu

    print(Fore.CYAN+"""
       ____         _         
      / __/ _    __(_)__  ___ 
     _\ \  | |/|/ / / _ \/ -_)
    /___/  |__,__/_/ .__/\__/ 
                  /_/         
    \n"""+Fore.BLUE+"Super wipe tool\t"+Fore.RED+"@saricayemre"  )                                                                  
    
    
def optionsList(): #seçenekler listesi
    
    print("\n"+
    Fore.RED+"{-1-} "+Fore.CYAN+"Linux komutu   ile işlem yapmak istiyorum\n"+
    Fore.RED+"{-2-} "+Fore.CYAN+"wipe eklentisi ile işlem yapmak istiyorum\n"+
    Fore.RED+"{-3-} "+Fore.RED+"Çıkış\n")
 
def option1(): # 1. seçenek (Linux Komutu) işlemini yapan metot 
    
    print("\n"+Fore.WHITE+"+"+"-"*20+"*BİLGİ*"+"-"*20+"+")
    print(Fore.BLUE+"✓ İşlem Linux komutu ile devam edecektir.")  
    print(Back.RED+"!!! Not: İşlem diskin boyutuna göre uzun sürebilir !!!")
    print(Fore.WHITE+"+"+"-"*47+"+\n")  
    os.system("dd if=/dev/urandom of=/dev/sdb bs=4096") #rastgele 0-1 yazma işlemi
    print(Back.RED+"✓ İşlem tamamlandı.")

def option2(): # 2.seçenek(wipe eklentisi) işlemini yapan metot

    os.system("xterm -e apt-get update") # Sistem güncellemesi
    os.system("xterm -e apt-get install wipe") # wipe eklentisini linux sisteme indirme veya import etme
    print("\n"+Fore.WHITE+"+"+"-"*20+"*BİLGİ*"+"-"*20+"+")
    print(Fore.BLUE+"✓ İşlem wipe eklentisi ile devam edecektir.")
    print(Fore.BLUE+"✓ Sistem güncellendi ve wipe eklentisi indirildi.")  
    print(Fore.WHITE+"+"+"-"*47+"+")      
    print(Fore.RED+"",end="")
    os.system("wipe /dev/sdb") # wipe işlemini gerçekleştiren wipe eklentisinin komutu
    print(Back.RED+"✓ İşlem tamamlandı.")

# Kullanıcının seçim yapması ve ardından gerçekleştirilecek olan işlemler

os.system("clear")
banner()
optionsList()
option = input(Fore.RED+"Bir Seçenek Seçiniz!> "+Fore.CYAN)
  
if(option == "1"):
    os.system("clear")
    banner()
    option1()
  
elif(option == "2"):
    os.system("clear")
    banner()
    option2()

elif(option=="3"):
    os.system("exit")
    
else:
    print(Fore.RED+"Yanlış bir seçenek seçtiniz! Lütfen tekrar seçim yapınız!")


