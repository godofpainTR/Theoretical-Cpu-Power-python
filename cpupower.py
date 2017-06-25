import os
import time

def MIPSF():
    print("Enter your CPU clock (in MHz):")
    clock = int(input())
    print("Enter physical core count:")
    core = int(input())
    MIPSS = core * clock * ipcs
    MIPSD = core * clock * ipcd
    print(MIPSS, " MIPS (Single Precision)")
    print(MIPSD, " MIPS (Double Precision)")
    time.sleep(3)
    print("Type 1 to start over or type 2 to exit")
while True:
    print("Choose CPU brand:")
    print("1.AMD")
    print("2.Intel")
    ipcs = 1
    ipcd = 1
    ipcs == int(ipcs)
    ipcd == int(ipcd)
    choice = input()
    if choice == "1":
        print("Choose architecture:")
        print("1.K10 (Athlon,Phenom etc.)")
        print("2.Piledriver (FX-x3xx and 9590)")
        print("3.Bulldozer (Other FX processors)")
        print("4.Steamroller (AX series APUs)")
        print("5.Zen (Ryzen processors)")
        choice2 = input()
        if choice2 == "1":
            ipcs = 8
            ipcd = int(ipcs/2)
            MIPSF()
            choice3 = input()
            if choice3 == "1":
                os.system("cls" if os.name == "nt" else "clear")
                continue
            elif choice3 == "2":
                time.sleep(1)
                break
            else:
                raise TypeError
        elif choice2 == "2" or "3" or "4":
            ipcs = 8
            ipcd = int(ipcs / 2)
            MIPSF()
            choice3 = input()
            if choice3 == "1":
                os.system("cls" if os.name == "nt" else "clear")
                continue
            elif choice3 == "2":
                time.sleep(1)
                break
            else:
                raise TypeError
        elif choice2 == "5":
            ipcs = 16
            ipcd = int(ipcs / 2)
            MIPSF()
            choice3 = input()
            if choice3 == "1":
                os.system("cls" if os.name == "nt" else "clear")
                continue
            elif choice3 == "2":
                time.sleep(1)
                break
            else:
                raise TypeError
        else:
            raise TypeError
    elif choice == "2":
        print("Choose architecture:")
        print("1.Core2")
        print("2.Nehalem (Core i3/5/7-xxx series)")
        print("3.Sandy Bridge (Core i3/5/7-2xxx series)")
        print("4.Ivy Bridge (Core i3/5/7-3xxx series)")
        print("5.Haswell (Core i3/5/7-4xxx series)")
        print("6.Broadwell (Core i3/5/7-5xxx series)")
        print("7.Skylake or Kaby Lake (Core i3/5/7-6xxx or 7xxx series)")
        print("8.Intel Atom")
        choice5 = input()
        if choice5 == "1":
            ipcs = 8
            ipcd = int(ipcs / 2)
            MIPSF()
            choice3 = input()
            if choice3 == "1":
                os.system("cls" if os.name == "nt" else "clear")
                continue
            elif choice3 == "2":
                time.sleep(1)
                break
            else:
                raise TypeError
        elif choice5 == "2":
            ipcs = 8
            ipcd = int(ipcs / 2)
            MIPSF()
            choice3 = input()
            if choice3 == "1":
                os.system("cls" if os.name == "nt" else "clear")
                continue
            elif choice3 == "2":
                time.sleep(1)
                break
            else:
                raise TypeError
        elif choice5 == "3":
            ipcs = 16
            ipcd = int(ipcs / 2)
            MIPSF()
            choice3 = input()
            if choice3 == "1":
                os.system("cls" if os.name == "nt" else "clear")
                continue
            elif choice3 == "2":
                time.sleep(1)
                break
            else:
                raise TypeError
        elif choice5 == "4":
            ipcs = 16
            ipcd = int(ipcs / 2)
            MIPSF()
            choice3 = input()
            if choice3 == "1":
                os.system("cls" if os.name == "nt" else "clear")
                continue
            elif choice3 == "2":
                time.sleep(1)
                break
            else:
                raise TypeError
        elif choice5 == "5" or "6" or "7":
            ipcs = 32
            ipcd = int(ipcs / 2)
            MIPSF()
            choice3 = input()
            if choice3 == "1":
                os.system("cls" if os.name == "nt" else "clear")
                continue
            elif choice3 == "2":
                time.sleep(1)
                break
            else:
                raise TypeError
        elif choice5 == "8":
            ipcs = 4
            ipcd = int(ipcs / 2)
            MIPSF()
            choice3 = input()
            if choice3 == "1":
                os.system("cls" if os.name == "nt" else "clear")
                continue
            elif choice3 == "2":
                time.sleep(1)
                break
            else:
                raise TypeError
        else:
            raise TypeError
    else:
        raise TypeError
