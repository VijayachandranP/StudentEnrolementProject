import pandas as pd
import requests
import json
from Environment import TestEnvironment







def ExecuteTestScenario(TestCaseNumber):
    pd.set_option('max_columns', None)
    pd.set_option('expand_frame_repr',False)
    df = pd.read_excel("StudentAppTestCases.xlsx",sheet_name="POSTTestCases",engine='openpyxl')
    df=df.loc[(df['TestCaseNumber']==TestCaseNumber)]
    df.index=range(len(df))

    if str(df.at[0,'httpMethod']).strip()=="POST":

        id = str(df.at[0, "id"])
        Count=0

        try:
            id=float(id)
            Count=Count+1
        except:
            a=0
        if Count==1:
            if 0<float(str(df.at[0, "id"]))%1<1:
                id=float(str(df.at[0, "id"]))
            else:
                id = int(float(str(df.at[0, "id"])))

        firstName = df.at[0, "firstName"]
        lastName = df.at[0, "lastName"]
        studentClass = df.at[0, "studentClass"]
        nationality=df.at[0, "nationality"]
        payload={"id":id,"firstName":firstName,"lastName":lastName,"studentClass":studentClass,"nationality":nationality}
        # Url='http://localhost:9080/studentmgmt/addStudent'
        Url = TestEnvironment()[0]
        response= requests.post(Url,json=payload)
        response.text

        return [str(df.at[0,'httpMethod']).strip(),response.text,response.status_code,df.at[0, "ExpectedResponse"],df.at[0, "ExpectedHttpCode"],df]

    elif str(df.at[0,'httpMethod']).strip()=="DELETE":

        id = str(df.at[0, "id"])
        if int(float(str(df.at[0, "id"])))%1==0:
            id=int(float(str(df.at[0, "id"])))
        payload={"id":id}
        # Url='http://localhost:9080/studentmgmt/deleteStudent'
        Url = TestEnvironment()[1]
        response= requests.delete(Url,json=payload)

        return [str(df.at[0,'httpMethod']).strip(),response.text,response.status_code,df.at[0, "ExpectedResponse"],df.at[0, "ExpectedHttpCode"],df]

    elif str(df.at[0,'httpMethod']).strip()=="PUT":

        id = str(df.at[0, "id"])
        if int(float(str(df.at[0, "id"])))%1==0:
            id=int(float(str(df.at[0, "id"])))
        firstName = df.at[0, "firstName"]
        lastName = df.at[0, "lastName"]
        studentClass = df.at[0, "studentClass"]
        nationality=df.at[0, "nationality"]
        payload={"id":id,"firstName":firstName,"lastName":lastName,"studentClass":studentClass,"nationality":nationality}
        Url='http://localhost:9080/studentmgmt/updateStudent'
        Url = TestEnvironment()[2]
        response= requests.put(Url,json=payload)

        return [str(df.at[0,'httpMethod']).strip(),response.text,response.status_code,df.at[0, "ExpectedResponse"],df.at[0, "ExpectedHttpCode"],df]

    elif str(df.at[0,'httpMethod']).strip()=="GET1":

        id = str(df.at[0, "id"])
        if int(float(str(df.at[0, "id"])))%1==0:
            id=int(float(str(df.at[0, "id"])))
        payload={"id":id}
        Url='http://localhost:9080/studentmgmt/fetchStudents?id={}'.format(id)
        Url = TestEnvironment()[3]+'{}'.format(id)
        response= requests.get(Url)

        return [str(df.at[0,'httpMethod']).strip(),response.text,response.status_code,df.at[0, "ExpectedResponse"],df.at[0, "ExpectedHttpCode"],df]

    elif str(df.at[0,'httpMethod']).strip()=="GET2":

        studentClass = str(df.at[0, "studentClass"])
        # Url='http://localhost:9080/studentmgmt/fetchStudents?studentsClass={}'.format(studentClass)
        Url = TestEnvironment()[4]+'{}'.format(studentClass)
        response= requests.get(Url)

        return [str(df.at[0,'httpMethod']).strip(),response.text,response.status_code,df.at[0, "ExpectedResponse"],df.at[0, "ExpectedHttpCode"],df]








if __name__== "__main__":



    print(ReadPostTestScenario(1))