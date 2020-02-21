##Author: Kuang Sheng
from flask import Flask, escape, request

app = Flask(__name__)

DB = {"students": [],
    "classes": []}

studentId = 0
classId = 0
studentList = []
@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'


@app.route('/students', methods=['POST'])
def create_student():
    global studentId
    ##print(request.get_json())
    #typedName = input("please input the name of the student:")
    name = request.args.get("name", "typedName")

    DB["students"].append({"name": name, "ID": studentId})
    studentId = studentId + 1
    return DB["students"][-1]
    #for student in DB["students"]:
'''
    DB["students"].append({"id": "fix-me", "name": "fix-me"})
    DB["classes"].append({"name": "hello", "id" : "1234"})
'''


@app.route('/students/<idInfo>', methods = ['GET'])
def get_student(idInfo):

    for student in DB["students"]:
        if student["ID"] == int(idInfo):
            return student
    return "No such student found"
@app.route('/students/<idInfo>', methods = ['PUT'])
def put_student(idInfo):
    name = request.args.get("name", "typedName")
    #id = request.args.get("ID", 0)
    for student in DB["students"]:
        if name == student["name"]:
            student["ID"] = int(idInfo)
            return student
    DB["students"].append({"name": name, "ID": int(idInfo)})
    return DB["students"][-1]

@app.route('/classes', methods = ['POST'])
def create_class():
    global classId, studentList
    classname = request.args.get("name", "className")
    DB["classes"].append({"name": classname, "ID": classId, "students": studentList})
    classId = classId + 1
    return DB["classes"][-1]

@app.route('/classes/<classId>', methods = ['GET'])
def get_class(classId):
    for classes in DB["classes"]:
        if classes["ID"] == int(classId):
            return classes
    return "No such class found"

@app.route('/classes/<cId>', methods = ['PATCH'])
def add_student_to_class(cId):
    sName = ""
    sId = request.args.get("ID", "sIdt")

    for classes in DB["classes"]:
        if classes["ID"] == int(cId):
            for student in DB["students"]:
                if student["ID"] == int(sId):
                    sName = student["name"]
                    stuId = int(sId)
                    DB["classes"][0]["students"].append({"ID": stuId, "name": sName})
                    return classes
            return "No such student found"
        #return "Please add classes first"

@app.route('/students/printall', methods = ['GET'])
def getAll():
    return DB

#if __name__ == "__main__":
#    app.run(debug = True)
