#Hospital management system v1.0
#Code credits:
#       Frontend/GUI - Ram
#       Backend/SQL - Sai
#       Documentation - Yash


#Importing necessary modules
import tkinter as tk
import os
from tkinter import Menu, ttk, messagebox
from PIL import ImageTk, Image

#custom sql module

#Declaring path variables for extensive support with asset folder
file_path = os.path.dirname(os.path.realpath(__file__))
asset_path = os.path.join(file_path, "Assets")
ico_path = os.path.join(asset_path, "titleicon.ico")
bg_path = os.path.join(asset_path, "img24.png")
bgm_path = os.path.join(asset_path, "main.png")
theme_path = os.path.join(asset_path, "azure-dark.tcl")

#defining function to be triggered on perfect login to execute main window
def lgin():
    #grabbing username and password and referencing it with csv
    user = usern_ent.get()
    pwd = passwd_ent.get()
    if user == "" and pwd == "":
        messagebox.showinfo("Status", "Login Success")

        #destroying login and loading main window
        #Giving it a theme and attributes with ttkthemes
        login.destroy()
        main = tk.Tk(className="Mainwindow")
        style = ttk.Style()
        main.tk.call("source", theme_path)
        style.theme_use("azure-dark")
        main.geometry("1024x650")
        main.attributes("-alpha", 0.98)
        main.title("Hospital Management Software v1.0")
        main.iconbitmap(ico_path)

        #making a menubar with "file" as an option
        menubar = Menu(main)

        main.config(bg = "grey1", menu = menubar)
        main.resizable(False,False)
        main.option_add('*tearOff', False)
        menubar = Menu(main)
        main.config(menu = menubar)
        tmpbgm = Image.open(bgm_path)
        tmp1bgm = tmpbgm.resize((1024,650))
        bgm = ImageTk.PhotoImage(tmp1bgm)

        menu_file = Menu(menubar)

        menubar.add_cascade(menu=menu_file, label = "File")
        menu_file.add_command(label = "Exit", command = login.destroy)

        #making a notebook with tabs for accessing different tables from database
        ntbk = ttk.Notebook(master=main)
        frm1 = ttk.Frame(master=ntbk)
        frm2 = ttk.Frame(master=ntbk)
        frm3 = ttk.Frame(master=ntbk)
        frm4 = ttk.Frame(master=ntbk)
        frm5 = ttk.Frame(master=ntbk)

        #set of internal tabs for accessing in view tab
        internalntbk = ttk.Notebook(master=frm1)
        intfrm1 = ttk.Frame(master=internalntbk)
        intfrm2 = ttk.Frame(master=internalntbk)
        intfrm3 = ttk.Frame(master=internalntbk)
        intfrm4 = ttk.Frame(master=internalntbk)

        #set of internal tabs for accessing in add tab
        internalntbk1 = ttk.Notebook(master=frm2)
        intfrm5 = ttk.Frame(master=internalntbk1)
        intfrm6 = ttk.Frame(master=internalntbk1)
        intfrm7 = ttk.Frame(master=internalntbk1)
        intfrm8 = ttk.Frame(master=internalntbk1)

        #set of internal tabs for accessing in delete tab
        internalntbk2 = ttk.Notebook(master=frm3)
        intfrm9 = ttk.Frame(master=internalntbk2)
        intfrm10 = ttk.Frame(master=internalntbk2)
        intfrm11 = ttk.Frame(master=internalntbk2)
        intfrm12= ttk.Frame(master=internalntbk2)

        #set of internal tabs for accessing in update tab
        internalntbk3 = ttk.Notebook(master=frm4)
        intfrm13 = ttk.Frame(master=internalntbk3)
        intfrm14 = ttk.Frame(master=internalntbk3)
        intfrm15 = ttk.Frame(master=internalntbk3)
        intfrm16 = ttk.Frame(master=internalntbk3)

        #set of internal tabs for accessing in search tab
        internalntbk4 = ttk.Notebook(master=frm5)
        intfrm17 = ttk.Frame(master=internalntbk4)
        intfrm18 = ttk.Frame(master=internalntbk4)
        intfrm19 = ttk.Frame(master=internalntbk4)
        intfrm20 = ttk.Frame(master=internalntbk4)

        #scrollbar for scrolling (-_-)
        scrlbrfrm1 = ttk.Frame(master=intfrm1)
        scrlbr1 = ttk.Scrollbar(master=scrlbrfrm1)
        scrlbrfrm2 = ttk.Frame(master=intfrm2)
        scrlbr2 = ttk.Scrollbar(master=scrlbrfrm2)
        scrlbrfrm3 = ttk.Frame(master=intfrm3)
        scrlbr3 = ttk.Scrollbar(master=scrlbrfrm3)
        scrlbrfrm4 = ttk.Frame(master=intfrm4)
        scrlbr4 = ttk.Scrollbar(master=scrlbrfrm4)
        scrlbrfrm5 = ttk.Frame(master=intfrm9)
        scrlbr5 = ttk.Scrollbar(master=scrlbrfrm5)
        scrlbrfrm6 = ttk.Frame(master=intfrm10)
        scrlbr6 = ttk.Scrollbar(master=scrlbrfrm6)
        scrlbrfrm7 = ttk.Frame(master=intfrm11)
        scrlbr7 = ttk.Scrollbar(master=scrlbrfrm7)
        scrlbrfrm8 = ttk.Frame(master=intfrm12)
        scrlbr8 = ttk.Scrollbar(master=scrlbrfrm8)

        #Making tables with treeview
        treedat1 = ttk.Treeview(master=scrlbrfrm1, yscrollcommand=scrlbr1.set)
        scrlbr1.config(command = treedat1.yview)
        treedat1["columns"] = ("Patient ID", "Name", "Age", "Ailment", "Payment type", "Payment status", "Contact", "Amount")
        treedat1.column("#0", width = 0, minwidth = 0, stretch=0)
        treedat1.column("Patient ID", anchor="center", width = 120)
        treedat1.column("Name", anchor = "center", width = 120)
        treedat1.column("Age", anchor = "center", width = 120)
        treedat1.column("Ailment", anchor = "center", width = 120)
        treedat1.column("Payment type", anchor = "center", width = 120)
        treedat1.column("Payment status", anchor = "center", width = 120)
        treedat1.column("Contact", anchor = "center", width = 120)
        treedat1.column("Amount", anchor = "center", width = 120)

        treedat1.heading("#0", text="", anchor="center")
        treedat1.heading("Patient ID", text="Patient ID", anchor="center")
        treedat1.heading("Name", text="Name", anchor="center")
        treedat1.heading("Age", text="Age", anchor="center")
        treedat1.heading("Ailment", text="Ailment", anchor="center")
        treedat1.heading("Payment type", text="Payment type", anchor="center")
        treedat1.heading("Payment status", text="Payment status", anchor="center")
        treedat1.heading("Contact", text="Contact", anchor="center")
        treedat1.heading("Amount", text="Amount", anchor="center")

        treedat2 = ttk.Treeview(master=scrlbrfrm2, yscrollcommand=scrlbr2.set)
        treedat2["columns"] = ("Doctor ID", "Name", "Specialization", "DOJ", "Contact", "Salary")
        treedat2.column("#0", width = 0, minwidth = 0, stretch=0)
        treedat2.column("Doctor ID", anchor="center", width = 120)
        treedat2.column("Name", anchor = "center", width = 120)
        treedat2.column("Specialization", anchor = "center", width = 120)
        treedat2.column("DOJ", anchor = "center", width = 120)
        treedat2.column("Contact", anchor = "center", width = 120)
        treedat2.column("Salary", anchor = "center", width = 120)

        treedat2.heading("#0", text="", anchor="center")
        treedat2.heading("Doctor ID", text="Doctor ID", anchor="center")
        treedat2.heading("Name", text="Name", anchor="center")
        treedat2.heading("Specialization", text="Specialization", anchor="center")
        treedat2.heading("DOJ", text="DOJ", anchor="center")
        treedat2.heading("Contact", text="Contact", anchor="center")
        treedat2.heading("Salary", text="Salary", anchor="center")

        treedat3 = ttk.Treeview(master=scrlbrfrm3, yscrollcommand=scrlbr3.set)
        treedat3["columns"] = ("Nurse ID", "Name", "Department", "DOJ", "Contact", "Salary")
        treedat3.column("#0", width = 0, minwidth = 0, stretch=0)
        treedat3.column("Nurse ID", anchor="center", width = 120)
        treedat3.column("Name", anchor = "center", width = 120)
        treedat3.column("Department", anchor = "center", width = 120)
        treedat3.column("DOJ", anchor = "center", width = 120)
        treedat3.column("Contact", anchor = "center", width = 120)
        treedat3.column("Salary", anchor = "center", width = 120)

        treedat3.heading("#0", text="", anchor="center")
        treedat3.heading("Nurse ID", text="Nurse ID", anchor="center")
        treedat3.heading("Name", text="Name", anchor="center")
        treedat3.heading("Department", text="Department", anchor="center")
        treedat3.heading("DOJ", text="DOJ", anchor="center")
        treedat3.heading("Contact", text="Contact", anchor="center")
        treedat3.heading("Salary", text="Salary", anchor="center")

        treedat4 = ttk.Treeview(master=scrlbrfrm4, yscrollcommand=scrlbr4.set)
        treedat4["columns"] = ("Employee ID", "Name", "Job", "DOJ", "Contact", "Salary")
        treedat4.column("#0", width = 0, minwidth = 0, stretch=0)
        treedat4.column("Employee ID", anchor="center", width = 120)
        treedat4.column("Name", anchor = "center", width = 120)
        treedat4.column("Job", anchor = "center", width = 120)
        treedat4.column("DOJ", anchor = "center", width = 120)
        treedat4.column("Contact", anchor = "center", width = 120)
        treedat4.column("Salary", anchor = "center", width = 120)

        treedat4.heading("#0", text="", anchor="center")
        treedat4.heading("Employee ID", text="Employee ID", anchor="center")
        treedat4.heading("Name", text="Name", anchor="center")
        treedat4.heading("Job", text="Job", anchor="center")
        treedat4.heading("DOJ", text="Payment type", anchor="center")
        treedat4.heading("Contact", text="Contact", anchor="center")
        treedat4.heading("Salary", text="Salary", anchor="center")

        treedat5 = ttk.Treeview(master=scrlbrfrm5, yscrollcommand=scrlbr5.set)
        scrlbr5.config(command = treedat5.yview)
        treedat5["columns"] = ("Patient ID", "Name", "Age", "Ailment", "Payment type", "Payment status", "Contact", "Amount")
        treedat5.column("#0", width = 0, minwidth = 0, stretch=0)
        treedat5.column("Patient ID", anchor="center", width = 120)
        treedat5.column("Name", anchor = "center", width = 120)
        treedat5.column("Age", anchor = "center", width = 120)
        treedat5.column("Ailment", anchor = "center", width = 120)
        treedat5.column("Payment type", anchor = "center", width = 120)
        treedat5.column("Payment status", anchor = "center", width = 120)
        treedat5.column("Contact", anchor = "center", width = 120)
        treedat5.column("Amount", anchor = "center", width = 120)

        treedat5.heading("#0", text="", anchor="center")
        treedat5.heading("Patient ID", text="Patient ID", anchor="center")
        treedat5.heading("Name", text="Name", anchor="center")
        treedat5.heading("Age", text="Age", anchor="center")
        treedat5.heading("Ailment", text="Ailment", anchor="center")
        treedat5.heading("Payment type", text="Payment type", anchor="center")
        treedat5.heading("Payment status", text="Payment status", anchor="center")
        treedat5.heading("Contact", text="Contact", anchor="center")
        treedat5.heading("Amount", text="Amount", anchor="center")

        treedat6 = ttk.Treeview(master=scrlbrfrm6, yscrollcommand=scrlbr6.set)
        treedat6["columns"] = ("Doctor ID", "Name", "Specialization", "DOJ", "Contact", "Salary")
        treedat6.column("#0", width = 0, minwidth = 0, stretch=0)
        treedat6.column("Doctor ID", anchor="center", width = 120)
        treedat6.column("Name", anchor = "center", width = 120)
        treedat6.column("Specialization", anchor = "center", width = 120)
        treedat6.column("DOJ", anchor = "center", width = 120)
        treedat6.column("Contact", anchor = "center", width = 120)
        treedat6.column("Salary", anchor = "center", width = 120)

        treedat6.heading("#0", text="", anchor="center")
        treedat6.heading("Doctor ID", text="Doctor ID", anchor="center")
        treedat6.heading("Name", text="Name", anchor="center")
        treedat6.heading("Specialization", text="Specialization", anchor="center")
        treedat6.heading("DOJ", text="DOJ", anchor="center")
        treedat6.heading("Contact", text="Contact", anchor="center")
        treedat6.heading("Salary", text="Salary", anchor="center")

        treedat7 = ttk.Treeview(master=scrlbrfrm7, yscrollcommand=scrlbr7.set)
        treedat7["columns"] = ("Nurse ID", "Name", "Department", "DOJ", "Contact", "Salary")
        treedat7.column("#0", width = 0, minwidth = 0, stretch=0)
        treedat7.column("Nurse ID", anchor="center", width = 120)
        treedat7.column("Name", anchor = "center", width = 120)
        treedat7.column("Department", anchor = "center", width = 120)
        treedat7.column("DOJ", anchor = "center", width = 120)
        treedat7.column("Contact", anchor = "center", width = 120)
        treedat7.column("Salary", anchor = "center", width = 120)

        treedat7.heading("#0", text="", anchor="center")
        treedat7.heading("Nurse ID", text="Nurse ID", anchor="center")
        treedat7.heading("Name", text="Name", anchor="center")
        treedat7.heading("Department", text="Department", anchor="center")
        treedat7.heading("DOJ", text="DOJ", anchor="center")
        treedat7.heading("Contact", text="Contact", anchor="center")
        treedat7.heading("Salary", text="Salary", anchor="center")

        treedat8 = ttk.Treeview(master=scrlbrfrm8, yscrollcommand=scrlbr8.set)
        treedat8["columns"] = ("Employee ID", "Name", "Job", "DOJ", "Contact", "Salary")
        treedat8.column("#0", width = 0, minwidth = 0, stretch=0)
        treedat8.column("Employee ID", anchor="center", width = 120)
        treedat8.column("Name", anchor = "center", width = 120)
        treedat8.column("Job", anchor = "center", width = 120)
        treedat8.column("DOJ", anchor = "center", width = 120)
        treedat1.column("Contact", anchor = "center", width = 120)
        treedat8.column("Salary", anchor = "center", width = 120)

        treedat8.heading("#0", text="", anchor="center")
        treedat8.heading("Employee ID", text="Employee ID", anchor="center")
        treedat8.heading("Name", text="Name", anchor="center")
        treedat8.heading("Job", text="Job", anchor="center")
        treedat8.heading("DOJ", text="Payment type", anchor="center")
        treedat8.heading("Contact", text="Contact", anchor="center")
        treedat8.heading("Salary", text="Salary", anchor="center")

        #query commit for patient data
        def patcomm(PID_val, Name_val, age_val, ailment_val, payment, status, contactdet, amt_val):
            treedat1.insert(parent="", index=tk.END, text = "", values = (PID_val, Name_val, age_val, ailment_val, payment, status, contactdet, amt_val))
            treedat5.insert(parent="", index=tk.END, text = "", values = (PID_val, Name_val, age_val, ailment_val, payment, status, contactdet, amt_val))

        #query commit for doctor data
        def doccomm(DID_val, Name_Doc_val, spec_val, DOJ_val_doc, contactdet, sal_val):
            treedat2.insert(parent="", index=tk.END, text = "", values = (DID_val, Name_Doc_val, spec_val, DOJ_val_doc, contactdet, sal_val))
            treedat6.insert(parent="", index=tk.END, text = "", values = (DID_val, Name_Doc_val, spec_val, DOJ_val_doc, contactdet, sal_val))
        
        #query commit for nurse data
        def nurcomm(NID_val, Name_Nur_val, dept_val, DOJ_val_nur, contactdet, sal_val):
            treedat3.insert(parent="", index=tk.END, text = "", values = (NID_val, Name_Nur_val, dept_val, DOJ_val_nur, contactdet, sal_val))
            treedat7.insert(parent="", index=tk.END, text = "", values = (NID_val, Name_Nur_val, dept_val, DOJ_val_nur, contactdet, sal_val))
        
        #query commit for employee data
        def empcomm(EID_val, Name_emp_val, job_val, DOJ_val_emp, contactdet, sal_val):
            treedat4.insert(parent="", index=tk.END, text = "", values = (EID_val, Name_emp_val, job_val, DOJ_val_emp, contactdet, sal_val))
            treedat8.insert(parent="", index=tk.END, text = "", values = (EID_val, Name_emp_val, job_val, DOJ_val_emp, contactdet, sal_val))

        #code fragment for adding data to SQL and to Treeview (Patient table)
        paymentval = tk.IntVar()
        statusval = tk.IntVar()
        age_val = tk.IntVar()
        ent_PID = ttk.Entry(master=intfrm5, width = 30)
        lbl_PID = ttk.Label(master=intfrm5, text = "Patient ID: ")
        ent_Name = ttk.Entry(master=intfrm5, width = 30)
        lbl_Name = ttk.Label(master=intfrm5, text = "Name: ")
        ent_ailment = ttk.Entry(master=intfrm5, width = 30)
        lbl_ailment = ttk.Label(master=intfrm5, text = "Ailments: ")
        ent_amt = ttk.Entry(master=intfrm5, width = 30)
        lbl_amt = ttk.Label(master=intfrm5, text = "Amount: ")
        lbl_payment = ttk.Label(master=intfrm5, text = "Payment Type:")
        rdb_cash = ttk.Radiobutton(master=intfrm5, text="Cash", value=1, variable=paymentval)
        rdb_card = ttk.Radiobutton(master=intfrm5, text="Card", value=2, variable=paymentval)
        rdb_cheque = ttk.Radiobutton(master=intfrm5, text="Cheque", value=3, variable=paymentval)
        lbl_status = ttk.Label(master=intfrm5, text = "Payment Status: ")
        rdb_paid = ttk.Radiobutton(master=intfrm5, text="Paid", value=1, variable=statusval)
        rdb_pending = ttk.Radiobutton(master=intfrm5, text="Pending", value=2, variable=statusval)
        age_cbbx = ttk.Combobox(master=intfrm5, textvariable=age_val, width=5)
        agelis = [int(i) for i in range(1,120)]
        age_cbbx["values"] = tuple(agelis)
        age_cbbx.state(["readonly"])
        lbl_age = ttk.Label(master=intfrm5, text="Age: ")
        ent_contact = ttk.Entry(master=intfrm5, width=30)
        lbl_contact = ttk.Label(master=intfrm5, text="Contact: ")

        #separators and beautification
        sep_pay_stat = ttk.Separator(master=intfrm5, orient=tk.HORIZONTAL)
        sep_pay_stat1 = ttk.Separator(master=intfrm5, orient=tk.HORIZONTAL)

        def addrecpat():
            PID_val = ent_PID.get()
            Name_val = ent_Name.get()
            ailment_val = ent_ailment.get()
            amt_val = ent_amt.get()
            age = age_val.get()
            contact = ent_contact.get()
            if paymentval.get() == 1:
                payment = "Cash"
            elif paymentval.get() == 2:
                payment = "Card"
            elif paymentval.get() == 3:
                payment = "Cheque"
            else:
                pass
            
            if statusval.get() == 1:
                status = "Paid"
            elif statusval.get() == 2:
                status = "Pending"
            else:
                pass
            patcomm(PID_val, Name_val, age, ailment_val, payment, status, contact, amt_val)
            messagebox.showinfo("Add", message="Added Successfully")
            ent_PID.delete(0, tk.END)
            ent_Name.delete(0, tk.END)
            ent_ailment.delete(0, tk.END)
            ent_amt.delete(0, tk.END)
        addbtnpat = ttk.Button(master=intfrm5, text = "Add Data", command = addrecpat)

        #code fragment for adding data to SQL and to Treeview (Doctors)
        datevar_doc = tk.StringVar()
        monthvar_doc = tk.StringVar()
        yearvar_doc = tk.StringVar()
        ent_DID = ttk.Entry(master=intfrm6, width = 30)
        lbl_DID = ttk.Label(master=intfrm6, text = "Doctor ID: ")
        ent_Name_doc = ttk.Entry(master=intfrm6, width = 30)
        lbl_Name_doc = ttk.Label(master=intfrm6, text = "Name: ")
        ent_spec = ttk.Entry(master=intfrm6, width = 30)
        lbl_spec = ttk.Label(master=intfrm6, text = "Specialization: ")
        lbl_DOJ = ttk.Label(master=intfrm6, text = "Date Of Joining: ")

        #small frame for DOJ
        dojfrm_doc = ttk.Frame(master=intfrm6)

        date_cbbx1 = ttk.Combobox(master=dojfrm_doc, textvariable = datevar_doc, width = 3)
        date_cbbx1["values"] = ("01", "02", "03", "04", "05", "06", "07", "08", "09", 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31)
        date_cbbx1.state(["readonly"])
        month_cbbx1 = ttk.Combobox(master=dojfrm_doc, textvariable = monthvar_doc, width = 9)
        month_cbbx1["values"] = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
        month_cbbx1.state(["readonly"])
        ylist = []
        for i in range(1950, 2022):
            ylist.append(i)
        year_cbbx1 = ttk.Combobox(master=dojfrm_doc, textvariable = yearvar_doc, width = 5)
        year_cbbx1["values"] = tuple(ylist)
        year_cbbx1.state(["readonly"])
        ent_contact_doc = ttk.Entry(master=intfrm6, width = 30)
        lbl_contact_doc = ttk.Label(master=intfrm6, text="Contact: ")
        ent_sal = ttk.Entry(master=intfrm6, width = 30)
        lbl_sal = ttk.Label(master=intfrm6, text = "Salary:")

        def addrecdoc():
            DID_val = ent_DID.get()
            Name_Doc_val = ent_Name_doc.get()
            spec_val = ent_spec.get()
            sal_val = ent_sal.get()
            DOJ_val_doc = f"{int(datevar_doc.get())}/{monthvar_doc.get()}/{int(yearvar_doc.get())}"
            contact_doc = ent_contact_doc.get()
            doccomm(DID_val, Name_Doc_val, spec_val, DOJ_val_doc, contact_doc, sal_val)
            messagebox.showinfo("Add", message="Added Successfully")
            ent_DID.delete(0, tk.END)
            ent_Name_doc.delete(0, tk.END)
            ent_spec.delete(0, tk.END)
            ent_sal.delete(0, tk.END)
        addbtndoc = ttk.Button(master=intfrm6, text = "Add Data", command = addrecdoc)

        #code fragment for adding data to SQL and to Treeview (Nurses)
        datevar_nur = tk.StringVar()
        monthvar_nur = tk.StringVar()
        yearvar_nur = tk.StringVar()
        ent_NID = ttk.Entry(master=intfrm7, width = 30)
        lbl_NID = ttk.Label(master=intfrm7, text = "Nurse ID: ")
        ent_Name_nur = ttk.Entry(master=intfrm7, width = 30)
        lbl_Name_nur = ttk.Label(master=intfrm7, text = "Name: ")
        ent_dept = ttk.Entry(master=intfrm7, width = 30)
        lbl_dept = ttk.Label(master=intfrm7, text = "Department: ")
        lbl_DOJ_nur = ttk.Label(master=intfrm7, text = "Date Of Joining: ")

        #small frame for DOJ
        dojfrm_nur = ttk.Frame(master=intfrm7)

        date_cbbx2 = ttk.Combobox(master=dojfrm_nur, textvariable = datevar_nur, width = 3)
        date_cbbx2["values"] = ("01", "02", "03", "04", "05", "06", "07", "08", "09", 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31)
        date_cbbx2.state(["readonly"])
        month_cbbx2 = ttk.Combobox(master=dojfrm_nur, textvariable = monthvar_nur, width = 9)
        month_cbbx2["values"] = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
        month_cbbx2.state(["readonly"])
        ylist = []
        for i in range(1950, 2022):
            ylist.append(i)
        year_cbbx2 = ttk.Combobox(master=dojfrm_nur, textvariable = yearvar_nur, width = 5)
        year_cbbx2["values"] = tuple(ylist)
        year_cbbx2.state(["readonly"])
        ent_sal_nur = ttk.Entry(master=intfrm7, width = 30)
        lbl_sal_nur = ttk.Label(master=intfrm7, text = "Salary:")

        def addrecnur():
            NID_val = ent_NID.get()
            Name_Nur_val = ent_Name_nur.get()
            dept_val = ent_dept.get()
            sal_val = ent_sal_nur.get()
            DOJ_val_nur = f"{int(datevar_nur.get())}/{monthvar_nur.get()}/{int(yearvar_nur.get())}"
            nurcomm(NID_val, Name_Nur_val, dept_val, DOJ_val_nur, sal_val)
            messagebox.showinfo("Add", message="Added Successfully")
            ent_NID.delete(0, tk.END)
            ent_Name_nur.delete(0, tk.END)
            ent_dept.delete(0, tk.END)
            ent_sal_nur.delete(0, tk.END)
        addbtnnur = ttk.Button(master=intfrm7, text = "Add Data", command = addrecnur)

        #code fragment for adding data to SQL and to Treeview (Employees)
        datevar_emp = tk.StringVar()
        monthvar_emp = tk.StringVar()
        yearvar_emp = tk.StringVar()
        ent_EID = ttk.Entry(master=intfrm8, width = 30)
        lbl_EID = ttk.Label(master=intfrm8, text = "Employee ID: ")
        ent_Name_emp = ttk.Entry(master=intfrm8, width = 30)
        lbl_Name_emp = ttk.Label(master=intfrm8, text = "Name: ")
        ent_job = ttk.Entry(master=intfrm8, width = 30)
        lbl_job = ttk.Label(master=intfrm8, text = "Job: ")
        lbl_DOJ_emp = ttk.Label(master=intfrm8, text = "Date Of Joining: ")

        #small frame for DOJ
        dojfrm_emp = ttk.Frame(master=intfrm8)

        date_cbbx3 = ttk.Combobox(master=dojfrm_emp, textvariable = datevar_emp, width = 3)
        date_cbbx3["values"] = ("01", "02", "03", "04", "05", "06", "07", "08", "09", 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31)
        date_cbbx3.state(["readonly"])
        month_cbbx3 = ttk.Combobox(master=dojfrm_emp, textvariable = monthvar_emp, width = 9)
        month_cbbx3["values"] = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
        month_cbbx3.state(["readonly"])
        ylist = []
        for i in range(1950, 2022):
            ylist.append(i)
        year_cbbx3 = ttk.Combobox(master=dojfrm_emp, textvariable = yearvar_emp, width = 5)
        year_cbbx3["values"] = tuple(ylist)
        year_cbbx3.state(["readonly"])
        ent_sal_emp = ttk.Entry(master=intfrm8, width = 30)
        lbl_sal_emp = ttk.Label(master=intfrm8, text = "Salary:")

        def addrecemp():
            EID_val = ent_EID.get()
            Name_emp_val = ent_Name_emp.get()
            job_val = ent_job.get()
            sal_val = ent_sal_emp.get()
            DOJ_val_emp = f"{int(datevar_emp.get())}/{monthvar_emp.get()}/{int(yearvar_emp.get())}"
            empcomm(EID_val, Name_emp_val, job_val, DOJ_val_emp, sal_val)
            messagebox.showinfo("Add", message="Added Successfully")
            ent_EID.delete(0, tk.END)
            ent_Name_emp.delete(0, tk.END)
            ent_job.delete(0, tk.END)
            ent_sal_emp.delete(0, tk.END)
        addbtnemp = ttk.Button(master=intfrm8, text = "Add Data", command = addrecemp)

        #Packing and adding everything
        ntbk.add(frm1, text="View DB")
        ntbk.add(frm2, text="Add Data")
        ntbk.add(frm3, text="Delete Data")
        ntbk.add(frm4, text="Update Data")
        ntbk.add(frm5, text="Search")

        internalntbk.add(intfrm1, text="Patient Table")
        internalntbk.add(intfrm2, text="Doctor Table")
        internalntbk.add(intfrm3, text="Nurse Table")
        internalntbk.add(intfrm4, text="Employee Table")

        internalntbk1.add(intfrm5, text="Patient Table")
        internalntbk1.add(intfrm6, text="Doctor Table")
        internalntbk1.add(intfrm7, text="Nurse Table")
        internalntbk1.add(intfrm8, text="Employee Table")

        internalntbk2.add(intfrm9, text="Patient Table")
        internalntbk2.add(intfrm10, text="Doctor Table")
        internalntbk2.add(intfrm11, text="Nurse Table")
        internalntbk2.add(intfrm12, text="Employee Table")

        internalntbk3.add(intfrm13, text="Patient Table")
        internalntbk3.add(intfrm14, text="Doctor Table")
        internalntbk3.add(intfrm15, text="Nurse Table")
        internalntbk3.add(intfrm16, text="Employee Table")

        internalntbk4.add(intfrm17, text="Patient Table")
        internalntbk4.add(intfrm18, text="Doctor Table")
        internalntbk4.add(intfrm19, text="Nurse Table")
        internalntbk4.add(intfrm20, text="Employee Table")

        ntbk.pack()
        internalntbk.pack()
        internalntbk1.pack()
        internalntbk2.pack()
        internalntbk3.pack()
        internalntbk4.pack()
        scrlbrfrm1.pack()
        scrlbr1.pack(fill = tk.Y, side = tk.RIGHT)
        scrlbrfrm2.pack()
        scrlbr2.pack(fill = tk.Y, side = tk.RIGHT)
        scrlbrfrm3.pack()
        scrlbr3.pack(fill = tk.Y, side = tk.RIGHT)
        scrlbrfrm4.pack()
        scrlbr4.pack(fill = tk.Y, side = tk.RIGHT)
        scrlbrfrm5.pack()
        scrlbr5.pack(fill = tk.Y, side = tk.RIGHT)
        scrlbrfrm6.pack()
        scrlbr6.pack(fill = tk.Y, side = tk.RIGHT)
        scrlbrfrm7.pack()
        scrlbr7.pack(fill = tk.Y, side = tk.RIGHT)
        scrlbrfrm8.pack()
        scrlbr8.pack(fill = tk.Y, side = tk.RIGHT)
        treedat1.pack()
        treedat2.pack()
        treedat3.pack()
        treedat4.pack()
        treedat5.pack()
        treedat6.pack()
        treedat7.pack()
        treedat8.pack()

        ent_PID.grid(row=0, column=1, pady=5)
        lbl_PID.grid(row=0, column=0, pady=5)
        ent_Name.grid(row=1, column=1, pady=5)
        lbl_Name.grid(row=1, column=0, pady=5)
        lbl_age.grid(row=2, column=0)
        age_cbbx.grid(row=2, column=1)
        ent_ailment.grid(row=3, column=1, pady=5)
        lbl_ailment.grid(row=3, column=0, pady=5) 
        lbl_payment.grid(row=4, column=0, pady=5)
        rdb_cash.grid(row=4, column=1, sticky="w", pady=5)
        rdb_card.grid(row=5, column=1, sticky="w", pady=5)
        rdb_cheque.grid(row=6, column=1, sticky="w", pady=5)
        sep_pay_stat.grid(row=7, column=1, sticky='ew', pady=5)
        sep_pay_stat1.grid(row=7, column=0, sticky='ew', pady=5)
        lbl_status.grid(row=8, column=0, pady=5)
        rdb_paid.grid(row=8, column=1, sticky="w")
        rdb_pending.grid(row=9, column=1, sticky="w")
        ent_contact.grid(row=10, column=1, pady=5)
        lbl_contact.grid(row=10, column=0, pady=5)
        lbl_amt.grid(row=11, column=0, pady=5)
        ent_amt.grid(row=11, column=1, pady=5)
        addbtnpat.grid(row=12, column=1, pady=5)

        ent_DID.grid(row=0, column=1, pady=5)
        lbl_DID.grid(row=0, column=0, pady=5)
        ent_Name_doc.grid(row=1, column=1, pady=5)
        lbl_Name_doc.grid(row=1, column=0, pady=5)
        ent_spec.grid(row=2, column=1, pady=5)
        lbl_spec.grid(row=2, column=0, pady=5)
        dojfrm_doc.grid(row=3, column=1, pady=5)
        date_cbbx1.grid(row=0, column=0, padx=10, pady=5)
        month_cbbx1.grid(row=0, column=2, padx=10, pady=5)
        year_cbbx1.grid(row=0, column=4, padx=10, pady=5)
        lbl_DOJ.grid(row=3, column=0, pady=5)
        ent_contact_doc
        lbl_contact_doc
        ent_sal.grid(row=4, column=1, pady=5)
        lbl_sal.grid(row=4, column=0, pady=5)
        addbtndoc.grid(row=5, column=1, pady=5)

        ent_NID.grid(row=0, column=1, pady=5)
        lbl_NID.grid(row=0, column=0, pady=5)
        ent_Name_nur.grid(row=1, column=1, pady=5)
        lbl_Name_nur.grid(row=1, column=0, pady=5)
        ent_dept.grid(row=2, column=1, pady=5)
        lbl_dept.grid(row=2, column=0, pady=5)
        lbl_DOJ_nur.grid(row=3, column=0, pady=5)
        dojfrm_nur.grid(row=3, column=1, pady=5)
        date_cbbx3.grid(row=0, column=0, padx=10, pady=5)
        month_cbbx3.grid(row=0, column=1, padx=10, pady=5)
        year_cbbx3.grid(row=0, column=2, padx=10, pady=5)
        ent_sal_emp.grid(row=4, column=1, pady=5)
        lbl_sal_emp.grid(row=4, column=0, pady=5)
        addbtnemp.grid(row=5, column=1, pady=5)

        ent_EID.grid(row=0, column=1, pady=5)
        lbl_EID.grid(row=0, column=0, pady=5)
        ent_Name_emp.grid(row=1, column=1, pady=5)
        lbl_Name_emp.grid(row=1, column=0, pady=5)
        ent_job.grid(row=2, column=1, pady=5)
        lbl_job.grid(row=2, column=0, pady=5)
        lbl_DOJ_emp.grid(row=3, column=0, pady=5)
        dojfrm_emp.grid(row=3, column=1, pady=5)
        date_cbbx2.grid(row=0, column=0, padx=10, pady=5)
        month_cbbx2.grid(row=0, column=1, padx=10, pady=5)
        year_cbbx2.grid(row=0, column=2, padx=10, pady=5)
        ent_sal_nur.grid(row=4, column=1, pady=5)
        lbl_sal_nur.grid(row=4, column=0, pady=5)
        addbtnnur.grid(row=5, column=1, pady=5)


        l1 = [frm1, frm2, frm3, frm4]
        for i in l1:
            lbl_bgm = tk.Label(master=i, width = 1024, height = 650, image = bgm)
            lbl_bgm.pack()

        main.mainloop()
    else:
        #Executes on login failure
        fin = messagebox.askyesno("Status", "Login Failed. Would you like to try again?")
        if fin == True:    
            usern_ent.delete(0, tk.END)
            passwd_ent.delete(0, tk.END)
        else:
            login.destroy()

