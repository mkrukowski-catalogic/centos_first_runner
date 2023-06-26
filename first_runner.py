#Run script and click on system login screen displayed in VSphare
import pyautogui
import time
from faker import Faker
fake = Faker()

login = 'login'
password = 'password'
interval = 1
host_prefix = 'prefix'
host_name_command = f"hostnamectl set-hostname {host_prefix}-{fake.user_name()}"

time.sleep(2)

commands = (login, password,host_name_command,'nmcli connection modify ens192 ipv4.method auto', 'nmcli connection up ens192', 'systemctl disable firewalld', 'systemctl stop firewalld', 'logout')

def input_function(*args):
    for arg in args:
        index = args.index(arg)
        x = len(commands)
        if index == len(commands)-1:
            time.sleep(1)
        pyautogui.write(arg, interval = 0.1)
        pyautogui.press('Enter')
        time.sleep(interval)
print('FIN')
