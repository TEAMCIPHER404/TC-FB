import sys, platform

bit = platform.architecture()[0]
if bit == '64bit':
    try:
        __import__("TC").chck()
    except KeyboardInterrupt:
        exit()
elif bit == '32bit':
    try:
        __import__("TC").chck()
    except KeyboardInterrupt:
        sys.exit()
    except:
        sys.exit("Opps Your device is not compatible")
