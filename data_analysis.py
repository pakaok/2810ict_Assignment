
import pandas as pd
from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt
def readCsv(file):
    try:
        return pd.read_csv(file)
    except:
        return False

df = readCsv('Crash Statistics Victoria.csv')



wid='1075'
hgt='600'
lst_day=['01','02','03','04','05','06','07','08','09']+[i for i in range(10,32)]
lst_month=[i for i in range(1,13)]
lst_year=[i for i in range(2013,2020)]

date_list=[]

for i in df.ACCIDENT_DATE:
    i = i.split('/')
    if int(i[0])<10:
        i[0]='0'+i[0]
    date_list.append(i[2]+i[1]+i[0])
    
def date_range(y0,m0,d0,y1,m1,d1):
    return y0+m0+d0,y1+m1+d1

def btn1():
    tree.delete(*tree.get_children())
    date_set= date_range(year_comboBox_0.get(),month_comboBox_0.get(),day_comboBox_0.get(),
    year_comboBox_1.get(),month_comboBox_1.get(),day_comboBox_1.get())

    if option_val.get() ==1 : searchBy_date(date_set)
    if option_val.get() ==2 : opt2(date_set,day_comboBox_0.get()+'/'+month_comboBox_0.get()+'/'+year_comboBox_0.get()+' To '
              +day_comboBox_1.get()+'/'+month_comboBox_1.get()+'/'+ year_comboBox_1.get())
    if option_val.get() ==3 : opt3(date_set,search_text.get())
    if option_val.get() ==4 : opt4(date_set)
    if option_val.get() ==5 : opt5(date_set,speed_comboBox.get())

