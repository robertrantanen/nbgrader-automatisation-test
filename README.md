# nbgrader semi-automatisation without jupyterhub

The file `students.txt` contains student ids, one id per line. The python file `students_to_db.py` puts all the student ids into the nbgrader database. If the student file is structured in different way then the python script can be altered.

The instructor should generate the assignment, either with nbgrader tool or with `nbgrader generate_assignment <name>` command. The assignments in `release`folder should then be distributed to students somehow, for example as a downloadable file.

The folder `returned` contains assignments that students have submitted with some system outside nbgrader. The contents of the folder should be structured as `student_id/assignment_name/notebook` because nbgrader requires this structure. 

The python file `autograde.py` first transfers all the contents of `returned` folder inside the nbgrader's `submitted` folder. Then the python code autogrades all the assignments and exports it into the `grades.csv` file.

A general problem with nbgrader is that it can't automatically grade assignments once a student submits them. The `autograde.py` code could be automated to run once every hour and then transfer the contens of `grades.csv`to some site that the students can access.
