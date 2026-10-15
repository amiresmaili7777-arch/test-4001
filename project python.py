import json
class Course:
    id:int=0
    name:str=""
    units:int=0
    score:float=0
    def __init__(self,id,name,units):
        self.id=id
        self.name=name
        self.units=units
    def __eq__(self,other):
        return self.id==other
    def __str__(self):
        return f"{self.id}\t{self.name}\t{self.units}"
class Student:
    id:int=0
    name:str=""
    family:str=""
    courses:list[Course]
    def __init__(self,id,name,family):
        self.id=id
        self.name=name
        self.family=family
        self.courses=[]
    def __eq__(self,other):
        if isinstance(other,Student):
            return self.id==other.id
        return self.id==other
    def __str__(self):
        return f"{self.id}\t{self.name}\t{self.family}"
    def show_info(self):
        print(f"id:{self.id}\nname:{self.name}\nfamily:{self.family}\ncourses:")
        print("id\tname\tunits\tscore")
        for detail in self.courses:
            print(f"{detail.id}\t{detail.name}\t{detail.units}\t{detail.score}")
    def add_course(self,course):
        if course not in self.courses:
            self.courses.append(course)
        else:
            print("this course already exist")
    def remove_course(self,course):
        if course not in self.courses:
            print("course doesnt exis")
        else:
            self.courses.remove(course)
    def set_score(self):
        print(f"id\tname\tunits\tscore")
        for detail in self.courses:
            print(f"{detail.id}\t{detail.name}\t{detail.units}\t{detail.score}")
        for name_course in self.courses:
            print(f"{name_course.name}:",end="")
            new_score=float(input())
            name_course.score=new_score
        

class Teacher:
    id:int=0
    name:str=""
    family:str=""
    grade:str=""
    courses:list[Course]
    def __init__(self,id,name,family,grade):
        self.id=id
        self.name=name
        self.family=family
        self.grade=grade
        self.courses=[]
    def __eq__(self,other):
        if isinstance(other,Teacher):
            return self.id==other.id
        return self.id==other
    def __str__(self):
        return f"{self.id}\t{self.name}\t{self.family}\t{self.grade}"
    def show_info(self):
        print(f"id:{self.id}\nname:{self.name} \nfamily:{self.family}\ngrade:{self.grade}\ncourses:")
        print(f"id\tname\tunits\tscore")
        for detail in self.courses:
            print(f"{detail.id}\t{detail.name}\t{detail.units}\t{detail.score}")
    def add_course(self,course):
        if course not in self.courses:
            self.courses.append(course)
        else:
            print("this course already exist")
    def remove_course(self,course):
        if course not in self.courses:
            print("course doesnt exis")
        else:
            self.courses.remove(course)
class Classroom:
    id:int=0
    name:str=""
    course:Course=None
    teacher:Teacher=None
    students:list[Student]
    def __init__(self,id,name):
        self.id=id
        self.name=name
        self.course=None
        self.teacher=None
        self.students=[]
    def __eq__(self,other):
        if isinstance(other,Classroom):
            return self.id==other.id
        return self.id==other
    def __str__(self):
        return f"{self.id}\t{self.name}\t{self.course.name}\t{self.teacher.name} {self.teacher.family}\t{len(self.students)}"
    def show_info(self):
        if self.teacher is not None:
            teacher_info=f"{self.teacher.name}{self.teacher.family}"
        else:
            teacher_info ="None"
        print(f"id:{self.id}\nname:{self.name} \ncourses:{self.course.name} \nteachers:{teacher_info}\nstudents:")  
        print(f"id\tname\tfamily")
        for detail in self.students:
            print(f"{detail.id}\t{detail.name}\t{detail.family}")
    def change_course(self,all_course):
        print("id\tname\tunits")
        for course in all_course:
            print(f"{course.id}\t{course.name}\t{course.units}")
        course_id=int(input("enter course id: "))
        selected_course=all_course[all_course.index(course_id)]
        self.course=selected_course
        if self.teacher!=None and selected_course not in self.teacher.courses:
            self.teacher=None
        valid_students=[]
        for student in self.students:
            if selected_course in student.courses:
                valid_students.append(student)
        self.students=valid_students
    def change_teacher(self,all_teacher):
        print("id\tname\tfamily\tgrade")
        for teacher in all_teacher:
            if self.course in teacher.courses:
                print(f"{teacher.id}\t{teacher.name}\t{teacher.family}\t{teacher.grade}")
        teacher_id=int(input("enter teacher id: "))
        selected_teacher=all_teacher[all_teacher.index(teacher_id)]
        self.teacher=selected_teacher
    def add_student(self,all_student):
        student_under_ten=[]
        for student in all_student:
            if self.course in student.courses:
                student_course=student.courses[student.courses.index(self.course)]
                if student_course.score<10 and student not in self.students:
                    student_under_ten.append(student)
        print("id\tname\tfamily")
        for student in student_under_ten:
            print(f"{student.id}\t{student.name}\t{student.family}")
        student_id=int(input("enter student id: "))
        selected_student=student_under_ten[student_under_ten.index(student_id)]
        self.students.append(selected_student)
    def remove_student(self):
        print("id\tname\tfamily")
        for student in self.students:
            print(f"{student.id}\t{student.name}\t{student.family}")
        student_id=int(input("enter student id: "))
        selected_student=self.students[self.students.index(student_id)]
        self.students.remove(selected_student)
    
