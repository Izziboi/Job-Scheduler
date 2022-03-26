from tkinter import *
from tkinter import messagebox
import sqlite3
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from twilio.rest import Client
from pathlib import Path
import smtplib

root = Tk()
root["bg"] = "sky blue"
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry(f"{width}x{height}")
root.title("Scheduler")
root.iconbitmap('C:/Users/izzit/OneDrive/Desktop/bros/cleans.ico')

title_l = Label(root, text="Appointment Manager",
                font=("times 20"), bg="sky blue")
title_l.place(x=600, y=20)

info_l = Label(root, text="Please fill in customer and other details in the fields below",
               font=("times 15"), bg="sky blue")
info_l.place(x=450, y=title_l.winfo_reqheight()+40)

jobdate_l = Label(root, text="Job Date", font=("times 15"), bg="sky blue")
jobdate_l.place(x=450, y=title_l.winfo_reqheight()+100)

custname_l = Label(root, text="Customer Name",
                   font=("times 15"), bg="sky blue")
custname_l.place(x=450, y=title_l.winfo_reqheight()+150)

custaddress_l = Label(root, text="Customer Address",
                      font=("times 15"), bg="sky blue")
custaddress_l.place(x=450, y=title_l.winfo_reqheight()+200)

custphone_l = Label(root, text="Customer Phone",
                    font=("times 15"), bg="sky blue")
custphone_l.place(x=450, y=title_l.winfo_reqheight()+250)

jobtype_l = Label(root, text="Job Type",
                  font=("times 15"), bg="sky blue")
jobtype_l.place(x=450, y=title_l.winfo_reqheight()+300)

workwith_l = Label(root, text="Working With",
                   font=("times 15"), bg="sky blue")
workwith_l.place(x=450, y=title_l.winfo_reqheight()+350)

jobdate_e = Entry(root, font=("times 15"), width=35)
jobdate_e.place(x=620, y=title_l.winfo_reqheight()+95)

custname_e = Entry(root, font=("times 15"), width=35)
custname_e.place(x=620, y=title_l.winfo_reqheight()+145)

custaddress_e = Entry(root, font=("times 15"), width=35)
custaddress_e.place(x=620, y=title_l.winfo_reqheight()+195)

custphone_e = Entry(root, font=("times 15"), width=35)
custphone_e.place(x=620, y=title_l.winfo_reqheight()+245)

jobtype_e = Entry(root, font=("times 15"), width=35)
jobtype_e.place(x=620, y=title_l.winfo_reqheight()+295)

workwith_e = Entry(root, font=("times 15"), width=35)
workwith_e.place(x=620, y=title_l.winfo_reqheight()+345)

phone_e = Entry(root, font=("times 15"), width=18)
phone_e.place(x=435, y=title_l.winfo_reqheight()+462)

email_e = Entry(root, font=("times 15"), width=20)
email_e.place(x=905, y=title_l.winfo_reqheight()+462)

editjob_b = Button(root, text="Edit Schedule", font=(
    "times 15"), bg="light green", width=10, command=lambda: editrecord())
editjob_b.place(x=330, y=title_l.winfo_reqheight()+400)

viewjob_b = Button(root, text="View Schedule", font=(
    "times 15"), bg="light green", width=12, command=lambda: viewrecord())
viewjob_b.place(x=635,
                y=title_l.winfo_reqheight()+400)

newjob_b = Button(root, text="Add New Schedule", font=(
    "times 15"), bg="light green", width=14, command=lambda: insertrecord())
newjob_b.place(x=460,
               y=title_l.winfo_reqheight()+400)

editlogin_b = Button(root, text="Edit Login Details", font=(
    "times 15"), bg="light green", width=14, command=lambda: edlogin())
editlogin_b.place(x=workwith_e.winfo_reqwidth()+590,
                  y=title_l.winfo_reqheight()+400)

clearwin_b = Button(root, text="Clear Window", font=(
    "times 15"), bg="light green", width=12, command=lambda: clears())
