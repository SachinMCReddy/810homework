''' python program HW-09
Sachin MC Reddy'''
import datetime
import os
import unittest
from collections import defaultdict
from prettytable import PrettyTable

def file_reader(path, num_fields, seperator=',', header=False):
    a = open(path, 'r')
    with a:
        for i, line in enumerate(a):
            line_split = line.rstrip("\n")
            line_split = line_split.split(seperator)
            if len(line_split) != num_fields:
                raise ValueError(f"{path} line: {i+1}: read {len(line_split)} fields but expected {num_fields}")
            if header and i == 0 :
                continue
            yield tuple(line_split)


class Repository():

    def __init__(self, dir):
        print("Created instance of University class.")
        self.students = dict()
        self.instructors = dict()
        self.add_students(os.path.join(dir, "students.txt"))
        self.add_instructors(os.path.join(dir, "instructors.txt"))
        self.add_grades(os.path.join(dir, "grades.txt"))
        self.student_pt()
        self.instructor_pt()
        # self.print_stuff()

    
    def print_stuff(self):
        print("1.", self.instructors)


    def add_students(self, students_file_path):
        for cwid, name, major in file_reader(students_file_path, 3, "\t"):
            print(cwid, name, major, cwid not in self.students)
            # students_summary.append(Student(grade[0], ))
            if cwid not in self.students:
                # print("adding this:", cwid)
                self.students[cwid] = Student(cwid, name, major)
                print("New students dictionary:", self.students)


    def add_instructors(self, instructor_file_path):
        for cwid, name, department in file_reader(instructor_file_path, 3, "\t"):
            print(cwid, name, department)
            # students_summary.append(Student(grade[0], ))
            if cwid not in self.instructors:
                self.instructors[cwid] = Instructor(cwid, name, department)


    def add_grades(self, grades_file_path):
        for scwid, course, grade, icwid in file_reader(grades_file_path, 4, "\t"):
            self.students[scwid].add_course(course, grade)
            self.instructors[icwid].add_course(course)

        
    def student_pt(self):
        pt = PrettyTable(field_names=["CWID", "Name", "Completed Courses"])

        for student in self.students.values():
            pt.add_row(student.details())

        print(pt)


    def instructor_pt(self):
        pt = PrettyTable(field_names=["CWID", "Name", "Dept", "Course", "Students"])

        for instructor in self.instructors.values():
            for i in instructor.details():
                pt.add_row(i)

        print(pt)

class Student:
    def __init__(self,cwid,name,major):
        self.cwid = cwid
        self.name = name
        self.major = major
        self.course = dict()
    
    def add_course(self,course,grade):
        self.course[course] = grade

    def details(self):
        return[self.cwid,self.name,sorted(self.course.keys())]

    @staticmethod
    def fields():
        return['CWID','name','course']

    
class Instructor:
    def __init__(self,cwid,name,dept):
        self.cwid = cwid
        self.name = name
        self.dept = dept
        self.course = defaultdict(int)
    
    def add_course(self,course):
        self.course[course] += 1
    
    def details(self):
        for course,Student in self.course.items():
            yield[self.cwid,self.name,self.dept, course,Student]
    
    @staticmethod
    def fields():
        return["Cwid","name","dept","course","students"]

class RepositoryTest(unittest.TestCase):

    def test_init(self):
        directory_path = "/Users/sachinmcreddy/Desktop/pyhton"
        repo_1 = Repository(directory_path)
        repo_1_student_expected_dict = {'10103': ['10103', 'Baldwin, C', ['CS 501', 'SSW 564', 'SSW 567', 'SSW 687']], '10115': ['10115', 'Wyatt, X', ['CS 545', 'SSW 564', 'SSW 567', 'SSW 687']], '10172': ['10172', 'Forbes, I', ['SSW 555', 'SSW 567']], '10175': ['10175', 'Erickson, D', ['SSW 564', 'SSW 567', 'SSW 687']], '10183': ['10183', 'Chapman, O', ['SSW 689']], '11399': ['11399', 'Cordova, I', ['SSW 540']], '11461': ['11461', 'Wright, U', ['SYS 611', 'SYS 750', 'SYS 800']], '11658': ['11658', 'Kelly, P', ['SSW 540']], '11714': ['11714', 'Morton, A', ['SYS 611', 'SYS 645']], '11788': ['11788', 'Fuller, E', ['SSW 540']]}
        repo_1_student_result_dict = dict()


        for student_cwid, values in repo_1.students.items():
            repo_1_student_result_dict[student_cwid] = values.details()

        self.assertEqual(repo_1_student_expected_dict, repo_1_student_result_dict)
        


    
def main():
    re = Repository("/Users/sachinmcreddy/Desktop/pyhton")


if __name__ == '__main__':
    main()
