# retroscores-django

This project is to build a website that is used to keep record of my highscores when playing old arcade games.

## Prerequisites

+ Python 3
+ Django 2.2
+ Pillow

## Execute 

    python manage.py runserver

## Ports

The website will then be accessible using port :8000 for example http://localhost:8000 

## Additional

As part of the DevOps with Docker course I am including a Dockerfile for easy deployment. This is my first Dockerfile of my own personal project.

Example to run

    docker run -d --name retroscores -p 8000:8000 digitalight/retroscores-django
