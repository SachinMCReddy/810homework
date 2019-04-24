import os
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World! this is flask"

@app.route('/Goodbye')
def see_ya():
    return "See you later!"

@app.route('/sample_template')
def tempelate_demo():
    return render_template('para.html', 
    title= "Stevens Repository",
    my_header= "My Stevens Repository",
    my_param="My custom parameter")   

@app.route('/students')
def students_summary():
    students = [
        { 'cwid' : '11658',
          'name' : 'Kelly, P',
          'major' : 'SYEN',
          'taken' : ['SSW 540'],
          'remain' : ['SYS 612', 'SYS 671', 'SYS 672' 'SYS 673' 'SYS 674' 'SYS 800']
        },
        {
          'cwid' : '11714',
          'name' : 'Morton, A',
          'major' : 'SYEN',
          'taken' : ['SSW 611' 'SYS 645'],
          'remain' : ['SYS 612', 'SYS 671', 'SYS 672' 'SYS 673' 'SYS 674' 'SYS 800']   
        }
    ]
    return render_template('student_table.html',
                title='Stevens Repository', 
                table_title='student Summary',
                students=students)

import sqlite3

@app.route('/student_courses')
def student_courses():
  DB_FILE = "/Users/sachinmcreddy/Desktop/pyhton/HW11.db"
  db = sqlite3.connect(DB_FILE)
  query = '''select CWID,Name,Dept,Course, count(*) as students from HW11_instructors as i join HW11_grades
            on Instructor_CWID = CWID
            group by CWID,Name,Dept,Course'''

  db = sqlite3.connect(DB_FILE)
  results = db.execute(query)
#convert the query

  data = [{'cwid': cwid, 'name': name, 'Dept': Dept, 'Course': Course, 'students': students}
        for cwid, name, Dept, Course, students in results]
  db.close()

  return render_template('students_courses.html',
            title='Stevens Repository',
            table_title="Number of completed courses by Students",
            students=data)                      
app.run(debug=True)
