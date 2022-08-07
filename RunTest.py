from Utilities import ExecuteTestScenario
import json
import pandas as pd
import time


def RunTest(TestCaseNumber):
    Response=ExecuteTestScenario(TestCaseNumber)

    try:
        ExpectedResponse=json.loads(Response[3])

    except:
        ExpectedResponse=Response[3]

    try:
        ActualResponse=json.loads(Response[1])
        try:
            ActualResponse.pop('timestamp')
            ActualResponse.pop('message')
        except:
            a=0
    except:
        ActualResponse=Response[1]
    if TestCaseNumber in [1,12,14,16,18]:
        if (ActualResponse==ExpectedResponse or ActualResponse=='') and (Response[2]==Response[4] or Response[2]==200):
            Result="TEST PASS"
        else:
            Result = "TEST FAIL"
    else:

        if ActualResponse==ExpectedResponse and Response[2]==Response[4]:
            Result="TEST PASS"
        else:
            Result = "TEST FAIL"

    # print (Response)
    # print(Result)
    df=Response[5]
    df['ActualResponse']=str(ActualResponse)
    df['ActualHttpCode']=Response[2]
    df['TestResult'] = Result

    return df




















if __name__== "__main__":

    TotalNumberOfTestCases=19
    count=0
    for i in range (1,TotalNumberOfTestCases+1,1): # Select this for running all tests
    # for i in [12,13,14,15,16,17,18,19]: # Enter Test Case numbers individually in list
        count=count+1
        # print (i)
        if count ==1:
            df_final=RunTest(i)
        else:
            df=RunTest(i)
            df_final=pd.concat([df_final,df], ignore_index=True)
    Time=round(time.time())
    filename="TestResults_{}.xlsx".format(Time)
    df_final.to_excel(filename,index=False)






