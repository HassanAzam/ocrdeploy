FROM python:3.5.2

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app
COPY requirement.txt ./
RUN pip install --upgrade pip
RUN pip	 install -r requirement.txt
COPY . .
CMD [ "python", "manage.py", "migrate", "--noinput" ]
CMD [ "python", "manage.py", "runserver" ]
