from tkinter import * 
import tkinter as tk
from functools import partial
import os
import subprocess
StatusUser=[0]
loginuser=[]

data = []
f = open("idadmin.txt", "r")

for line in f:
    data.append((line))

f.close()
numadmin=[]
for i in range(len(data)):
    z=data[i].rstrip('\n')

    numadmin.append(z)

data = []
f = open("USER.txt", "r")

for line in f:
    data.append((line))

f.close()
ID=[]
for i in range(len(data)):
    z=data[i].rstrip('\n')

    ID.append(z)





#print("Username Connect!!")


data = []
f = open("Password.txt", "r")

for line in f:
    data.append((line))

f.close()
PASSWORD=[]
for i in range(len(data)):
    z=data[i].rstrip('\n')

    PASSWORD.append(z)





#print("Password Connect!!")



def login(label_result,label_result1, KEY1, KEY2,label_result2):
    KEY1 = (KEY1.get())
    KEY2 = (KEY2.get())
    KEY3=""     
    if KEY1 in ID:
        KEY4="correct"
        #print("Username Correct")
        i=0
        while True:
            if KEY1==ID[i]:
                
                break
            i+=1
        loginuser.append(i)
        #print(i)
        
    else:
        KEY4="try again"
        #print("Username Invalid")
        
        

        

        
    if KEY1 in ID:
        if KEY2 == PASSWORD[i] :
            KEY2="correct"
            #print("Password Correct")
        else:
            KEY2="try again"
            #print("Password Invalid")
        if KEY4=="correct" and KEY2=="correct":
            KEY3="Login Success"
            #print(numadmin)
            StatusUser.clear()
            
            if KEY1 in numadmin:
                StatusUser.append("admin")
            else:
                StatusUser.append("0")
                    
                
            n = open("StatusUser.txt", "w")
            for v in StatusUser:
                n.write(str(v) + "\n")
            n.close()
            
            t = open("loginuser.txt", "w")
            for v in loginuser:
                t.write(str(v) + "\n")
            t.close()
            #os.system('main.py')
            subprocess.Popen("main.py 1", shell=True)
            root.quit()
            
            
        else:
            KEY3=""
    else:
        KEY2="try again"
        
        
        
      
    
    
    
    label_result.config(text=" %s" % KEY4)
    label_result1.config(text="%s" % KEY2)
    label_result2.config(text="%s"% KEY3)
    return
 
root = tk.Tk()
root.geometry('250x150')
filename = PhotoImage(file ="bg.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
root.title('Login')
 
key1 = tk.StringVar()
key2 = tk.StringVar()

labelTitle = tk.Label(root, text="").grid(row=1, column=2)
labelKey1 = tk.Label(root, text="\nUsername").grid(row=2, column=0)
labelkey2 = tk.Label(root, text="Password").grid(row=3, column=0)
labelResult = tk.Label(root)
labelResult.grid(row=2, column=9)
labelResult1 = tk.Label(root)
labelResult1.grid(row=3, column=9)
labelResult2 = tk.Label(root)
labelResult2.grid(row=4, column=2)

 
entrykey1 = tk.Entry(root, textvariable=key1).grid(row=2, column=2)
entrykey2 = tk.Entry(root, textvariable=key2, show='*').grid(row=3, column=2)


login = partial(login, labelResult,labelResult1, key1, key2,labelResult2)
buttonCal = tk.Button(root, text="Login", command=login).grid(row=5, column=2)
root.mainloop()
