from tkinter import *
import json
import math

class GUI:
    def __init__(self,window):
        self.month_days = {"January": 31, "February": 28, "March": 31, "April": 30, "May": 31, "June": 30,"July": 31, "August": 31,"September": 30,"October": 31,"November": 30,"December": 31 }
        self.month_order =  ['January', 'February', 'March', 'April', 'May', 'June','July', 'August', 'September', 'October', 'November', 'December']
        self.year = 2023
        self.month = 'April'
        self.file_name = 'Calendar.json'
        self.month_num_dict = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12}


        with open(self.file_name, 'a') as jsonfile:
            pass
        try:
            with open(self.file_name,'r') as jsonfile:
                self.cal_events = json.load(jsonfile)
        except:
            self.cal_events = {}


        self.window = window

        self.frame_name = Frame(self.window,bg = 'red',highlightbackground='black', highlightthickness=3)
        self.label_name = Label(self.frame_name,bg='red', text = 'Calendar', font=('Arial',50),width= 1001 )

        self.label_name.pack(pady = 20, side='top',)

        self.frame_specfic = Frame(self.window, highlightbackground= 'black', highlightthickness= 1.5)
        self.label_specific = Label(self.frame_specfic, text = 'Specific Date', font=('Arial', 15),anchor='w',borderwidth=1,relief='solid',highlightcolor='black',)
        self.label_specfic_month = Label(self.frame_specfic, text = 'Month', font=('Arial', 15),anchor='w',padx= 10,borderwidth=1,relief='solid',highlightcolor='black',)
        self.entry_month = Entry(self.frame_specfic, width= 5, highlightthickness= 1.5, highlightbackground= 'black')
        self.label_specfic_day = Label(self.frame_specfic, text = 'Day', font=('Arial', 15),anchor='w',borderwidth=1,relief='solid',highlightcolor='black',padx= 10,)
        self.entry_day = Entry(self.frame_specfic, width= 5, highlightthickness= 1.5, highlightbackground= 'black')
        self.label_specfic_year = Label(self.frame_specfic, text = 'Year', font=('Arial', 15),anchor='w',borderwidth=1,relief='solid',highlightcolor='black',padx= 10,)
        self.entry_year = Entry(self.frame_specfic, width= 10, highlightthickness= 1.5, highlightbackground= 'black',)
        self.button_add = Button(self.frame_specfic, width = 13, text = 'Add Event',padx= 10, command= self.add_button)
        self.button_goto = Button(self.frame_specfic, width = 13, text = 'GOTO',padx= 10, command = self.goto)
        self.label_specfic_instruct = Label(self.frame_specfic, text = 'Dates Should be Numeric, 5/7/2023, (No leading 0s)',padx= 10,)
        self.label_specific.pack(anchor= 'w', side=LEFT, expand = 1)
        self.label_specfic_month.pack(side=LEFT)
        self.entry_month.pack(side = LEFT)
        self.label_specfic_day.pack(side=LEFT)
        self.entry_day.pack(side = LEFT)
        self.label_specfic_year.pack(side=LEFT)
        self.entry_year.pack(side = LEFT)
        self.button_add.pack(side = LEFT)
        self.button_goto.pack(side = LEFT)
        self.label_specfic_instruct.pack(side= LEFT, expand = 1, fill = X)

        self.frame_calx1 = Frame(self.window, highlightbackground= 'black', highlightthickness= 1,width = 1001)
        self.frame_calx2 = Frame(self.window, highlightbackground= 'black', highlightthickness= 1,width = 1001)
        self.frame_calx3 = Frame(self.window, highlightbackground= 'black', highlightthickness= 1,width = 1001)
        self.frame_calx4 = Frame(self.window, highlightbackground= 'black', highlightthickness= 1,width = 1001)
        self.frame_calx5 = Frame(self.window, highlightbackground= 'black', highlightthickness= 1,width = 1001)
        self.frame_calx6 = Frame(self.window, highlightbackground= 'black', highlightthickness= 1,width = 1001)


    
        self.frame_month = Frame(self.window,highlightbackground='black', highlightthickness=3)
        self.label_month = Label(self.frame_month, text = f'{self.month} {self.year}', font=('Arial',20))
        self.month_foward_but = Button(self.frame_month, text = '>', command = self.month_foward ,width= 10)
        self.month_foward_but2 = Button(self.frame_month, text = '<',width= 10, command= self.month_backwards)
        self.label_nothing = Label(self.frame_month, text =' ', width = 31)
        self.label_nothing.pack(side = LEFT, anchor = 'w')
        self.label_month.pack(anchor = 'center' ,side = LEFT, expand= 1 )
        self.month_foward_but2.pack(fill= Y, side = LEFT,anchor= 'e')
        self.month_foward_but.pack(fill= Y, side = LEFT,anchor= 'e')
       

        self.frame_days = Frame(self.window,highlightbackground='black',highlightthickness=3, width = 1001)
        self.label_monday = Label(self.frame_days, text='Monday', font=('Arial',10))
        self.label_tuesday = Label(self.frame_days, text='Tuesday', font=('Arial',10))
        self.label_wednesday = Label(self.frame_days, text='Wednesday', font=('Arial',10))
        self.label_thursday = Label(self.frame_days, text='Thursday', font=('Arial',10))
        self.label_friday = Label(self.frame_days, text='Friday', font=('Arial',10))
        self.label_saturday = Label(self.frame_days, text='Saturday', font=('Arial',10))
        self.label_sunday = Label(self.frame_days, text='Sunday', font=('Arial',10))    

        self.label_monday.pack(side=LEFT, expand = True)
        self.label_tuesday.pack( side=LEFT, expand=True)
        self.label_wednesday.pack( side=LEFT, expand = True)
        self.label_thursday.pack( side=LEFT, expand= True)
        self.label_friday.pack( side=LEFT, expand= True)
        self.label_saturday.pack( side=LEFT, expand=True)
        self.label_sunday.pack( side=LEFT, expand=True)
 
        
        self.frame_name.pack()
        self.frame_specfic.pack()
        self.frame_month.pack(fill= X)
        self.frame_days.pack(fill = X)
        self.create_cal(self.month_days)


    def create_cal(self,month_list):

        
        start = self.figure_day(self.year,self.month)


        if start == 0:
           start = 5
        elif start == 1:
            start = 6
        else:
            start -= 2
        
        end = month_list[self.month]

        if self.month ==  'February':
            if self.year % 100 == 0:
                if self.year % 400 == 0:
                    end += 1
            elif self.year % 4 == 0:
                end += 1

        check = False
        count = 0

        for i in range(42):
            

            if start == i:
                check = True
                end = end + i + 1
            if end == i + 1:
                check = False

            if check:
                count += 1
                self.frame_calx_choose(count, i)
            else:
                self.frame_calx_choose(' ',i)

        

        self.frame_calx1.pack(fill = BOTH, expand= 1)
        self.frame_calx2.pack(fill = BOTH, expand = 1)
        self.frame_calx3.pack(fill = BOTH, expand = 1)
        self.frame_calx4.pack(fill = BOTH, expand = 1)
        self.frame_calx5.pack(fill = BOTH, expand = 1)

        self.check_extra = True

        check_day = self.figure_day(self.year,self.month)

        

        if check_day == 0:
            check_day= 5
        elif check_day == 1:
            check_day= 6
        else:
            check_day -= 2



        if (check_day + self.month_days[self.month]) >= 36:
            self.check_extra = True

        else:
            self.check_extra = False

        
        if self.check_extra:
            self.frame_calx6.pack(fill = BOTH, expand = 1)
        else:
            self.frame_calx6.forget()

                   
    def figure_day(self,year,month):

        # Uses Zeller's Rule, A way to determine the day from a given date 
        #Formula was used from https://en.wikipedia.org/wiki/Zeller%27s_congruence but code was written by me
        
        day = 1

        
        if month == "March":
            month_number = 3
        elif month == "April":
            month_number = 4
        elif month == "May":
            month_number = 5
        elif month == "June":
            month_number = 6
        elif month == "July":
            month_number = 7
        elif month == "August":
            month_number = 8
        elif month == "September":
            month_number = 9
        elif month == "October":
            month_number = 10
        elif month == "November":
            month_number = 11
        elif month == "December":
            month_number = 12
        elif month == "January":
            month_number = 13
        elif month == "February":
            month_number = 14
        
        cen = year//100
        cur_year = year % 100

        if month_number >= 13:
            if cur_year == 0:
                cen -= 1
                cur_year = 99
            else:
                cur_year -= 1
            

        day_number = (day +  (math.floor(13*(month_number+1)/5)) + cur_year + math.floor(cur_year/4) + math.floor(cen/4) - 2*cen) % 7


        if day_number == 0:
            day = "Saturday"
        elif day_number == 1:
            day = "Sunday"
        elif day_number == 2:
            day = "Monday"
        elif day_number == 3:
            day = "Tuesday"
        elif day_number == 4:
            day = "Wednesday"
        elif day_number == 5:
            day = "Thursday"
        elif day_number == 6:
            day = "Friday"



        return day_number

   
    def frame_calx_choose(self,count,place):
        month_number = self.month_num_dict[self.month]
        date = f'{month_number}/{count}/{self.year}'
        if date in self.cal_events:
            if len(self.cal_events[date]) > 1:
                count = f'{count}\n 1+ Event'
            else:
                count = f'{count}\n 1  Event'
        else:
            count =     f'{count}\n         '
          
        

        if  place<= 6:
            label = Label(self.frame_calx1,text = str(count),highlightthickness=1, highlightcolor='black')
            label.pack(side = LEFT, expand = True)
        elif place <= 13:
            label = Label(self.frame_calx2,text = str(count),highlightthickness=1)
            label.pack(side = LEFT, expand = True)
        elif place <= 20:
            label = Label(self.frame_calx3,text = str(count),highlightthickness=1)
            label.pack(side = LEFT, expand = True)
        elif place <= 27:
            label = Label(self.frame_calx4,text = str(count),highlightthickness=1)
            label.pack(side = LEFT, expand = True)
        elif place <= 34:
            label = Label(self.frame_calx5,text = str(count),highlightthickness=1)
            label.pack(side = LEFT, expand = True)
        elif place <= 41:
            label = Label(self.frame_calx6,text = str(count),highlightthickness=1)
            label.pack(side = LEFT, expand = True)
        
    
    def month_foward(self):

        self.cal_destory()
        for i in range(len(self.month_order)):
            if self.month == self.month_order[i]:
                if self.month_order[i] == 'December':
                    self.year += 1
                    self.month = self.month_order[0]
                    break
                else:
                    self.month = self.month_order[i+1]
                    break
        
        self.label_month.config(text = f'{self.month} {self.year}')
        self.label_month.pack()

        check_day = self.figure_day(self.year,self.month)

        if check_day == 0:
            check_day= 6
        elif check_day == 1:
            check_day= 7
        else:
            check_day -= 2





        self.create_cal(self.month_days)

        
    def month_backwards(self):

        self.cal_destory()
        for i in range(len(self.month_order)):
            if self.month == self.month_order[i]:
                if self.month_order[i] == 'January':
                    self.year += -1
                    self.month = self.month_order[11]
                    break
                else:
                    self.month = self.month_order[i-1]
                    break
        
        self.label_month.config(text = f'{self.month} {self.year}')
        self.label_month.pack()

        check_day = self.figure_day(self.year,self.month)

        if check_day == 0:
            check_day= 6
        elif check_day == 1:
            check_day= 7
        else:
            check_day -= 2





        self.create_cal(self.month_days)


    def cal_destory(self):
        
        for widgets in self.frame_calx1.winfo_children():
            widgets.destroy()
        for widgets in self.frame_calx2.winfo_children():
            widgets.destroy()
        for widgets in self.frame_calx3.winfo_children():
            widgets.destroy()
        for widgets in self.frame_calx4.winfo_children():
            widgets.destroy()
        for widgets in self.frame_calx5.winfo_children():
            widgets.destroy()
        for widgets in self.frame_calx6.winfo_children():
            widgets.destroy()


    def check_right_data(self,type):

        get_month = self.entry_month.get()
        get_day = self.entry_day.get()
        get_year = self.entry_year.get()
        
        try:
            get_month = int(get_month)
            if get_month < 1 or get_month > 12:
                raise ValueError
            get_year = int(get_year)
            if get_year < 0:
                raise ValueError
            if type == 'add':
                get_day = int(get_day)
                if get_day < 1 or get_day > self.month_days[self.month_order[get_month - 1]]:
                    raise ValueError
            return True

        except:
            return False
    

    def add_button(self):
        if self.check_right_data('add'):

            get_month = self.entry_month.get()
            get_day = self.entry_day.get()
            get_year = self.entry_year.get()

            self.event_window(get_month,get_day,get_year)


    def event_window(self,month,day,year):
        event_window = Toplevel(self.window)
        date = f'{month}/{day}/{year}'
        event_window.title(date)
        event_window.geometry('350x350')
        event_window.resizable(False,True)

        month = self.month_order[int(month)-1]

        date_label = Label(event_window, text= f'{month} {day}, {year}', font=('Arial',25), bg= 'blue', highlightbackground= 'black', highlightthickness= 3)
        date_label.pack(fill= X)
        
        if date in self.cal_events:
            events = self.cal_events[date]
            for item in events:
                event_frame = Frame(event_window)
                event_label = Label(event_frame, text= item)
                event_button = Button(event_frame, text = 'X', command = lambda item=item : self.del_event(item,date,event_window))

                event_label.pack(fill= X,side = LEFT)
                event_button.pack(side = LEFT)

                event_frame.pack(fill= X)

        add_event_frame = Frame(event_window)
        self.add_event_entry = Entry(add_event_frame)
        add_event_button = Button(add_event_frame, text = 'ADD EVENT', command= lambda : self.add_event(date,event_window))


        add_event_frame.pack(fill= X,pady = 10)
        self.add_event_entry.pack(fill=X, expand= True,side= LEFT, padx = 5)
        add_event_button.pack()

    def add_event(self, date,window):
        events = []
        event = self.add_event_entry.get()
        if not event.isspace():
            if date in self.cal_events:
                events = self.cal_events[date]
            events.append(event)
            self.cal_events[date] = events
            
            with open(self.file_name, 'w') as jsonfile:
                
                json.dump(self.cal_events, jsonfile)

            window.destroy()
            mdy = date.split('/')
            self.event_window(mdy[0],mdy[1],mdy[2])
            
            self.cal_destory()

            self.label_month.config(text = f'{self.month} {self.year}')
            self.label_month.pack()
            self.create_cal(self.month_days)
        

    def del_event(self,item,date,window):
        event = self.cal_events[date]
        for i in range(len(event)-1, -1, -1):
            if event[i] == item:
                del event[i]
                break
        window.destroy()
        mdy = date.split('/')
        self.event_window(mdy[0],mdy[1],mdy[2])
        self.cal_destory()
        self.create_cal(self.month_days)


    def goto(self):
        if self.check_right_data('goto'):
            self.cal_destory()

            self.month = self.month_order[int(self.entry_month.get()) - 1]
            self.year = int(self.entry_year.get())

            self.label_month.config(text = f'{self.month} {self.year}')
            self.label_month.pack()

            self.create_cal(self.month_days)
