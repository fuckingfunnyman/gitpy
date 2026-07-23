import time
import sys
import random

def clear_screen():
    print("\033c", end="")

def type_effect(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def fake_hack_menu():
    clear_screen()
    while True:
        print("\033[1;31m" + "="*50 + "\033[0m")
        print("\033[1;32m          FAKE HACKER TERMINAL v1337          \033[0m")
        print("\033[1;31m" + "="*50 + "\033[0m")
        print("\033[1;33m1.\033[0m \033[1;37mPort Scanner\033[0m")
        print("\033[1;33m2.\033[0m \033[1;37mSQL Injection Attack\033[0m")
        print("\033[1;33m3.\033[0m \033[1;37mDDoS Flood\033[0m")
        print("\033[1;33m4.\033[0m \033[1;37mPassword Cracker\033[0m")
        print("\033[1;33m5.\033[0m \033[1;37mExploit Framework\033[0m")
        print("\033[1;33m6.\033[0m \033[1;37mGet Root Access\033[0m")
        print("\033[1;33m7.\033[0m \033[1;37mSteal Bitcoin Wallet\033[0m")
        print("\033[1;33m8.\033[0m \033[1;37mExit to Matrix\033[0m")
        print("\033[1;31m" + "="*50 + "\033[0m")
        
        choice = input("\033[1;36mroot@darkweb:\~$\033[0m ")
        
        if choice == "1":
            target = input("\033[1;35mEnter target IP: \033[0m")
            print(f"\033[1;32m[*] Scanning {target} for open ports...\033[0m")
            time.sleep(1.5)
            ports = [22, 80, 443, 3389, random.randint(1000, 9999)]
            for p in ports:
                print(f"\033[1;33m[+] Port {p} OPEN - Vulnerable\033[0m")
                time.sleep(0.4)
            print("\033[1;32mScan complete. 5 vulnerabilities found.\033[0m")
            
        elif choice == "2":
            target = input("\033[1;35mEnter target URL: \033[0m")
            print(f"\033[1;32m[*] Injecting SQL payload into {target}...\033[0m")
            time.sleep(2)
            type_effect("Database dumped successfully. 1,337,420 user records retrieved.")
            
        elif choice == "3":
            target = input("\033[1;35mEnter target IP: \033[0m")
            print(f"\033[1;31m[*] Launching SYN flood on {target}...\033[0m")
            for i in range(1, 11):
                print(f"\033[1;33m[ATTACK] Packet {i*1000} sent...\033[0m")
                time.sleep(0.3)
            print("\033[1;32mDDoS complete. Target is DOWN.\033[0m")
            
        elif choice == "4":
            print("\033[1;32m[*] Brute forcing password with 10 million combinations/sec...\033[0m")
            time.sleep(2)
            passwords = ["admin123", "password", "letmein", "hunter2", "1337hax"]
            for pw in passwords:
                print(f"\033[1;33m[+] Trying: {pw}\033[0m")
                time.sleep(0.5)
            print("\033[1;32mPassword cracked: ilovehacking2025\033[0m")
            
        elif choice == "5":
            print("\033[1;32mLoading Metasploit Framework (fake edition)...\033[0m")
            time.sleep(1.5)
            type_effect("Exploit executed. Shell obtained. You now own the machine.")
            
        elif choice == "6":
            print("\033[1;31mGaining root privileges...\033[0m")
            for i in range(5):
                print("." * (i+1), end=" ")
                time.sleep(0.6)
            print("\n\033[1;32mROOT ACCESS GRANTED. You are now god.\033[0m")
            
        elif choice == "7":
            print("\033[1;33mConnecting to Blockchain...\033[0m")
            time.sleep(1)
            print("\033[1;32m[+] 0.69 BTC transferred to your wallet.\033[0m")
            print("\033[1;31mWarning: FBI trace started (jk, this is fake)\033[0m")
            
        elif choice == "8":
            print("\033[1;31mDisconnecting from the Matrix... Goodbye hacker.\033[0m")
            break
            
        else:
            print("\033[1;31mInvalid option. Try harder.\033[0m")
        
        input("\n\033[1;36mPress Enter to return to menu...\033[0m")
        clear_screen()

if __name__ == "__main__":
    try:
        fake_hack_menu()
    except KeyboardInterrupt:
        print("\n\033[1;31mConnection terminated by user. Stay anonymous.\033[0m")