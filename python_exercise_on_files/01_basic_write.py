
try:
    h=open("01_basic_write.txt","w+")
    h.write('1,almasud,Abdullah Al Masud\n'
            '2,rimon,Rimol Ali\n'
            '3,niloy,Niloy Roy\n'
            '4,sourov,Sourov Deb Sharma\n'
            '5,sathi,Sathi Rani Roy\n'
            )

except IOError:
    print("An IOError has occurred!")
finally:
    h.close()


