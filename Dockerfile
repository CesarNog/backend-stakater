FROM python:3.7

RUN mkdir /app
WORKDIR /app
ADD . /app/
RUN pip install --no-cache-dir --upgrade pip &&\
    pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt

EXPOSE 8080

ENTRYPOINT [ "python" ]

CMD ["/app/main.py"]