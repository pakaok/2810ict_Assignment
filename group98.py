
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

combobox_ypos=25
day_comboBox_1= ttk.Combobox(root,height=len(lst_day),width=5, values=lst_day,state='readonly')
day_comboBox_1.set('01')
day_comboBox_1.place(x=xpos+100,y=ypos+combobox_ypos)
month_comboBox_1=ttk.Combobox(root,height=len(lst_month),width=5,values=lst_month,state='readonly')
month_comboBox_1.set('1')
month_comboBox_1.place(x=xpos+175,y=ypos+combobox_ypos)
year_comboBox_1=ttk.Combobox(root,height=len(lst_year),width=5,values=lst_year,state='readonly')
year_comboBox_1.set('2016')
year_comboBox_1.place(x=xpos+250,y=ypos+combobox_ypos)
lb3=Label(root,text='/')
lb4=Label(root,text='/')
lb3.place(x=xpos+160,y=ypos+combobox_ypos)
lb4.place(x=xpos+235,y=ypos+combobox_ypos)
lb5=Label(root,text='From')
lb6=Label(root,text='To')
lb5.place(x=xpos+395/2,y=ypos-combobox_ypos_0-15,anchor=CENTER)
lb6.place(x=xpos+395/2,y=ypos+combobox_ypos-15,anchor=CENTER)




option_ypos=25
option_ypos_1=50
option_val=IntVar()
analyze_option1= Radiobutton(root,text='one',value=1,variable=option_val)
analyze_option1.select()
analyze_option2= Radiobutton(root,text='two',value=2,variable=option_val)
analyze_option3= Radiobutton(root,text='three',value=3,variable=option_val)
analyze_option4= Radiobutton(root,text='four',value=4,variable=option_val)
analyze_option5= Radiobutton(root,text='fifth',value=5,variable=option_val)  

search_text= Entry(root,width=30)
search_text.place(x=xpos+600,y=ypos+option_ypos*2-option_ypos_1+5)

analyze_option1.place(x=xpos+325,y=ypos-option_ypos_1)
analyze_option2.place(x=xpos+325,y=ypos+option_ypos-option_ypos_1)
analyze_option3.place(x=xpos+325,y=ypos+option_ypos*2-option_ypos_1)
analyze_option4.place(x=xpos+325,y=ypos+option_ypos*3-option_ypos_1)
analyze_option5.place(x=xpos+325,y=ypos+option_ypos*4-option_ypos_1)   

speedzone=['30km/hr', '40 km/hr','50 km/hr', '60 km/hr','70 km/hr','75 km/hr','80 km/hr', '90 km/hr',
           '100 km/hr','110 km/hr','Other speed limit','Camping grounds or off road' , 'Not known']
speedzone.sort()
speed_comboBox= ttk.Combobox(root,height=len(speedzone),width=15, values=speedzone,state='readonly')
speed_comboBox.set('Speed Select')
speed_comboBox.place(x=xpos+600,y=ypos+option_ypos*4-option_ypos_1)


tree= ttk.Treeview(root,columns=[i for i in range(1,12)],show='headings',height=19)
tree.column(1,width=95,anchor='center')
tree.column(2,width=70,anchor='center')
tree.column(3,width=50,anchor='center')
tree.column(4,width=85,anchor='center')
tree.column(5,width=180,anchor='center')
tree.column(6,width=80,anchor='center')
tree.column(7,width=120,anchor='center')
tree.column(8,width=120,anchor='center')
tree.column(9,width=90,anchor='center')
tree.column(10,width=80,anchor='center')
tree.column(11,width=80,anchor='center')

tree.heading(1, text='Accident_No')
tree.heading(2, text='Date')
tree.heading(3, text='Time')
tree.heading(4, text='Alcohol_Time')
tree.heading(5, text='Accident_Type')
tree.heading(6, text='Day_of_Week')
tree.heading(7, text='Light_Condition')
tree.heading(8, text='Road_Geometry')
tree.heading(9, text='Severity')
tree.heading(10, text='Speed_Zone')
tree.heading(11, text='Run_Offroad')
tree.tag_configure('even', background='#E8E8E8')

treeScroll = ttk.Scrollbar(root)
treeScroll.configure(command=tree.yview)
tree.configure(yscrollcommand=treeScroll.set)
treeScroll.place(x=int(wid)-20,y=25,height=410)

tree.place(x=10,y=25)
root.mainloop()
