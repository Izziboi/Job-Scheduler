from tkinter import *
from tkinter import messagebox
import sqlite3


root = Tk()
root["bg"] = "sky blue"
root.geometry("640x760")
root.title("Editor")
root.iconbitmap('C:/Users/izzit/OneDrive/Desktop/bros/cleans.ico')

title_l = Label(root, text="Edit Already Existing Records Here",
                font=("times 20"), bg="sky blue")
title_l.place(x=120, y=20)

info_l = Label(root, text="Enter the jobdate and customer name you are searching for",
               font=("times 15"), bg="sky blue")
info_l.place(x=110, y=title_l.winfo_reqheight()+70)

oldjobdate_l = Label(root, text="Old Job Date",
                     font=("times 15"), bg="sky blue")
oldjobdate_l.place(x=50, y=title_l.winfo_reqheight()+130)

oldcustname_l = Label(root, text="Old Customer Name",
                      font=("times 15"), bg="sky blue")
oldcustname_l.place(x=50, y=title_l.winfo_reqheight()+180)

oldjobdate_e = Entry(root, font=("times 15"), width=35)
oldjobdate_e.place(x=230, y=title_l.winfo_reqheight()+130)

oldcustname_e = Entry(root, font=("times 15"), width=35)
oldcustname_e.place(x=230, y=title_l.winfo_reqheight()+180)

demarc_l = Label(root, text="************************************************************",
                 font=("times 15"), bg="sky blue", fg="purple")
demarc_l.place(x=50, y=title_l.winfo_reqheight()+270)

info_l = Label(root, text="Enter the correct customer and other details below",
               font=("times 15"), bg="sky blue")
info_l.place(x=110, y=title_l.winfo_reqheight()+330)

jobdate_l = Label(root, text="Job Date", font=("times 15"), bg="sky blue")
jobdate_l.place(x=50, y=title_l.winfo_reqheight()+395)

custname_l = Label(root, text="Customer Name",
                   font=("times 15"), bg="sky blue")
custname_l.place(x=50, y=title_l.winfo_reqheight()+440)

custaddress_l = Label(root, text="Customer Address",
                      font=("times 15"), bg="sky blue")
custaddress_l.place(x=50, y=title_l.winfo_reqheight()+488)

custphone_l = Label(root, text="Customer Phone",
                    font=("times 15"), bg="sky blue")
custphone_l.place(x=50, y=title_l.winfo_reqheight()+540)

jobtype_l = Label(root, text="Job Type",
                  font=("times 15"), bg="sky blue")
jobtype_l.place(x=50, y=title_l.winfo_reqheight()+584)

workwith_l = Label(root, text="Working With",
                   font=("times 15"), bg="sky blue")
workwith_l.place(x=50, y=title_l.winfo_reqheight()+630)

jobdate_e = Entry(root, font=("times 15"), width=35)
jobdate_e.place(x=230, y=title_l.winfo_reqheight()+392)

custname_e = Entry(root, font=("times 15"), width=35)
custname_e.place(x=230, y=title_l.winfo_reqheight()+438)

custaddress_e = Entry(root, font=("times 15"), width=35)
custaddress_e.place(x=230, y=title_l.winfo_reqheight()+485)

custphone_e = Entry(root, font=("times 15"), width=35)
custphone_e.place(x=230, y=title_l.winfo_reqheight()+535)

jobtype_e = Entry(root, font=("times 15"), width=35)
jobtype_e.place(x=230, y=title_l.winfo_reqheight()+580)

workwith_e = Entry(root, font=("times 15"), width=35)
workwith_e.place(x=230, y=title_l.winfo_reqheight()+625)

editjob_b = Button(root, text="Edit Schedule", font=(
    "times 15"), bg="light green", width=10, command=lambda: recedit())
editjob_b.place(x=250, y=title_l.winfo_reqheight()+680)


def recedit():
    oldj = oldjobdate_e.get()
    oldc = oldcustname_e.get()
    date1 = jobdate_e.get()
    name1 = custname_e.get()
    address1 = custaddress_e.get()
    phone1 = custphone_e.get()
    jobtype1 = jobtype_e.get()
    with1 = workwith_e.get()
    if oldj == "" or oldc == "" or date1 == "" or name1 == "" or address1 == "" or phone1 == "" or jobtype1 == "" or with1 == "":
        messagebox.showinfo("Error", "You must fill all empty fields")
        return
    else:
        connection6 = sqlite3.connect(database="appointments.db", timeout=20)
        curss5 = connection6.cursor()

        queries7 = """SELECT jobdate,
        customername
        FROM customers
        WHERE jobdate IN ("%s") AND customername IN ("%s")""" % (oldj, oldc)

        curss5.execute(queries7)
        output3 = curss5.fetchall()
        # print(output3)
        mylist2 = len(list(output3))

        if mylist2 == 0:
            messagebox.showinfo(
                "Error", "No job date or customer name matches your search entries")
            return
        else:
            decision = messagebox.askquestion(
                "Confirm", "Sure to make the changes?", icon="question")
            if decision == "no":
                return
            else:
                queries8 = """UPDATE customers
                SET jobdate = "%s",
                customername = "%s",
                customeraddress = "%s",
                customerphone = "%s",
                jobtype = "%s",
                workingwith = "%s"
                WHERE jobdate IN ("%s") AND customername IN ("%s")""" % (date1, name1, address1, phone1, jobtype1, with1, oldj, oldc)

                curss5.execute(queries8)
                connection6.commit()
                curss5.close()
                oldjobdate_e.delete(0, END)
                oldcustname_e.delete(0, END)
                jobdate_e.delete(0, END)
                custname_e.delete(0, END)
                custaddress_e.delete(0, END)
                custphone_e.delete(0, END)
                jobtype_e.delete(0, END)
                workwith_e.delete(0, END)
                messagebox.showinfo("Success", "Changes successfully made")

                if connection6:
                    connection6.close()


root.mainloop()
