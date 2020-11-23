FROM ubuntu:18.04


RUN apt-get update && apt-get install -y lib32z1 xinetd
RUN apt-get update && apt-get install -y python-dev python3-dev python-pip python3-pip

RUN useradd -m ctf

COPY ./bin/ /home/ctf/
COPY ./ctf.xinetd /etc/xinetd.d/ctf
COPY ./start.sh /start.sh
RUN echo "Blocked by ctf_xinetd" > /etc/banner_fail

RUN chmod +x /start.sh
RUN chown -R root:ctf /home/ctf
RUN chmod -R 750 /home/ctf
RUN chmod +x /home/ctf/serve.py
WORKDIR /home/ctf

CMD ["/start.sh"]

EXPOSE 9999
