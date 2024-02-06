from tkinter import * 
import tkinter as tk
from functools import partial
from tkinter import messagebox
import subprocess
numi=[]
ss=[]
data = []
f = open("COIN.txt", "r")

for line in f:
    data.append((line))

f.close()
coiny=[]
for i in range(len(data)):
    z=data[i].rstrip('\n')

    coiny.append(z)
    
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

def sc():
    numi.clear()

    if ss[0] in ID:
        i=ID.index(ss[0])
        numi.append(i)
        print('sssss',numi)
    else:
        warning()
def main():
    #os.system('game1.py')
    subprocess.Popen("main.py 1", shell=True)
    root.destroy()
def warning():                   
    messagebox.showinfo(title="User หรือ Password ไม่ถูกต้อง",message="User หรือ Password ไม่ถูกต้อง")
def warning1():
    messagebox.showinfo(title="Password ไม่ถูกต้อง",message="Password ไม่ถูกต้อง")

def warning2():
    messagebox.showinfo(title="Delete User Correct",message="Delete User สำเร็จ")
def warnin3():                   
    messagebox.showinfo(title="",message="")

def call_result(label_result,label_result1, KEY1, KEY2,label_result2):
    KEY1 = (KEY1.get())
    KEY2 = (KEY2.get())
    ss.clear()
    ss.append(KEY1)
    sc()
    KEY3=""
    if KEY1 in ID:
        if KEY2 in PASSWORD:

            if KEY1!="":
                ID.remove(KEY1)
                f = open("USER.txt", "w")
                for v in ID:
                    f.write(str(v) + "\n")
                KEY1="Correct"
               
                f.close()
            else:
                KEY1=""


            if KEY2 !="":
                PASSWORD.remove(KEY2)
                f = open("PASSWORD.txt", "w")
                for v in PASSWORD:
                    f.write(str(v) + "\n")
                KEY2="correct"
                
                
                f.close()
                x=int(numi[0])
                coiny.remove(str(coiny[x]))
                f = open("COIN.txt", "w")
                for v in coiny:
                    f.write(str(v) + "\n")
                f.close()
            else:
                KEY2=""
                
            if KEY1 != "" and KEY2 != "":
                KEY3="Delete User Correct"
                warning2()
                    
                
                

            
            
           
                
              
            
            
            
            label_result.config(text=" %s" % KEY1)
            label_result1.config(text="%s" % KEY2)
            label_result2.config(text="%s"% KEY3)
            return
        else:
            warning1()
    else:
        warning()
        
 
root = tk.Tk()
root.geometry("250x150")
filename = PhotoImage(file ="bg.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
root.title("DeleteUser")
 
key1 = tk.StringVar()
key2 = tk.StringVar()
labelTitle = tk.Label(root, text="").grid(row=0, column=2) 

labelKey1 = tk.Label(root, text="Username").grid(row=1, column=0)
labelKey2 = tk.Label(root, text="Password").grid(row=2, column=0)
labelResult = tk.Label(root)
labelResult.grid(row=1, column=9)
labelResult1 = tk.Label(root)
labelResult1.grid(row=2, column=9)
labelResult2 = tk.Label(root)
labelResult2.grid(row=3, column=2)

 
entryKey1 = tk.Entry(root, textvariable=key1).grid(row=1, column=2)
entryKey2 = tk.Entry(root, textvariable=key2).grid(row=2, column=2)
call_result = partial(call_result, labelResult,labelResult1, key1, key2,labelResult2)
buttonCal = tk.Button(root, text="Create", command=call_result).grid(row=4, column=2)
buttonCa2 = tk.Button(root, text="Back", command=main).place(x=185, y=118, relwidth=0.25, relheight=0.2)

root.mainloop()



 