clearwin_b.place(x=790, y=title_l.winfo_reqheight()+400)

phone_b = Button(root, text="To Phone", font=(
    "times 15"), bg="light green", width=8, command=lambda: toPhone())
phone_b.place(x=330, y=title_l.winfo_reqheight()+450)

email_b = Button(root, text="To Email", font=(
    "times 15"), width=8, bg="light green", command=lambda: toEmail())
email_b.place(x=800, y=title_l.winfo_reqheight()+450)

frames_f = Frame(root, bg='sky blue', width='1320', height='160')
frames_f.place(x=80, y=title_l.winfo_reqheight()+500)


def edlogin():
    import editlock


def insertrecord():
    date1 = jobdate_e.get()
    name1 = custname_e.get()
    address1 = custaddress_e.get()
    phone1 = custphone_e.get()
    jobtype1 = jobtype_e.get()
    with1 = workwith_e.get()

    connection3 = sqlite3.connect(database="appointments.db", timeout=20)
    curss2 = connection3.cursor()

    if date1 == "" or name1 == "" or address1 == "" or phone1 == "" or jobtype1 == "":
        messagebox.showinfo("Error", "Fill empty field(s)")
    else:
        queries4 = """INSERT INTO customers(jobdate, customername, customeraddress, customerphone, jobtype, workingwith)
        VALUES ("%s", "%s", "%s", "%s", "%s", "%s")""" % (date1, name1, address1, phone1, jobtype1, with1)

        decide2 = messagebox.askquestion(
            "Confirm", "Sure to add record?", icon="question")
        if decide2 == "no":
            return
        else:
            curss2.execute(queries4)
            connection3.commit()
            curss2.close()
            connection3.close()

            jobdate_e.delete(0, END)
            custname_e.delete(0, END)
            custaddress_e.delete(0, END)
            custphone_e.delete(0, END)
            jobtype_e.delete(0, END)
            workwith_e.delete(0, END)
            messagebox.showinfo("Success", "Record added successfully")


def editrecord():
    import editrecs


captions = ["Job_Date", "Customer_Name", "Customer_Address",
            "Customer_Phone", "Job_Type", "Working_With"]


