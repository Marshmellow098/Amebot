FROM Marshmellow098/amebot:latest

#clonning repo
RUN git clone https://github.com/Marshmellow098/amebot.git /root/amebot
#working directory 
WORKDIR /root/amebot

# Install requirements
RUN pip3 install -U -r requirements-startup.txt

ENV PATH="/home/amebot/bin:$PATH"

CMD ["python3","-m","amebot"]
