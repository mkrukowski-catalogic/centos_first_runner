# Script for Running and Clicking on System Login Screen in vSphere

This script automates the process of logging in to a system displayed in vSphere and performs a series of commands. It utilizes the pyautogui library for GUI automation, the time module for adding delays, and the Faker library for generating fake data.
Prerequisites

    Python 3.x installed
    Required Python libraries: pyautogui, time, faker

Instructions

1. Install the required libraries by running the following commands in your terminal:

```
pip install pyautogui
pip install Faker
```

2. Open a text editor and create a new Python file. Copy the script into the file.

3. Customize the script variables to match your specific requirements:

```
login = 'login'
password = 'password'
interval = 1
host_prefix = 'prefix'
host_name_command = f"hostname {host_prefix}-{fake.user_name()}"
```
* login: The login username.
* password: The login password.
* interval: The interval between each command execution (in seconds).
* host_prefix: The prefix to be added to the hostname.
* host_name_command: The command to change the hostname using the Faker library.

4. Save the file with a suitable name, such as vsphere_login_script.py.

5. Open a terminal or command prompt and navigate to the directory where the script file is saved.

6. Execute the script by running the following command and click on system login screen:
```
    python vsphere_login_script.py
```
After executing the script, it will automatically perform the following actions:
* Type the login username.
* Press Enter.
* Type the login password.
* Press Enter.
* Execute the command to change the hostname using the host_name_command variable.
* Execute additional commands to modify network connections, disable the firewalld service, and reboot the system.

Make sure to verify the successful execution of the script and validate the changes made to the system.

Note: This script is intended for educational or testing purposes only. Use it responsibly and ensure that you have the necessary permissions and authorization before automating actions on systems.
