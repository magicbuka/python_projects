from tkinter import *  
from tkcalendar import DateEntry
from tkinter import scrolledtext, ttk, messagebox, W, Menu
import calendar
import time

all_tastks = ''
comment_txt = ''
lst = []
d = {}
d2 = {}
count = 0
days = 0

window = Tk()  
window.title("Учет выполненных задач")  
window.geometry('700x500')  
tab_control = ttk.Notebook(window)  
tab1 = ttk.Frame(tab_control)  
tab2 = ttk.Frame(tab_control)  
tab_control.add(tab1, text='Окно ввода данных')  
tab_control.add(tab2, text='Календарь') 

#-------------------------------
#Меню
#-------------------------------

def about():
    messagebox.showinfo("О программе", "Редактор для учета выполненных задач на дату.")

def close():
    if messagebox.askokcancel("Выход из программы", "Хотите выйти из программы?"):
        window.destroy()

menu = Menu(window)  
menu_out = Menu(menu, tearoff=0)  
menu_out.add_cascade(label='Выход', command=close)    
menu.add_cascade(label='Файл', menu=menu_out) 
menu_file = Menu(menu, tearoff=0)  
menu_file.add_cascade(label='О программе', command=about)
menu.add_cascade(label='Справка', menu=menu_file) 
window.config(menu=menu) 

#-------------------------------
#Выбор даты
#-------------------------------

data_lbl = Label(tab1, text="Выбор даты:", font=("Arial Bold", 10))  
data_lbl.grid(column=0, row=1, sticky=W, padx=25)
cal = DateEntry(tab1, width=12, background='darkblue',foreground='white', borderwidth=2, date_pattern='dd.mm.yyyy')
cal.grid(column=0, row=2, sticky=W, padx=25) 

#-------------------------------
#Выбор типа задачи
#-------------------------------

label2 = Label(tab1, text="Тип задачи:", font=("Arial Bold", 10))
label2.grid(column=0, row=3, sticky=W, padx=25)
combo = ttk.Combobox(tab1)  
combo['values'] = ('Python', 'Machine learning', 'English', 'Paleoontology', 'Other activity')  
combo.grid(column=0, row=4, sticky=W, padx=25)  

#-------------------------------
#Установить количество задач
#-------------------------------

def cliker():
    if selected_class.get()==1:
        all_entry.delete(0, 'end')
        all_entry.configure(state='disabled')
        easy_entry.configure(state='normal')
        medium_entry.configure(state='normal')
        hard_entry.configure(state='normal')
    else:
        all_entry.configure(state='normal')
        easy_entry.delete(0, 'end')
        easy_entry.configure(state='disabled')
        medium_entry.delete(0, 'end')
        medium_entry.configure(state='disabled')
        hard_entry.delete(0, 'end')
        hard_entry.configure(state='disabled')

selected_class = IntVar()
first_class = Radiobutton(tab1, text='Вести учет сложности задач', value=1, variable=selected_class, command=cliker)
first_class.grid(column=0, row=6, sticky=W, padx=25)

easy = Label(tab1,text="easy")
easy.grid(column=1, row=5)
easy_entry = Entry(tab1, width=10)
easy_entry.grid(column=1, row=6)

medium= Label(tab1,text="medium")
medium.grid(column=2, row=5)
medium_entry = Entry(tab1, width=10)
medium_entry.grid(column=2, row=6)

hard = Label(tab1,text="hard")
hard.grid(column=3, row=5)
hard_entry = Entry(tab1, width=10)
hard_entry.grid(column=3, row=6)

second_class = Radiobutton(tab1, text='Ввести общее количество задач', value=2, variable=selected_class, command=cliker)
second_class.grid(column=0, row=10, sticky=W, padx=25)
all_entry = Entry(tab1, width=10)
all_entry.grid(column=1, row=10)

#--------------------------------
#Блок комментарий
#--------------------------------

