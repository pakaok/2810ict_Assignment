
import pandas as pd
from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt
df = pd.read_csv('Crash Statistics Victoria.csv')

wid='1075'
hgt='600'
lst_day=['01','02','03','04','05','06','07','08','09']+[i for i in range(10,32)]
lst_month=[i for i in range(1,13)]
lst_year=[i for i in range(2013,2020)]
date_list=[]

def btn1():
    print('hello')
            
root = Tk()
root.title('2810ICT/Kim/Mausham/Sam')
root.geometry(wid+'x'+hgt+'+170+50')
# root_style=ttk.Style()
# root_style.theme_use('alt')
# root.resizable(False,False)
btn1 = Button(root,width=10,height=8,text='start',command=btn1)
xpos=20
ypos=500
btn1.place(x=xpos ,y=450)

combobox_ypos_0=25
day_comboBox_0= ttk.Combobox(root,height=len(lst_day),width=5, values=lst_day,state='readonly')
day_comboBox_0.set('01')
day_comboBox_0.place(x=xpos+100,y=ypos-combobox_ypos_0)
month_comboBox_0=ttk.Combobox(root,height=len(lst_month),width=5,values=lst_month,state='readonly')
month_comboBox_0.set('1')
month_comboBox_0.place(x=xpos+175,y=ypos-combobox_ypos_0)
year_comboBox_0=ttk.Combobox(root,height=len(lst_year),width=5,values=lst_year,state='readonly')
year_comboBox_0.set('2013')
year_comboBox_0.place(x=xpos+250,y=ypos-combobox_ypos_0)
lb1=Label(root,text='/')
lb2=Label(root,text='/')
lb1.place(x=xpos+160,y=ypos-combobox_ypos_0)
lb2.place(x=xpos+235,y=ypos-combobox_ypos_0)