class School:
    name:str=""
    students:list[Student]=[]
    teachers:list[Teacher]=[]
    courses:list[Course]=[]
    classrooms:list[Classroom]=[]
    selected_student:Student=None
    selected_teacher:Teacher=None
    selected_classroom:Classroom=None
    def __init__(self,name):
        self.name=name
    def add_classroom(self,classroom):
        if classroom not in self.classrooms:
            self.classrooms.append(classroom)
        else:
            print("classroom already exits")
    def add_student(self,student):
        if student not in self.students:
            self.students.append(student)
        else:
            print("student already exits")
    def add_teacher(self,teacher):
        if teacher not in self.teachers:
            self.teachers.append(teacher)
        else:
            print("teacher already exits")
    def add_course(self,course):
        if course not in self.courses:
            self.courses.append(course)
        else:
            print("course already exits")
        
    def remove_student(self,student):
        if student in [student for c in self.classrooms if student in c.students]:
            print("this student already use in classroom")
        else:
            if student in self.students:
                self.students.remove(student)
            else:
                print("student doesnt exits")
    def remove_teacher(self,teacher):
        if teacher in [c.teacher for c in self.classrooms]:
            print("this teacher already use in classroom")
        else:
            if teacher in self.teachers:
                self.teachers.remove(teacher)
            else:
                print("teacher doesnt exits")
    def remove_course(self,course):
        if course in [course for t in self.teachers if course in t.courses]:
            print("this course already use")
        elif course in [course for s in self.students if course in [c[0] for c in s.courses]]:
            print("this course already use")
        elif course in [course  for c in self.classrooms if course in c.courses]:
            print("this course already use")
        else:
            if course not in self.courses:
                print("course doesnt exits")
            else:
                self.courses.remove(course)
    def remove_classroom(self,classroom_id):
        if classroom_id not in self.classrooms:
            print("classroom doesnt exits")
        else:
            selected_classroom=self.classrooms[self.classrooms.index(classroom_id)]
            self.classrooms.remove(selected_classroom)
    def show_students(self):
        print("id\tname\tfamily")
        for student in self.students:
            print(student)

    def show_teachers(self):
        print("id\tname\tfamily\tgrade")
        for teacher in self.teachers:
            print(teacher)
    def show_courses(self):
        print("id\tname\tunits")
        for course in self.courses:
            print(course)
    def show_classroom(self):
        print("id\tname\tcourse\tteacher\t  students")
        for classroom in self.classrooms:
            print(classroom)
    def edit_student(self,id,name,family):
        if id in self.students:
            index=self.students.index(id)
            self.students[index].name=name
            self.students[index].family=family
        else:
            print("student doesnt exits")
    def edit_teacher(self,id,name,family,grade):
        if id in sc1.teacher:
            index=sc1.teacher.index(id)
            sc1.teacher[index].name=name
            sc1.teacher[index].family=family
            sc1.teacher[index].grade=grade
        else:
            print("teacher doesnt exits")
    def edit_courses(self,id,name,units):
        if id in sc1.courses:
            index=sc1.courses.index(id)
            sc1.courses[index].name=name
            sc1.courses[index].units=units
        else:
            print("course doesnt exits")
    def edit_classroom(self,id,name):
        if id not in self.classrooms:
            print("classroom doesnt exits")
        else:
            index=self.classrooms.index(id)
            self.classrooms[index].name=name
    def select_classroom(self,id):
        if id not in self.classrooms:
            print("classroom doesnt exis")
        else:
            index=self.classrooms.index(id)
            sc1.selected_classroom=self.classrooms[index]
    
        
    def load_data(self):
        f1=open("data4.json","rt")
        s=f1.read()
        data_jsons=json.loads(s)
        f1.close()
        for data_json in data_jsons["courses"]:
            course=Course(data_json["id"],data_json["name"],data_json["units"])
            self.courses.append(course)
        for data_json in data_jsons["students"]:
            st1=Student(data_json["id"],data_json["name"],data_json["family"])
            for raw_course in data_json["courses"]:
                    if raw_course[0] in self.courses:
                        load_course=self.courses[self.courses.index(raw_course[0])]
                        load_course=Course(load_course.id,load_course.name,load_course.units)
                        load_course.score=raw_course[1]
                        st1.courses.append(load_course)
            self.students.append(st1)
            
        for data_json in data_jsons["teachers"]:
            t1=Teacher(data_json["id"],data_json["name"],data_json["family"],data_json["grade"])  
            for course_id in data_json["courses"]:
                if course_id in self.courses:
                    load_course=self.courses[self.courses.index(course_id)]
                    t1.courses.append(load_course)
            self.teachers.append(t1)
        for data_json in data_jsons["classrooms"]:
            cl1=Classroom(data_json["id"],data_json["name"])
            if data_json["course"] in self.courses:
                cl1.course=self.courses[self.courses.index(data_json["course"])]
            if data_json["teacher"] in self.teachers:
                cl1.teacher=self.teachers[self.teachers.index(data_json["teacher"])]
            else:
                cl1.teacher=Teacher(None,None,None,None)
                    
            for classroom_student_id in data_json["students"]:
                if classroom_student_id in self.students:
                    cl1.students.append(self.students[self.students.index(classroom_student_id)])
            self.classrooms.append(cl1)
            
            

    def save_data(self):
        students=[]
        teachers=[]
        courses=[]
        classrooms=[]
        for student in self.students:
            json_student={
                "id":student.id,
                "name":student.name,
                "family":student.family,
                "courses":[[s.id,s.score]for s in student.courses]
                }
            students.append(json_student)
        for teacher in self.teachers:
            json_teacher={
                "id":teacher.id,
                "name":teacher.name,
                "family":teacher.family,
                "grade":teacher.grade,
                "courses":[s.id for s in teacher.courses]
                
                    }
            teachers.append(json_teacher)
        for course in self.courses:
            json_course={
                "id":course.id,
                "name":course.name,
                "units":course.units,
                "score":course.score
                    }
            courses.append(json_course)
        for classroom in self.classrooms:
            json_classroom={
                "id":classroom.id,
                "name":classroom.name,
                "course":classroom.course.id,
                "teacher":classroom.teacher.id,
                "students":[s.id for s in classroom.students]
                }
            classrooms.append(json_classroom)
        result={
            "students":students,
            "teachers":teachers,
            "courses":courses,
            "classrooms":classrooms
            }
        s=json.dumps(result)
        f1=open("data4.json","wt")
        f1.write(s)
        f1.close()
                
            
        