def show_comment():
    global comment_txt
    comment_lbl = Label(tab1, text="Комментарий:", font=("Arial Bold", 10))  
    comment_lbl.grid(column=0, row=19, sticky=W, padx=25)
    comment_txt = scrolledtext.ScrolledText(tab1, width=40, height=2)  
    comment_txt.grid(column=0, row=20, sticky=W, padx=25)
        
chk_state = BooleanVar()  
chk_state.set(False)
check_com = ttk.Checkbutton(tab1, text="Отобразить окно для ввода комментария", var=chk_state, command=show_comment)
check_com.grid(column=0, row=18, sticky=W, padx=25)  

#--------------------------------
#Блок формирования сводной информации
#--------------------------------

def read_info():
    d_tasts = {}
    d_tasts['easy'], d_tasts['medium'], d_tasts['hard'] = easy_entry.get(), medium_entry.get(), hard_entry.get()
    if selected_class.get() == 1:
        count_task = 0
        comp_txt = ''
        for key, value in d_tasts.items():
            if value != '':
                count_task += int(value)
                comp_txt += f', {value} {key}'
        lst.append(count_task)
        if d_tasts['easy'] == '' and d_tasts['medium'] == '' and d_tasts['hard'] == '' or combo.get()=='':
            messagebox.showinfo('Ошибка заполнения', 'В поле ввода задач с учетом сложности не указано ни одного значения или не указан тип задачи.')
        else:
            tasks_txt.insert(END, f"{combo.get()}: {count_task}\n({comp_txt[2:]})\n")
            clear(flag=False)
    elif selected_class.get() == 2: 
        if all_entry.get() != '':
            tasks_txt.insert(END, f"{combo.get()}: {all_entry.get()}\n")
            lst.append(int(all_entry.get()))
            clear(flag=False)
        else:
            messagebox.showinfo('Ошибка заполнения', 'В поле ввода общего количества задач не указано значение.')
    else:
        messagebox.showinfo('Ошибка заполнения', 'Не выбран тип учета задач')
    
class_btn = Button(tab1, text="Зафиксировать введенные данные в сводном окне", command=read_info)
class_btn.grid(column=0, row=11, sticky=W, padx=25)
tasks_lbl = Label(tab1, text="Сводная информация по выполненным задачам:", font=("Arial Bold", 10))  
tasks_lbl.grid(column=0, row=12, sticky=W, padx=25)
tasks_txt = scrolledtext.ScrolledText(tab1, width=40, height=7)  
tasks_txt.grid(column=0, row=13, sticky=W, padx=25)

#--------------------------------
#Сохренение в файл. Очистка формы
#--------------------------------

def clear(flag=True):
    all_entry.delete(0, 'end')
    easy_entry.delete(0, 'end')
    medium_entry.delete(0, 'end')
    hard_entry.delete(0, 'end')
    if flag:
        tasks_txt.delete("1.0", END)
        if chk_state.get() == True:
            comment_txt.delete("1.0", END)
    combo.delete(0, END)


def save():
    global d, comment_txt, lst, d2, count 
    main_info = list(filter(None, tasks_txt.get("1.0", END).split('\n')))
    date = cal.get()
    d[f'{date}_main_info'] = main_info
    d[f'{date}_tasksum'] = sum(lst)
    if comment_txt != '':
        comment = list(filter(None, comment_txt.get("1.0", END).split('\n')))
        d[f'{date}_comment'] = comment
           
    with open(f'output.txt','a') as output:
        for key, val in d.items():
            output.write(f'{key}<sep>{val}\n')
            d2[key] = val
    lst=[]
    make_calendar(tab2)
    count += days
    messagebox.showinfo("Оповещение о записи", "Данные успешно записаны в файл output.txt")
    clear()
        
save_button = Button(tab1, text="Сохранить в файл", command=save, background='SlateGray2')
save_button.grid(column=0, row=22, sticky=W, padx=25)
clear_button = Button(tab1, text="Очистить форму", command=clear)
clear_button.grid(column=0, row=21, sticky=W, padx=25)

