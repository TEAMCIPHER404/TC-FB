import sys, platform

bit = platform.architecture()[0]
if bit == '64bit':
    try:
        __import__("TC").chck()
    except:
        pass
elif bit == '32bit':
    try:
        __import__("TC").chck()
    except:
        sys.exit("Sorry Your device is not compatible")
