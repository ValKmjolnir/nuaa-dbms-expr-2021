from tkinter.constants import DISABLED, NORMAL, END
import pymysql
import tkinter as tk
import tkinter.messagebox as ms
import time

db=pymysql.NULL
admin_login=False

# Main window
window=tk.Tk()
window.title("Book Manage")
window.geometry("1080x640")
window.resizable(width=False,height=False)

# Left side bar->Frame
frame=[]
for i in range(15):
    frame.append(tk.Frame(window,bg='mediumaquamarine',width=880,height=640))
now_frame=frame[0]
def frame_clear():
    now_frame.place_forget()
    return
def set_frame(index):
    global now_frame
    now_frame=frame[index]
    now_frame.place(x=200,y=0,anchor='nw')
    return

# Text
time_text=tk.Text(
    window,font=('microsoft yahei',10),
    bg='mediumaquamarine',fg='white',
    width=880,height=30)
time_text.place(x=200,y=320,anchor='nw')
text=tk.Text(
    window,font=('microsoft yahei',10),
    bg='mediumaquamarine',fg='white',
    width=880,height=200)
text.place(x=200,y=350,anchor='nw')
text.configure(state=DISABLED)
time_text.configure(state=DISABLED)
def show_info(s):
    text.configure(state=NORMAL)
    text.delete('1.0',END)
    text.insert(END,s)
    text.configure(state=DISABLED)
    return
def search_info(s):
    # execute sql
    cursor=db.cursor()
    start=time.time()
    cursor.execute(s)
    end=time.time()
    # text write
    text.configure(state=NORMAL)
    text.delete('1.0',END)
    info=cursor.fetchall()
    for i in info:
        text.insert(END,str(i)+'\n')
    text.configure(state=DISABLED)
    # time info write
    time_text.configure(state=NORMAL)
    time_text.delete('1.0',END)
    time_text.insert(END,"time usage: "+str(end-start)+"s")
    time_text.configure(state=DISABLED)
    return

def main_not_login():
    tk.Label(
        frame[0],text='Welcome',
        font=('microsoft yahei',10),
        bg='mediumseagreen',fg='white'
    ).place(x=0,y=0,width=880,height=80,anchor='nw')
    tk.Label(
        frame[0],text='Please login first.',
        font=('microsoft yahei',10),
        bg='mediumaquamarine',fg='white'
    ).place(x=0,y=80,width=880,height=80,anchor='nw')
    return
def main_login():
    tk.Label(
        frame[1],text='Welcome',
        font=('microsoft yahei',10),
        bg='mediumseagreen',fg='white'
    ).place(x=0,y=0,width=880,height=80,anchor='nw')
    return
def main_page():
    frame_clear()
    if(not admin_login):
        show_info('Welcome to book manage system v0.1\nPlease login first')
        set_frame(0)
        return
    show_info(
        'Welcome to book manage system v0.1\n'
        'Press user to manage user\n'
        'Press book to manage book\n'
        'Press comment to manage comment\n'
        'Press recommend to manage recommendation\n'
        'Press logout to log out\n'
        'If want help when managing,press main'
    )
    set_frame(1)
    return

login_username=tk.Entry(frame[2],show=None,font=('microsoft yahei',10),bg='mediumseagreen',fg='white')
login_password=tk.Entry(frame[2],show='*',font=('microsoft yahei',10),bg='mediumseagreen',fg='white')
def confirm_login():
    global db
    try:
        db=pymysql.connect(
            host="localhost",
            port=3306,
            user=login_username.get(),
            password=login_password.get(),
            database="bookshare",
            charset="utf8"
        )
    except pymysql.err.OperationalError:
        show_info('Login failed: invalid username or password')
    else:
        global admin_login
        admin_login=True
        show_info('Login successfully')
        main_page()
    return
