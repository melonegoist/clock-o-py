from tkinter import *
import time
import sqlite3
from tkinter import colorchooser
from widget_winfo import widget_h, widget_w
import os
import sys





l = []

db = sqlite3.connect('db.db')
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS users (
    theme TEXT
)""")

db.commit()


w = 195
h = 46

sc = Tk()
sc.geometry(f"{w}x{h}+1000+0")
sc.resizable(False, False)
sc.configure(bg = '#121212')
sc.overrideredirect(True)
sc.wm_attributes('-transparentcolor', '#121212')

counter = 0


color = '#121212'
redc = '#fa897b'
greenc = '#d0e6a5'


def exit_w():
    sc.destroy()

def clock():
    timeh = time.strftime('%H')
    timem = time.strftime('%M')
    times = time.strftime('%S')
    label['text'] = f'{int(timeh)+2}:{timem}:{times}'
    label.after(1000, clock)

def show(event):
    global counter, sc2
    if counter %2 == 0:
        exit_bttn.place(x = 0, y = 10)
        sc2.wm_attributes('-disabled', False)
        sc2.wm_attributes('-alpha', 100)
        
    else:
        exit_bttn.place_forget()
        sc2.wm_attributes('-disabled', True)
        sc2.wm_attributes('-alpha', 0)
        sc3.wm_attributes('-disabled', True)
        sc3.wm_attributes('-alpha', 0)
    counter += 1

def purple():
    theme = 'purple'
    sql.execute("SELECT theme FROM users")

    sql.execute(f"INSERT INTO users VALUES ('{theme}')")
    db.commit()
    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)

def red():
    theme = 'red'
    sql.execute("SELECT theme FROM users")
    sql.execute(f"INSERT INTO users VALUES ('{theme}')")
    db.commit()
    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)

def green():
    theme = 'green'
    sql.execute("SELECT theme FROM users")
    sql.execute(f"INSERT INTO users VALUES ('{theme}')")
    db.commit()
    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)


def export():
    (rgb,hex) = colorchooser.askcolor()

    sql.execute("SELECT theme FROM users")
    sql.execute(f"INSERT INTO users VALUES ('{hex}')")
    db.commit()
    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)


def convert():
    global value
    value = entry.get()

    
    sql.execute("SELECT theme FROM users")
    sql.execute(f"INSERT INTO users VALUES ('{value}')")
    db.commit()
    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)


def custom():
    global sc3, sw

    sc3.wm_attributes('-disabled', False)
    sc3.wm_attributes('-alpha', 100)


    entry.pack()

    
    bttnentry = Button(sc3,
        text = '->',
        bg = 'white',
        fg = 'black',
        relief = 'flat',
        overrelief= 'solid',
        font = ('Consolas', 10, 'bold'),
        command = convert
    )

    bttnentry.place(x = sw - 30, y = 3)

sql.execute("SELECT * FROM users")
db.commit()
output = sql.fetchall()
for row in output:
    l.insert(0, row)


try:
    a = str(l[0])
except:
    pass

try:
    if a == "('purple',)":
        theme_color = '#9966cc'
        sc.update_idletasks()
    elif a == "('red',)":
        theme_color = f'{redc}'
        sc.update_idletasks()
    elif a == "('green',)":
        theme_color = f'{greenc}'
        sc.update_idletasks()
    elif a == "('None',)":
        theme_color = '#e3131a'
        sc.update_idletasks()
    else:
        theme_color = a[2:9]
        
except:
    theme_color = '#678987'



exit_bttn = Button(
    text = 'X',
    bg = 'red',
    fg = 'white',
    relief = 'flat',
    overrelief = 'solid',
    font = ('Verdana', 10),
    width = 2,
    command = exit_w
)

label = Label(
    text = '00:00:00',
    font = ('Verdana',25, "bold"),
    bg = '#121212',
    fg = f'{theme_color}'
)

lw = widget_w(label)
lh = widget_h(label)

sc2 = Toplevel()
sc2.overrideredirect(1)

sc2.config(bg = f'{color}')
sc2.geometry(f"{lw}x{28*5}+1000+{lh}")
sc2.wm_attributes('-disabled', True)
sc2.wm_attributes('-alpha', 0)



bttnp = Button(sc2,
    text = 'amethyst',
    command = purple,
    relief = 'flat',
    overrelief='solid',
    bg = '#9966cc',
    fg = 'white',
    font = ('Verdana', 10),
    width = 20
)

bttnr = Button(sc2,
    text = 'red',
    command = red,
    relief = 'flat',
    overrelief='solid',
    bg = f'{redc}',
    fg = 'white',
    font = ('Verdana', 10)
)

bttng = Button(sc2,
    text = 'green',
    command = green,
    relief = 'flat',
    overrelief='solid',
    bg = f'{greenc}',
    fg = 'white',
    font = ('Verdana', 10),
    width = 5
)

bttnexp = Button(sc2,
    text = 'export',
    relief = 'flat',
    overrelief = 'solid',
    bg = '#808080',
    fg = 'white',
    font = ('Verdana', 10),
    command = export
)

bttninp = Button(sc2,
    text = 'custom',
    relief = 'flat',
    overrelief = 'solid',
    bg = '#808080',
    fg = 'white',
    font = ('Verdana', 10),
    command = custom
)


sw = widget_w(bttnp)
sh = widget_h(bttnp)
sc3 = Toplevel()
sc3.overrideredirect(1)

sc3.geometry(f"{sw}x{sh}+{26+1000}+186")
sc3.wm_attributes('-disabled', True)
sc3.wm_attributes('-alpha', 0)

entry = Entry(sc3, justify='center',width = 15, font = ('Icon', 15), )
entry.insert(0, '#')

label.place(x = 26, y = 0)
bttnp.grid(column=0,row = 1,sticky='we')
bttnr.grid(column=0,row = 2,sticky='we')
bttng.grid(column=0,row = 3,sticky='we')
bttnexp.grid(column=0,row = 4,sticky='we')
bttninp.grid(column=0,row = 5,sticky='we')


sc.bind('<Button-3>', show)
clock()


sc.mainloop()