def viewrecord():
    date1 = jobdate_e.get()
    name1 = custname_e.get()
    if date1 == "" and name1 == "":
        messagebox.showinfo(
            "Error", "Please fill job date or customer name")
        return
    else:
        connection5 = sqlite3.connect(
            database="appointments.db", timeout=20)
        curss4 = connection5.cursor()

        if date1 != "" and name1 == "":
            queries6 = """SELECT *
            FROM customers
            WHERE jobdate IN ("%s")""" % (date1)

            curss4.execute(queries6)
            output4 = curss4.fetchall()

        if date1 == "" and name1 != "":
            queries6 = """SELECT *
            FROM customers
            WHERE customername IN ("%s")""" % (name1)

            curss4.execute(queries6)
            output4 = curss4.fetchall()

        if date1 != "" and name1 != "":
            queries6 = """SELECT *
            FROM customers
            WHERE jobdate IN ("%s") AND customername IN ("%s")""" % (date1, name1)

            curss4.execute(queries6)
            output4 = curss4.fetchall()

        if len(output4) == 0:
            messagebox.showinfo(
                "Error", "No job date or customer name matches your entry")
            return
        else:
            counts = 0
            newlist = []

            for i in range(len(output4)):
                counts += 1
                if counts <= len(output4):
                    for k, l in enumerate(output4[i]):
                        if k == 0:
                            pass
                        else:
                            newlist.append(l)

            newlength = int(len(newlist)/len(captions))

            if newlength == 1:
                clears()

                for caps in range(len(captions)):
                    Label(frames_f, text=newlist[caps], width=30, height=1).grid(
                        row=newlength, column=caps, padx=1, pady=1)
            elif newlength == 2:
                clears()

                for caps1 in range(len(captions)):
                    Label(frames_f, text=newlist[caps1], width=30, height=1).grid(
                        row=1, column=caps1, padx=1, pady=1)
                for caps2 in range(6, 12):
                    Label(frames_f, text=newlist[caps2], width=30, height=1).grid(
                        row=2, column=caps2-6, padx=1, pady=1)
            elif newlength == 3:
                clears()

                for caps1 in range(len(captions)):
                    Label(frames_f, text=newlist[caps1], width=30, height=1).grid(
                        row=1, column=caps1, padx=1, pady=1)
                for caps2 in range(6, 12):
                    Label(frames_f, text=newlist[caps2], width=30, height=1).grid(
                        row=2, column=caps2-6, padx=1, pady=1)
                for caps3 in range(12, 18):
                    Label(frames_f, text=newlist[caps3], width=30, height=1).grid(
                        row=3, column=caps3-12, padx=1, pady=1)
            elif newlength == 4:
                clears()

                for caps1 in range(len(captions)):
                    Label(frames_f, text=newlist[caps1], width=30, height=1).grid(
                        row=1, column=caps1, padx=1, pady=1)
                for caps2 in range(6, 12):
                    Label(frames_f, text=newlist[caps2], width=30, height=1).grid(
                        row=2, column=caps2-6, padx=1, pady=1)
                for caps3 in range(12, 18):
                    Label(frames_f, text=newlist[caps3], width=30, height=1).grid(
                        row=3, column=caps3-12, padx=1, pady=1)
                for caps4 in range(18, 24):
                    Label(frames_f, text=newlist[caps4], width=30, height=1).grid(
                        row=4, column=caps4-18, padx=1, pady=1)
            elif newlength == 5:
                clears()

                for caps1 in range(len(captions)):
                    Label(frames_f, text=newlist[caps1], width=30, height=1).grid(
                        row=1, column=caps1, padx=1, pady=1)
                for caps2 in range(6, 12):
                    Label(frames_f, text=newlist[caps2], width=30, height=1).grid(
                        row=2, column=caps2-6, padx=1, pady=1)
                for caps3 in range(12, 18):
                    Label(frames_f, text=newlist[caps3], width=30, height=1).grid(
                        row=3, column=caps3-12, padx=1, pady=1)
                for caps4 in range(18, 24):
                    Label(frames_f, text=newlist[caps4], width=30, height=1).grid(
                        row=4, column=caps4-18, padx=1, pady=1)
                for caps5 in range(24, 30):
                    Label(frames_f, text=newlist[caps5], width=30, height=1).grid(
                        row=5, column=caps5-24, padx=1, pady=1)

    if connection5:
        connection5.close()


def clears():
    for caps in range(len(captions)):
        Label(frames_f, text=captions[caps], font=("Arial 9 bold"), width=30, height=1).grid(
            row=0, column=caps, padx=1, pady=1)
    for caps1 in range(len(captions)):
        Label(frames_f, text="", width=30, height=1).grid(
            row=1, column=caps1, padx=1, pady=1)
    for caps2 in range(6, 12):
        Label(frames_f, text="", width=30, height=1).grid(
            row=2, column=caps2-6, padx=1, pady=1)
    for caps3 in range(12, 18):
        Label(frames_f, text="", width=30, height=1).grid(
            row=3, column=caps3-12, padx=1, pady=1)
    for caps4 in range(18, 24):
        Label(frames_f, text="", width=30, height=1).grid(
            row=4, column=caps4-18, padx=1, pady=1)
    for caps5 in range(24, 30):
        Label(frames_f, text="", width=30, height=1).grid(
            row=5, column=caps5-24, padx=1, pady=1)