def login_not_login():
    tk.Label(
        frame[2],text='Login',
        font=('microsoft yahei',10),
        bg='mediumseagreen',fg='white'
    ).place(x=0,y=0,width=880,height=80,anchor='nw')
    tk.Label(
        frame[2],text="Username :",
        font=('microsoft yahei',10),
        bg='mediumaquamarine',fg='white'
    ).place(x=340,y=140,width=100,height=20,anchor='nw')
    tk.Label(
        frame[2],text="Password :",
        font=('microsoft yahei',10),
        bg='mediumaquamarine',fg='white'
    ).place(x=340,y=190,width=100,height=20,anchor='nw')
    login_username.place(x=360,y=165,width=200,height=20,anchor='nw')
    login_password.place(x=360,y=215,width=200,height=20,anchor='nw')
    tk.Button(frame[2],text='confirm',
        font=('microsoft yahei',10),relief='flat',
        bg='mediumseagreen',fg='white',
        activebackground='aquamarine',activeforeground='black',
        command=confirm_login
    ).place(x=420,y=260,width=60,height=30,anchor='nw')
    return
def login_login():
    tk.Label(
        frame[3],text='Login Successfully',
        font=('microsoft yahei',10),
        bg='mediumseagreen',fg='white'
    ).place(x=0,y=0,width=880,height=80,anchor='nw')
    tk.Label(
        frame[3],text='You\'ve already logged in.',
        font=('microsoft yahei',10),
        bg='mediumaquamarine',fg='white'
    ).place(x=0,y=80,width=880,height=80,anchor='nw')
    return
def login_page():
    frame_clear()
    if(not admin_login):
        set_frame(2)
        return
    set_frame(3)
    return

def logout_not_login():
    tk.Label(
        frame[4],text='Logout Failed',
        font=('microsoft yahei',10),
        bg='mediumseagreen',fg='white'
    ).place(x=0,y=0,width=880,height=80,anchor='nw')
    tk.Label(
        frame[4],text='You haven\'t logged in yet.',
        font=('microsoft yahei',10),
        bg='mediumaquamarine',fg='white'
    ).place(x=0,y=80,width=880,height=80,anchor='nw')
    return
def logout_login():
    tk.Label(
        frame[5],text='Logout Successfully',
        font=('microsoft yahei',10),
        bg='mediumseagreen',fg='white'
    ).place(x=0,y=0,width=880,height=80,anchor='nw')
    return
def logout_page():
    global admin_login
    frame_clear()
    if(not admin_login):
        set_frame(4)
        return
    admin_login=False
    show_info('Logout successfully')
    set_frame(5)
    return


userid=  tk.Entry(frame[7],show=None,font=('microsoft yahei',10),bg='mediumseagreen',fg='white')
username=tk.Entry(frame[7],show=None,font=('microsoft yahei',10),bg='mediumseagreen',fg='white')
sex=     tk.Entry(frame[7],show=None,font=('microsoft yahei',10),bg='mediumseagreen',fg='white')
age=     tk.Entry(frame[7],show=None,font=('microsoft yahei',10),bg='mediumseagreen',fg='white')
password=tk.Entry(frame[7],show='*', font=('microsoft yahei',10),bg='mediumseagreen',fg='white')

def add_user():
    cursor=db.cursor()
    for i in [i.get() for i in[userid,username,sex,age]]:
        if(len(i)==0):
            ms.showerror('invalid data',"Please input correct data")
            return
    cursor.execute("select userid from user where userid=\""+userid.get()+"\";")
    if(len(cursor.fetchall())):
        ms.showerror('user exists','This user already exists.')
        return
    try:
        cursor.execute(
            "insert into user(userid,username,sex,age,password) "
            "values (\""+userid.get()+"\",\""+username.get()+"\",\""+sex.get()+"\","+age.get()+",\""+password.get()+"\");"
        )
    except pymysql.err.ProgrammingError:
        ms.showerror('invalid data','Please input correct data')
    else:
        db.commit()
        search_info("select userid,username,sex,age from user limit 20;")
    return

def del_user():
    cursor=db.cursor()
    if(len(userid.get())==0):
        ms.showerror('invalid userid',"Please input correct userid")
        return
    try:
        cursor.execute("delete from user where userid=\""+userid.get()+"\";")
        cursor.execute("delete from recm_book where userid=\""+userid.get()+"\";")
        cursor.execute("delete from comment where userid=\""+userid.get()+"\";")
    except pymysql.err.ProgrammingError:
        ms.showerror('invalid userid','Please input correct userid')
    else:
        db.commit()
        search_info("select userid,username,sex,age from user limit 20;")
    return

