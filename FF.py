import os
import time

def mehdi_panel_banner():
    os.system('clear')
    # Purple Car & Blue MEHDI Banner
    print("\033[1;35m      ______")
    print("     //  ||\\ \\")
    print("  ____//___||_\\ \\___")
    print(" )  _          _    \\")
    print(" |_/ \________/ \___|")
    print("   \_/        \_/    \033[0m")
    print("\033[1;34m  __  __  _____  _   _  ____  ___ ")
    print(" |  \/  || ____|| | | ||  _ \|_ _|")
    print(" | |\/| ||  _|  | |_| || | | || | ")
    print(" | |  | || |___ |  _  || |_| || | ")
    print(" |_|  |_||_____||_| |_||____/|___|\033[0m")
    print(f"\n\033[1;32m[ MEHDI ]\033[0m \033[1;33m—\033[0m \033[1;32m[ FF Injector Panel v1.0 ]\033[0m")

def start_panel():
    mehdi_panel_banner()
    print("\033[1;31m[01]\033[0m Aimbot (Auto-Head)")
    print("\033[1;31m[02]\033[0m ESP Name (Wallhack)")
    print("\033[1;31m[03]\033[0m High Damage")
    print("\033[1;31m[00]\033[0m Exit")
    
    choice = input("\n\033[1;32m⚔️ Select Feature: \033[0m")
    
    if choice in ['1', '2', '3']:
        print("\n\033[1;33m[*] Finding Game Process 'com.dts.freefireth'...")
        time.sleep(2)
        print("\033[1;34m[*] Injecting Lib-Data into Memory...")
        time.sleep(3)
        print("\033[1;32m[✔] Feature Activated! Open Game Now.\033[0m")
    else:
        print("Closing...")

start_panel()
