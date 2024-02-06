from tkinter import *
from tkinter import messagebox
import tkinter as tk
from functools import partial
import random
import subprocess




    
    

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
loginuser=[]
Color=["Black","Red","Blue","Yellow"]
Num=[52,37,10,1]
Color_Random=[]
game=[]
coin_in=[]
ss=[]

coin_input=[]
b=[]
az=["a"," "]
def sc():
    loginuser.clear()

    if ss[0] in ID:
        i=ID.index(ss[0])
        loginuser.append(i)
        print('sssss',loginuser)
    else:
        warning()
        
        
        
        
       
        
            
                
                
def main():
    #os.system('game1.py')
    subprocess.Popen("main.py 1", shell=True)
    root.destroy()            
        
def del_space(a):
    for n in range(len(az)):
        b.clear()
        v=""
        a=list(a)
        k=a.count(az[n])
        for i in range(k):
            a.remove(az[n]) 
        for i in range(len(a)):
            v+=a[i]
        b.append(v)
        print(b)

        
def warning():
    messagebox.showinfo(title="ไม่พบ User",message="ไม่พบ User")
def warning1():
    messagebox.showinfo(title="ไม่ได้ใส่จำนวนเงิน",message="กรุณาใส่จำนวนเงิน")

def test():
    ncode()
    del_space(coin_input[0])
    coin_input.clear()
    coin_input.append(b[0])
    print(coin_input[0])
    if coin_input[0]=="":
        coin_input.clear()
        coin_input.append("0")
        warning1()
           
        
        
        
    
    
def ncode(KEY1,KEY2):
      coin_input.clear()
      key1=(KEY1.get())
      key2=(KEY2.get())
      ss.clear()
      ss.append(key2)
      coin_input.append(key1)
      print(ID)
      print("ss:",ID)
def Random():
    Color_Random.clear()
    Color_random=random.choice(Data)
    #print(Color_random)
    Color_Random.append(Color_random)
    print(Color_Random)
    

    
    
        

    

    
def set_coin():
    
    test()
    sc()
    x=int(loginuser[0])
    print(x)
    
    coiny.remove(str(coiny[x]))
    print(coiny)
    
    
    print(coin_input[0])
    coiny.insert(x,coin_input[0])
    print(coiny)
    f = open("COIN.txt", "w")
    for v in coiny:
        f.write(str(v) + "\n")
    f.close()
    #coin.clear()
    #coin.append(coiny[0])
    
    
    background_label1 = Label(root, text="Coin : %d"%int(coiny[x]))
    background_label1.place(x=150, y=0, relwidth=0.4, relheight=0.3)
        


    

root = tk.Tk()


root.geometry('250x150')
filename = PhotoImage(file ="bg.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
#background_label1 = Label(root, text="Coin : %d"%int(coiny[int(loginuser[0])]))
#background_label1.place(x=150, y=0, relwidth=0.4, relheight=0.3)
root.title('Set Coin')
key1 = tk.StringVar()
key2 = tk.StringVar()

labelKey1 = tk.Label(root, text="Username").place(x=0, y=40, relwidth=0.3, relheight=0.1)
labelkey2 = tk.Label(root, text="Coin").place(x=0, y=70, relwidth=0.3, relheight=0.1)
entrykey1 = tk.Entry(root, textvariable=key1).place(x=70, y=70, relwidth=0.5, relheight=0.15)
entrykey2 = tk.Entry(root, textvariable=key2).place(x=70, y=40, relwidth=0.5, relheight=0.15)
background_label1 = Label(root, text="input coin : ")

ncode = partial(ncode,key1,key2)

buttonCal = tk.Button(root, text="Set Coin", command=set_coin).place(x=90, y=100, relwidth=0.3, relheight=0.15)
buttonCa2 = tk.Button(root, text="Back", command=main).place(x=185, y=118, relwidth=0.25, relheight=0.2)

root.mainloop()