def change_user():
    cursor=db.cursor()
    if(len(userid.get())==0):
        ms.showerror('invalid userid',"Please input correct userid")
        return
    cursor.execute("select * from user where userid=\""+userid.get()+"\";")
    if(len(cursor.fetchall())==0):
        ms.showerror('invalid userid',"Please input correct userid")
        return
    val=[]
    for i in [("username=\"",username.get(),"\""),("sex=\"",sex.get(),"\""),("age=",age.get(),""),("password=\"",password.get(),"\"")]:
        if(len(i[1])):
            val.append(i[0]+i[1]+i[2])
    if(len(val)==0):
        ms.showerror('invalid data',"Please input changed data")
        return
    cypher="update user set "
    for i in range(len(val)):
        cypher+=val[i]
        if(i!=len(val)-1):
            cypher+=","
    cypher+=" where userid=\""+userid.get()+"\";"
    try:
        cursor.execute(cypher)
    except pymysql.err.ProgrammingError:
        ms.showerror('invalid data','Please input correct data')
    else:
        db.commit()
        search_info("select userid,username,sex,age from user limit 20;")
    return

def search_user():
    val=[]
    for i in [("userid like \"%",userid.get(),"%\""),("username like \"%",username.get(),"%\""),("sex=\"",sex.get(),"\""),("age=",age.get(),"")]:
        if(len(i[1])):
            val.append(i[0]+i[1]+i[2])
    cypher="select userid,username,sex,age from user"
    if(len(val)):
        cypher+=" where "
        for i in range(len(val)):
            cypher+=val[i]
            if(i!=len(val)-1):
                cypher+=" and "
    cypher+=";"
    search_info(cypher)
    return

def user_not_login():
    tk.Label(
        frame[6],text='User Manage',
        font=('microsoft yahei',10),
        bg='mediumseagreen',fg='white'
    ).place(x=0,y=0,width=880,height=80,anchor='nw')
    tk.Label(
        frame[6],text='Please login first.',
        font=('microsoft yahei',10),
        bg='mediumaquamarine',fg='white'
    ).place(x=0,y=80,width=880,height=80,anchor='nw')
    return
def user_login():
    tk.Label(
        frame[7],text='User Manage',
        font=('microsoft yahei',10),
        bg='mediumseagreen',fg='white'
    ).place(x=0,y=0,width=880,height=80,anchor='nw')
    tk.Label(
        frame[7],text="userid :",
        font=('microsoft yahei',10),
        bg='mediumaquamarine',fg='white'
    ).place(x=0,y=85,width=100,height=20,anchor='nw')
    tk.Label(
        frame[7],text="username :",
        font=('microsoft yahei',10),
        bg='mediumaquamarine',fg='white'
    ).place(x=0,y=110,width=100,height=20,anchor='nw')
    tk.Label(
        frame[7],text="sex :",
        font=('microsoft yahei',10),
        bg='mediumaquamarine',fg='white'
    ).place(x=0,y=135,width=100,height=20,anchor='nw')
    tk.Label(
        frame[7],text="age :",
        font=('microsoft yahei',10),
        bg='mediumaquamarine',fg='white'
    ).place(x=0,y=160,width=100,height=20,anchor='nw')
    tk.Label(
        frame[7],text="password :",
        font=('microsoft yahei',10),
        bg='mediumaquamarine',fg='white'
    ).place(x=0,y=185,width=100,height=20,anchor='nw')
    
    userid.place(x=120,y=85,width=200,height=20,anchor='nw')
    username.place(x=120,y=110,width=200,height=20,anchor='nw')
    sex.place(x=120,y=135,width=200,height=20,anchor='nw')
    age.place(x=120,y=160,width=200,height=20,anchor='nw')
    password.place(x=120,y=185,width=200,height=20,anchor='nw')
    tk.Button(
        frame[7],text='add',relief='flat',
        font=('microsoft yahei',12),
        bg='mediumseagreen',fg='white',
        activebackground='aquamarine',activeforeground='black',
        command=add_user
    ).place(x=330,y=85,width=60,height=120,anchor='nw')
    tk.Button(
        frame[7],text="delete",relief='flat',
        font=('microsoft yahei',12),
        bg='mediumseagreen',fg='white',
        activebackground='aquamarine',activeforeground='black',
        command=del_user
    ).place(x=395,y=85,width=60,height=120,anchor='nw')
    tk.Button(
        frame[7],text="change",relief='flat',
        font=('microsoft yahei',12),
        bg='mediumseagreen',fg='white',
        activebackground='aquamarine',activeforeground='black',
        command=change_user
    ).place(x=460,y=85,width=60,height=120,anchor='nw')
    tk.Button(
        frame[7],text="search",relief='flat',
        font=('microsoft yahei',12),
        bg='mediumseagreen',fg='white',
        activebackground='aquamarine',activeforeground='black',
        command=search_user
    ).place(x=525,y=85,width=60,height=120,anchor='nw')
    return

