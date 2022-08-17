## import modules
from tkinter import *
import tkinter.messagebox
import sqlite3

# class for Front End UI (user interface)
class Specimen:

    def __init__(self,root):
        # Initialise database class (create object reference for Database class as d)
        d = Database()
        d.conn()

        self.root = root
        self.root.title("Specimen Metadata Management System")
        self.root.iconbitmap("24_048.ico")
        self.root.geometry("1290x600")
        self.root.config(bg='black')
        
        entryID = StringVar()        
        pID = StringVar()
        pName = StringVar()
        pType = StringVar()
        pAge = StringVar()
        pAgeUnit = StringVar()
        pWeight = StringVar()
        pWeightUnit = StringVar()
        pSex = StringVar()
        pStrain = StringVar()
        pAttribute = StringVar()
        pPathology = StringVar()
        newPathology = StringVar(value="N/A")

        """ Let's call the Database methods to perform the database operations"""

        # Function to close the frame
        def close():
            print("Specimen : close method called")
            close = tkinter.messagebox.askyesno("Specimen Metadata Management System", 
            "Are you sure you want to close the system?" )
            if close > 0:
                root.destroy()
                print("Specimen : close method finished\n")
                return

        # Function to clear and reset the widget
        def clear():
            print("Specimen : clear method called")
            self.txtEntryID.delete(0, END)
            self.txtpID.delete(0, END)
            self.txtpName.delete(0, END)
            pType.set("select specimen type") 
            self.txtpAge.delete(0, END)
            pAgeUnit.set("select unit") 
            self.txtpWeight.delete(0, END)
            pWeightUnit.set("select unit") 
            pSex.set("select sex") 
            self.txtpStrain.delete(0, END)
            pAttribute.set("select attribute") 
            pPathology.set("select pathology") 
            self.txtpPathology.delete(0, END)
            print("Specimen : close method finished\n")


        # Function to save the Specimen details in database table
        def insert():
            print("Specimen : insert method called")
            if len(entryID.get()) != 0 :
                d.insert(entryID.get(), pID.get(), pName.get(), pType.get(), pAge.get(), pAgeUnit.get(), pWeight.get(), pWeightUnit.get(), 
                        pSex.get(), pStrain.get(), pAttribute.get(), pPathology.get(), newPathology.get())
                SpecimenList.delete(0, END)
                SpecimenList.insert(END, entryID.get(), pID.get(), pName.get(), pType.get(), pAge.get(), pAgeUnit.get(), pWeight.get(), pWeightUnit.get(), 
                        pSex.get(), pStrain.get(), pAttribute.get(), pPathology.get(), newPathology.get())
            
                # Call showInSpecimenList method after inserting the data record
                showInSpecimenList()
                clear()
            else:
                tkinter.messagebox.askyesno("Specimen Metadata Management System", 
                                            "Enter Specimen id" )
            
            print("Specimen : insert method finished\n")

        # Function to show Specimen information in the scrollbar
        def showInSpecimenList():
            print("Specimen : showInSpecimenList method called")
            SpecimenList.delete(0,END)
            for row in d.show():
                SpecimenList.insert(END, row)#, str(""))
            print("Specimen : showInSpecimenList method finished\n")

        # Function to add to scroll bar
        def SpecimenRec(event): # function to tbe called from scroll bar SpecimenList
            print("Specimen : SpecimenRec method called")
            global pd

            searchPd = SpecimenList.curselection()[0]
            pd = SpecimenList.get(searchPd)

            # Fill in databaseID
            self.txtEntryID.delete(0, END)
            self.txtEntryID.insert(END, pd[0])

            # Fill in specimenID
            self.txtpID.delete(0, END)
            self.txtpID.insert(END, pd[1])

            # Fill in specimenName
            self.txtpName.delete(0, END)
            self.txtpName.insert(END, pd[2])

            # Fill in specimenType
            pType.set(pd[3]) 
            
            # Fill in specimenAge
            self.txtpAge.delete(0, END)
            self.txtpAge.insert(END, pd[4])

            # Fill in specimenAgeUnit
            pAgeUnit.set(pd[5]) 

            # Fill in specimenWeight
            self.txtpWeight.delete(0, END)
            self.txtpWeight.insert(END, pd[6])

            # Fill in specimenWeightUnit
            pWeightUnit.set(pd[7]) 

            # Fill in specimenSex
            pSex.set(pd[8]) 

            # FIll in specimenStrain
            self.txtpStrain.delete(0, END)
            self.txtpStrain.insert(END, pd[9])

            # Fill in specimenAttribute
            selectAttribute(pd[3])
            pAttribute.set(pd[10])

            # Fill in specimenPathology
            pPathology.set(pd[11]) 
            self.txtpPathology.delete(0, END)
            self.txtpPathology.insert(END, pd[12])
            if pd[11] == "Other":
                entry_state = "normal"
            else:
                entry_state = "disabled"
            self.txtpPathology = Entry(LeftBodyFrame, font=("calibri", 12, "bold"), 
                textvariable=newPathology, width=20, state=entry_state)                   


            print("Specimen : SpecimenRec method finished")

        # Function to delete the data record from database table
        def delete():
            print("Specimen : delete method called")
            if len(entryID.get()) != 0 :
                d.delete(pd[0])
                clear()
                showInSpecimenList()

            print("Specimen : delete method finished\n")

        # Search the record from the database table
        def search():
            print("Specimen : search method called")
            SpecimenList.delete(0,END)
            for row in d.search(entryID.get(), pID.get(), pName.get(), pType.get(), pAge.get(), pAgeUnit.get(), pWeight.get(), pWeightUnit.get(), pSex.get(), pStrain.get(), pAttribute.get(), pPathology.get(), newPathology.get()):
                SpecimenList.insert(END, row)#, str(""))
            print("Specimen : search method finished\n")

        # function to update the record
        def update():
            print("Specimen : update method called")
            if len(entryID.get()) != 0:
                print("pd[0]", pd[0])
                d.delete(pd[0])
            if len(entryID.get()) != 0:
                d.insert(entryID.get(), pID.get(), pName.get(), pType.get(), pAge.get(), pAgeUnit.get(), pWeight.get(), pWeightUnit.get(), 
                             pSex.get(), pStrain.get(), pAttribute.get(), pPathology.get(), newPathology.get())
                SpecimenList.delete(0, END)
                SpecimenList.insert(END, (entryID.get(), pID.get(), pName.get(), pType.get(), pAge.get(), pAgeUnit.get(), pWeight.get(), 
                                    pWeightUnit.get(), pSex.get(), pStrain.get(), pAttribute.get(), pPathology.get(), newPathology.get()))
            showInSpecimenList()
            print("Specimen : update method finished\n")


        """Create frames"""
        MainFrame = Frame(self.root, bg="black")
        MainFrame.grid()

        HeadFrame = Frame(MainFrame, bd=2, width=1500, height= 50, padx=50, pady = 10, 
                            bg="#800020", relief = RIDGE)
        HeadFrame.pack(side = TOP)

        self.ITitle = Label(HeadFrame, font=("calibri", 40, "bold"), fg = "White", 
                        text = "        Specimen Metadata Management System          ", 
                        bg = "#800020")

        self.ITitle.grid()

        OperationFrame = Frame(MainFrame,bd = 2, width=1300, height= 50, 
                                padx= 121, pady=20, bg= "#800020",relief= RIDGE)

        OperationFrame.pack(side=BOTTOM)

        BodyFrame = Frame(MainFrame,bd = 2, width=1300, height= 500, 
                                padx= 19, pady=20, bg= "#800020",relief= RIDGE)

        BodyFrame.pack(side=BOTTOM)

        LeftBodyFrame = LabelFrame(BodyFrame,bd = 2, width=800, height= 380, 
                                padx= 20, pady=10, bg= "#800020", fg = "white", relief= RIDGE, 
                                font=("calibri", 12, "bold"), text="Specimen Metadata Details:")

        LeftBodyFrame.pack(side=LEFT)

        RightBodyFrame = LabelFrame(BodyFrame,bd = 2, width=500, height= 380, 
                                padx= 20, pady=10, bg= "#800020", fg = "white", relief= RIDGE, 
                                font=("calibri", 12, "bold"), text="Specimen Metadata Overview:")

        RightBodyFrame.pack(side=RIGHT)

        """Add the Widgets to the LeftBodyFrame"""

        # entryID
        self.labelEntryID = Label(LeftBodyFrame, bd = 2, font=("calibri", 12, "bold"), 
                            text="Database ID: ", padx=2, pady=2, bg="#800020", fg="white")
        self.labelEntryID.grid(row =0, column=0, sticky=W)
        
        self.txtEntryID = Entry(LeftBodyFrame, font=("calibri", 12, "bold"), 
                    textvariable=entryID)
        self.txtEntryID.grid(row=0, column=1, sticky='NSEW', columnspan = 2)

        # pID
        self.labelpID = Label(LeftBodyFrame, bd = 2, font=("calibri", 12, "bold"), 
                            text="Specimen ID: ", padx=2, pady=2, bg="#800020", fg="white")
        self.labelpID.grid(row =1, column=0, sticky=W)
        
        self.txtpID = Entry(LeftBodyFrame, font=("calibri", 12, "bold"), 
                    textvariable=pID)
        self.txtpID.grid(row=1, column=1, sticky='NSEW', columnspan = 2)

        # pName
        self.labelpName = Label(LeftBodyFrame, bd = 2, font=("calibri", 12, "bold"), 
                            text="Specimen Name: ", padx=2, pady=2, bg="#800020", fg="white")
        self.labelpName.grid(row =2, column=0, sticky=W)

        self.txtpName = Entry(LeftBodyFrame, font=("calibri", 12, "bold"), 
                    textvariable=pName)
        self.txtpName.grid(row=2, column=1, sticky='NSEW', columnspan = 2)

        # pAttribute
        self.labelpAttribute = Label(LeftBodyFrame, bd = 2, font=("calibri", 12, "bold"), 
                            text="Attribute: ", padx=2, pady=2, bg="#800020", fg="white")
        self.labelpAttribute.grid(row =8, column=0, sticky=W)
        attributes = ["None"]  
        self.txtpAttribute = OptionMenu(LeftBodyFrame, pAttribute, *attributes)
        self.txtpAttribute.config(font=("calibri", 10, "bold"))
        self.txtpAttribute.grid(row=8, column=1, sticky='NSEW', columnspan=2)
        pAttribute.set("select attribute") 

        def selectAttribute(event):
            if pType.get() == "subjectGroup" or pType.get() == "subject":
                attributes = [
                    "anaesthetized",
                    "asleep",
                    "awake",
                    "comatose",
                    "control",
                    "deceased",
                    "freelyMoving",
                    "hasImplantedDevice",
                    "hasInsertedDevice",
                    "headRestrained",
                    "knockin",
                    "knockout",
                    "restrained",
                    "treated",
                    "untreated"
                    ]

            elif pType.get() == "tsc" or pType.get() == "ts":
                attributes = [
                    "stained",
                    "unstained",
                    "untreated",
                    "fixated",
                    "labeled",
                    "freeFloating",
                    "mounted"
                ]   
            self.txtpAttribute = OptionMenu(LeftBodyFrame, pAttribute, *attributes)
            self.txtpAttribute.config(font=("calibri", 10, "bold"))
            self.txtpAttribute.grid(row=8, column=1, sticky='NSEW', columnspan=2)
            pAttribute.set("select attribute")   
              
        #pType
        self.labelpType = Label(LeftBodyFrame, bd = 2, font=("calibri", 12, "bold"), 
                            text="Specimen Type: ", padx=2, pady=2, bg="#800020", fg="white")
        self.labelpType.grid(row =3, column=0, sticky=W) 

        specimenTypes = [
            "subjectGroup", 
            "subject", 
            "tsc", 
            "ts"
            ]
        self.txtpType = OptionMenu(LeftBodyFrame, pType, *specimenTypes, command=selectAttribute)
        self.txtpType.config(font=("calibri", 10, "bold"))
        self.txtpType.grid(row=3, column=1, sticky='NSEW', columnspan = 2)
        pType.set("select specimen type")

        #pAge
        self.labelpAge = Label(LeftBodyFrame, bd = 2, font=("calibri", 12, "bold"), 
                            text="Specimen Age: ", padx=2, pady=2, bg="#800020", fg="white")
        self.labelpAge.grid(row =4, column=0, sticky=W)

        self.txtpAge = Entry(LeftBodyFrame, font=("calibri", 12, "bold"), 
                    textvariable=pAge)
        self.txtpAge.grid(row=4, column=1, sticky='NSEW')

        ageUnits = [
            "day", 
            "week", 
            "month", 
            "year"
            ]
        self.txtpAgeUnit = OptionMenu(LeftBodyFrame, pAgeUnit, *ageUnits)
        self.txtpAgeUnit.config(font=("calibri", 10, "bold"), width = 20)
        self.txtpAgeUnit.grid(row=4, column=2, sticky='W')
        pAgeUnit.set("select unit")

        #pWeight
        self.labelpWeight = Label(LeftBodyFrame, bd = 2, font=("calibri", 12, "bold"), 
                            text="Specimen Weight: ", padx=2, pady=2, bg="#800020", fg="white")
        self.labelpWeight.grid(row =5, column=0, sticky=W)

        self.txtpWeight = Entry(LeftBodyFrame, font=("calibri", 12, "bold"), 
                    textvariable=pWeight)
        self.txtpWeight.grid(row=5, column=1, sticky='NSEW')

        weightUnits = [
            "gram", 
            "kilogram"
            ]
        self.txtpWeightUnit = OptionMenu(LeftBodyFrame, pWeightUnit, *weightUnits)
        self.txtpWeightUnit.config(font=("calibri", 10, "bold"), width = 20)
        self.txtpWeightUnit.grid(row=5, column=2, sticky='W')
        pWeightUnit.set("select unit")

        #pSex
        self.labelpSex = Label(LeftBodyFrame, bd = 2, font=("calibri", 12, "bold"), 
                            text="Sex", padx=2, pady=2, bg="#800020", fg="white")
        self.labelpSex.grid(row =6, column=0, sticky=W)

        sexes = [
            "male", 
            "female", 
            "hermaphrodite", 
            "undetected"
            ]
        self.txtpSex = OptionMenu(LeftBodyFrame, pSex, *sexes)
        self.txtpSex.config(font=("calibri", 10, "bold"))
        self.txtpSex.grid(row=6, column=1, sticky='NSEW', columnspan=2)
        pSex.set("select sex")

        #pStrain
        self.labelpStrain = Label(LeftBodyFrame, bd = 2, font=("calibri", 12, "bold"), 
                            text="Strain", padx=2, pady=2, bg="#800020", fg="white")
        self.labelpStrain.grid(row =7, column=0, sticky=W)

        self.txtpStrain = Entry(LeftBodyFrame, font=("calibri", 12, "bold"), 
                    textvariable=pStrain)
        self.txtpStrain.grid(row=7, column=1, sticky='NSEW', columnspan = 2)

        #pPathology
        self.labelpPathology = Label(LeftBodyFrame, bd = 2, font=("calibri", 12, "bold"), 
                            text="Specimen Pathology: ", padx=2, pady=2, bg="#800020", fg="white")
        self.labelpPathology.grid(row =9, column=0, sticky=W)

        self.txtpPathology = Entry(LeftBodyFrame, font=("calibri", 12, "bold"), 
            textvariable=newPathology, width=20)#, state="disabled")
        self.txtpPathology.grid(row=9, column=2, sticky='NSEW')

        def selectPathology(event):
            if pPathology.get() == "Other":
                entry_state = "normal"
                newPathology = StringVar(value="")
            else:
                entry_state = "disabled"

            self.txtpPathology = Entry(LeftBodyFrame, font=("calibri", 12, "bold"), 
                textvariable=newPathology, width=20, state=entry_state)
            self.txtpPathology.grid(row=9, column=2, sticky='NSEW')

        pathologies = [
            "None",
            "glioma",
            "meningioma",
            "fragileXsyndrome",
            "epilepsy",
            "congenitalBlindness",
            "disorderOfConsciousness",
            "autismSpectrumDisorder",
            "alzheimersDisease",
            "acquiredBlindness",
            "parkinsonsDisease",
            "stroke",
            "williamsBeurenSyndrome",
            "alzheimersDiseaseModel",
            "autismSpectrumDisorderModel",
            "epilepsyModel",
            "fragileXsyndromeModel",
            "huntingtonsDiseaseModel",
            "parkinsonsDiseaseModel",
            "strokeModel",
            "williamsBeurenSyndromeModel",
            "Other"
            ]
        self.txtpPathologyOption = OptionMenu(LeftBodyFrame, pPathology, *pathologies, command=selectPathology)
        self.txtpPathologyOption.config(font=("calibri", 10, "bold"), width = 30)
        self.txtpPathologyOption.grid(row=9, column=1, sticky='NSEW')
        pPathology.set("select pathology")

        """ Add Scroll bar """
        scrolly = Scrollbar(RightBodyFrame)
        scrolly.grid(row =0, column=1, sticky = "ns")

        scrollx = Scrollbar(RightBodyFrame, orient=HORIZONTAL)
        scrollx.grid(row =1, column=0, sticky='NSEW')

        SpecimenList = Listbox(RightBodyFrame, width=60, height=15, font=("calibri", 12, "bold"),
                            yscrollcommand=scrolly.set, xscrollcommand=scrollx.set, selectmode="single")
        
        # Call SpecimenRec function from init function
        SpecimenList.bind("<<ListboxSelect>>", SpecimenRec)
        SpecimenList.grid(row=0, column=0, padx=8)

        scrolly.config(command=SpecimenList.yview())
        scrollx.config(command=SpecimenList.xview())

        """ Add the buttons to operation Frame """
        #Save
        self.buttonSave = Button(OperationFrame, text="Save", font=("calibri", 12, "bold"), 
                                height=1, width=16, bd = 4, command = insert)
        self.buttonSave.grid(row=0, column=0)
        #Show
        self.buttonShow = Button(OperationFrame, text="Show metadata", font=("calibri", 12, "bold"), 
                                height=1, width=16, bd = 4, command = showInSpecimenList)
        self.buttonShow.grid(row=0, column=1)
        # Clear
        self.buttonClear = Button(OperationFrame, text="Clear", font=("calibri", 12, "bold"), 
                                height=1, width=16, bd = 4, command = clear)
        self.buttonClear.grid(row=0, column=2)        
        #Delete
        self.buttonDelete = Button(OperationFrame, text="Delete", font=("calibri", 12, "bold"), 
                                height=1, width=16, bd = 4, command = delete)
        self.buttonDelete.grid(row=0, column=3)
        # Search
        self.buttonSearch = Button(OperationFrame, text="Search", font=("calibri", 12, "bold"), 
                                height=1, width=16, bd = 4, command = search)
        self.buttonSearch.grid(row=0, column=4)
        # Update
        self.buttonUpdate = Button(OperationFrame, text="Update", font=("calibri", 12, "bold"), 
                                height=1, width=16, bd = 4, command = update)
        self.buttonUpdate.grid(row=0, column=5)
        # Close
        self.buttonClose = Button(OperationFrame, text="Close", font=("calibri", 12, "bold"), 
                                height=1, width=16, bd = 4, command = close)
        self.buttonClose.grid(row=0, column=6)

