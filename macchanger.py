import subprocess
import optparse
import re
import sys
from colorama import Fore, Style, init

init()

def print_usage():
    print(Fore.CYAN + """
    
     
                                                   
 _____         _____ _                       
|     |___ ___|     | |_ ___ ___ ___ ___ ___ 
| | | | .'|  _|   --|   | .'|   | . | -_|  _|
|_|_|_|__,|___|_____|_|_|__,|_|_|_  |___|_|  
                                |___|        
       
        
         
           """ + Style.RESET_ALL)    
    
    
    print(Fore.CYAN + "MacChanger V1.0 | Coder Telegram: pizza_0day" + Style.RESET_ALL)
    print("Kullanım:")
    print("  python macchanger.py -i <ağ arayüzü> -m <yeni_mac_adresi>")
    print("Açıklama:")
    print("  -i, --interface : Değiştirilecek ağ arayüzü")
    print("  -m, --mac : Yeni MAC adresi")
    print("Örnek:")
    print("  python3 macchanger.py -i eth0 -m 00:11:22:33:44:55")
    sys.exit()

if len(sys.argv) == 1:
    print_usage()


def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i", "--interface", dest="interface", help="Değiştirilecek arayüz")
    parse_object.add_option("-m", "--mac", dest="mac_address", help="Yeni MAC adresi")

    return parse_object.parse_args()

def change_mac_address(user_interface, user_mac_address):
    subprocess.call(["ifconfig", user_interface, "down"])
    subprocess.call(["ifconfig", user_interface, "hw", "ether", user_mac_address])
    subprocess.call(["ifconfig", user_interface, "up"])

def control_new_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result.decode("utf-8"))

    if new_mac:
        return new_mac.group(0)
    else:
        return None

(user_input, arguments) = get_user_input()

print(Fore.YELLOW + "MAC adresi değiştirme işlemi başlatılıyor..." + Style.RESET_ALL)
change_mac_address(user_input.interface, user_input.mac_address)

print(Fore.YELLOW + "Yeni MAC adresi kontrol ediliyor..." + Style.RESET_ALL)
finalized_mac = control_new_mac(user_input.interface)

if finalized_mac == user_input.mac_address:
    print(Fore.GREEN + "MAC adresiniz başarıyla değiştirildi!" + Style.RESET_ALL)
else:
    print(Fore.RED + "Hata! MAC adresi değişmedi." + Style.RESET_ALL)