def user_page():
    frame_clear()
    if(not admin_login):
        set_frame(6)
        return
    set_frame(7)
    return

bookid  =tk.Entry(frame[9],show=None,font=('microsoft yahei',10),bg='mediumseagreen',fg='white')
bookname=tk.Entry(frame[9],show=None,font=('microsoft yahei',10),bg='mediumseagreen',fg='white')
bookinfo=tk.Entry(frame[9],show=None,font=('microsoft yahei',10),bg='mediumseagreen',fg='white')

def add_book():
    cursor=db.cursor()
    for i in [i.get() for i in[bookid,bookname,bookinfo]]:
        if(len(i)==0):
            ms.showerror('invalid data',"Please input correct data")
            return
    cursor.execute("select bookid from book where bookid=\""+bookid.get()+"\";")
    if(len(cursor.fetchall())):
        ms.showerror('book exists','This book already exists.')
        return
    try:
        cursor.execute(
            "insert into book(bookid,bookname,bookinfo) "
            "values (\""+bookid.get()+"\",\""+bookname.get()+"\",\""+bookinfo.get()+"\");"
        )
    except pymysql.err.ProgrammingError:
        ms.showerror('invalid data','Please input correct data')
    else:
        db.commit()
        search_info("select * from book limit 20;")
    return

def del_book():
    cursor=db.cursor()
    if(len(bookid.get())==0):
        ms.showerror('invalid bookid',"Please input correct bookid")
        return
    try:
        cursor.execute("delete from book where bookid=\""+bookid.get()+"\";")
        cursor.execute("delete from comment where bookid=\""+bookid.get()+"\";")
        cursor.execute("delete from recm_book where bookid=\""+bookid.get()+"\";")
    except pymysql.err.ProgrammingError:
        ms.showerror('invalid bookid','Please input correct bookid')
    else:
        db.commit()
        search_info("select * from book limit 20;")
    return

def change_book():
    cursor=db.cursor()
    if(len(bookid.get())==0):
        ms.showerror('invalid bookid',"Please input correct bookid")
        return
    cursor.execute("select * from book where bookid=\""+bookid.get()+"\";")
    if(len(cursor.fetchall())==0):
        ms.showerror('invalid bookid',"Please input correct bookid")
        return
    val=[]
    for i in [("bookname=\"",bookname.get(),"\""),("bookinfo=\"",bookinfo.get(),"\"")]:
        if(len(i[1])):
            val.append(i[0]+i[1]+i[2])
    if(len(val)==0):
        ms.showerror('invalid data',"Please input changed data")
        return
    cypher="update book set "
    for i in range(len(val)):
        cypher+=val[i]
        if(i!=len(val)-1):
            cypher+=","
    cypher+=" where bookid=\""+bookid.get()+"\";"
    try:
        cursor.execute(cypher)
    except pymysql.err.ProgrammingError:
        ms.showerror('invalid data','Please input correct data')
    else:
        db.commit()
        search_info("select * from book limit 20;")
    return

def search_book():
    val=[]
    for i in [("bookid like \"%",bookid.get(),"%\""),("bookname like \"%",bookname.get(),"%\""),("bookinfo like \"%",bookinfo.get(),"%\"")]:
        if(len(i[1])):
            val.append(i[0]+i[1]+i[2])
    cypher="select * from book"
    if(len(val)):
        cypher+=" where "
        for i in range(len(val)):
            cypher+=val[i]
            if(i!=len(val)-1):
                cypher+=" and "
    cypher+=";"
    search_info(cypher)
    return

def book_not_login():
    tk.Label(
        frame[8],text='Book Manage',
        font=('microsoft yahei',10),
        bg='mediumseagreen',fg='white'
    ).place(x=0,y=0,width=880,height=80,anchor='nw')
    tk.Label(
        frame[8],text='Please login first.',
        font=('microsoft yahei',10),
        bg='mediumaquamarine',fg='white'
    ).place(x=0,y=80,width=880,height=80,anchor='nw')
    return
