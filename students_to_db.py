from nbgrader.api import Gradebook
import os

course = 'test_course'

file =  '../students.txt'

os.chdir(course+'/')

with Gradebook('sqlite:///gradebook.db') as gb:
    with open(file) as f:
        for id in f.readlines():
            id = id.strip()
            id = id.strip("\n")
            try:
                gb.find_student(id)
            except:
                gb.add_student(id)

os.chdir('../')