FROM python 
WORKDIR /app
COPY ./requirements.txt /app
RUN pip install --upgrade -r requirements.txt 
COPY . /app 
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]
EXPOSE 8000