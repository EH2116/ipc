import os
try:
    import requests
except:
    os.system("pip install requests")
import requests,time,subprocess
try:
    if "install ok installed" in subprocess.check_output('dpkg -s tor', shell=True).decode():
        pass
    else:
        os.system("apt update ; apt install tor")
except:
    os.system("apt update ; apt install tor")
logo="""
     _____ ___     ____   ____ 
    |_   _|_ _|   |  _ \ / ___|
      | |  | |    | |_) | |    
      | |  | |    |  __/| |___ 
      |_| |___|___|_|    \____|
             |_____|           

          [ DEV ] EKRAMUL HASSAN [ d ]
          [ PAGE ] TERMUX HACKER BD [ p ]
"""
def start():
    try:
        processNumber=int(subprocess.check_output('pgrep tor', shell=True).decode())
        killProcess=subprocess.check_output(f'kill -9 {processNumber}', shell=True).decode()
    except:
        pass
    os.system("tor --HTTPTunnelPort 2006 > /dev/null 2>&1 &")
    os.system("clear")
    print(logo)
    print(f"[ ! ]> Ip adress is connecting ...")
    while True:
        try:
            ip=requests.get("https://api.ipify.org/?format=text",proxies={"http":"http://127.0.0.1:2006","https":"http://127.0.0.1:2006"}).text
            break
        except:
            pass
    os.system("clear")
    print(logo)
    print(" [ ! ]> Your Host Name is : 127.0.0.1")
    print(" [ ! ]> Your Port is : 2006")
    print(f" [ ! ]> Ip adress is : {ip}")
def reload():
    try:
        os.system("kill -HUP $(pidof tor)")
        time.sleep(5)
        ip=requests.get("https://api.ipify.org/?format=text",proxies={"http":"http://127.0.0.1:2006","https":"http://127.0.0.1:2006"}).text
        print(f" [ IP ] Your new ip address is : {ip}")
    except Exception as err:
        print(f" [ ! ]> {err} ")
    except KeyboardInterrupt:
        processNumber=int(subprocess.check_output('pgrep tor', shell=True).decode())
        killProcess=subprocess.check_output(f'kill -9 {processNumber}', shell=True).decode()
        if "exiting cleanly" in killProcess:
            print("[ ! ]> Turn off ip chnager successfully ! ")
        else:
            print(killProcess)
def main():
    try:
        start()
        print(" [ ! ]> Type `help` to user guide [ ! ]")
        menus = input(" [ ! ]> Enter your input : ")
        if menus.lower() == "help" :
            os.system("clear")
            print(logo)
            print(" [ ! ]> Enter numbers to set ip changing second ,")
            print("        It will change ip continuously !")
            print(" [ ! ]> Enter `s` to single ip !")
            print(" [ ! ]> Enter `d` to concact with developer !")

            if input(" [ ! ]> To back in main menu type [ yes ] : ").lower() == "yes":
                main()
            else:
                exit()
        elif menus.lower() =="s":
            os.system("clear")
            print(logo)
            try:
                processNumber=int(subprocess.check_output('pgrep tor', shell=True).decode())
                killProcess=subprocess.check_output(f'kill -9 {processNumber}', shell=True).decode()
            except:
                pass
            os.system("tor --HTTPTunnelPort 2006")
        elif menus.lower() == "d":
            try:
                processNumber=int(subprocess.check_output('pgrep tor', shell=True).decode())
                killProcess=subprocess.check_output(f'kill -9 {processNumber}', shell=True).decode()
            except:
                pass
            os.system("xdg-open https://fb.com/m.e.h.2116")
        elif menus.lower() == "p":
            try:
                processNumber=int(subprocess.check_output('pgrep tor', shell=True).decode())
                killProcess=subprocess.check_output(f'kill -9 {processNumber}', shell=True).decode()
            except:
                pass
            os.system("xdg-open https://www.facebook.com/Termux.Hacker.Bd.Official")
        else:
            while True:
                try:
                    time.sleep(int(menus))
                    reload()
                except KeyboardInterrupt:
                    processNumber=int(subprocess.check_output('pgrep tor', shell=True).decode())
                    killProcess=subprocess.check_output(f'kill -9 {processNumber}', shell=True).decode()
                    if "exiting cleanly" in killProcess:
                        print("[ ! ]> Turn off ip chnager successfully ! ")
                    else:
                        print(killProcess)
                except Exception as err:
                    print(f" [ ! ]> {err} ")
                    exit()
    except KeyboardInterrupt:
        processNumber=int(subprocess.check_output('pgrep tor', shell=True).decode())
        killProcess=subprocess.check_output(f'kill -9 {processNumber}', shell=True).decode()
        if "exiting cleanly" in killProcess:
            print("[ ! ]> Turn off ip chnager successfully ! ")
        else:
            print(killProcess)
if __name__ == '__main__':
    main()
