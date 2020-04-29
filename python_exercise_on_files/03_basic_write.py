
try:
    h=open("03_basic_read.txt","r+")
    for i in h:
         b=i.split(",")
         print(b[0]+'-'+b[2],end='')

except IOError:
    print("An IOError has occurred!")
finally:
    h.close()


