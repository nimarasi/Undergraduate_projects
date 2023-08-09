import datetime
import tkinter as tk
from tkinter import ttk
from tkinter import  font
import ctypes as ct
from PIL import Image,ImageTk
import Functions
def dark_title_bar(window):
    window.update()
    DWMWA_USE_IMMERSIVE_DARK_MODE = 20
    set_window_attribute = ct.windll.dwmapi.DwmSetWindowAttribute
    get_parent = ct.windll.user32.GetParent
    hwnd = get_parent(window.winfo_id())
    rendering_policy = DWMWA_USE_IMMERSIVE_DARK_MODE
    value = 2
    value = ct.c_int(value)
    set_window_attribute(hwnd, rendering_policy, ct.byref(value), ct.sizeof(value))

class Root(tk.Tk):
    def __init__(self):
        super().__init__()
        self.font = ('Segoe Print', 11)
        self.resizable(False, False)
        dark_title_bar(self)
        self.geometry("800x600")
        self.title("Fix")
        self.wm_iconphoto(False,ImageTk.PhotoImage(Image.open("better2.png").resize(size=(64,64))))
        self.tk.call("source", "Azure-ttk-theme-main/azure.tcl")
        self.tk.call("set_theme", "dark")

        self.loginFrame=LoginFrame(self.font)
        self.signUpFramePatient=SignUpFramePatient(self.font)
        self.signUpFrameDoctor=SignUpFrameDoctor(self.font)
        self.patientPanel=PatientPanel(self.font)

        self.patientPanel.phoneNumberVar.set("87364383434")

        self.doctorPanel=DoctorPanel(self.font)

        self.doctorPanel.firstNameVar.set("djkfhdkjd")


        self.adminPanel=AdminFrame(self.font)

        self.appoinmentReservePanel=AppoinementReservePanel(self.font)
        self.messageFrame=MessageFrame(self.font,BackToPanel)
        self.messageFrameSignup=MessageFrame(self.font,Logout)
        self.rowconfigure(0,weight=1)
        self.columnconfigure(0,weight=1)

        self.loginFrame.grid(row=0,column=0)
        self.loginFrame.tkraise()
def Login():

    if root.loginFrame.userModeVar.get() == "Doctor" :
            doctor=Functions.CheckLogin(root.loginFrame.usernameVar.get(),
                                    root.loginFrame.passwordVar.get(),root.loginFrame.userModeVar.get())
            if doctor!="Wrong Username or Password ":
                root.loginFrame.grid_remove()
                root.doctorPanel.grid(row=0, column=0)
                root.doctorPanel.firstNameVar.set(doctor.firstName)
                root.doctorPanel.lastNameVar.set(doctor.lastName)
                root.doctorPanel.hospitalVar.set(doctor.hospital)
                root.doctorPanel.proficiencyVar.set(doctor.proficiency)
                root.doctorPanel.phoneNumberVar.set(doctor.number)
                root.doctorPanel.idVar.set(doctor.id)
                appoinments=Functions.GetAppoinmentsDoctor(doctor.firstName+" "+doctor.lastName)
                for a in appoinments:
                    root.doctorPanel.treeview.insert(parent="",index="end",text=a.patientName,
                                                     values=(a.patientId,a.time,str(a.date).split(" ")[0]))
            else:
                root.loginFrame.statusVar.set("Wrong Username or Password ")

    elif root.loginFrame.userModeVar.get() == "Patient":
        patient = Functions.CheckLogin(root.loginFrame.usernameVar.get(),
                                       root.loginFrame.passwordVar.get(), root.loginFrame.userModeVar.get())
        if patient != "Wrong Username or Password ":
            root.loginFrame.grid_remove()
            root.patientPanel.grid(row=0, column=0)
            root.patientPanel.firstNameVar.set(patient.firstName)
            root.patientPanel.lastNameVar.set(patient.lastName)
            root.patientPanel.idVar.set(patient.id)
            root.patientPanel.phoneNumberVar.set(patient.number)
            root.patientPanel.insuranceNumberVar.set(patient.ins_id)
            root.patientPanel.genderVar.set(patient.gender)
            appoinments = Functions.GetAppoinmentsPatient(patient.id)
            for a in appoinments:
                root.patientPanel.treeview.insert("", "end", text=a.hospital, values=(a.doctor, str(a.date).split(" ")[0], a.time))
            root.loginFrame.grid_remove()
            root.patientPanel.grid(row=0, column=0)
        else:
            root.loginFrame.statusVar.set("Wrong Username or Password ")
    elif root.loginFrame.userModeVar.get() == "Admin":
        if root.loginFrame.usernameVar.get()=="A" and root.loginFrame.passwordVar.get()=="1234":
            root.adminPanel.hospitals=Functions.GetHospitals()
            for item in Functions.GetHospitals():
                root.adminPanel.treeview.insert(parent="", index="end", text=item.name, values=(item.address))
            for item in Functions.GetPatiensts():
                root.adminPanel.treeview2.insert(parent="",index="end",text=str(item.firstName)+" "+str(item.lastName),values=(str(item.id)))


            root.loginFrame.grid_remove()
            root.adminPanel.grid(row=0, column=0)
    else:
        root.loginFrame.statusVar.set("Please choose User Mode")


def SignUp():

    if root.loginFrame.userModeVar.get()=="Doctor":
        root.loginFrame.grid_remove()
        root.signUpFrameDoctor.grid(row=0,column=0)
        hospitals=Functions.GetHospitals()
        values=[]
        for v in hospitals:
            values.append(v.name)
        root.signUpFrameDoctor.hospitalComboBox.configure(values=values)
        for a in root.signUpFrameDoctor.variables:
            a.set("")
    elif root.loginFrame.userModeVar.get()=="Patient":
        root.loginFrame.grid_remove()
        root.signUpFramePatient.grid(row=0,column=0)
        for a in root.signUpFramePatient.variables:
            a.set("")
    else:
        root.loginFrame.statusVar.set("Please choose User Mode")
