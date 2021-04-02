FROM python:3.7

COPY ../requirements.txt

RUN pip3 install

COPY . .

EXPOSE 5500

ENTRYPOINT ["python", "app.py"]