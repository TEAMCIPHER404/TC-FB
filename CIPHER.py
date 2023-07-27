import sys, platform, os
os.system('git pull >/dev/null 2>&1')
bit = platform.architecture()[0]
if bit == '64bit':
    try:
        if not os.path.exists("TC_FILE.cpython-311.so"):
            print(" [PLEASE WAIT...]")
            os.system("curl -LJO https://github.com/TEAMCIPHER404/TC-FILE/raw/main/TC_FILE.cpython-311.so > /dev/null 2>&1")
        import TC
    except KeyboardInterrupt:
        exit()
elif bit == '32bit':
    try:
        import TC
    except KeyboardInterrupt:
        sys.exit()
    except:
        sys.exit("Opps Your device is not compatible")