def SignUpButton():
    if root.loginFrame.userModeVar.get()=="Doctor":
        Functions.addDoctor(root.signUpFrameDoctor.idVar.get(),
                            root.signUpFrameDoctor.firstNameVar.get(),
                            root.signUpFrameDoctor.lastNameVar.get(),
                            root.signUpFrameDoctor.ageVar.get(),
                            root.signUpFrameDoctor.phoneNumberVar.get(),
                            root.signUpFrameDoctor.usernameVar.get(),
                            root.signUpFrameDoctor.passwordVar.get(),
                            root.signUpFrameDoctor.genderVar.get(),
                            root.signUpFrameDoctor.hospitalVar.get(),
                            root.signUpFrameDoctor.proficiencyVar.get(),
                            root.signUpFrameDoctor.dayOfWeekVar.get(),
                            root.signUpFrameDoctor.dayOfWeekVar1.get(),
                            root.signUpFrameDoctor.timeVar.get(),
                            root.signUpFrameDoctor.timeVar1.get())

        root.signUpFrameDoctor.grid_remove()
        root.messageFrameSignup.grid(row=0,column=0)
        root.messageFrameSignup.labelVar.set("SignUp Succesfull!")
    elif root.loginFrame.userModeVar.get()=="Patient":
        patient=Functions.P(root.signUpFramePatient.idVar.get(),
                             root.signUpFramePatient.firstNameVar.get(),
                             root.signUpFramePatient.lastNameVar.get(),
                             root.signUpFramePatient.ageVar.get(),
                             root.signUpFramePatient.phoneNumberVar.get(),
                             root.signUpFramePatient.usernameVar.get(),
                             root.signUpFramePatient.passwordVar.get(),
                             root.signUpFramePatient.genderVar.get(),
                             root.signUpFramePatient.insuranceNumberVar.get())

        Functions.addPatient(root.signUpFramePatient.idVar.get(),
                             root.signUpFramePatient.firstNameVar.get(),
                             root.signUpFramePatient.lastNameVar.get(),
                             root.signUpFramePatient.ageVar.get(),
                             root.signUpFramePatient.phoneNumberVar.get(),
                             root.signUpFramePatient.usernameVar.get(),
                             root.signUpFramePatient.passwordVar.get(),
                             root.signUpFramePatient.genderVar.get(),
                             root.signUpFramePatient.insuranceNumberVar.get())

        root.signUpFramePatient.grid_remove()
        root.messageFrameSignup.grid(row=0, column=0)
        root.messageFrameSignup.labelVar.set("SignUp Succesfull!")

def Logout():
    root.messageFrame.grid_remove()
    root.messageFrameSignup.grid_remove()
    root.loginFrame.usernameVar.set("")
    root.loginFrame.passwordVar.set("")
    root.loginFrame.userModeVar.set("")
    root.loginFrame.grid(row=0,column=0)
    root.signUpFrameDoctor.grid_remove()
    root.signUpFramePatient.grid_remove()
    root.patientPanel.grid_remove()
    root.doctorPanel.grid_remove()
    root.adminPanel.grid_remove()
    root.loginFrame.statusVar.set("")
    for a in root.doctorPanel.variables:
        a.set("")
    for a in root.patientPanel.variables:
        a.set("")
    for item in root.patientPanel.treeview.get_children():
        root.patientPanel.treeview.delete(item)
    for item in root.doctorPanel.treeview.get_children():
        root.patientPanel.treeview.delete(item)
    for a in root.signUpFramePatient.variables:
        a.set("")
    for a in root.signUpFrameDoctor.variables:
        a.set("")
    root.signUpFramePatient=SignUpFramePatient(root.font)
    root.signUpFrameDoctor=SignUpFrameDoctor(root.font)
    root.adminPanel=AdminFrame(root.font)
def ReservePanel():
    hospitals = Functions.GetHospitals()
    for item in root.appoinmentReservePanel.treeview.get_children():
        root.appoinmentReservePanel.treeview.delete(item)
    for v in hospitals:
        root.appoinmentReservePanel.treeview.insert(parent="",index="end",text=v.name,values=(v.address))
    root.patientPanel.grid_remove()
    root.appoinmentReservePanel.grid(row=0,column=0)
def BackToPanel():
    if root.loginFrame.userModeVar.get()=="Patient":
        root.appoinmentReservePanel.grid_remove()
        root.messageFrame.grid_remove()
        root.patientPanel.grid(row=0,column=0)
        for item in root.appoinmentReservePanel.treeview1.get_children():
            root.appoinmentReservePanel.treeview1.delete(item)
        for item in root.appoinmentReservePanel.treeview2.get_children():
            root.appoinmentReservePanel.treeview2.delete(item)
    elif root.loginFrame.userModeVar.get()=="Doctor":
        root.appoinmentReservePanel.grid_remove()
        root.messageFrame.grid_remove()
        root.doctorPanel.grid(row=0,column=0)

def highlight_clear(event,combobox):
    # added for deleting combobox highlight issue
    current = combobox.get()
    combobox.set("")
    combobox.set(current)
def Message(message):

    root.appoinmentReservePanel.grid_remove()
    root.messageFrame.labelVar.set(message)
    root.messageFrame.grid(row=0,column=0)
