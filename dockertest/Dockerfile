From jupyter/pyspark-notebook:5197709e9f23

USER root

RUN pip3 install graphframes && \
wget http://repos.spark-packages.org/graphframes/graphframes/0.8.0-spark3.0-s_2.12/graphframes-0.8.0-spark3.0-s_2.12.jar -qO $SPARK_HOME/jars/graphframes.jar

RUN pip3 install nbgrader && \
jupyter nbextension install --sys-prefix --py nbgrader --overwrite && \
jupyter nbextension enable --sys-prefix --py nbgrader && \
jupyter serverextension enable --sys-prefix --py nbgrader && \
jupyter nbextension disable --sys-prefix assignment_list/main --section=tree && \
jupyter serverextension disable --sys-prefix nbgrader.server_extensions.assignment_list && \
jupyter nbextension disable --sys-prefix create_assignment/main && \
jupyter nbextension disable --sys-prefix formgrader/main --section=tree && \
jupyter serverextension disable --sys-prefix nbgrader.server_extensions.formgrader && \
jupyter nbextension disable --sys-prefix course_list/main --section=tree && \
jupyter serverextension disable --sys-prefix nbgrader.server_extensions.course_list

RUN apt-get -y update && apt-get -y install git

RUN git clone https://github.com/robertrantanen/jupyter_submit_extension

RUN jupyter nbextension install jupyter_submit_extension --user

RUN jupyter nbextension enable jupyter_submit_extension/main

RUN rm -rf jupyter_submit_extension

COPY . /work

WORKDIR /work

CMD ["jupyter", "notebook", "--port=8888", "--ip=0.0.0.0", "--allow-root", "--no-browser", "--NotebookApp.token=''"]