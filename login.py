username="yeagre_sama"
password="2009"
trues=3
while True:
    user=input("pleas entre your username\n")
    pas=input("pleas entre your pass\n")
    if password!=pas or username!=user:
        print("the username or the password is not corect try aggain")
        trues-=1
    if trues ==0:
        print("your accont is locked ")
        break
    elif password==pas and user==username:
        print("welcome admine")
        while True:
           liste=int(input("1.show prifile \n2.change password\n3.logout\n"))
           if liste ==1:
               print("============profile===========\nuser==",username,"\n================")
           elif liste ==2:
               old_pass=input("pleas entre your old password\n")
               if old_pass==password:
                   new_pass=input("pleas entre your new password \n")
                   password=new_pass
                   print("yor password is changed")
               else :
                   print("your old password is no corect try again")
           else:
               print("good bye ")
               break
    break