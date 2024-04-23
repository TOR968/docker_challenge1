FROM python:3.9-slim

# Copying requirements file and installing dependencies
COPY . .

RUN pip3 install -r requirements.txt

# Setting the default command to run the application
CMD ["python", "app.py"]