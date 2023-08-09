import numpy as np
import pandas as pd

class doctor():

    @staticmethod
    def read_file():
        "read data from xlsx file and return it as dataframe"
        df_doctor = pd.read_excel("doctor.xlsx")

        return df_doctor

    @staticmethod
    def add(id,firstName,lastName,age,number,username,password,gender,hospital,
                 proficiency,fromDay,toDay,fromTime,toTime):
        "add one row to the data frame and then save in xlsx file"
        new_row = {"id": int(id), "firstName": firstName,"lastName" : lastName, "age": age, "number": number,
                   "username": username,"password": password, "gender": gender,
                   "proficiency": proficiency, "hospital":hospital,"fromDay":fromDay,"toDay":toDay,"fromTime":fromTime,"toTime":toTime}

        df_doctor = pd.read_excel("doctor.xlsx")
        df_doctor = df_doctor.append(new_row, ignore_index=True)
        df_doctor.to_excel("doctor.xlsx",index = False , index_label= None)

    @staticmethod
    def delete(id):
        """
        df_doctor : dataframe pandas
        who : String (name of person you want to delete from data frame)

        delete row from data frame with name of a person and then save this change in xlsx file
        """
        df_doctor = pd.read_excel("doctor.xlsx")
        df_doctor.drop(np.where(df_doctor["id"] == id)[0][0], axis=0, inplace=True)
        df_doctor.to_excel("doctor.xlsx",index = False , index_label= None)


class patient():

    @staticmethod
    def read_file():
        "read data from xlsx file and return it as dataframe"
        df_patient = pd.read_excel("patient.xlsx")
        return df_patient

    @staticmethod
    def add(id,firstName,lastName,age,number,username,password,gender,
                insurance_id):
        "add one row to the data frame and then save in xlsx file"
        new_row = {"id": int(id), "firstName": firstName, "lastName" : lastName, "age": age, "number": number,
                    "username": username, "password": password, "gender": gender,
                    "insurance_id": insurance_id}
        df_patient = pd.read_excel("patient.xlsx")
        df_patient = df_patient.append(new_row, ignore_index=True)
        df_patient.to_excel("patient.xlsx",index = False , index_label= None)

    @staticmethod
    def delete(id):
        """
        df_patient : dataframe pandas
        who : String (name of person you want to delete from data frame)

        delete row from data frame with name of a person and then save this change in xlsx file
        """
        df_patient = pd.read_excel("patient.xlsx")
        df_patient.drop(np.where(df_patient["id"] == id)[0][0], axis=0, inplace=True)
        df_patient.to_excel("patient.xlsx",index = False , index_label= None)

class hospital:
    @staticmethod
    def read_file():
        "read data from xlsx file and return it as dataframe"
        df_hospital = pd.read_excel("hospital.xlsx")
        return df_hospital

    @staticmethod
    def add(name,address):
        "add one row to the data frame and then save in xlsx file"

        df_hospital = pd.read_excel("hospital.xlsx")
        new_row = {"name": name, "address" : address}
        df_hospital = df_hospital.append(new_row, ignore_index=True)
        df_hospital.to_excel("hospital.xlsx",index = False , index_label= None)


    @staticmethod
    def delete(who):
        """
        df_hospital : dataframe pandas
        who : String (name of person you want to delete from data frame)

        delete row from data frame with name of a person and then save this change in xlsx file
        """
        df_hospital = pd.read_excel("hospital.xlsx")
        df_hospital.drop(np.where(df_hospital["name"] == who)[0][0], axis=0, inplace=True)
        df_hospital.to_excel("hospital.xlsx",index = False , index_label= None)

class appointment:
    @staticmethod
    def read_file():
        "read data from xlsx file and return it as dataframe"
        df_appointment = pd.read_excel("appointment.xlsx")
        return df_appointment

    @staticmethod
    def add(hospital,patientName,patientId , doctor, date , time):
        "add one row to the data frame and then save in xlsx file"

        df_appointment = pd.read_excel("appointment.xlsx")
        new_row = {"hospital":hospital,"patientName":patientName,"patientID":patientId , "doctor":doctor, "date":date , "time":time}
        df_appointment = df_appointment.append(new_row, ignore_index=True)
        df_appointment["date"]=pd.to_datetime(df_appointment["date"])
        df_appointment.to_excel("appointment.xlsx",index = False , index_label= None)

    def Get_sort_appointment(doctor_name):
        df = pd.read_excel("appointment.xlsx")
        temp = df[df["doctor"] == doctor_name]
        temp.sort_values(by='date', inplace=True)
        return temp.values.tolist()