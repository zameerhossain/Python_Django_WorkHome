author=[[1,'almasud','Abdullah Al Masud'],
[2,'rimon','Rimol Ali'],
[3,'niloy','Niloy Roy'],
[4,'sourov','Sourov Deb Sharma'],
[5,'sathi','Sathi Rani Roy']]
try:
    h=open("02_basic_write.txt","w+")
    for i in author:
        c=0
        for j in i:
            c=c+1
            if c!=len(i):
                h.write(str(j)+',')
            else:
                h.write(str(j))
        h.write('\r')
except IOError:
    print("An IOError has occurred!")
finally:
    h.close()


