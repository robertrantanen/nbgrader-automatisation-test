# nbgrader semi-automatisation without jupyterhub

The file `students.txt` contains student ids, one id per line. The python file `students_to_db.py` puts all the student ids into the nbgrader database. If the student file is structured in different way then the python script can be altered.

The instructor should generate the assignment, either with nbgrader tool or with `nbgrader generate_assignment <name>` command. The assignments in `release`folder should then be distributed to students somehow, for example as a downloadable file.

The folder `returned` contains assignments that students have submitted with some system outside nbgrader. The contents of the folder should be structured as `student_id/assignment_name/notebook` because nbgrader requires this structure. 

The python file `autograde.py` first transfers all the contents of `returned` folder inside the nbgrader's `submitted` folder. Then the python code autogrades all the assignments and exports it into the `grades.csv` file.

A general problem with nbgrader is that it can't automatically grade assignments once a student submits them. The `autograde.py` code could be automated to run once every hour and then transfer the contens of `grades.csv`to some site that the students can access.


# Using python virtual environment for students

The students should have python3 installed. Next, inside assignment folder create virtual environment with `python3 -m venv venv`. Then it can be activated with `source venv/bin/activate` and deactivated with `deactivate`

The `requirements.txt` file includes the required dependencies. When inside virtual environment, install dependencies with `pip3 -r install requirements.txt`.

For our course the students will also have to run the following commands inside virtual env:  
`export PYSPARK_PYTHON=$VIRTUAL_ENV/bin/python3`  
`export SPARK_HOME=$VIRTUAL_ENV/lib/python3.6/site-packages/pyspark`

The problem is if a student has different python version than 3.6, they would have to find their own python version and modify the command. Using Python with windows or mac might also require different commands.

# Running notebooks with docker

Students don't need to install any Python dependencies if they use Docker images. Folder `dockertest` contains a Dockerfile for jupyter notebook and pyspark. When inside `dockertest`folder:

Run `docker build -t jupyter .` to create a docker image called `jupyter`

Run `docker run -p 8888:8888 -v $(pwd):/work jupyter` to run the docker image and reflect the changes on your directory.

The notebook doesn't open automatically, you have to click a link in the terminal that looks like http://127.0.0.1:8888/?token=xxxxx.

The docker image can possibly be released in dockerhub so that students only have to use the `docker run` command.
