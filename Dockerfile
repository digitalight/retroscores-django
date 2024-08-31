#Based on Python image
FROM python:3.8
# Expose and set working dir
EXPOSE 8000
WORKDIR /usr/src/app
# Copy source files
COPY . .
# Install Django and Pillow
RUN pip install django==2.2.28
RUN pip install pillow==7.2.0
# Run migration
RUN python manage.py migrate
# Run the server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
