from tkinter import *
from tkinter import messagebox
import sqlite3

root = Tk()
root["bg"] = "sky blue"
root.geometry("900x300")
root.title("Edit")
root.iconbitmap('C:/Users/izzit/OneDrive/Desktop/bros/cleans.ico')

head1 = Label(root, text="Edit Your Login Details",
              font=("times 15"), bg="sky blue")
head1.place(x=350, y=10)

head2 = Label(root, text="Old Username", font=("times 15"), bg="sky blue")
head2.place(x=10, y=head1.winfo_reqheight()+50)

head3 = Label(root, text="Old PIN", font=("times 15"), bg="sky blue")
head3.place(x=10, y=head1.winfo_reqheight()+100)

username_e = Entry(root, width=25, font=("times 15"))
username_e.place(x=head2.winfo_reqwidth()+30, y=head1.winfo_reqheight()+50)

pin_e = Entry(root, width=25, font=("times 15"))
pin_e.place(x=head2.winfo_reqwidth()+30, y=head1.winfo_reqheight()+100)

head4 = Label(root, text="New Username", font=("times 15"), bg="sky blue")
head4.place(x=username_e.winfo_reqwidth()+200, y=head1.winfo_reqheight()+50)

head5 = Label(root, text="New PIN", font=("times 15"), bg="sky blue")
head5.place(x=pin_e.winfo_reqwidth()+200, y=head1.winfo_reqheight()+100)

nusername_e = Entry(root, width=25, font=("times 15"))
nusername_e.place(x=head4.winfo_reqwidth()+480, y=head1.winfo_reqheight()+50)

npin_e = Entry(root, width=25, font=("times 15"))
npin_e.place(x=head5.winfo_reqwidth()+526, y=head1.winfo_reqheight()+100)

editlogin_b = Button(root, text="Edit", font=(
    "times 15"), bg="light green", width=15, command=lambda: editdet())
editlogin_b.place(x=380, y=pin_e.winfo_reqheight()+180)


def editdet():
    olduse = username_e.get()
    oldpin = pin_e.get()
    newuse = nusername_e.get()
    newpins = npin_e.get()

    if not (oldpin.isdigit()) or not (newpins.isdigit()) or olduse == "" or newuse == "":
        messagebox.showinfo(
            "Error", "Please fill empty field(s) or edit entry")
        return
    else:
        connection1 = sqlite3.connect(database="appointments.db", timeout=20)
        curss = connection1.cursor()

        queries1 = """SELECT adminname,
        adminpin
        FROM access
        WHERE adminname IN ("%s") AND adminpin IN (%d)""" % (olduse, int(oldpin))

        curss.execute(queries1)
        output1 = curss.fetchall()
        mylist = len(list(output1))

        if mylist == 0:
            messagebox.showinfo(
                "Error", "No username or PIN matches your entry")
            return
        else:
            decision = messagebox.askquestion(
                "Confirm", "Sure to make the changes?", icon="question")
            if decision == "no":
                return
            else:

                queries2 = """UPDATE access
                SET adminname = "%s",
                adminpin = %d
                WHERE adminname IN ("%s")""" % (newuse, int(newpins), olduse)

                curss.execute(queries2)

                connection1.commit()
                curss.close()
                username_e.delete(0, END)
                pin_e.delete(0, END)
                nusername_e.delete(0, END)
                npin_e.delete(0, END)
                messagebox.showinfo(
                    "Success", "Changes successfully made")

    if connection1:
        connection1.close()


root.mainloop()