def newlength1():
    for caps in range(len(captions)):
        if caps == 0:
            myMess.attach(MIMEText("Job date: {}".format(newlist[0])))
        if caps == 1:
            myMess.attach(MIMEText("\nCustomer name: {}".format(newlist[1])))
        if caps == 2:
            myMess.attach(
                MIMEText("\nCustomer address: {}".format(newlist[2])))
        if caps == 3:
            myMess.attach(
                MIMEText("\nCustomer phone number: {}".format(newlist[3])))
        if caps == 4:
            myMess.attach(MIMEText("\nJob type: {}".format(newlist[4])))
        if caps == 5:
            myMess.attach(MIMEText("\nWorking with: {}".format(newlist[5])))


def newlength2():
    for caps in range(len(captions)):
        if caps == 0:
            myMess.attach(
                MIMEText("***Job 1***\n Job date: {}".format(newlist[0])))
        if caps == 1:
            myMess.attach(MIMEText("\nCustomer name: {}".format(newlist[1])))
        if caps == 2:
            myMess.attach(
                MIMEText("\nCustomer address: {}".format(newlist[2])))
        if caps == 3:
            myMess.attach(
                MIMEText("\nCustomer phone number: {}".format(newlist[3])))
        if caps == 4:
            myMess.attach(MIMEText("\nJob type: {}".format(newlist[4])))
        if caps == 5:
            myMess.attach(MIMEText("\nWorking with: {}\n".format(newlist[5])))

    for caps1 in range(6, 12):
        if caps1 == 6:
            myMess.attach(
                MIMEText("################################\n ***Job 2***\n"))
            myMess.attach(MIMEText("Job date: {}".format(newlist[6])))
        if caps1 == 7:
            myMess.attach(MIMEText("\nCustomer name: {}".format(newlist[7])))
        if caps1 == 8:
            myMess.attach(
                MIMEText("\nCustomer address: {}".format(newlist[8])))
        if caps1 == 9:
            myMess.attach(
                MIMEText("\nCustomer phone number: {}".format(newlist[9])))
        if caps1 == 10:
            myMess.attach(MIMEText("\nJob type: {}".format(newlist[10])))
        if caps1 == 11:
            myMess.attach(MIMEText("\nWorking with: {}".format(newlist[11])))


def newlength3():
    for caps in range(len(captions)):
        if caps == 0:
            myMess.attach(
                MIMEText("***Job 1***\n Job date: {}".format(newlist[0])))
        if caps == 1:
            myMess.attach(MIMEText("\nCustomer name: {}".format(newlist[1])))
        if caps == 2:
            myMess.attach(
                MIMEText("\nCustomer address: {}".format(newlist[2])))
        if caps == 3:
            myMess.attach(
                MIMEText("\nCustomer phone number: {}".format(newlist[3])))
        if caps == 4:
            myMess.attach(MIMEText("\nJob type: {}".format(newlist[4])))
        if caps == 5:
            myMess.attach(MIMEText("\nWorking with: {}\n".format(newlist[5])))

    for caps1 in range(6, 12):
        if caps1 == 6:
            myMess.attach(
                MIMEText("################################\n ***Job 2***\n"))
            myMess.attach(MIMEText("Job date: {}".format(newlist[6])))
        if caps1 == 7:
            myMess.attach(MIMEText("\nCustomer name: {}".format(newlist[7])))
        if caps1 == 8:
            myMess.attach(
                MIMEText("\nCustomer address: {}".format(newlist[8])))
        if caps1 == 9:
            myMess.attach(
                MIMEText("\nCustomer phone number: {}".format(newlist[9])))
        if caps1 == 10:
            myMess.attach(MIMEText("\nJob type: {}".format(newlist[10])))
        if caps1 == 11:
            myMess.attach(MIMEText("\nWorking with: {}\n".format(newlist[11])))

    for caps2 in range(12, 18):
        if caps2 == 12:
            myMess.attach(
                MIMEText("################################\n ***Job 3***\n"))
            myMess.attach(MIMEText("Job date: {}".format(newlist[12])))
        if caps2 == 13:
            myMess.attach(MIMEText("\nCustomer name: {}".format(newlist[13])))
        if caps2 == 14:
            myMess.attach(
                MIMEText("\nCustomer address: {}".format(newlist[14])))
        if caps2 == 15:
            myMess.attach(
                MIMEText("\nCustomer phone number: {}".format(newlist[15])))
        if caps2 == 16:
            myMess.attach(MIMEText("\nJob type: {}".format(newlist[16])))
        if caps2 == 17:
            myMess.attach(MIMEText("\nWorking with: {}\n".format(newlist[17])))


