from tkinter import *
import sqlite3
import cv2
from tkinter import messagebox
con = sqlite3.connect('evidence.db')
cursor = con.cursor()
table = TABLE_NAME
cursor.execute('''CREATE TABLE IF NOT EXISTS table(pattern TEXT, location TEXT images BLOB''')
def search():

    text = pattern_entry.get()
    data = cursor.execute(f'''SELECT "images" FROM {database} WHERE pattern="{text}"''')
    for i in data:
        date = i[0]
    try:
        with open('2.jpg', 'wb') as f:
            f.write(date)
        da = cv2.imread('2.jpg')
        cv2.imshow('resize', cv2.resize(da, (400, 300), interpolation=cv2.INTER_AREA))
        cv2.waitKey(0)
    except UnboundLocalError:
        dat = cursor.execute('''SELECT count(pattern) FROM evidences''')
        x = dat.fetchone()[0]
        messagebox.showerror(title='Invalid', message=f'Data not found\n your files capacity is {x}')
def blackandwhite():
    text = pattern_entry.get()
    data = cursor.execute(f'''SELECT "images" FROM {table_name} WHERE pattern="{text}"''')
    for i in data:
        date = i[0]
    try:
        with open('2.jpg', 'wb') as f:
            f.write(date)
        da = cv2.imread('2.jpg')
        gr = cv2.cvtColor(da, cv2.COLOR_BGR2GRAY)
        cv2.imshow('resize', cv2.resize(gr, (400, 300), interpolation=cv2.INTER_AREA))
        cv2.waitKey(0)
    except UnboundLocalError:
        dat = cursor.execute(f'''SELECT count(pattern) FROM {table_name}''')
        x = dat.fetchone()[0]
        messagebox.showerror(title='Invalid', message=f'Data not found\n your files capacity is {x}')
def blur1():
    text = pattern_entry.get()
    data = cursor.execute(f'''SELECT "images" FROM evidences WHERE pattern="{text}"''')
    for i in data :
        date = i[0]
    try :
        with open('2.jpg', 'wb') as f:
            f.write(date)
        da = cv2.imread('2.jpg')
        blur = cv2.GaussianBlur(da, (3, 3), cv2.BORDER_DEFAULT)
        cv2.imshow('resize', cv2.resize(blur, (400, 700), interpolation=cv2.INTER_AREA))
        cv2.waitKey(0)
    except UnboundLocalError:
        dat = cursor.execute('''SELECT count(pattern) FROM evidences1''')
        x = dat.fetchone()[0]
        messagebox.showerror(title='Invalid', message=f'Data not found\n your files capacity is {x}')
def canny1():
    text = pattern_entry.get()
    data = cursor.execute(f'''SELECT "images" FROM {table_name} WHERE pattern="{text}"''')
    for i in data :
        date = i[0]
    try:
        with open('2.jpg', 'wb') as f :
            f.write(date)
        da = cv2.imread('2.jpg')
        cany = cv2.Canny(da, 175, 125)
        cv2.imshow('resize', cv2.resize(cany, (400, 300), interpolation=cv2.INTER_AREA))
        cv2.waitKey(0)
    except UnboundLocalError:
        dat = cursor.execute('''SELECT count(pattern) FROM evidences1''')
        x = dat.fetchone()[0]
        messagebox.showerror(title='Invalid', message=f'Data not found\n your files capacity is {x}')
def delete():
    dat = cursor.execute('''SELECT count(pattern) FROM {table_name}''')
    y = dat.fetchone()[0]
    if int(y):
        x = pattern_entry.get()
        cursor.execute(f'''DELETE FROM {table_name} WHERE pattern={x}''')
    elif int(y) == 0:
        messagebox.showinfo(title="deletion", message=f"No images are in database")
    con.commit()
def count():
    dat = cursor.execute('''SELECT count(pattern) FROM evidences''')
    x = dat.fetchone()[0]
    if str(x) == "0":
        messagebox.showinfo(title="count", message=f"no images in database")
    elif str(x) == "1":
        messagebox.showinfo(title="count", message=f"{x} image in database")
    else:
        messagebox.showinfo(title="count", message=f"{x} images in database")
def delete_all1():
  cursor.execute(f'''DELETE FROM {table_name}''')
window = Tk()
window.title("Evidence collector")
window.config(width=500, height=500, bg="red")
pattern = Label(text='pattern: ')
pattern_entry = Entry(width=60)
search = Button(text='search', width=60, command=search)
dele = Button(text='delete', width=60, command=delete)
black = Button(text="B&W", width=60, command=blackandwhite)
blur = Button(text="blur", width=60, command=blur1)
canny = Button(text="canny", width=60, command=canny1)
coun = Button(text="count", width=60, command=count)
delete_all = Button(text="delete all", width=60, command=delete_all1)
pattern.pack(fill=X, ipady=1)
pattern_entry.pack(fill=X, pady=10)
search.pack(fill=X, pady=10)
dele.pack(fill=X, pady=10)
black.pack(fill=X, pady=10)
blur.pack(fill=X, pady=10)
coun.pack(fill=X, pady=10)
canny.pack(fill=Y, pady=5)
delete_all.pack(fill=Y, pady=5)

window.mainloop()
