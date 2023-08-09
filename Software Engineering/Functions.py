import Database
from datetime import datetime
from datetime import timedelta
class User:

    def __init__(self,id,firstName,lastName,age,number,username,password,gender):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.number = number
        self.username = username
        self.password = password
        self.gender = gender


class Doctor(User):
    def __init__(self,id,firstName,lastName,age,number,username,password,gender,hospital,
                 proficiency,fromDay,toDay,fromTime,toTime):
        super().__init__(id,firstName,lastName,age,number,username,password,gender)
        self.hospital=hospital
        self.proficiency = proficiency
        self.fromDay=fromDay
        self.toDay=toDay
        self.fromTime=fromTime
        self.toTime=toTime
class P(User):
    def __init__(self,id,firstName,lastName,age,number,username,password,gender,insurance_id):

        super().__init__(id,firstName,lastName,age,number,username,password,gender)
        self.ins_id = insurance_id
class Patient(User):
    def __int__(self,id,firstName,lastName,age,number,username,password,gender,insurance_id):
        super().__init__(id,firstName,lastName,age,number,username,password,gender)


class Hospital:
    def __init__(self,name,address):
        self.name = name
        self.address = address

class Appointment:
    def __init__(self,hospital,patientName,patientId,doctor,date,time):
        self.hospital=hospital
        self.patientName=patientName
        self.patientId=patientId
        self.doctor=doctor
        self.date=date
        self.time=time


def CheckLogin(username,password,userMode):
    try:

        if userMode=="Patient":
            dfOfPatients=Database.patient.read_file()
            patient = dfOfPatients[dfOfPatients["username"] == username].values.tolist()
            patient=patient[0]
            if patient[5]==username and str(patient[6])==password:
                p = P(patient[0], patient[1], patient[2], patient[3]
                            , patient[4], patient[5], patient[6], patient[7],patient[8])
                return p

        elif userMode=="Doctor":
            dfOfDoctor = Database.doctor.read_file()
            doctor=dfOfDoctor[dfOfDoctor["username"]==username].values.tolist()
            doctor=doctor[0]
            if doctor[5] == username and str(doctor[6]) == str(password):
                d=Doctor(doctor[0],doctor[1],doctor[2],doctor[3]
                         ,doctor[4],doctor[5],doctor[6],doctor[7],doctor[8],
                         doctor[9],doctor[10],doctor[11],doctor[12],doctor[13])
                return d
        return "Wrong Username or Password "
    except:
        return "Wrong Username or Password "


def GetDoctors(hospital):
    dfOfDoctor = Database.doctor.read_file()
    lis=dfOfDoctor[dfOfDoctor["hospital"]==hospital].values.tolist()
    lis1=[]
    for doctor in lis:
       lis1.append( Doctor(doctor[0],doctor[1],doctor[2],doctor[3],doctor[4],doctor[5],doctor[6],doctor[7]
                           ,doctor[8],doctor[9],doctor[10],doctor[11],doctor[12],doctor[13]))
    return lis1
def GetPatiensts():
    dfOfpatient = Database.patient.read_file()
    lis = dfOfpatient.values.tolist()
    listofPatients = []
    for patient in lis:
        listofPatients.append(
            P(patient[0], patient[1], patient[2], patient[3], patient[4], patient[5], patient[6], patient[7],
                    patient[8]))
    return listofPatients
def GetHospitals():
    HospitalList=Database.hospital.read_file().values.tolist()
    hospitals=[]
    for hospital in HospitalList:
        hospitals.append(Hospital(hospital[0],hospital[1]))
    return hospitals

def GetAppoinmentsPatient(patinetId):
    dfOfAppoinments=Database.appointment.read_file()
    lis=dfOfAppoinments[dfOfAppoinments["patientID"] == patinetId].values.tolist()
    listOfApp=[]
    for a in lis:
        listOfApp.append(Appointment(a[0],a[1],a[2],a[3],a[4],a[5]))
    return listOfApp

def GetAppoinmentsDoctor(doctorName):
    data=Database.appointment.Get_sort_appointment(doctorName)
    lis=[]
    for d in data:
        lis.append(Appointment(d[0],d[1],d[2],d[3],d[4],d[5]))
    return lis
def addAppoinement(hospital,patientName,patientId,doctor,date,time):
    Database.appointment.add(hospital,patientName,patientId,doctor,date,time)


def addDoctor(id,firstName,lastName,age,number,username,password,gender,hospital,
                 proficiency,fromDay,toDay,fromTime,toTime):

    Database.doctor.add(id,firstName,lastName,age,number,username,password,gender,hospital,
                 proficiency,fromDay,toDay,fromTime,toTime)


def addHospital(name,adress):
    Database.hospital.add(name,adress)

def addPatient(id,firstName,lastName,age,number,username,password,gender,
                insurance_id):
    Database.patient.add(id,firstName,lastName,age,number,username,password,gender,
                insurance_id)

def deleteDoctor(id):
    Database.doctor.delete(id)

def deleteHospital(name):
    Database.hospital.delete(name)

def deletePatient(NationalId):
    Database.patient.delete(NationalId)

def CreateAppoinments(doctor,hospital,patientId,patientName):
    lis=[]
    try:
        doctors=GetDoctors(hospital)
        for d in doctors:
            if d.firstName+" "+d.lastName==doctor:
                doctor=d
        weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        fromIndex = weekdays.index(doctor.fromDay)
        toIndex = weekdays.index(doctor.toDay)
        days = []
        if toIndex <= fromIndex:
            for i in range(toIndex + 1, fromIndex):
                days.append(i)
        else:
            for i in range(fromIndex, toIndex + 1):
                days.append(i)

        tommorow = datetime.today() + timedelta(days=0)
        for i in range(20):
            if toIndex <= fromIndex:
                tommorow = tommorow + timedelta(days=1)
                if tommorow.weekday() not in days:
                    lis.append(Appointment(hospital,patientName,patientId,doctor,str(tommorow).split(" ")[0],doctor.fromTime))
            else:
                tommorow = tommorow + timedelta(days=1)
                if tommorow.weekday() in days:
                    lis.append(
                        Appointment(hospital, patientName, patientId, doctor, str(tommorow).split(" ")[0], doctor.fromTime))
        return lis
    except:
        return lis
        pass