#----------------------------------        
#Вкладка 2
#----------------------------------

legend_txt = Label(tab2, text="Легенда:")
label_legend1 = Label(tab2, text="tasks<5", bg='DarkSeaGreen1')
label_legend2 = Label(tab2, text="5<=tasks<15", bg='PaleGreen3')
label_legend3 = Label(tab2, text="tasks>=15", bg='PaleGreen4')
legend_txt.grid(column=0, row=7)
label_legend1.grid(column=0, row=8)
label_legend2.grid(column=0, row=9)
label_legend3.grid(column=0, row=10)

def actual_info(event):
    global d2, count
    newWindow = Toplevel(tab2)
    newWindow.title("Список выполненных задач")
    newWindow.geometry('350x150')
    
    with open('output.txt') as inp:
        for i in inp.readlines():
            if '<sep>' in i:
                key, val = i.strip().split('<sep>')
                d2[key] = val
    
    currentButton = event.widget._name.split('!button')[1]
    if currentButton == '':
        currentButton = '1'
    currentButton = str(int(currentButton)-count)
    
    dict_keys = []
    for key in d2.keys():
        if currentButton == str(int(key.split('.')[0])):
            dict_keys.append(key)
            data = key.split('_')[0]
    txt_message = {}
    if len(dict_keys) != 0:
        for i in dict_keys:
            if 'main_info' in i:
                txt_message['Выполнено'] = d2[i]
            elif 'comment' in i:
                txt_message['Комментарий'] = d2[i]
        
        
        
        row = 1
        row_v = 1
        for key, value in txt_message.items():
            value = value[2:-2]
            if key == 'Комментарий':
                info_name = Label(newWindow, text=key)
                info_name.grid(column=0, row=row_v, sticky=W, padx=5)
            else:
                info_name = Label(newWindow, text=key)
                info_name.grid(column=0, row=row, sticky=W, padx=5)
            if len(value.split("', '")) > 1:
                row_v = 1
                for i in value.split("', '"):
                    info_txt = Label(newWindow, text=i)
                    info_txt.grid(column=1, row=row_v, sticky=W, padx=5)
                    row_v += 1
            else:
                info_txt = Label(newWindow, text=value)
                info_txt.grid(column=1, row=row_v, sticky=W, padx=5)
                row_v += 1
            row += 1
    data_name = Label(newWindow, text="Задачи на дату")
    data_name.grid(column=0, row=0, sticky=W, padx=5)
    data_txt = Label(newWindow, text=data)
    data_txt.grid(column=1, row=0, sticky=W, padx=5)

def make_calendar(tab2):
    global d2, count, days
    
    with open('output.txt') as inp:
        for i in inp.readlines():
            if '<sep>' in i:
                key, val = i.strip().split('<sep>')
                d2[key] = val
    
    month_names = tuple(calendar.month_name)
    year, month = int(time.strftime("%Y")), str(time.strftime("%B"))
    m_cal = calendar.monthcalendar(year, month_names.index(month))
    days = calendar.monthrange(2020, 7)[1]

    for dates in m_cal:
        row = m_cal.index(dates) + 1
        for date in dates:
            if date == 0:
                continue
            l = locals()
            l[date] = Button(tab2, text=f" {date} ", width=5)
            l[date].config(font=('Arial', 20))
            l[date].grid(row=row, column=dates.index(date))
            l[date].bind('<Button-1>', actual_info)
            for key in d2.keys():
                if date == int(key.split('.')[0]) and 'tasksum' in key:
                    sum_tasks = int(d2[key])
                    if sum_tasks < 5:
                        l[date].config(background='DarkSeaGreen1')
                    elif 5 <= sum_tasks < 15:
                        l[date].config(background='PaleGreen3')
                    elif 15 <= sum_tasks:
                        l[date].config(background='PaleGreen4')
                    else:
                        l[date].config(font=('Arial', 20))
    
make_calendar(tab2)
tab_control.grid() 

window.mainloop()