#Defining background
tmpbg = Image.open(bg_path)
tmp1bg = tmpbg.resize((1024,650))

#defining login window and its attributes
login = tk.Tk(className="Loginwindow")
login.geometry("1024x650")
login.title("Hospital Management Software v1.0")
style = ttk.Style()
os.chdir(asset_path)
login.tk.call("source", theme_path)
style.theme_use("azure-dark")
login.attributes("-alpha", 0.98)
login.iconbitmap(ico_path)
login.resizable(False,False)

login.option_add('*tearOff', False)
menubar = Menu(login)
login.config(menu = menubar,bg = "black")
bg = ImageTk.PhotoImage(tmp1bg)

lbl_bg = tk.Label(master=login, image = bg)

#taking username and password from user
usern_ent = ttk.Entry(master=login, width = 75)
passwd_ent = ttk.Entry(master=login, width = 75, show="*")

#login button
btn_login = ttk.Button(master=login, text = "Login", command = lgin, width = 25)

#register button
btn_reg = ttk.Button(master=login, text = "Register", command = 0, width = 25)

#file menu
menu_file = Menu(menubar)

menubar.add_cascade(menu=menu_file, label = "File")
menu_file.add_command(label = "Exit", command = login.destroy)

#pack everything
lbl_bg.pack()
usern_ent.place(x=230, y=465)
passwd_ent.place(x=230, y=500)
btn_login.place(x=230, y=550)
btn_reg.place(x=430, y=550)
login.mainloop()

###########################################################################################################################################################################################################################################################################################################################################################################################