sc1=School("sama")
sc1.load_data()
level="root"
while True:
    if level=="root":
        print("1.students")
        print("2.teachers")
        print("3.courses")
        print("4.classrooms")
        print("5.save")
        print("0.exit")
        cmd=int(input("choose your option:"))
        if cmd==1:
            level="students"
        elif cmd==2:
            level="teachers"
        elif cmd==3:
            level="courses"
        elif cmd==4:
            level="classroom"
        elif cmd==5:
            sc1.save_data()
        elif cmd==0:
            break
    elif level=="students":
        print("1.show student")
        print("2.add student")
        print("3.edit student")
        print("4.delete student")
        print("5.select student")
        print("0.back")
        cmd=int(input("choose your option:"))
        if cmd==1:
            sc1.show_students()
        elif cmd==2:
            id=int(input("id:"))
            name=input("name:")
            family=input("family:")
            s1=Student(id,name,family)
            sc1.add_student(s1)
        elif cmd==3:
            id=int(input("id:"))
            name=input("name:")
            family=input("family:")
            sc1.edit_student(id,name,family)
        elif cmd==4:
            id=int(input("id:"))
            sc1.remove_student(id)
        elif cmd==5:
            sc1.show_students()
            student_id=int(input("enter student id:"))
            if student_id not in sc1.students:
                print("student doesnt exis")
            else:
                index=sc1.students.index(student_id)
                sc1.selected_student=sc1.students[index]
            level="select student"
        elif cmd==0:
            level="root"
    elif level=="select student":
        print("1.info")
        print("2.add course")
        print("3.delete course")
        print("4.set scores")
        print("0.back")
        cmd=int(input("choose your option:"))
        if cmd==1:
            sc1.selected_student.show_info()
        elif cmd==2:
            print(f"id\tname\tunits")
            for course in sc1.courses:
                if course not in sc1.selected_student.courses:
                    print(course)
            course_id=int(input("enter course id:"))
            if course_id not in sc1.courses:
                print("course doesnt exis")
            else:
                index=sc1.courses.index(course_id)
                selected_course=sc1.courses[index]
                sc1.selected_student.add_course(selected_course)
        elif cmd==3:
            print(f"id\tname\tunits\tscore")
            for detail in sc1.selected_student.courses:
                print(f"{detail.id}\t{detail.name}\t{detail.units}\t{detail.score}")
            course_id=int(input("enter course id:"))
            if course_id not in sc1.courses:
                print("course doesnt exis")
            else:
                selected_course=sc1.courses[sc1.courses.index(course_id)]
                sc1.selected_student.remove_course(selected_course)
        elif cmd==4:
            sc1.selected_student.set_score()
        elif cmd==0:
            level="students"
    elif level=="teachers":
        print("1.show teacher")
        print("2.add teacher")
        print("3.edit teacher")
        print("4.delete teacher")
        print("5.select teacher")
        print("0.back")
        cmd=int(input("choose your option:"))
        if cmd==1:
            sc1.show_teachers()
        elif cmd==2:
            id=int(input("id:"))
            name=input("name:")
            family=input("family:")
            grade=input("grade:")
            t1=Teacher(id,name,family,grade)
            sc1.add_teacher(t1)
        elif cmd==3:
            id=int(input("id:"))
            name=input("name:")
            family=input("family:")
            grade=input("grade:")
            if id in sc1.teachers:
                index=sc1.teachers.index(id)
                sc1.teachers[index].name=name
                sc1.teachers[index].family=family
                sc1.teachers[index].grade=grade
        elif cmd==4:
            id=int(input("id:"))
            sc1.remove_teacher(id)
        elif cmd==5:
            sc1.show_teachers()
            teacher_id=int(input("enter teacher id:"))
            if teacher_id not in sc1.teachers:
                print("teacher doesnt exis")
            else:
                index=sc1.teachers.index(teacher_id)
                sc1.selected_teacher=sc1.teachers[index]
            level="select teachers"
        elif cmd==0:
            level="root"
    elif level=="select teachers":
        print("1.info")
        print("2.add course")
        print("3.delete course")
        print("0.back")
        cmd=int(input("choose your option:"))
        if cmd==1:
            sc1.selected_teacher.show_info()
        elif cmd==2:
            print(f"id\tname\tunits")
            for course in sc1.courses:
                if course not in sc1.selected_teacher.courses:
                    print(course)
            course_id=int(input("enter course id:"))
            if course_id not in sc1.courses:
                print("course doesnt exis")
            else:
                index=sc1.courses.index(course_id)
                selected_course=sc1.courses[index]
                sc1.selected_teacher.add_course(selected_course)
        elif cmd==3:
            print(f"id\tname\tunits\tscore")
            for detail in sc1.selected_teacher.courses:
                print(f"{detail.id}\t{detail.name}\t{detail.units}\t{detail.score}")
            course_id=int(input("enter course id:"))
            if course_id not in sc1.selected_teacher.courses:
                print("course doesnt exis")
            else:
                selected_course=sc1.selected_teacher.courses[sc1.selected_teacher.courses.index(course_id)]
                sc1.selected_teacher.remove_course(selected_course)
        elif cmd==0:
            level="teachers"
    elif level=="courses":
        print("1.show courses")
        print("2.add courses")
        print("3.edit courses")
        print("4.delete courses")
        print("0.back")
        cmd=int(input("choose your option:"))
        if cmd==1:
            sc1.show_courses()
        elif cmd==2:
            id=int(input("id:"))
            name=input("name:")
            units=int(input("units:"))
            c1=Course(id,name,units)
            sc1.add_course(c1)
        elif cmd==3:
            id=int(input("id:"))
            name=input("name:")
            units=input("units:")
            if id in sc1.courses:
                index=sc1.courses.index(id)
                sc1.courses[index].name=name
                sc1.courses[index].units=units
        elif cmd==4:
            id=int(input("id:"))
            sc1.remove_course(id)
        elif cmd==5:
            pass
        elif cmd==0:
            level="root"
    elif level=="classroom":
        print("1.show classrooms")
        print("2.add classrooms")
        print("3.edit classrooms")
        print("4.delete classrooms")
        print("5.select classrooms")
        print("0.back")
        cmd=int(input("choose your option:"))
        if cmd==1:
            sc1.show_classroom()
        elif cmd==2:
            id=int(input("id:"))
            name=input("name:")
            c1=Classroom(id,name)
            print(f"id\tname\tunits\tscore")
            for detail in sc1.courses:
                print(f"{detail.id}\t{detail.name}\t{detail.units}\t{detail.score}")
            id_course=int(input("course:"))
            selected_course=sc1.courses[sc1.courses.index(id_course)]
            c1.course=selected_course
            print(f"id\tname\tfamily\tgrade")
            for teacher in sc1.teachers:
                if selected_course in teacher.courses:
                    print(f"{teacher.id}\t{teacher.name}\t{teacher.family}\t{teacher.grade}")
            teacher_id=int(input("teacher:"))
            selected_teacher=sc1.teachers[sc1.teachers.index(teacher_id)]
            c1.teacher=selected_teacher
            student_under_ten=[]
            for student in sc1.students:
                if selected_course in student.courses:
                    student_course=student.courses[student.courses.index(selected_course)]
                    if student_course.score<10:
                        student_under_ten.append(student)
            if not  student_under_ten:
                pass
            else:
                while True:
                    print(f"id\tname\tfamily")
                    for student in student_under_ten:
                        print(f"{student.id}\t{student.name}\t{student.family}")
                    student_id=int(input("enter student id:"))
                    if student_id==0:
                        break
                    student_select_under_ten=student_under_ten[student_under_ten.index(student_id)]
                    c1.students.append(student_select_under_ten)
                    student_under_ten.remove(student_select_under_ten)
            sc1.add_classroom(c1)
        elif cmd==3:
           print(f"id\tname\tcourse\tteacher\tstudent")
           for detail in sc1.classrooms:
                print(f"{detail.id}\t{detail.name}\t{detail.course.name}\t{None if detail.teacher==None else detail.teacher.name} {None if detail.teacher==None else detail.teacher.family}\t{len(detail.students)}")
           classroom_id=int(input("enter classroom id:"))
           classroom_name=input("enter classroom name:")
           sc1.edit_classroom(classroom_id,classroom_name)
        elif cmd==4:
            print(f"id\tname\tcourse\tteacher\tstudent")
            for detail in sc1.classrooms:
                print(f"{detail.id}\t{detail.name}\t{detail.course.name}\t{None if detail.teacher==None else detail.teacher.name} {None if detail.teacher==None else detail.teacher.family}\t{len(detail.students)}")
            classroom_id=int(input("enter classroom id:"))
            sc1.remove_classroom(classroom_id)
        elif cmd==5:
            sc1.show_classroom()
            classroom_id=int(input("enter classroom id:"))
            sc1.select_classroom(classroom_id)
            level="select classroom"
        elif cmd==0:
            level="root"
    elif level=="select classroom":
        print("1.show info")
        print("2.change teacher")
        print("3.change course")
        print("4.add student")
        print("5.remove student")
        print("0.back")
        cmd=int(input("choose your option:"))
        if cmd==1:
            if sc1.selected_classroom.teacher is not None:
                teacher_info=f"{sc1.selected_classroom.teacher.name}{sc1.selected_classroom.teacher.family}"
            else:
                teacher_info ="None"
            print(f"id:{sc1.selected_classroom.id}\nname:{sc1.selected_classroom.name} \ncourses:{sc1.selected_classroom.course.name} \nteachers:{teacher_info}\nstudents:")  
            print(f"id\tname\tfamily")
            for detail in sc1.selected_classroom.students:
                print(f"{detail.id}\t{detail.name}\t{detail.family}")
        elif cmd==2:
            print("id\tname\tfamily\tgrade")
            for teacher in sc1.teachers:
                if sc1.selected_classroom.course in teacher.courses:
                    print(f"{teacher.id}\t{teacher.name}\t{teacher.family}\t{teacher.grade}")
            teacher_id=int(input("enter teacher id: "))
            selected_teacher=sc1.teachers[sc1.teachers.index(teacher_id)]
            sc1.selected_classroom.teacher=selected_teacher
        elif cmd==3:
            print("id\tname\tunits")
            for course in sc1.courses:
                print(f"{course.id}\t{course.name}\t{course.units}")
            course_id=int(input("enter course id: "))
            selected_course=sc1.courses[sc1.courses.index(course_id)]
            sc1.selected_classroom.course=selected_course
            if selected_course not in sc1.selected_classroom.teacher.courses:
                sc1.selected_classroom.teacher=None
                if sc1.selected_classroom.teacher is not None:
                    teacher_info=f"{sc1.selected_classroom.teacher.name}{sc1.selected_classroom.teacher.family}"
                else:
                    teacher_info ="None"
                print(f"id:{sc1.selected_classroom.id}\nname:{sc1.selected_classroom.name} \ncourses:{sc1.selected_classroom.course.name} \nteachers:{teacher_info}\nstudents:")  
                print(f"id\tname\tfamily")
                for detail in sc1.selected_classroom.students:
                    print(f"{detail.id}\t{detail.name}\t{detail.family}")
            valid_students=[]
            for student in sc1.students:
                if selected_course in student.courses:
                    valid_students.append(student)
            sc1.selected_classroom.students=valid_students
        elif cmd==4:
            student_under_ten=[]
            for student in sc1.students:
                if sc1.selected_classroom.course in student.courses:
                    student_course=student.courses[student.courses.index(sc1.selected_classroom.course)]
                    if student_course.score<10 and student not in sc1.selected_classroom.students:
                        student_under_ten.append(student)
            print("id\tname\tfamily")
            for student in student_under_ten:
                print(f"{student.id}\t{student.name}\t{student.family}")
            student_id=int(input("enter student id: "))
            selected_student=student_under_ten[student_under_ten.index(student_id)]
            sc1.selected_classroom.students.append(selected_student)
        elif cmd==5:
            print("id\tname\tfamily")
            for student in sc1.selected_classroom.students:
                print(f"{student.id}\t{student.name}\t{student.family}")
            student_id=int(input("enter student id: "))
            selected_student=sc1.selected_classroom.students[sc1.selected_classroom.students.index(student_id)]
            sc1.selected_classroom.students.remove(selected_student)
        elif cmd==0:
            level="classroom"
