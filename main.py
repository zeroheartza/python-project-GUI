from tkinter import *
from tkinter import messagebox
import tkinter as tk
from functools import partial
import random
#import os
import subprocess

data = []
f = open("StatusUser.txt", "r")

for line in f:
    data.append((line))

f.close()
StatusUser=[]
for i in range(len(data)):
    z=data[i].rstrip('\n')

    StatusUser.append(z)

data = []
f = open("COIN.txt", "r")

for line in f:
    data.append((line))

f.close()
coin=[]
for i in range(len(data)):
    z=data[i].rstrip('\n')

    coin.append(z)
Player=[]
Data=[]
Color=["Black","Red","Blue","Yellow"]
Num=[52,37,10,1]
Color_Random=[]
game=[]
coin_in=[]

coin_input=[]
b=[]
az=["a"," "]

        
def warning():
    messagebox.showinfo(title="สำหรับ admin",message="สามารถใช้ได้เฉพาะ admin")
def warning1():
    messagebox.showinfo(title="ไม่ได้ใส่จำนวนเงิน",message="กรุณาใส่จำนวนเงิน")


        
        
               
def Login():
    #os.system('game1.py')
    subprocess.Popen("Login.py 1", shell=True)
    root.destroy()         
        
    
    

    

        

    
def CreateUser():
    if StatusUser[0]=="admin":
        subprocess.Popen("CreateUser.py 1", shell=True)
        #os.system('CreateUser.py')
        root.destroy()
    else:
        warning()
    
def DeleteUser():
    if StatusUser[0]=="admin":
        subprocess.Popen("DeleteUser.py 1", shell=True)
        #os.system('CreateUser.py')
    root.destroy()
    #else:
        #warning()
    
    
def Setcoin():
    if StatusUser[0]=="admin":
        subprocess.Popen("Setcoin.py 1", shell=True)
        root.destroy()
    else:
        warning()
    
    
def game():
    #os.system('game1.py')
    subprocess.Popen("game.py 1", shell=True)
    root.destroy()
    
    

root = tk.Tk()




root.geometry('250x150')
filename = PhotoImage(file ="bg1.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

root.title('Main')
key1 = tk.StringVar()





if StatusUser[0]=="admin":
    buttonCal = tk.Button(root, text="Create User", command=CreateUser).place(x=90, y=20, relwidth=0.3, relheight=0.2)
if StatusUser[0]=="admin":
    buttonCa2 = tk.Button(root, text="Delete User", command=DeleteUser).place(x=90, y=50, relwidth=0.3, relheight=0.2)
if StatusUser[0]=="admin":
    buttonCa3 = tk.Button(root, text="Set coin", command=Setcoin).place(x=90, y=80, relwidth=0.3, relheight=0.2)
if StatusUser[0]=="admin":
    buttonCa4 = tk.Button(root, text="Play Game", command=game).place(x=90, y=110, relwidth=0.3, relheight=0.2)
if StatusUser[0]!="admin":
    buttonCa4 = tk.Button(root, text="Play Game", command=game).place(x=90, y=60, relwidth=0.3, relheight=0.2)

buttonCa5 = tk.Button(root, text="Logout", command=Login).place(x=185, y=118, relwidth=0.25, relheight=0.2)


root.mainloop()
