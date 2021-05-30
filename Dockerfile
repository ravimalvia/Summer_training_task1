FROM centos

RUN yum install python3 -y 
RUN pip3 install pandas numpy scikit-learn 

COPY Dataset/ /root/

CMD [ "python3", "/root/Ml.py" ]