def newlength4():
    for caps in range(len(captions)):
        if caps == 0:
            myMess.attach(
                MIMEText("***Job 1***\n Job date: {}".format(newlist[0])))
        if caps == 1:
            myMess.attach(MIMEText("\nCustomer name: {}".format(newlist[1])))
        if caps == 2:
            myMess.attach(
                MIMEText("\nCustomer address: {}".format(newlist[2])))
        if caps == 3:
            myMess.attach(
                MIMEText("\nCustomer phone number: {}".format(newlist[3])))
        if caps == 4:
            myMess.attach(MIMEText("\nJob type: {}".format(newlist[4])))
        if caps == 5:
            myMess.attach(MIMEText("\nWorking with: {}\n".format(newlist[5])))

    for caps1 in range(6, 12):
        if caps1 == 6:
            myMess.attach(
                MIMEText("################################\n ***Job 2***\n"))
            myMess.attach(MIMEText("Job date: {}".format(newlist[6])))
        if caps1 == 7:
            myMess.attach(MIMEText("\nCustomer name: {}".format(newlist[7])))
        if caps1 == 8:
            myMess.attach(
                MIMEText("\nCustomer address: {}".format(newlist[8])))
        if caps1 == 9:
            myMess.attach(
                MIMEText("\nCustomer phone number: {}".format(newlist[9])))
        if caps1 == 10:
            myMess.attach(MIMEText("\nJob type: {}".format(newlist[10])))
        if caps1 == 11:
            myMess.attach(MIMEText("\nWorking with: {}\n".format(newlist[11])))

    for caps2 in range(12, 18):
        if caps2 == 12:
            myMess.attach(
                MIMEText("################################\n ***Job 3***\n"))
            myMess.attach(MIMEText("Job date: {}".format(newlist[12])))
        if caps2 == 13:
            myMess.attach(MIMEText("\nCustomer name: {}".format(newlist[13])))
        if caps2 == 14:
            myMess.attach(
                MIMEText("\nCustomer address: {}".format(newlist[14])))
        if caps2 == 15:
            myMess.attach(
                MIMEText("\nCustomer phone number: {}".format(newlist[15])))
        if caps2 == 16:
            myMess.attach(MIMEText("\nJob type: {}".format(newlist[16])))
        if caps2 == 17:
            myMess.attach(MIMEText("\nWorking with: {}\n".format(newlist[17])))

    for caps3 in range(18, 24):
        if caps3 == 18:
            myMess.attach(
                MIMEText("################################\n ***Job 4***\n"))
            myMess.attach(MIMEText("Job date: {}".format(newlist[18])))
        if caps3 == 19:
            myMess.attach(MIMEText("\nCustomer name: {}".format(newlist[19])))
        if caps3 == 20:
            myMess.attach(
                MIMEText("\nCustomer address: {}".format(newlist[20])))
        if caps3 == 21:
            myMess.attach(
                MIMEText("\nCustomer phone number: {}".format(newlist[21])))
        if caps3 == 22:
            myMess.attach(MIMEText("\nJob type: {}".format(newlist[22])))
        if caps3 == 23:
            myMess.attach(MIMEText("\nWorking with: {}\n".format(newlist[23])))


