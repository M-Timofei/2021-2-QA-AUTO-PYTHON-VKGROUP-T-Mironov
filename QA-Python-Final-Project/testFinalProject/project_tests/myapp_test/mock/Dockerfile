FROM python:3.8

ADD requirements.txt /requirements.txt

RUN pip3 install -r /requirements.txt && rm -f /requirements.txt

WORKDIR /mockdir

ADD . mock

ENTRYPOINT ["python3", "mock/vk_mock.py"]

EXPOSE 5000