def book_login():
    tk.Label(
        frame[9],text='Book Manage',
        font=('microsoft yahei',10),
        bg='mediumseagreen',fg='white'
    ).place(x=0,y=0,width=880,height=80,anchor='nw')
    tk.Label(
        frame[9],text="bookid :",
        font=('microsoft yahei',10),
        bg='mediumaquamarine',fg='white'
    ).place(x=0,y=85,width=100,height=20,anchor='nw')
    tk.Label(
        frame[9],text="bookname :",
        font=('microsoft yahei',10),
        bg='mediumaquamarine',fg='white'
    ).place(x=0,y=110,width=100,height=20,anchor='nw')
    tk.Label(
        frame[9],text="bookinfo :",
        font=('microsoft yahei',10),
        bg='mediumaquamarine',fg='white'
    ).place(x=0,y=135,width=100,height=20,anchor='nw')
    bookid.place(x=120,y=85,width=200,height=20,anchor='nw')
    bookname.place(x=120,y=110,width=200,height=20,anchor='nw')
    bookinfo.place(x=120,y=135,width=200,height=20,anchor='nw')
    tk.Button(
        frame[9],text='add',relief='flat',
        font=('microsoft yahei',12),
        bg='mediumseagreen',fg='white',
        activebackground='aquamarine',activeforeground='black',
        command=add_book
    ).place(x=330,y=85,width=60,height=120,anchor='nw')
    tk.Button(
        frame[9],text="delete",relief='flat',
        font=('microsoft yahei',12),
        bg='mediumseagreen',fg='white',
        activebackground='aquamarine',activeforeground='black',
        command=del_book
    ).place(x=395,y=85,width=60,height=120,anchor='nw')
    tk.Button(
        frame[9],text="change",relief='flat',
        font=('microsoft yahei',12),
        bg='mediumseagreen',fg='white',
        activebackground='aquamarine',activeforeground='black',
        command=change_book
    ).place(x=460,y=85,width=60,height=120,anchor='nw')
    tk.Button(
        frame[9],text="search",relief='flat',
        font=('microsoft yahei',12),
        bg='mediumseagreen',fg='white',
        activebackground='aquamarine',activeforeground='black',
        command=search_book
    ).place(x=525,y=85,width=60,height=120,anchor='nw')
    return

def book_page():
    frame_clear()
    if(not admin_login):
        set_frame(8)
        return
    set_frame(9)
    return

cuserid=tk.Entry(frame[11],show=None,font=('microsoft yahei',10),bg='mediumseagreen',fg='white')
cbookid=tk.Entry(frame[11],show=None,font=('microsoft yahei',10),bg='mediumseagreen',fg='white')
cmid=   tk.Entry(frame[11],show=None,font=('microsoft yahei',10),bg='mediumseagreen',fg='white')
cminfo= tk.Entry(frame[11],show=None,font=('microsoft yahei',10),bg='mediumseagreen',fg='white')
def add_comment():
    cursor=db.cursor()
    for i in [i.get() for i in[cuserid,cbookid,cmid,cminfo]]:
        if(len(i)==0):
            ms.showerror('invalid data',"Please input correct data")
            return
    cursor.execute("select cmid from comment where cmid=\""+cmid.get()+"\";")
    if(len(cursor.fetchall())):
        ms.showerror('comment exists','This comment already exists.')
        return
    try:
        cursor.execute(
            "insert into comment(userid,bookid,cmid,info) "
            "values (\""+cuserid.get()+"\",\""+cbookid.get()+"\",\""+cmid.get()+"\",\""+cminfo.get()+"\");"
        )
    except pymysql.err.ProgrammingError:
        ms.showerror('invalid data','Please input correct data')
    else:
        db.commit()
        search_info("select * from comment limit 20;")
    return

def del_comment():
    cursor=db.cursor()
    if(len(cmid.get())==0):
        ms.showerror('invalid cmid',"Please input correct cmid")
        return
    try:
        cursor.execute("delete from comment where cmid=\""+cmid.get()+"\";")
    except pymysql.err.ProgrammingError:
        ms.showerror('invalid cmid','Please input correct cmid')
    else:
        db.commit()
        search_info("select * from comment limit 20;")
    return

