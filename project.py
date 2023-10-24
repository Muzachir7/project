import tkinter as tk 
from tkinter import ttk
import sqlite3
# создание главного окна
class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()
    def init_main(self):
        toolbar = tk.Frame(bg='#d7d7d7', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)
        #добавить
        self.add_img = tk.PhotoImage(file='./PROJECT/add.png')
        btn_add = tk.Button(toolbar, bg='#d7d7d7', bd=1,
                            image=self.add_PROJECT, command=self.open_child)
        btn_add.pack(side=tk.LEFT) 
        #МЕТОД ВЫЗЫВАЮЩИЙ ОКНО ДОБАВЛЕНИЯ
        def open_child(self):
            Child()
          

# класс дочернего окна
class Child(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()
        self.view = app
        
    def init_child(self):
        
        self.title('Добавление сотрудника')
        self.geometry('400x200')
        self.resizable(False, False)
        self.grab_set()
        self.focus_set()


        #создание кнопки редактирования сотрудника
        self.edit_img = tk.PhotoImage(file='update.png')
        btn_edit = tk.Button(toolbar, bg='#d7d7d7', bd=0, 
                            image=self.edit_img,
                            command=self.open_edit)
        btn_edit.pack(side=tk.LEFT)
          #создание кнопки удаления сотрудника
        self.del_img = tk.PhotoImage(file='delete.png')
        btn_del = tk.Button(toolbar, bg='#d7d7d7', bd=0, 
                            image=self.del_img,
                            command=self.delete_records)
        btn_del.pack(side=tk.LEFT)
         #создание кнопки поиска сотрудника 
        self.search_img = tk.PhotoImage(file='search.png')
        btn_search = tk.Button(toolbar, bg='#d7d7d7', bd=0, 
                            image=self.search_img,
                            command=self.open_search)
        btn_search.pack(side=tk.LEFT)   
        
        # создание дерева 
        self.tree = ttk.Treeview(root,
                                 columns=('id', 'name', 'tel', 'email','salary'),
                                 height=45, show='headings')
        self.tree.column('id', width=125, anchor=tk.CENTER)
        self.tree.column('name', width=125, anchor=tk.CENTER)
        self.tree.column('tel', width=125, anchor=tk.CENTER)
        self.tree.column('email', width=125, anchor=tk.CENTER)
        self.tree.column('salary', width=125, anchor=tk.CENTER)
        
        self.tree.heading('id', text='id')
        self.tree.heading('name', text='ФИО')
        self.tree.heading('tel', text='Телефон')
        self.tree.heading('email', text='e-mail')
        self.tree.heading('salary', text='salary')
        self.tree.pack(side=tk.LEFT)
        scroll = tk.Scrollbar(root,command=self.tree.yview)
        scroll.pack(side=tk.LEFT, fill=tk.Y)
        self.tree.configure(yscrollcommand=scroll.set)
    
    
    
    # метод добавления сотрудника
    def records(self, name, tel, email,salary):
        self.db.insert_data(name, tel, email,salary)
        self.view_records()
        self.db.conn.commit() # сохраняем изменения
    
    # метод редактирования
    def edit_record(self, name, tel, email,salary):
        ind = self.tree.set(self.tree.selection()[0], '#1')
        self.db.cur.execute('''
            UPDATE users SET name = ?, phone = ?, email = ?, salary = ?
            WHERE id = ?
        ''', (name, tel, email,salary, ind))
        self.db.conn.commit()
        self.view_records()
    
   # класс дочернего окна
class Child(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()
        self.view = app
        
    def init_child(self):
        
        self.title('Добавление сотрудника')
        self.geometry('400x200')
        self.resizable(False, False)
        self.grab_set()
        self.focus_set()
        label_name = tk.Label(self, text='ФИО')
        label_name.place(x=50, y=50)
        label_tel = tk.Label(self, text='Телефон')
        label_tel.place(x=50, y=80)
        label_email = tk.Label(self, text='E-mail')
        label_email.place(x=50, y=110)
        label_salary = tk.Label(self, text='salary')
        label_salary.place(x=50,y=140)
        self.entry_name = tk.Entry(self)
        self.entry_name.place(x=200, y=50)
        self.entry_tel = tk.Entry(self)
        self.entry_tel.place(x=200, y=80)
        self.entry_email = tk.Entry(self)
        self.entry_email.place(x=200, y=110)
        self.entry_salary = tk.Entry(self)
        self.entry_salary.place(x=200, y=135)
        
        self.btn_ok = tk.Button(self, text='Добавить', command=self.add_contact)
        self.btn_ok.place(x=300, y=160)
        btn_cancel = tk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=220, y=160)
    def add_contact(self):

        # кнопка редактировать
        self.btn_ok = tk.Button(self, text='Редактировать')
        self.btn_ok.bind('<Button-1>',lambda ev:self.view.edit_record(
           self.entry_name.get(),self.entry_tel.get(),
           self.entry_email.get(),self.entry_salary.get()))     
                                
        self.btn_ok.bind('<Button-1>',lambda ev:self.destroy(),
        add = '+')
        self.btn_ok.place(x=300, y=160)
       
   
# класс окна поиска
class Search(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_search()
        self.view = app
    def init_search(self):
        self.title('Поиск сотрудника')
        self.geometry('300x100')
        
# класс базы данных
class Db:
    def __init__(self):
        self.conn = sqlite3.connect('staff.db')
        self.cur = self.conn.cursor()
        self.cur.execute('''
                CREATE TABLE IF NOT EXISTS users(
                        id INTEGER PRIMARY KEY,
                        name TEXT,
                        phone TEXT,
                        email TEXT,
                        salary TEXT
                        )''')
    
        #метод добавления в бд
    def insert_data(self, name, tel, email,salary):
        self.cur.execute('''
            INSERT INTO users (name, phone, email, salary) 
            VALUES (?,?,?,?)''', (name, tel, email,salary))
    
    
# действия при запуске окна
if __name__ == '__main__':
    root = tk.Tk()
    db = Db()
    app = Main(root)
    app.pack()
    root.title('Список сотрудников компании')
    root.geometry('655x400')
    root.resizable(False, False)
    root.mainloop()