def opt2(date,title):
    try:
        start,end=date
        acc_num=[0 for i in range(0,24)]
        total_day=0
        max_value=0
        for i in range(len(date_list)):
            if int(date_list[i])>=int(start) and int(date_list[i])<=int(end) :
                total_day+=1
                acc_time=df.ACCIDENT_TIME[i].split('.')[0]
                acc_num[int(acc_time)] = acc_num[int(acc_time)] + 1
        max_value=max(acc_num)
        for i in range(0,len(acc_num)):
            acc_num[i]=acc_num[i]/total_day
        plt.bar([i for i in range(0,24)], acc_num)
        plt.xticks([i for i in range(0,24)])
        plt.yticks([i/total_day for i in range(0,max_value,(max_value)//5)])
        plt.xlabel('0-24h')
        plt.ylabel('Number of accident on average')
        plt.title(title)
        plt.tight_layout()
        plt.show()  
        return True
    except:
        return False

def searchBy_date(date):
    try:
        start,end=date
        for i in range(len(date_list)):
            if int(date_list[i])>=int(start) and int(date_list[i])<=int(end) :
                acc_time=df.ACCIDENT_TIME[i].split('.')
                acc_time = acc_time[0]+':'+acc_time[1]
                injury = df.SEVERITY[i].split()
                injury = injury[0]+' '+injury[1]
                if i%2 == 0: tagName='even' 
                else: tagName = ''
                tree.insert('','end',values=[
                    df.ACCIDENT_NO[i],
                    df.ACCIDENT_DATE[i],
                    acc_time,
                    df.ALCOHOLTIME[i],
                    df.ACCIDENT_TYPE[i],
                    df.DAY_OF_WEEK[i],
                    df.LIGHT_CONDITION[i],
                    df.ROAD_GEOMETRY[i],
                    injury,
                    df.SPEED_ZONE[i],
                    df.RUN_OFFROAD[i]],tag= tagName)
        return True
    except: 
        return False

def opt3(date,keyword):
    try:
        start,end=date
        search_word=keyword
        search_word_1=search_word[0].upper()+search_word[1:]
        for i in range(len(date_list)):
            if int(date_list[i])>=int(start) and int(date_list[i])<=int(end) :
                if search_word in df.ACCIDENT_TYPE[i] or search_word_1 in df.ACCIDENT_TYPE[i]:
                    acc_time=df.ACCIDENT_TIME[i].split('.')
                    acc_time = acc_time[0]+':'+acc_time[1]
                    injury = df.SEVERITY[i].split()
                    injury = injury[0]+' '+injury[1]
                    if i%2 == 0: tagName='even' 
                    else: tagName = ''
                    tree.insert('','end',values=[
                    df.ACCIDENT_NO[i],
                    df.ACCIDENT_DATE[i],
                    acc_time,
                    df.ALCOHOLTIME[i],
                    df.ACCIDENT_TYPE[i],
                    df.DAY_OF_WEEK[i],
                    df.LIGHT_CONDITION[i],
                    df.ROAD_GEOMETRY[i],
                    injury,
                    df.SPEED_ZONE[i],
                    df.RUN_OFFROAD[i]],tag= tagName)
        return True
    except:
        return False
def opt4(date):
    try:
        start,end=date
        acc_num_y=[i for i in range(0,24)]
        acc_num_n=[i for i in range(0,24)]
        day_y=dict()
        day_n=dict()
        total_day_y=0
        total_day_n=0
        for i in range(len(date_list)):
            if int(date_list[i])>=int(start) and int(date_list[i])<=int(end):
                if df.ALCOHOLTIME[i]=='Yes' :
                    acc_time=df.ACCIDENT_TIME[i].split('.')[0]
                    acc_num_y[int(acc_time)] = acc_num_y[int(acc_time)] + 1
                    day_y[df.DAY_OF_WEEK[i]] = day_y.get(df.DAY_OF_WEEK[i],0) + 1
                    total_day_y=total_day_y+1
                else: 
                    acc_time=df.ACCIDENT_TIME[i].split('.')[0]
                    acc_num_n[int(acc_time)] = acc_num_n[int(acc_time)] + 1
                    day_n[df.DAY_OF_WEEK[i]] = day_n.get(df.DAY_OF_WEEK[i],0) + 1
                    total_day_n=total_day_n+1
    
        plt.subplot(211)
        plt.plot([i for i in range(0,24)], [i/total_day_y for i in acc_num_y], 'ro-')
        plt.plot([i for i in range(0,24)], [i/total_day_n for i in acc_num_n], 'go-')   
        plt.xticks([i for i in range(0,24)])
        plt.xlabel('0-24h (Green-Alcohol not involved / Red-Alcohol involved)',loc='right')
        plt.ylabel('Average number',color='red',loc='top') 
        plt.title('The number of accidents on average in each hour of the day',color='blue')

        day_xaxis=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
        day_xaxis_1=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
        day_y_yaxis=[day_y.get(i,0)/total_day_y for i in day_xaxis_1]
        day_n_yaxis=[day_n.get(i,0)/total_day_n for i in day_xaxis_1]
        plt.subplot(212)
        plt.plot(day_xaxis, day_y_yaxis, 'ro-')
        plt.plot(day_xaxis, day_n_yaxis, 'go-')   
        plt.xlabel('Day of week',loc='right')
        plt.ylabel('Average number',loc='top',color='red') 
        plt.title('The number of accidents on average on each day of week',color='blue')
        plt.subplots_adjust(left=0.125, bottom=0.1, right=0.9, top=0.9, wspace=0.8, hspace=0.8)
        plt.show()  
        return True
    except:
        return False
    
def opt5(date,keyword):
    try:
        start,end=date
        search_word=keyword
        for i in range(len(date_list)):
            if int(date_list[i])>=int(start) and int(date_list[i])<=int(end) :
                if search_word in df.SPEED_ZONE[i]:
                    acc_time=df.ACCIDENT_TIME[i].split('.')
                    acc_time = acc_time[0]+':'+acc_time[1]
                    injury = df.SEVERITY[i].split()
                    injury = injury[0]+' '+injury[1]
                    if i%2 == 0: tagName='even' 
                    else: tagName = ''
                    tree.insert('','end',values=[
                    df.ACCIDENT_NO[i],
                    df.ACCIDENT_DATE[i],
                    acc_time,
                    df.ALCOHOLTIME[i],
                    df.ACCIDENT_TYPE[i],
                    df.DAY_OF_WEEK[i],
                    df.LIGHT_CONDITION[i],
                    df.ROAD_GEOMETRY[i],
                    injury,
                    df.SPEED_ZONE[i],
                    df.RUN_OFFROAD[i]],tag= tagName)
        return True
    except Exception as e:
        return e
            
            
root = Tk()
root.title('2810ICT/Group 98/Kim/Mausham/Sam')
root.geometry(wid+'x'+hgt+'+170+50')
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
analyze_option1= Radiobutton(root,text='Search by selected period',value=1,variable=option_val)
analyze_option1.select()
analyze_option2= Radiobutton(root,text='Visualise the number of accidents on average',value=2,variable=option_val)
analyze_option3= Radiobutton(root,text='Search by selected period and accident type',value=3,variable=option_val)
analyze_option4= Radiobutton(root,text='Visualise the impact of alcohol in accidents',value=4,variable=option_val)
analyze_option5= Radiobutton(root,text='Search by selected period and speed zone',value=5,variable=option_val)  

analyze_option1.place(x=xpos+325,y=ypos-option_ypos_1)
analyze_option2.place(x=xpos+325,y=ypos+option_ypos-option_ypos_1)
analyze_option3.place(x=xpos+325,y=ypos+option_ypos*2-option_ypos_1)
analyze_option4.place(x=xpos+325,y=ypos+option_ypos*3-option_ypos_1)
analyze_option5.place(x=xpos+325,y=ypos+option_ypos*4-option_ypos_1)   

search_text= Entry(root,width=30)
search_text.place(x=xpos+600,y=ypos+option_ypos*2-option_ypos_1+5)

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
