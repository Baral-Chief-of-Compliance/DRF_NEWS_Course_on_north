FROM python:3.9.6

RUN mkdir wd

WORKDIR wd 

COPY . .


RUN pip install --no-cache-dir -r requirements.txt

CMD ["gunicorn","-b 0.0.0.0:8001", "admin_panel.wsgi:application"]

EXPOSE 8001