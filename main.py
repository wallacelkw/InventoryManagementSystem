from tkinter import*
import tkinter.ttk
import tkinter.messagebox
import ivm_database

class Inventory:
    def __init__(self,root):
        self.root=root
        self.root.title("Inventory Management System")
        self.root.geometry("1250x650+0+0")
        self.root.configure(bg="white")
        self.root.m_title=Label(self.root,text="Inventory Management System",font=("arial",40,"bold"),bg="white").pack(side=TOP,fill=X)

        part_num = StringVar()
        description= StringVar()
        quantity = StringVar()
        r_date = StringVar()
        location = StringVar()
        r_remark = StringVar()
        delete = StringVar()
        job = StringVar()
        #=============================================def========================================

        def exit():
            exit=tkinter.messagebox.askyesno("Inventory Management System","Are you confirm?")
            if exit>0:
                root.destroy()


        def reset():
            txtp_num.delete(0,END)
            txtdes.delete(0, END)
            txtdate.delete(0, END)
            txtqty.delete(0, END)
            txtloc.delete(0, END)
            txtremark.delete(0, END)

        def addButton():
            if (len(part_num.get()) != 0):
                ivm_database.addInv(part_num.get(), description.get(),quantity.get(),r_date.get(),location.get(),r_remark.get())
                DisplayData()
                reset()

        def DisplayData():
            Inventory_table.delete(*Inventory_table.get_children())
            for row in ivm_database.viewData():
                Inventory_table.insert('',END,values=row)

        def InvRec(event):
            global sd
            cursor_row = Inventory_table.focus()
            sd=Inventory_table.item(cursor_row)
            row=sd['values']
            print(row)
            txtp_num.delete(0, END)
            txtp_num.insert(END,row[1])
            txtdes.delete(0, END)
            txtdes.insert(END ,row[2])
            txtqty.delete(0, END)
            txtqty.insert(END,row[3])
            txtdate.delete(0, END)
            txtdate.insert(END, row[4])
            txtloc.delete(0, END)
            txtloc.insert(END,row[5])
            txtremark.delete(0, END)
            txtremark.insert(END,row[6])

        def DeleteData():
            row = sd['values']
            ivm_database.deleteRecord(row[0])
            reset()
            DisplayData()

        def searchDatabase(*item):
            Inventory_table.delete(*Inventory_table.get_children())
            for row in ivm_database.searchData(part_num.get(), description.get(),quantity.get(),r_date.get(),location.get()):
                Inventory_table.insert('',END,values=row)


        def update():
            row = sd['values']
            ivm_database.deleteRecord(row[0])
            ivm_database.addInv(part_num.get(), description.get(), quantity.get(), r_date.get(), location.get(),r_remark.get())
            reset()
            DisplayData()

        # =====================================#Left Frame=====================================================
        L_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="light sky blue")
        L_Frame.place(x=20,y=80,width=550,height=430)

        p_num=Label(L_Frame,text= "Part Number",font=("arial",15,"bold"),bg="light sky blue",pady=5,padx=5)
        p_num.grid(row=0,column=0,sticky=W)
        txtp_num=Entry(L_Frame,font=("arial",15,"bold"),bg="white",width=20,bd=3,relief=GROOVE,textvariable = part_num)
        txtp_num.grid(row=0,column=1,sticky=W,padx=5,pady=5)

        des=Label(L_Frame,text= "Description",font=("arial",15,"bold"),bg="light sky blue",pady=5,padx=5)
        des.grid(row=1,column=0,sticky=W)
        txtdes=Entry(L_Frame,font=("arial",15,"bold"),bg="white",width=20,bd=3,relief=GROOVE,textvariable = description)
        txtdes.grid(row=1,column=1,sticky=W,padx=5,pady=5)

        qty=Label(L_Frame,text= "Quantity",font=("arial",15,"bold"),bg="light sky blue",pady=5,padx=5)
        qty.grid(row=2,column=0,sticky=W)
        txtqty=Entry(L_Frame,font=("arial",15,"bold"),bg="white",width=20,bd=3,relief=GROOVE,textvariable =quantity )
        txtqty.grid(row=2,column=1,sticky=W,padx=5,pady=5)

        date = Label(L_Frame, text="Date", font=("arial", 15, "bold"), bg="light sky blue", pady=5, padx=5)
        date.grid(row=3, column=0, sticky=W)
        txtdate=Entry(L_Frame,font=("arial",15,"bold"),bg="white",width=20,bd=3,relief=GROOVE,textvariable = r_date)
        txtdate.grid(row=3,column=1,sticky=W,padx=5,pady=5)

        loc=Label(L_Frame,text= "Location",font=("arial",15,"bold"),bg="light sky blue",pady=5,padx=5)
        loc.grid(row=4,column=0,sticky=W)
        txtloc=Entry(L_Frame,font=("arial",15,"bold"),bg="white",width=20,bd=3,relief=GROOVE,textvariable = location)
        txtloc.grid(row=4,column=1,sticky=W,padx=5,pady=5)

        remark=Label(L_Frame,text= "Remark",font=("arial",15,"bold"),bg="light sky blue",pady=5,padx=5)
        remark.grid(row=5,column=0,sticky="WN")
        txtremark=Entry(L_Frame,font=("arial",15,"bold"),bg="white",width=20,bd=3,relief=GROOVE,textvariable = r_remark)
        txtremark.grid(row=5,column=1,padx=5,pady=5)

        reset_button=Button(L_Frame,text= "Clear",font=("arial",15,"bold"),bg="light sky blue",relief=RIDGE,bd=5,command=reset)
        reset_button.grid(row=10,column=0,pady=100,padx=5,sticky=W)


        #=====================================#RIght Frame=======================================================
        R_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="light sky blue")
        R_Frame.place(x=580,y=80,width=650,height=500)
        scroll_x = Scrollbar(R_Frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(R_Frame, orient=VERTICAL)
        Inventory_table=tkinter.ttk.Treeview(R_Frame,columns=("Job","Part Number", "Description","Quantity", "Date","Location","Remark"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=Inventory_table.xview)
        scroll_y.config(command=Inventory_table.yview)
        Inventory_table.heading("Job",text="Job")
        Inventory_table.heading("Part Number", text="Part Number")
        Inventory_table.heading("Description", text="Description")
        Inventory_table.heading("Quantity", text="Qty")
        Inventory_table.heading("Date", text="Date")
        Inventory_table.heading("Location", text="Location")
        Inventory_table.heading("Remark", text="Remark")
        Inventory_table['show']='headings'
        Inventory_table.column("Job",width=10)
        Inventory_table.column("Part Number", width=100)
        Inventory_table.column("Description", width=200)
        Inventory_table.column("Quantity", width=40)
        Inventory_table.column("Date", width=80)
        Inventory_table.column("Location", width=75)
        Inventory_table.column("Remark", width=300)

        Inventory_table.pack(fill=BOTH, expand=1)
        Inventory_table.bind('<ButtonRelease-1>',InvRec)

        # =====================================#Bottom Frame=======================================================
        Btm_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="light sky blue")
        Btm_Frame.place(x=20,y=510,width=550,height=70)

        add_button=Button(Btm_Frame,text= "Add",font=("arial",15,"bold"),bg="light sky blue",relief=RIDGE,bd=5,command =addButton)
        add_button.grid(row=0,column=0,pady=7,padx=5)

        reset_button=Button(Btm_Frame,text= "Delete",font=("arial",15,"bold"),bg="light sky blue",relief=RIDGE,bd=5,command=DeleteData)
        reset_button.grid(row=0,column=1,pady=7,padx=5)

        search_button=Button(Btm_Frame,text= "Search",font=("arial",15,"bold"),bg="light sky blue",relief=RIDGE,bd=5,command=searchDatabase)
        search_button.grid(row=0,column=2,pady=7,padx=5)

        display_button=Button(Btm_Frame,text= "Display",font=("arial",15,"bold"),bg="light sky blue",relief=RIDGE,bd=5,command=DisplayData)
        display_button.grid(row=0,column=3,pady=7,padx=5)

        update_button=Button(Btm_Frame,text= "Update",font=("arial",15,"bold"),bg="light sky blue",relief=RIDGE,bd=5,command=update)
        update_button.grid(row=0,column=4,pady=7,padx=5)

        exit_button=Button(Btm_Frame,text= "Exit",font=("arial",15,"bold"),bg="light sky blue",relief=RIDGE,bd=5,command=exit)
        exit_button.grid(row=0,column=5,pady=7,padx=5)




if __name__=='__main__':
    root=Tk()

    application = Inventory(root)
    root.mainloop()