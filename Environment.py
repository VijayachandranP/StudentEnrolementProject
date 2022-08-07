

def TestEnvironment():
    PostUrl='http://localhost:9080/studentmgmt/addStudent'
    DeleteUrl='http://localhost:9080/studentmgmt/deleteStudent'
    PutUrl='http://localhost:9080/studentmgmt/updateStudent'
    Get1Url='http://localhost:9080/studentmgmt/fetchStudents?id='
    Get2Url='http://localhost:9080/studentmgmt/fetchStudents?studentsClass='
    return[PostUrl,DeleteUrl,PutUrl,Get1Url,Get2Url]