# Backend Database Operations

class Database:
    def conn(self): 
        print("Database : connection method called")
        con = sqlite3.connect("specimenList.db") # creates a db file called inventory
        cur = con.cursor()
        query = "create table if not exists Specimen (databaseID integer primary key,\
            specimenID text, specimenName text, specimenType text, specimenAge text, specimenAgeUnit text, \
            specimenWeight text, specimenWeightUnit text, specimenSex text, specimenStrain text, \
            specimenAttribute text, specimenPathology text, specimenPathologyNew text)"
        cur.execute(query)
        con.commit()
        con.close()
        print("Database : connection method finished\n")

    def insert(self, entryid, pid, pname, ptype, age, ageunit, weight, weightunit, sex, strain, attribute, pathology, newpathology):
        print("Database : insert method called")
        con = sqlite3.connect("specimenList.db")
        cur = con.cursor()
        query = "Insert or replace into Specimen values (?,?,?,?,?,?,?,?,?,?,?,?,?)"
        cur.execute(query, (entryid, pid, pname, ptype, age, ageunit, weight, weightunit, sex, strain, attribute, pathology, newpathology))
        con.commit()
        con.close()
        print("Database : insert method finished\n")

    def show(self):
        print("Database : show method called")
        con = sqlite3.connect("specimenList.db")
        cur = con.cursor()
        query = "select * from Specimen"
        cur.execute(query)
        rows = cur.fetchall()
        con.close()
        print("Database : show method finished\n")
        return rows

    def delete(self, entryid):
        print("Database : delete method called ", entryid)
        con = sqlite3.connect("specimenList.db")
        cur = con.cursor()
        cur.execute("delete from Specimen where specimenID=? ", (entryid,))
        con.commit()
        con.close()
        print(entryid, "Database : delete method finished\n")        

    def search(self, entryid="", pid="", pname="", ptype="", age="", ageunit="", weight="", weightunit="", sex="", strain="", attribute="", pathology="", newpathology=""):
        print("Database : search method called ", entryid)
        con = sqlite3.connect("specimenList.db")
        cur = con.cursor()
        cur.execute("select * from Specimen where databaseID=? or specimenID=? or specimenName=? or \
            specimenType=? or specimenAge=? or specimenAgeUnit=? or specimenWeight=? or specimenWeightunit=? \
            or specimenSex=? or specimenStrain=? or specimenAttribute=? or specimenPathology=? or specimenPathologyNew=?", 
            (entryid, pid, pname, ptype, age, ageunit, weight, weightunit, sex, strain, attribute, pathology, newpathology))
        row = cur.fetchall()
        con.close()
        print(entryid, "Database : search method finished\n")   
        return row

    def update(self, entryid="", pid="", pname="", ptype="", age="", ageunit="", weight="", weightunit="", sex="", strain="", attribute="", pathology="", newpathology=""):
        print("Database : update method called ", entryid)
        con = sqlite3.connect("specimenList.db")
        cur = con.cursor()
        cur.execute("update Specimen set databaseID=? or specimenID=? or specimenName=? or \
            specimenType=? or specimenAge=? or specimenAgeUnit=? or specimenWeight=? or specimenWeightunit=? \
            or specimenSex=? or specimenStrain=? or specimenAttribute=? or specimenPathology=? or specimenPathologyNew=?\
            where databaseID=?", 
            (entryid, pid, pname, ptype, age, ageunit, weight, weightunit, sex, strain, attribute, pathology, newpathology, entryid))
        con.commit()
        con.close()
        print(entryid, "Database : update method finished\n")  



if __name__ =='__main__':
    root = Tk()
    application = Specimen(root)
    root.mainloop()


