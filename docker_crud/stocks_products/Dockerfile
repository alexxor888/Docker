FROM python

WORKDIR src

COPY . /src

#COPY ./requirements.txt /src/requirements.txt

RUN pip3 install --no-cache-dir --upgrade -r /src/requirements.txt

ENV MY_ENV=top_env

EXPOSE 8000

ENTRYPOINT ["./migrate_and_run.sh"]

#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]