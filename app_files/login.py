from tkinter import *
from tkinter import messagebox
import sqlite3

root = Tk()
root["bg"] = "sky blue"
root.geometry("400x300")
root.title("Access")
root.iconbitmap('C:/Users/izzit/OneDrive/Desktop/bros/cleans.ico')

head1 = Label(root, text="Enter Or Edit Your Login Details",
              font=("times 15"), bg="sky blue")
head1.place(x=50, y=10)

head2 = Label(root, text="Username", font=("times 15"), bg="sky blue")
head2.place(x=10, y=head1.winfo_reqheight()+50)

head3 = Label(root, text="PIN", font=("times 15"), bg="sky blue")
head3.place(x=10, y=head1.winfo_reqheight()+80)

username_e = Entry(root, width=25, font=("times 15"))
username_e.place(x=head2.winfo_reqwidth()+30, y=head1.winfo_reqheight()+50)

pin_e = Entry(root, width=25, font=("times 15"))
pin_e.place(x=head2.winfo_reqwidth()+30, y=head1.winfo_reqheight()+80)

login_b = Button(root, text="Login", font=(
    "times 15"), bg="light green", width=15, command=lambda: logging())
login_b.place(x=head2.winfo_reqwidth()+30, y=head3.winfo_reqheight()+130)

editlogin_b = Button(root, text="Edit Login Details", font=(
    "times 15"), bg="light green", width=15, command=lambda: editing())
editlogin_b.place(x=head2.winfo_reqwidth()+30, y=login_b.winfo_reqheight()+180)


def logging():

    use1 = username_e.get()
    pin1 = pin_e.get()

    connection2 = sqlite3.connect(database="appointments.db", timeout=20)
    curss1 = connection2.cursor()

    if use1 == "" or pin1 == "":
        messagebox.showinfo("Error", "Please fill empty field(s)")
        return
    elif use1.isdigit() or not(pin1.isdigit()):
        messagebox.showinfo(
            "Error", "Use text for username and digits for PIN")
        return
    else:
        queries3 = """SELECT *
        FROM access
        WHERE adminname IN ("%s") AND adminpin IN (%d)""" % (use1, int(pin1))

        curss1.execute(queries3)
        output2 = curss1.fetchall()
        mylist1 = len(list(output2))

        if mylist1 == 0:
            messagebox.showinfo(
                "Error", "No username or PIN matches your entry")
            return
        else:
            curss1.close()
            connection2.close()
            root.destroy()
            import tablepaste


def editing():
    import editlock


root.mainloop()
