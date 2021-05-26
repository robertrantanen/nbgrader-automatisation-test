import shutil
import os
from nbgrader.apps import NbGraderAPI

api = NbGraderAPI()

dir = 'returned/'

course = 'test_course'

submitted_dir = course+'/submitted/'

if os.path.exists(submitted_dir):
    shutil.rmtree(submitted_dir)

shutil.copytree(dir, submitted_dir)

os.chdir(course+'/')

assignments = api.get_source_assignments()

for assignment in assignments:
    os.system("nbgrader autograde '%s' --force" % assignment)

os.system("nbgrader export")

shutil.copy("grades.csv", "../grades.csv")

os.chdir('../')