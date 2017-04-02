try:
    num=5/0
    raise TypeError("RajeshException")
except: 
    print("The error has been excepted (catched)")
finally:
    print("idan last uh print aagum")
