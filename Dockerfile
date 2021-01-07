FROM Marshmellow098/Amebot:latest

#clonning repo 
RUN git clone https://github.com/Marshmellow098/Amebot.git /root/amebot
#working directory 
WORKDIR /root/userbot

# Install requirements
RUN pip3 install -U -r requirements.txt

ENV PATH="/home/userbot/bin:$PATH"

CMD ["python3","-m","amebot"]
