FROM python:latest
WORKDIR C:\Users\src\app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["Web_API_Address_to_State.py"]
ENTRYPOINT ["python3"]