#!/usr/bin/python3
#enryu
import pandas as pd
from pandas import read_csv
from tkinter import *
import time
filename = "data.csv"
i=[]
p=[]
df=None
raw_data=None
class Store:
    def add(self):
        global i 
        global p
        global filename
        global raw_data
        item=input("Enter the name of product->")
        price=int(input("Enter the price of product->"))
        i.append(item)
        p.append(price)
        
        raw_data={
            "ITEM":i,
            "PRICE":p
        }
        global df
        df=pd.DataFrame(raw_data)
        df["PRICE"]=df['PRICE'].astype(int)
        with open(filename,'a') as f:
            df.to_csv(f,header=False,index=False)
        print(df)
        print("Item was added sucessfully")
    def Search(self):
        global raw_data
        find=input("Enter the product you wanna find->")
        print("Searching for product....")
        time.sleep(2)
        b=pd.read_csv(filename,index_col='ITEM')
        a=b.loc[find]
        if a.any()==True:
            print(find,"is available")
        else:
            print(find,"is not available")
    def product(self):
        global filename
        csvfile=pd.read_csv(filename)
        print(csvfile)
    def discount(self):
        global raw_data
        z=[]
        global df
        global filename
        #b=pd.read_csv(filename,index_col='PRICE')
        #v=b.values.tolist()
        df=pd.read_csv(filename)
        a=df['PRICE'].values.tolist()
        for x in a:
            if x>=1000:
                x=x-(x//10)
                z.append(x)
            else:
                z.append("NA")
        df["DISCOUNT"]=z
        #with open(filename,'a') as f:
        # df["DISCOUNT"].to_csv(f,header=False,index=False)   
        print(df) 
s=Store() 
def main():
    print("****Welcome to MIRACLE****")
    print("1.Enter the item:")
    print("2.Search for item:")
    print("3.All the availabe product:")
    print("4.Discout on items:")
    print("5.Exit")
    ch=int(input("Select the choice->"))
    global df
    global filename
    if ch==1:
        s.add()
    elif ch==2:
        s.Search()
    elif ch==3:
        print("****All the availabe product are****")
        s.product()
        ans=input("Do you wann add product?->")
        if ans=='y' or ans=='yes':
            s.add()
        else:
            exit
    elif ch==4:
        print("****List of discounted item****")
        s.discount()
    else:
        print("Invalid choice")
        main()
if __name__=="__main__":
    main()