def newlength5():
    for caps in range(len(captions)):
        if caps == 0:
            myMess.attach(
                MIMEText("***Job 1***\n Job date: {}".format(newlist[0])))
        if caps == 1:
            myMess.attach(MIMEText("\nCustomer name: {}".format(newlist[1])))
        if caps == 2:
            myMess.attach(
                MIMEText("\nCustomer address: {}".format(newlist[2])))
        if caps == 3:
            myMess.attach(
                MIMEText("\nCustomer phone number: {}".format(newlist[3])))
        if caps == 4:
            myMess.attach(MIMEText("\nJob type: {}".format(newlist[4])))
        if caps == 5:
            myMess.attach(MIMEText("\nWorking with: {}\n".format(newlist[5])))

    for caps1 in range(6, 12):
        if caps1 == 6:
            myMess.attach(
                MIMEText("################################\n ***Job 2***\n"))
            myMess.attach(MIMEText("Job date: {}".format(newlist[6])))
        if caps1 == 7:
            myMess.attach(MIMEText("\nCustomer name: {}".format(newlist[7])))
        if caps1 == 8:
            myMess.attach(
                MIMEText("\nCustomer address: {}".format(newlist[8])))
        if caps1 == 9:
            myMess.attach(
                MIMEText("\nCustomer phone number: {}".format(newlist[9])))
        if caps1 == 10:
            myMess.attach(MIMEText("\nJob type: {}".format(newlist[10])))
        if caps1 == 11:
            myMess.attach(MIMEText("\nWorking with: {}\n".format(newlist[11])))

    for caps2 in range(12, 18):
        if caps2 == 12:
            myMess.attach(
                MIMEText("################################\n ***Job 3***\n"))
            myMess.attach(MIMEText("Job date: {}".format(newlist[12])))
        if caps2 == 13:
            myMess.attach(MIMEText("\nCustomer name: {}".format(newlist[13])))
        if caps2 == 14:
            myMess.attach(
                MIMEText("\nCustomer address: {}".format(newlist[14])))
        if caps2 == 15:
            myMess.attach(
                MIMEText("\nCustomer phone number: {}".format(newlist[15])))
        if caps2 == 16:
            myMess.attach(MIMEText("\nJob type: {}".format(newlist[16])))
        if caps2 == 17:
            myMess.attach(MIMEText("\nWorking with: {}\n".format(newlist[17])))

    for caps3 in range(18, 24):
        if caps3 == 18:
            myMess.attach(
                MIMEText("################################\n ***Job 4***\n"))
            myMess.attach(MIMEText("Job date: {}".format(newlist[18])))
        if caps3 == 19:
            myMess.attach(MIMEText("\nCustomer name: {}".format(newlist[19])))
        if caps3 == 20:
            myMess.attach(
                MIMEText("\nCustomer address: {}".format(newlist[20])))
        if caps3 == 21:
            myMess.attach(
                MIMEText("\nCustomer phone number: {}".format(newlist[21])))
        if caps3 == 22:
            myMess.attach(MIMEText("\nJob type: {}".format(newlist[22])))
        if caps3 == 23:
            myMess.attach(MIMEText("\nWorking with: {}\n".format(newlist[23])))

    for caps4 in range(24, 30):
        if caps4 == 24:
            myMess.attach(
                MIMEText("################################\n ***Job 5***\n"))
            myMess.attach(MIMEText("Job date: {}".format(newlist[24])))
        if caps4 == 25:
            myMess.attach(MIMEText("\nCustomer name: {}".format(newlist[25])))
        if caps4 == 26:
            myMess.attach(
                MIMEText("\nCustomer address: {}".format(newlist[26])))
        if caps4 == 27:
            myMess.attach(
                MIMEText("\nCustomer phone number: {}".format(newlist[27])))
        if caps4 == 28:
            myMess.attach(MIMEText("\nJob type: {}".format(newlist[28])))
        if caps4 == 29:
            myMess.attach(MIMEText("\nWorking with: {}\n".format(newlist[29])))