def change_comment():
    cursor=db.cursor()
    if(len(cmid.get())==0):
        ms.showerror('invalid cmid',"Please input correct cmid")
        return
    cursor.execute("select * from comment where cmid=\""+cmid.get()+"\";")
    if(len(cursor.fetchall())==0):
        ms.showerror('invalid cmid',"Please input correct cmid")
        return
    if(len(cminfo.get())==0):
        ms.showerror('invalid data',"Please input changed data")
        return
    try:
        cursor.execute("update comment set info=\""+cminfo.get()+"\" where cmid=\""+cmid.get()+"\";")
    except pymysql.err.ProgrammingError:
        ms.showerror('invalid data','Please input correct data')
    else:
        db.commit()
        search_info("select * from comment limit 20;")
    return

def search_comment():
    val=[]
    for i in [("userid like \"%",cuserid.get(),"%\""),("bookid like \"%",cbookid.get(),"%\""),("cmid like \"%",cmid.get(),"%\""),("info like \"%",cminfo.get(),"%\"")]:
        if(len(i[1])):
            val.append(i[0]+i[1]+i[2])
    cypher="select * from comment"
    if(len(val)):
        cypher+=" where "
        for i in range(len(val)):
            cypher+=val[i]
            if(i!=len(val)-1):
                cypher+=" and "
    cypher+=";"
    search_info(cypher)
    return

def comment_not_login():
    tk.Label(
        frame[10],text='Comment Manage',
        font=('microsoft yahei',10),
        bg='mediumseagreen',fg='white'
    ).place(x=0,y=0,width=880,height=80,anchor='nw')
    tk.Label(
        frame[10],text='Please login first.',
        font=('microsoft yahei',10),
        bg='mediumaquamarine',fg='white'
    ).place(x=0,y=80,width=880,height=80,anchor='nw')
    return
def comment_login():
    tk.Label(
        frame[11],text='Comment Manage',
        font=('microsoft yahei',10),
        bg='mediumseagreen',fg='white'
    ).place(x=0,y=0,width=880,height=80,anchor='nw')
    tk.Label(
        frame[11],text="userid :",
        font=('microsoft yahei',10),
        bg='mediumaquamarine',fg='white'
    ).place(x=0,y=85,width=100,height=20,anchor='nw')
    tk.Label(
        frame[11],text="bookid :",
        font=('microsoft yahei',10),
        bg='mediumaquamarine',fg='white'
    ).place(x=0,y=110,width=100,height=20,anchor='nw')
    tk.Label(
        frame[11],text="cmid :",
        font=('microsoft yahei',10),
        bg='mediumaquamarine',fg='white'
    ).place(x=0,y=135,width=100,height=20,anchor='nw')
    tk.Label(
        frame[11],text="cminfo :",
        font=('microsoft yahei',10),
        bg='mediumaquamarine',fg='white'
    ).place(x=0,y=160,width=100,height=20,anchor='nw')
    cuserid.place(x=120,y=85,width=200,height=20,anchor='nw')
    cbookid.place(x=120,y=110,width=200,height=20,anchor='nw')
    cmid.place(x=120,y=135,width=200,height=20,anchor='nw')
    cminfo.place(x=120,y=160,width=200,height=20,anchor='nw')
    tk.Button(
        frame[11],text='add',relief='flat',
        font=('microsoft yahei',12),
        bg='mediumseagreen',fg='white',
        activebackground='aquamarine',activeforeground='black',
        command=add_comment
    ).place(x=330,y=85,width=60,height=120,anchor='nw')
    tk.Button(
        frame[11],text="delete",relief='flat',
        font=('microsoft yahei',12),
        bg='mediumseagreen',fg='white',
        activebackground='aquamarine',activeforeground='black',
        command=del_comment
    ).place(x=395,y=85,width=60,height=120,anchor='nw')
    tk.Button(
        frame[11],text="change",relief='flat',
        font=('microsoft yahei',12),
        bg='mediumseagreen',fg='white',
        activebackground='aquamarine',activeforeground='black',
        command=change_comment
    ).place(x=460,y=85,width=60,height=120,anchor='nw')
    tk.Button(
        frame[11],text="search",relief='flat',
        font=('microsoft yahei',12),
        bg='mediumseagreen',fg='white',
        activebackground='aquamarine',activeforeground='black',
        command=search_comment
    ).place(x=525,y=85,width=60,height=120,anchor='nw')
    return
