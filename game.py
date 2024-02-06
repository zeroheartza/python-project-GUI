from tkinter import *
from tkinter import messagebox
import tkinter as tk
from functools import partial
import random
import subprocess

data = []
f = open("loginuser.txt", "r")

for line in f:
    data.append((line))

f.close()
loginuser=[]
for i in range(len(data)):
    z=data[i].rstrip('\n')

    loginuser.append(z)
    #print(loginuser)

    
data = []
f = open("COIN.txt", "r")

for line in f:
    data.append((line))

f.close()
coinx=[]
for i in range(len(data)):
    z=data[i].rstrip('\n')

    coinx.append(z)
    #print(coinx)
coin=[]
numi=int(loginuser[0])
#print(numi)
coin.append(coinx[numi])
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
        #print(b)

        
def warning():
    messagebox.showinfo(title="เงินหมด",message="coin หมด ")
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
    if int(coin[0])-int(coin_input[0])<0:
        coin_input.clear()
        coin_input.append("0")
        warning()
    
        
        
        
        
        
        
    
    
def ncode(KEY1):
      coin_input.clear()
      key1=(KEY1.get())
      
      coin_input.append(key1)
      #print(coin_input)
def Random():
    Color_Random.clear()
    Color_random=random.choice(Data)
    #print(Color_random)
    Color_Random.append(Color_random)
    #print(Color_Random)
    
def set():
    
    
    Color_Random.clear()
    for i in range(len(Color)):
        for j in range(Num[i]):
            Data.append(Color[i])

    #print(Data)
    Random()
    
    
        
def start():
    

    if Player[0]==Color_Random[0]:
        #print(len(Data))
        Coin_New=int(coin[0])+int(coin_input[0])-int(coin_in[0])
        coin.clear()
        coin.append(Coin_New)
        print("coinx:",coinx)
        print("coinx[numi]:",coinx[numi])
        coinx.remove((coinx[numi]))
        print("coinx:",coinx)
    
    
        print("coin[0]:",coin[0])
        coinx.insert(numi,coin[0])
        print("coinx : " ,coinx)
        
        f = open("COIN.txt", "w")
        for v in coinx:
            f.write(str(v) + "\n")
        f.close()
        
        game.clear()
        game.append("win")
        #labelResult = tk.Label(root, text=game[0])
        #labelResult.grid(row=1, column=5)
        #labelResult1 = tk.Label(root, text="Coin:%d"%int(coin[0]))
        #labelResult1.grid(row=1, column=0)
        background_label1 = Label(root, text="Coin : %d"%int(coin[0]))
        background_label1.place(x=150, y=5, relwidth=0.4, relheight=0.2)
        background_label2 = Label(root, text="Color : %s"%str(Color_Random[0]))
        background_label2.place(x=0, y=0, relwidth=0.3, relheight=0.3)
        Random()
    else:
        Coin_New=int(coin[0])-int(coin_in[0])
        coin.clear()
        coin.append(Coin_New)
        print("coinx:",coinx)
        print("coinx[numi]:",coinx[numi])
        coinx.remove((coinx[numi]))
        print("coinx:",coinx)
    
    
        print("coin[0]:",coin[0])
        coinx.insert(numi,coin[0])
        print("coinx : " ,coinx)
        f = open("COIN.txt", "w")
        for v in coinx:
            f.write(str(v) + "\n")
        f.close()
        print("lose")
        game.clear()
        game.append("lose")
        #labelResult = tk.Label(root, text=game[0])
        #labelResult.grid(x=1, column=5)
        background_label1 = Label(root, text="Coin : %d"%int(coin[0]))
        background_label1.place(x=150, y=5, relwidth=0.4, relheight=0.2)
        background_label2 = Label(root, text="Color : %s"%str(Color_Random[0]))
        background_label2.place(x=0, y=0, relwidth=0.3, relheight=0.3)
        Random()
def main():
    #os.system('game1.py')
    subprocess.Popen("main.py 1", shell=True)
    root.destroy() 
    
def BLACK():
    Player.clear()
    Player.append("Black")
    
    test()
    coin_in.clear()
    coin_in.append(coin_input[0])
    coin_black=int(coin_input[0])*2
    print(coin_black)
    coin_input.clear()
    coin_input.append(coin_black)
    print(coin_input)
    
    start()
    
def RED():
    Player.clear()
    Player.append("Red")
    #print(Player)
    test()
    coin_in.clear()
    coin_in.append(coin_input[0])
    coin_black=int(coin_input[0])*3
    print(coin_black)
    coin_input.clear()
    coin_input.append(coin_black)
    print(coin_input)
    start()
def BLUE():
    Player.clear()
    Player.append("Blue")
    test()
    #print(Player)
    coin_in.clear()
    coin_in.append(coin_input[0])
    coin_black=int(coin_input[0])*5
    print(coin_black)
    coin_input.clear()
    coin_input.append(coin_black)
    print(coin_input)
    start()
def YELLOW():
    Player.clear()
    Player.append("Yellow")
    #print(Player)
    test()
    coin_in.clear()
    coin_in.append(coin_input[0])
    coin_black=int(coin_input[0])*20
    #print(coin_black)
    coin_input.clear()
    coin_input.append(coin_black)
    print(coin_input)
    start()
    

root = tk.Tk()

set()


root.geometry('250x150')
filename = PhotoImage(file ="bg.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
background_label1 = Label(root, text="Coin : %d"%int(coin[0]))
background_label1.place(x=150, y=5, relwidth=0.4, relheight=0.2)
root.title('Game')
key1 = tk.StringVar()

labelTitle = tk.Label(root, text="\n\n").grid(row=1, column=0)
labelTitle = tk.Label(root, text="\n").grid(row=3, column=0)
labelTitle1 = tk.Label(root, text="   ").grid(row=5, column=1)



labelTitle2 = tk.Label(root, text="   ").grid(row=5, column=3)
labelTitle3 = tk.Label(root, text="   ").grid(row=5, column=5)
labelTitle4 = tk.Label(root, text="   ").grid(row=5, column=7)
entrykey1 = tk.Entry(root, textvariable=key1).place(x=80, y=40, relwidth=0.5, relheight=0.15)
background_label1 = Label(root, text="input coin : ")
background_label1.place(x=7, y=45, relwidth=0.25, relheight=0.1)
ncode = partial(ncode,key1)

tk.Label(root, text="x2").place(x=10, y=90, relwidth=0.175, relheight=0.15)
tk.Label(root, text="x3").place(x=70, y=90, relwidth=0.175, relheight=0.15)
tk.Label(root, text="x5").place(x=130, y=90, relwidth=0.175, relheight=0.15)
tk.Label(root, text="x20").place(x=190, y=90, relwidth=0.175, relheight=0.15)

buttonCal = tk.Button(root, text="Black", command=BLACK).place(x=10, y=70, relwidth=0.175, relheight=0.15)
buttonCa2 = tk.Button(root, text="Red", command=RED).place(x=70, y=70, relwidth=0.175, relheight=0.15)
buttonCa3 = tk.Button(root, text="Blue", command=BLUE).place(x=130, y=70, relwidth=0.175, relheight=0.15)
buttonCa4 = tk.Button(root, text="Yellow", command=YELLOW).place(x=190, y=70, relwidth=0.175, relheight=0.15)
buttonCa5 = tk.Button(root, text="Back", command=main).place(x=185, y=118, relwidth=0.25, relheight=0.2)


root.mainloop()