class LoginFrame(ttk.Frame):
    def __init__(self,font):
        super().__init__()
        self.font=font
        image = Image.open("better2.png").resize(size=(2100//5,1500//5))
        self.photo = ImageTk.PhotoImage(image)
        self.photoLabel=ttk.Label(self,image=self.photo,anchor="center")
        self.usernameVar=tk.StringVar()
        self.passwordVar=tk.StringVar()
        self.userModeVar=tk.StringVar()

        self.modeLabel=ttk.Label(self,font=self.font,text="User Mode: ")
        self.modeComboBox=ttk.Combobox(self,font=self.font,values=("Patient","Doctor","Admin"),textvariable=self.userModeVar,state="readonly")
        self.modeComboBox.bind("<<ComboboxSelected>>", self.highlight_clear)

        self.usernameLabel=ttk.Label(self,text="Username: ",font=self.font)
        self.usernameEntry=ttk.Entry(self,textvariable=self.usernameVar,width=40,font=self.font)

        self.passwordLabel=ttk.Label(self,text="Password: ",font=self.font)
        self.passwordEntry=ttk.Entry(self,textvariable=self.passwordVar,width=40,font=self.font,show="*")

        ttk.Style().configure('TButton', font=(self.font[0],9))
        self.loginButton=ttk.Button(self,text="Login",command=Login,style="TButton")
        self.signUpButton=ttk.Button(self,text="No Account? Signup",command=SignUp,style="TButton")

        self.statusVar=tk.StringVar()
        self.statusLabel=ttk.Label(self,textvariable=self.statusVar,font=self.font)
        self.photoLabel.grid(row=0,column=0,columnspan=2,sticky="EW")

        self.modeLabel.grid(row=1,column=0,sticky="EWNS")
        self.modeComboBox.grid(row=1,column=1,sticky="EWNS")
        self.usernameLabel.grid(row=2,column=0,sticky="EWNS")
        self.usernameEntry.focus()
        self.usernameEntry.grid(row=2,column=1,sticky="EWNS")

        self.passwordEntry.grid(row=3,column=1,sticky="EWNS")
        self.passwordLabel.grid(row=3,column=0,sticky="EWNS")

        self.loginButton.grid(row=4,column=0,columnspan=2,sticky="EW",pady=(10,5))
        self.signUpButton.grid(row=5,column=0,columnspan=2,sticky="EW",pady=(0,5))

        self.statusLabel.grid(row=6,column=0,columnspan=2,sticky="EW")
    def highlight_clear(self, event):
        # added for deleting combobox highlight issue
        current = self.userModeVar.get()
        self.modeComboBox.set("")
        self.modeComboBox.set(current)
        if current=="Admin":
            self.signUpButton.config(state="disabled")
        else:
            self.signUpButton.config(state="normal")
class SignUpFramePatient(ttk.Frame):

    def __init__(self,font):
        super().__init__()
        self.font = font
        self.usernameVar = tk.StringVar()
        self.passwordVar = tk.StringVar()
        self.firstNameVar=tk.StringVar()
        self.lastNameVar=tk.StringVar()
        self.idVar=tk.StringVar()
        self.phoneNumberVar=tk.StringVar()
        self.insuranceNumberVar=tk.StringVar()
        self.genderVar=tk.StringVar()
        self.ageVar=tk.StringVar()
        self.variables = [self.usernameVar, self.passwordVar, self.firstNameVar, self.lastNameVar,
                          self.idVar, self.phoneNumberVar, self.insuranceNumberVar,self.ageVar ]
        self.usernameLabel = ttk.Label(self, text="Username: ", font=self.font)
        self.usernameEntry = ttk.Entry(self, textvariable=self.usernameVar, width=40, font=self.font)

        self.passwordLabel = ttk.Label(self, text="Password: ", font=self.font)
        self.passwordEntry = ttk.Entry(self, textvariable=self.passwordVar, width=40, font=self.font, show="*")

        self.firstNameLabel=ttk.Label(self, text="First Name: ", font=self.font)
        self.lastNameLabel=ttk.Label(self, text="Last Name: ", font=self.font)
        self.idLabel=ttk.Label(self, text="National Code: ", font=self.font)
        self.phoneNumberLabel=ttk.Label(self, text="Phone Number: ", font=self.font)
        self.insuranceNumberLabel=ttk.Label(self, text="Insurance Number: ", font=self.font)
        self.genderLabel=ttk.Label(self, text="Gender: ", font=self.font)
        self.ageLabel=ttk.Label(self, text="Age: ", font=self.font)

        self.firstNameEntry = ttk.Entry(self, textvariable=self.firstNameVar, font=self.font)
        self.lastNameEntry = ttk.Entry(self, textvariable=self.lastNameVar, font=self.font)
        self.idEntry = ttk.Entry(self, textvariable=self.idVar, font=self.font)
        self.phoneNumberEntry = ttk.Entry(self, textvariable=self.phoneNumberVar, font=self.font)
        self.insuranceNumberEntry = ttk.Entry(self, textvariable=self.insuranceNumberVar, font=self.font)
        self.ageEntry=ttk.Entry(self, textvariable=self.ageVar, font=self.font)
        self.genderComboBox=ttk.Combobox(self,values=("Male","Female"),font=self.font,state="readonly",textvariable=self.genderVar)
        self.genderComboBox.bind("<<ComboboxSelected>>",
                                    lambda event, combobox=self.genderComboBox: highlight_clear(event, combobox))
        ttk.Style().configure('TButton', font=(self.font[0],9))
        self.signUpButton = ttk.Button(self, text="Signup", command=SignUpButton, style="TButton")
        self.backButton = ttk.Button(self, text="Back", command=Logout, style="TButton")

        self.statusVar = tk.StringVar()
        self.statusLabel = ttk.Label(self, textvariable=self.statusVar, font=self.font)

        self.usernameLabel.grid(row=0, column=0, sticky="EWNS")
        self.usernameEntry.focus()
        self.usernameEntry.grid(row=0, column=1, sticky="EWNS")

        self.passwordEntry.grid(row=1, column=1, sticky="EWNS")
        self.passwordLabel.grid(row=1, column=0, sticky="EWNS")

        self.firstNameLabel.grid(row=2,column=0,sticky="EWNS")
        self.lastNameLabel.grid(row=3,column=0,sticky="EWNS")
        self.idLabel.grid(row=4,column=0,sticky="EWNS")
        self.phoneNumberLabel.grid(row=5,column=0,sticky="EWNS")
        self.insuranceNumberLabel.grid(row=6,column=0,sticky="EWNS")
        self.ageLabel.grid(row=7,column=0,sticky="EWNS")
        self.genderLabel.grid(row=8,column=0,sticky="EWNS")

        self.firstNameEntry.grid(row=2,column=1,sticky="EWNS")
        self.lastNameEntry.grid(row=3,column=1,sticky="EWNS")
        self.idEntry.grid(row=4,column=1,sticky="EWNS")
        self.phoneNumberEntry.grid(row=5,column=1,sticky="EWNS")
        self.insuranceNumberEntry.grid(row=6,column=1,sticky="EWNS")
        self.ageEntry.grid(row=7, column=1, sticky="EWNS")
        self.genderComboBox.grid(row=8,column=1,sticky="EWNS")

        self.signUpButton.grid(row=9, column=0, columnspan=2, sticky="EW", pady=(10, 5))
        self.backButton.grid(row=10, column=0, columnspan=2, sticky="EW", pady=(0, 5))

        self.statusLabel.grid(row=11, column=0, columnspan=2, sticky="EW")

class SignUpFrameDoctor(SignUpFramePatient):

    def __init__(self,font):

        super().__init__(font)
        self.font=(font[0],9)
        self.insuranceNumberLabel.grid_remove()
        self.insuranceNumberEntry.grid_remove()
        self.backButton.grid_remove()
        self.signUpButton.grid_remove()
        self.ageLabel.grid_remove()
        self.ageEntry.grid_remove()
        self.proficiencyVar=tk.StringVar()
        self.hospitalVar = tk.StringVar()
        self.dayOfWeekVar=tk.StringVar()
        self.dayOfWeekVar1=tk.StringVar()
        self.timeVar=tk.StringVar()
        self.timeVar1=tk.StringVar()
        self.proficiencyLabel=ttk.Label(self, text="Proficiency: ", font=self.font)
        self.proficiencyEntry = ttk.Entry(self, textvariable=self.proficiencyVar, font=self.font)

        self.hospitalLabel = ttk.Label(self, text="Hospital:", font=self.font)

        self.dayTimeFrame=ttk.Frame(self,borderwidth=2,relief="solid",)
        self.buttonFrame=ttk.Frame(self)

        ttk.Style().configure('TButton', font=(self.font[0], 9))
        self.signUpButton = ttk.Button(self.buttonFrame, text="Signup", command=SignUpButton, style="TButton")
        self.backButton = ttk.Button(self.buttonFrame, text="Back", command=Logout, style="TButton")
        self.backButton.grid(row=0, column=0,padx=(0,5))
        self.signUpButton.grid(row=0, column=1,padx=(5,0))

        self.dayLabel = ttk.Label(self.dayTimeFrame, text="Day:", font=self.font)
        self.dayFromLabel=ttk.Label(self.dayTimeFrame, text="From:", font=self.font)
        self.dayToLabel=ttk.Label(self.dayTimeFrame, text="To:", font=self.font)
        self.timeLabel = ttk.Label(self.dayTimeFrame, text="Time:", font=self.font)
        self.timeFromLabel = ttk.Label(self.dayTimeFrame, text="From:", font=self.font)
        self.timeToLabel = ttk.Label(self.dayTimeFrame, text="To:", font=self.font)

        self.variables = [self.usernameVar, self.passwordVar, self.firstNameVar, self.lastNameVar,
                          self.idVar, self.phoneNumberVar, self.ageVar,self.proficiencyVar,self.hospitalVar,
                        self.dayOfWeekVar,self.dayOfWeekVar1,self.timeVar,
                        self.timeVar1]
        self.hospitalComboBox = ttk.Combobox(self, textvariable=self.hospitalVar,values=("hospital1","hospital2"),
                                             state="readonly", font=self.font)
        self.hospitalComboBox.bind("<<ComboboxSelected>>", lambda event,combobox=self.hospitalComboBox :highlight_clear(event,combobox))

        self.dayOfWeekComboBox=ttk.Combobox(self.dayTimeFrame,
                                            textvariable=self.dayOfWeekVar,values=("Saturday","Sunday","Monday",
                                            "Tuesday","Wednesday","Thursday","Friday"),state="readonly", font=self.font)
        self.dayOfWeekComboBox.bind("<<ComboboxSelected>>",
                                   lambda event, combobox=self.dayOfWeekComboBox: highlight_clear(event, combobox))
        self.dayOfWeekComboBox1=ttk.Combobox(self.dayTimeFrame,
                                            textvariable=self.dayOfWeekVar1,values=("Saturday","Sunday","Monday",
                                            "Tuesday","Wednesday","Thursday","Friday"),state="readonly", font=self.font)
        self.dayOfWeekComboBox1.bind("<<ComboboxSelected>>",
                                    lambda event, combobox=self.dayOfWeekComboBox1: highlight_clear(event, combobox))
        self.timeComboBox=ttk.Combobox(self.dayTimeFrame,
                            textvariable=self.timeVar,values=("7","8","9","10","15","16","17","18","19","20","21","22","23"),state="readonly", font=self.font)
        self.timeComboBox.bind("<<ComboboxSelected>>",
                                    lambda event, combobox=self.timeComboBox: highlight_clear(event, combobox))
        self.timeComboBox1=ttk.Combobox(self.dayTimeFrame,
                            textvariable=self.timeVar1,values=("7","8","9","10","15","16","17","18","19","20","21","22","23"),state="readonly", font=self.font)
        self.timeComboBox1.bind("<<ComboboxSelected>>",
                               lambda event, combobox=self.timeComboBox1: highlight_clear(event, combobox))

        self.dayLabel.grid(row=0, column=0, padx=(1, 0))
        self.dayFromLabel.grid(row=1, column=1, padx=(5, 0))
        self.dayOfWeekComboBox.grid(row=1, column=2, padx=(5, 0))
        self.dayToLabel.grid(row=1, column=3, padx=(5, 0))
        self.dayOfWeekComboBox1.grid(row=1, column=4, padx=(5, 0))
        self.timeLabel.grid(row=2, column=0, padx=(5, 0))

        self.timeFromLabel.grid(row=3, column=1, padx=(5, 0))
        self.timeComboBox.grid(row=3,column=2,padx=(5,0))
        self.timeToLabel.grid(row=3, column=3, padx=(5, 0))
        self.timeComboBox1.grid(row=3,column=4,padx=(5,0))
        self.variables = [self.usernameVar, self.passwordVar, self.firstNameVar, self.lastNameVar,
                          self.idVar, self.phoneNumberVar, self.proficiencyVar ]



        self.proficiencyLabel.grid(row=6,column=0,sticky="EWNS")
        self.proficiencyEntry.grid(row=6,column=1,sticky="EWNS")
        self.ageLabel.grid(row=7,column=0,sticky="EWNS")
        self.ageEntry.grid(row=7,column=1,sticky="EWNS")
        self.hospitalLabel.grid(row=8,column=0,sticky="EWNS")
        self.hospitalComboBox.grid(row=8,column=1,sticky="EWNS",pady=(0,5))

        self.genderLabel.grid(row=9,column=0,sticky="EWNS",pady=(0,5))
        self.genderComboBox.grid(row=9,column=1,sticky="EWNS",pady=(0,5))
        self.dayTimeFrame.grid(row=10,column=0,columnspan=2)
        self.buttonFrame.grid(row=11,column=0,columnspan=2,pady=(1,5))

        self.statusLabel.grid(row=12, column=0, columnspan=2, sticky="EW")

class PatientPanel(ttk.Frame):
    def addAppoinment(self,appinment):
        self.treeview.insert(parent="",index="end",text=appinment.hospital,values=(appinment.doctor,appinment.date,appinment.time))
    def __init__(self,font):
        super().__init__()
        self.usernameVar = tk.StringVar()
        self.passwordVar = tk.StringVar()
        self.firstNameVar = tk.StringVar()
        self.lastNameVar = tk.StringVar()
        self.idVar = tk.StringVar()
        self.phoneNumberVar = tk.StringVar()
        self.insuranceNumberVar = tk.StringVar()
        self.genderVar=tk.StringVar()
        self.variables=[self.usernameVar,self.passwordVar,self.firstNameVar,self.lastNameVar,
                        self.idVar,self.phoneNumberVar,self.insuranceNumberVar,self.genderVar]

        self.font=font
        ttk.Style().configure('TButton', font=(self.font[0], 9))
        self.backButton = ttk.Button(self, text="Logout", command=Logout, style="TButton")
        self.reserveButton = ttk.Button(self, text="Appoinement Reserve", command=ReservePanel, style="TButton")

        self.firstNameLabel = ttk.Label(self, text="First Name:", font=self.font)
        self.lastNameLabel = ttk.Label(self, text="Last Name:", font=self.font)
        self.idLabel = ttk.Label(self, text="National Code:", font=self.font)
        self.phoneNumberLabel = ttk.Label(self, text="Phone Number:", font=self.font)
        self.insuranceNumberLabel = ttk.Label(self, text="Insurance Number:", font=self.font)
        self.genderLabel = ttk.Label(self, text="Gender:", font=self.font)

        self.firstNameLabel1 = ttk.Label(self, textvariable=self.firstNameVar , font=self.font)
        self.lastNameLabel1 = ttk.Label(self, textvariable=self.lastNameVar, font=self.font)
        self.idLabel1 = ttk.Label(self, textvariable=self.idVar, font=self.font)
        self.phoneNumberLabel1 = ttk.Label(self, textvariable=self.phoneNumberVar, font=self.font)
        self.insuranceNumberLabel1 = ttk.Label(self, textvariable=self.insuranceNumberVar, font=self.font)
        self.genderLabel1 = ttk.Label(self, textvariable=self.genderVar, font=self.font)

        self.appoinementsLabel=ttk.Label(self, text="Appoinements:", font=(self.font[0],15),anchor="center")
        self.panelLabel=ttk.Label(self, text="Patient Panel", font=(self.font[0],20),anchor="center")

        self.scrollbar = ttk.Scrollbar(self)
        self.scrollbar.grid(row=5,column=5,sticky="NS")

        self.treeview = ttk.Treeview(self,selectmode="none",yscrollcommand=self.scrollbar.set,columns=(1, 2,3),height=10)
        self.treeview.grid(row=5,column=0,columnspan=4)
        self.scrollbar.config(command=self.treeview.yview)

        self.treeview.column("#0", anchor="center", width=120)
        self.treeview.column(1, anchor="center", width=120)
        self.treeview.column(2, anchor="center", width=120)
        self.treeview.column(3, anchor="center", width=120)


        self.treeview.heading("#0", text="Hospital", anchor="center")
        self.treeview.heading(1, text="Doctor", anchor="center")
        self.treeview.heading(2, text="Date", anchor="center")
        self.treeview.heading(3, text="Time", anchor="center")


        self.panelLabel.grid(row=0,column=0,sticky="N",columnspan=4,pady=(0,20))
        self.firstNameLabel.grid(row=1,column=0,sticky="EW")
        self.lastNameLabel.grid(row=2,column=0,sticky="EW")
        self.idLabel.grid(row=3,column=0,sticky="EW")
        self.appoinementsLabel.grid(row=4,column=0,columnspan=4,sticky="EW")
        self.phoneNumberLabel.grid(row=1,column=2,sticky="EW")
        self.insuranceNumberLabel.grid(row=2,column=2,sticky="EW")
        self.genderLabel.grid(row=3,column=2,sticky="EW")

        self.firstNameLabel1.grid(row=1,column=1,sticky="EW")
        self.lastNameLabel1.grid(row=2,column=1,sticky="EW")
        self.idLabel1.grid(row=3,column=1,sticky="EW")
        self.phoneNumberLabel1.grid(row=1,column=3,sticky="EW")
        self.insuranceNumberLabel1.grid(row=2,column=3,sticky="EW")
        self.genderLabel1.grid(row=3, column=3, sticky="EW")
        self.backButton.grid(row=6,column=1,sticky="WE",pady=(10,0),padx=(0,5))
        self.reserveButton.grid(row=6,column=2,sticky="WE",pady=(10,0),padx=(5,0))

class DoctorPanel(ttk.Frame):
    def __init__(self,font):
        super().__init__()
        self.usernameVar = tk.StringVar()
        self.passwordVar = tk.StringVar()
        self.firstNameVar = tk.StringVar()
        self.lastNameVar = tk.StringVar()
        self.idVar = tk.StringVar()
        self.phoneNumberVar = tk.StringVar()
        self.proficiencyVar = tk.StringVar()
        self.hospitalVar = tk.StringVar()
        self.variables = [self.usernameVar, self.passwordVar, self.firstNameVar, self.lastNameVar,
                          self.idVar, self.phoneNumberVar, self.proficiencyVar ,self.hospitalVar]


        self.font=font
        ttk.Style().configure('TButton', font=(self.font[0], 9))
        self.backButton = ttk.Button(self, text="Logout", command=Logout, style="TButton")

        self.firstNameLabel = ttk.Label(self, text="First Name:", font=self.font)
        self.lastNameLabel = ttk.Label(self, text="Last Name:", font=self.font)
        self.idLabel = ttk.Label(self, text="National Code:", font=self.font)
        self.phoneNumberLabel = ttk.Label(self, text="Phone Number:", font=self.font)
        self.proficiencyLabel = ttk.Label(self, text="Proficiency:", font=self.font)
        self.hospitalLabel = ttk.Label(self, text="Hospital:", font=self.font)

        self.firstNameLabel1 = ttk.Label(self, textvariable=self.firstNameVar , font=self.font)
        self.lastNameLabel1 = ttk.Label(self, textvariable=self.lastNameVar, font=self.font)
        self.idLabel1 = ttk.Label(self, textvariable=self.idVar, font=self.font)
        self.phoneNumberLabel1 = ttk.Label(self, textvariable=self.phoneNumberVar, font=self.font,anchor="w")
        self.proficiencyLabel1 = ttk.Label(self, textvariable=self.proficiencyVar, font=self.font,anchor="w")
        self.hospitalLabel1 = ttk.Label(self, textvariable=self.hospitalVar, font=self.font,anchor="w")

        self.appoinementsLabel=ttk.Label(self, text="Appoinements:", font=(self.font[0],15),anchor="center")
        self.panelLabel=ttk.Label(self, text="Doctor Panel", font=(self.font[0],20),anchor="center")

        self.scrollbar = ttk.Scrollbar(self)


        self.treeview = ttk.Treeview(self,selectmode="none",yscrollcommand=self.scrollbar.set,columns=(1, 2,3),height=10)
        self.scrollbar.config(command=self.treeview.yview)

        self.treeview.column("#0", anchor="center", width=120)
        self.treeview.column(1, anchor="center", width=120)
        self.treeview.column(2, anchor="center", width=120)
        self.treeview.column(3, anchor="center", width=120)


        self.treeview.heading("#0", text="Patient", anchor="center")
        self.treeview.heading(1, text="National Id", anchor="center")
        self.treeview.heading(2, text="Time", anchor="center")
        self.treeview.heading(3, text="Date", anchor="center")


        self.panelLabel.grid(row=0,column=0,sticky="N",columnspan=5,pady=(0,20))
        self.firstNameLabel.grid(row=1,column=0,sticky="EW")
        self.lastNameLabel.grid(row=2,column=0,sticky="EW")
        self.idLabel.grid(row=3,column=0,sticky="EW")
        self.appoinementsLabel.grid(row=4,column=0,columnspan=4,sticky="EW")
        self.phoneNumberLabel.grid(row=1,column=2,sticky="EW")
        self.proficiencyLabel.grid(row=2,column=2,sticky="EW")
        self.hospitalLabel.grid(row=3,column=2,sticky="EW")

        self.firstNameLabel1.grid(row=1,column=1,sticky="EW")
        self.lastNameLabel1.grid(row=2,column=1,sticky="EW")
        self.idLabel1.grid(row=3,column=1,sticky="EW")
        self.phoneNumberLabel1.grid(row=1,column=3,sticky="EW")
        self.proficiencyLabel1.grid(row=2,column=3,sticky="EW")
        self.hospitalLabel1.grid(row=3, column=3, sticky="EW")

        self.scrollbar.grid(row=5, column=4, sticky="NS")
        self.treeview.grid(row=5, column=0, columnspan=5)
        self.backButton.grid(row=6,column=2,sticky="WE",pady=(10,0),padx=(0,110))

class AppoinementReservePanel(ttk.Frame):
    def getDoctors(self,event):
        self.hospitalName=self.treeview.item(self.treeview.focus())["text"]
        self.doctors=Functions.GetDoctors(self.hospitalName)
        for item in self.treeview1.get_children():
            self.treeview1.delete(item)
        for item in self.doctors:
            self.treeview1.insert(parent="", index="end", text=(item.firstName+" "+item.lastName), values=(item.proficiency))
    def getAppoinments(self,event):
        for item in self.treeview2.get_children():
            self.treeview2.delete(item)
        self.doctorName=self.treeview1.item(self.treeview1.focus())["text"]
        appoinments=Functions.CreateAppoinments(self.doctorName,self.hospitalName,root.patientPanel.idVar.get(),
                                                root.patientPanel.firstNameVar.get()+" "+root.patientPanel.lastNameVar.get())
        self.weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        for app in appoinments:
            date=str(app.date).split("-")

            self.treeview2.insert(parent="", index="end",
                                  text=self.weekdays[datetime.date(int(date[0]),int(date[1]),int(date[2])).weekday()],
                                  values=(app.date,str(app.time).split(".")[0]))


    def Reserve(self):
        datet=self.treeview2.item(self.treeview2.focus())["values"]
        Functions.addAppoinement(self.hospitalName
                                 ,root.patientPanel.firstNameVar.get()+" "+root.patientPanel.lastNameVar.get()
                                 ,root.patientPanel.idVar.get(),self.doctorName,datet[0],datet[1])
        root.patientPanel.addAppoinment(Functions.Appointment(self.hospitalName,
                                        root.patientPanel.firstNameVar.get()+" "+ root.patientPanel.lastNameVar.get(),
                                        root.patientPanel.idVar.get(),self.doctorName,datet[0],datet[1]))
        for item in self.treeview1.get_children():
            self.treeview1.delete(item)
        for item in self.treeview2.get_children():
            self.treeview2.delete(item)
        Message("Reserve Was Succesfull!!")
    def __init__(self,font):
        super().__init__()
        self.font=font

        self.hospitalLabel=ttk.Label(self,text="  Hospital: ",font=self.font)
        self.doctorLabel=ttk.Label(self,text="  Doctor: ",font=self.font)
        self.appoinmentLabel=ttk.Label(self,text="Appoinment:",font=self.font,anchor="center")


        ttk.Style().configure('TButton', font=(self.font[0], 9))
        self.backButton = ttk.Button(self, text="Back", command=BackToPanel, style="TButton")
        self.reserveButton = ttk.Button(self, text="Reserve", command=self.Reserve, style="TButton")

        self.scrollbar = ttk.Scrollbar(self)
        self.scrollbar1 = ttk.Scrollbar(self)
        self.scrollbar2 = ttk.Scrollbar(self)

        self.treeview = ttk.Treeview(self, selectmode="browse", yscrollcommand=self.scrollbar.set, columns=(1),
                                     height=5)
        self.treeview.bind("<<TreeviewSelect>>",self.getDoctors)

        self.scrollbar.config(command=self.treeview.yview)
        self.treeview.column("#0", anchor="center", width=120)
        self.treeview.column(1, anchor="center", width=120)

        self.treeview.heading("#0", text="Name", anchor="center")
        self.treeview.heading(1, text="Address", anchor="center")


        self.treeview1 = ttk.Treeview(self, selectmode="browse", yscrollcommand=self.scrollbar1.set, columns=(1),
                                     height=5)

        self.treeview1.bind("<<TreeviewSelect>>", self.getAppoinments)

        self.scrollbar1.config(command=self.treeview1.yview)
        self.treeview1.column("#0", anchor="center", width=120)
        self.treeview1.column(1, anchor="center", width=120)

        self.treeview1.heading("#0", text="Name", anchor="center")
        self.treeview1.heading(1, text="proficiency", anchor="center")


        self.treeview2 = ttk.Treeview(self, selectmode="browse", yscrollcommand=self.scrollbar2.set, columns=(1, 2),
                                     height=5)
        self.scrollbar2.config(command=self.treeview2.yview)
        self.treeview2.column("#0", anchor="center", width=120)
        self.treeview2.column(1, anchor="center", width=120)
        self.treeview2.column(2, anchor="center", width=120)


        self.treeview2.heading("#0", text="Day of week", anchor="center")
        self.treeview2.heading(1, text="Date", anchor="center")
        self.treeview2.heading(2, text="Time", anchor="center")

        self.hospitalLabel.grid(row=0,column=0,columnspan=2,sticky="EW")

        self.treeview.grid(row=1,column=0,columnspan=2,sticky="EW",pady=(10,10))
        self.scrollbar.grid(row=1, column=2, sticky="NS",pady=(10,10),padx=(0,10))

        self.doctorLabel.grid(row=0,column=4,sticky="EW")
        self.treeview1.grid(row=1,column=4,columnspan=2,sticky="EW")
        self.scrollbar1.grid(row=1, column=6, sticky="NS",pady=(10,10))

        self.appoinmentLabel.grid(row=2,column=0,columnspan=4,sticky="EW")
        self.treeview2.grid(row=3,column=0,columnspan=6,sticky="EW",pady=(10,10))
        self.scrollbar2.grid(row=3, column=6, sticky="NS",pady=(10,10))

        self.backButton.grid(row=4,column=1,sticky="EW")
        self.reserveButton.grid(row=4,column=4,sticky="EW")
class MessageFrame(ttk.Frame):
    def __init__(self,font,command):
        super().__init__()
        self.configure(border=True,borderwidth=30,relief="solid")
        self.labelVar=tk.StringVar()
        self.label=ttk.Label(self,textvariable=self.labelVar,anchor="center",font=font)
        self.label.grid(row=0,column=0,pady=(0,20))

        ttk.Style().configure('TButton', font=(font[0], 9))
        self.button = ttk.Button(self, text="Ok", command=command, style="TButton")
        self.button.grid(row=1,column=0)

class AdminFrame(ttk.Frame):
    def addHospital(self):
        name=self.nameVar.get()
        address=self.addressVar.get()
        Functions.addHospital(name,address)
        self.treeview.insert(parent="", index="end", text=name, values=(address))
    def deleteHospital(self):
        item=self.treeview.focus()
        Functions.deleteHospital(self.treeview.item(item)["text"])
        self.treeview.delete(item)

    def addDoctors(self,event):
        for item in self.treeview1.get_children():
            self.treeview1.delete(item)
        for doctor in Functions.GetDoctors(self.treeview.item(self.treeview.focus())["text"]):
            self.treeview1.insert(parent="",index="end",text=doctor.firstName+" "+doctor.lastName,values=(doctor.id))

    def deleteDoctor(self):
        item = self.treeview1.focus()
        Functions.deleteDoctor(self.treeview1.item(item)["values"][0])
        self.treeview1.delete(item)

    def deletePatient(self):
        item = self.treeview2.focus()
        Functions.deletePatient(self.treeview2.item(item)["values"][0])
        self.treeview2.delete(item)

    def __init__(self,font):
        super().__init__()
        self.font=font

        self.hospitals=[]
        self.doctors=[]
        self.patients=[]
        self.backButton = ttk.Button(self, text="Logout", command=Logout, style="TButton")


        self.hospitalFrame=ttk.Frame(self,borderwidth=5,relief="solid")

        self.hospitalsLabel=ttk.Label(self,font=self.font,text="Hospitals:",anchor="center")
        self.doctorsLabel=ttk.Label(self,font=self.font,text="Doctors:")
        self.patientsLabel=ttk.Label(self,font=self.font,text="Patient:")

        self.nameLabel=ttk.Label(self.hospitalFrame,font=self.font,text="Name:")
        self.addressLabel=ttk.Label(self.hospitalFrame,font=self.font,text="Address:")

        self.nameVar=tk.StringVar()
        self.addressVar=tk.StringVar()

        self.nameEntry=ttk.Entry(self.hospitalFrame,textvariable=self.nameVar)
        self.addressEntry=ttk.Entry(self.hospitalFrame,textvariable=self.addressVar,width=35)
        ttk.Style().configure('TButton', font=(self.font[0], 9))
        self.addButton = ttk.Button(self.hospitalFrame, text="Add Hospital", command=self.addHospital, style="TButton")
        self.deleteButtonHospital= ttk.Button(self, text="delete Hospital", command=self.deleteHospital, style="TButton")
        self.deleteButtonDoctor= ttk.Button(self, text="delete doctor", command=self.deleteDoctor, style="TButton")
        self.deleteButtonPatient= ttk.Button(self, text="delete patient", command=self.deletePatient, style="TButton")

        self.scrollbar = ttk.Scrollbar(self)
        self.scrollbar1 = ttk.Scrollbar(self)
        self.scrollbar2 = ttk.Scrollbar(self)

        self.treeview = ttk.Treeview(self, selectmode="browse", yscrollcommand=self.scrollbar.set, columns=(1),
                                     height=1)
        self.treeview.bind("<<TreeviewSelect>>", self.addDoctors)
        self.scrollbar.config(command=self.treeview.yview)
        self.treeview.column("#0", anchor="center", width=120)
        self.treeview.column(1, anchor="center", width=320)

        self.treeview.heading("#0", text="Name", anchor="center")
        self.treeview.heading(1, text="Address", anchor="center")


        for item in self.hospitals:
            self.treeview.insert(parent="", index="end", text=item.name, values=(item.address))
        self.treeview1 = ttk.Treeview(self, selectmode="browse", yscrollcommand=self.scrollbar1.set, columns=(1),
                                      height=1)


        self.scrollbar1.config(command=self.treeview1.yview)
        self.treeview1.column("#0", anchor="center", width=120)
        self.treeview1.column(1, anchor="center", width=120)


        self.treeview1.heading("#0", text="Name", anchor="center")
        self.treeview1.heading(1, text="National Id", anchor="center")

        self.treeview2 = ttk.Treeview(self, selectmode="browse", yscrollcommand=self.scrollbar2.set, columns=(1),
                                      height=1)
        self.scrollbar2.config(command=self.treeview2.yview)
        self.treeview2.column("#0", anchor="center", width=120)
        self.treeview2.column(1, anchor="center", width=120)


        self.treeview2.heading("#0", text="Name", anchor="center")
        self.treeview2.heading(1, text="Natinal Id", anchor="center")


        self.backButton.grid(row=0,column=0,sticky="W",pady=(0,3))
        self.nameLabel.grid(row=0,column=0)
        self.nameEntry.grid(row=0,column=1)
        self.addressLabel.grid(row=0,column=2)
        self.addressEntry.grid(row=0,column=3,columnspan=3)
        self.addButton.grid(row=0,column=6,padx=(10,5))

        self.hospitalFrame.grid(row=1,column=0)

        self.hospitalsLabel.grid(row=2,column=0)
        self.treeview.grid(row=3,column=0,sticky="EW")
        self.scrollbar.grid(row=3,column=2,sticky="NS")
        self.deleteButtonHospital.grid(row=4,column=0,pady=(9,0))

        self.doctorsLabel.grid(row=5,column=0)
        self.treeview1.grid(row=6,column=0,sticky="EW")
        self.scrollbar1.grid(row=6,column=2,sticky="NS")
        self.deleteButtonDoctor.grid(row=7,column=0,pady=(9,0))

        self.patientsLabel.grid(row=8, column=0)
        self.treeview2.grid(row=9, column=0, sticky="EW")
        self.scrollbar2.grid(row=9, column=2, sticky="NS")
        self.deleteButtonPatient.grid(row=10, column=0, pady=(9,0))
root=Root()

root.mainloop()