def comment_page():
    frame_clear()
    if(not admin_login):
        set_frame(10)
        return
    set_frame(11)
    return

ruserid=tk.Entry(frame[13],show=None,font=('microsoft yahei',10),bg='mediumseagreen',fg='white')
rbookid=tk.Entry(frame[13],show=None,font=('microsoft yahei',10),bg='mediumseagreen',fg='white')
def add_recom():
    cursor=db.cursor()
    for i in [i.get() for i in[ruserid,rbookid]]:
        if(len(i)==0):
            ms.showerror('invalid data',"Please input correct data")
            return
    cursor.execute("select userid from recm_book where userid=\""+ruserid.get()+"\" and bookid=\""+rbookid.get()+"\";")
    if(len(cursor.fetchall())):
        ms.showerror('recommendation exists','This recommendation already exists.')
        return
    try:
        cursor.execute(
            "insert into recm_book(userid,bookid) "
            "values (\""+ruserid.get()+"\",\""+rbookid.get()+"\");"
        )
    except pymysql.err.ProgrammingError:
        ms.showerror('invalid data','Please input correct data')
    else:
        db.commit()
        search_info("select * from recm_book limit 20;")
    return
def del_recom():
    cursor=db.cursor()
    if(len(ruserid.get())==0 or len(rbookid.get())==0):
        ms.showerror('invalid data',"Please input correct userid and bookid")
        return
    try:
        cursor.execute("delete from recm_book where userid=\""+ruserid.get()+"\" and bookid=\""+rbookid.get()+"\";")
    except pymysql.err.ProgrammingError:
        ms.showerror('invalid data','Please input correct userid and bookid')
    else:
        db.commit()
        search_info("select * from recm_book limit 20;")
    return
def search_recom():
    val=[]
    for i in [("userid like \"%",ruserid.get(),"%\""),("bookid like \"%",rbookid.get(),"%\"")]:
        if(len(i[1])):
            val.append(i[0]+i[1]+i[2])
    cypher="select * from recm_book"
    if(len(val)):
        cypher+=" where "
        for i in range(len(val)):
            cypher+=val[i]
            if(i!=len(val)-1):
                cypher+=" and "
    cypher+=";"
    search_info(cypher)
    return
def recom_not_login():
    tk.Label(
        frame[12],text='Recommend Manage',
        font=('microsoft yahei',10),
        bg='mediumseagreen',fg='white'
    ).place(x=0,y=0,width=880,height=80,anchor='nw')
    tk.Label(
        frame[12],text='Please login first.',
        font=('microsoft yahei',10),
        bg='mediumaquamarine',fg='white'
    ).place(x=0,y=80,width=880,height=80,anchor='nw')
    return
def recom_login():
    tk.Label(
        frame[13],text='Recommend Manage',
        font=('microsoft yahei',10),
        bg='mediumseagreen',fg='white'
    ).place(x=0,y=0,width=880,height=80,anchor='nw')
    tk.Label(
        frame[13],text="userid :",
        font=('microsoft yahei',10),
        bg='mediumaquamarine',fg='white'
    ).place(x=0,y=85,width=100,height=20,anchor='nw')
    tk.Label(
        frame[13],text="bookid :",
        font=('microsoft yahei',10),
        bg='mediumaquamarine',fg='white'
    ).place(x=0,y=110,width=100,height=20,anchor='nw')
    ruserid.place(x=120,y=85,width=200,height=20,anchor='nw')
    rbookid.place(x=120,y=110,width=200,height=20,anchor='nw')
    tk.Button(
        frame[13],text='add',relief='flat',
        font=('microsoft yahei',12),
        bg='mediumseagreen',fg='white',
        activebackground='aquamarine',activeforeground='black',
        command=add_recom
    ).place(x=330,y=85,width=60,height=120,anchor='nw')
    tk.Button(
        frame[13],text="delete",relief='flat',
        font=('microsoft yahei',12),
        bg='mediumseagreen',fg='white',
        activebackground='aquamarine',activeforeground='black',
        command=del_recom
    ).place(x=395,y=85,width=60,height=120,anchor='nw')
    tk.Button(
        frame[13],text="search",relief='flat',
        font=('microsoft yahei',12),
        bg='mediumseagreen',fg='white',
        activebackground='aquamarine',activeforeground='black',
        command=search_recom
    ).place(x=460,y=85,width=60,height=120,anchor='nw')
    return