def toEmail():
    global myMess
    global newlist

    date1 = jobdate_e.get()
    name1 = custname_e.get()

    if date1 == "" and name1 == "":
        messagebox.showinfo(
            "Error", "Please fill job date or customer name")
        return

    if "@" not in email_e.get():
        messagebox.showinfo(
            "Error", "Please give a valid email address")
        return

    else:
        connection5 = sqlite3.connect(
            database="appointments.db", timeout=20)
        curss4 = connection5.cursor()

        if date1 != "" and name1 == "":
            queries6 = """SELECT *
            FROM customers
            WHERE jobdate IN ("%s")""" % (date1)

            curss4.execute(queries6)
            output4 = curss4.fetchall()

        if date1 == "" and name1 != "":
            queries6 = """SELECT *
            FROM customers
            WHERE customername IN ("%s")""" % (name1)

            curss4.execute(queries6)
            output4 = curss4.fetchall()

        if date1 != "" and name1 != "":
            queries6 = """SELECT *
            FROM customers
            WHERE jobdate IN ("%s") AND customername IN ("%s")""" % (date1, name1)

            curss4.execute(queries6)
            output4 = curss4.fetchall()

        if len(output4) == 0:
            messagebox.showinfo(
                "Error", "No job date or customer name matches your entry")
            return

        elif len(output4) > 0:
            counts = 0
            newlist = []

            for i in range(len(output4)):
                counts += 1
                if counts <= len(output4):
                    for k, l in enumerate(output4[i]):
                        if k == 0:
                            pass
                        else:
                            newlist.append(l)

            newlength = int(len(newlist)/len(captions))

            myMess = MIMEMultipart()
            myMess["from"] = "Israel"
            myMess["to"] = email_e.get()
            myMess["subject"] = "Your Requested Job Schedule"

            myMess.attach(
                MIMEText("Please find your schedule(s) below:\n"))

            if newlength == 1:
                newlength1()

            if newlength == 2:
                newlength2()

            if newlength == 3:
                newlength3()

            if newlength == 4:
                newlength4()

            if newlength == 5:
                newlength5()

            myMess.attach(
                MIMEText("\n\n\nPowered by Izziboi Technologies (c) 2022"))
            # myMess.attach(MIMEImage(Path("izzi.png").read_bytes()))
            with smtplib.SMTP(host="smtp.gmail.com", port=587) as mySmtp:
                mySmtp.ehlo()
                mySmtp.starttls()
                # Password removed for security reasons
                mySmtp.login("actright133@gmail.com", "")
                mySmtp.send_message(myMess)

    if connection5:
        connection5.close()


def toPhone():
    acct_sid = ""  # Account SID removed for security reasons
    auth_token = ""  # Auth token removed for security reasons

    myPhone = phone_e.get()

    date1 = jobdate_e.get()
    name1 = custname_e.get()

    if date1 == "" and name1 == "":
        messagebox.showinfo(
            "Error", "Please fill job date or customer name")
        return

    if myPhone[0] != "+":
        messagebox.showinfo(
            "Error", "Please put correct phone number")
        return

    else:
        connection5 = sqlite3.connect(
            database="appointments.db", timeout=20)
        curss4 = connection5.cursor()

        if date1 != "" and name1 == "":
            queries6 = """SELECT *
            FROM customers
            WHERE jobdate IN ("%s")""" % (date1)

            curss4.execute(queries6)
            output4 = curss4.fetchall()

        if date1 == "" and name1 != "":
            queries6 = """SELECT *
            FROM customers
            WHERE customername IN ("%s")""" % (name1)

            curss4.execute(queries6)
            output4 = curss4.fetchall()

        if date1 != "" and name1 != "":
            queries6 = """SELECT *
            FROM customers
            WHERE jobdate IN ("%s") AND customername IN ("%s")""" % (date1, name1)

            curss4.execute(queries6)
            output4 = curss4.fetchall()

        if len(output4) == 0:
            messagebox.showinfo(
                "Error", "No job date or customer name matches your entry")
            return

        elif len(output4) > 0:
            clients = Client(acct_sid, auth_token)
            texts = clients.messages.create(
                to=myPhone, from_="+17406973314", body="Your schedule\n {}".format(output4))

    if connection5:
        connection5.close()


root.mainloop()