def recom_page():
    frame_clear()
    if(not admin_login):
        set_frame(12)
        return
    set_frame(13)
    return

def init_version_page():
    tk.Label(
        frame[14],text='Version',
        font=('microsoft yahei',10),
        bg='mediumseagreen',fg='white'
    ).place(x=0,y=0,width=880,height=80,anchor='nw')
    tk.Label(
        frame[14],text='Book Manage System v0.1',
        font=('microsoft yahei',10),
        bg='mediumaquamarine',fg='white'
    ).place(x=0,y=80,width=880,height=80,anchor='nw')
    return
def version_page():
    frame_clear()
    set_frame(14)
    return

def set_menu():
    menubar=tk.Menu(window,font=('microsoft yahei',16),tearoff=0)
    def set_second_menu(labels):
        sec_menu=tk.Menu(window,font=('microsoft yahei',8),tearoff=0)
        for i in labels:
            sec_menu.add_command(label=i[0],command=i[1])
        return sec_menu
    menubar.add_cascade(label='Options',menu=set_second_menu([('Login',login_page),('Logout',logout_page)]))
    menubar.add_cascade(label='Manage', menu=set_second_menu([('User',user_page),('Book',book_page),('Comment',comment_page),('Recommend',recom_page)]))
    menubar.add_command(label='Version',command=version_page)
    window['menu']=menubar
    return

def sidebar():
    side=tk.Frame(window,width=200,height=640)
    side.place(x=0,y=0,anchor='nw')
    button=[
        tk.Button(
            side,text='Main    ',
            font=('microsoft yahei',10),relief='flat',bg='mediumseagreen',fg='white',
            activebackground='aquamarine',activeforeground='black',command=main_page),
        tk.Button(
            side,text='Login   ',
            font=('microsoft yahei',10),relief='flat',bg='mediumseagreen',fg='white',
            activebackground='aquamarine',activeforeground='black',command=login_page),
        tk.Button(
            side,text='Logout  ',
            font=('microsoft yahei',10),relief='flat',bg='mediumseagreen',fg='white',
            activebackground='aquamarine',activeforeground='black',command=logout_page),
        tk.Button(
            side,text='User    ',
            font=('microsoft yahei',10),relief='flat',bg='mediumseagreen',fg='white',
            activebackground='aquamarine',activeforeground='black',command=user_page),
        tk.Button(
            side,text='Book    ',
            font=('microsoft yahei',10),relief='flat',bg='mediumseagreen',fg='white',
            activebackground='aquamarine',activeforeground='black',command=book_page),
        tk.Button(
            side,text='Comment ',
            font=('microsoft yahei',10),relief='flat',bg='mediumseagreen',fg='white',
            activebackground='aquamarine',activeforeground='black',command=comment_page),
        tk.Button(
            side,text='Recommend',
            font=('microsoft yahei',10),relief='flat',bg='mediumseagreen',fg='white',
            activebackground='aquamarine',activeforeground='black',command=recom_page),
        tk.Button(
            side,text='Version ',
            font=('microsoft yahei',10),relief='flat',bg='mediumseagreen',fg='white',
            activebackground='aquamarine',activeforeground='black',command=version_page)
    ]
    label=tk.Label(side,text=' ',bg='seagreen')
    label.place(x=0,y=0,anchor='nw',width=50,height=640)
    for i in range(len(button)):
        button[i].place(x=50,y=80*i,anchor='nw',width=150,height=80)
    return

set_menu()
sidebar()
main_not_login()
main_login()
login_not_login()
login_login()
logout_not_login()
logout_login()
user_not_login()
user_login()
book_not_login()
book_login()
comment_not_login()
comment_login()
recom_not_login()
recom_login()
init_version_page()

photo=tk.PhotoImage(file='sweat_smile.png')
img_label=tk.Button(window,image=photo,width=45,height=45,bg='seagreen',activebackground='mediumaquamarine',relief='flat',command=login_page)
img_label.place(x=0,y=0)

login_page()

window.mainloop()