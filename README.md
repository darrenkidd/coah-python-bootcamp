# City on a Hill Python Bootcamp

A fun introduction to the joys of programming with Python 3. No planking.

![Python Logo](https://www.python.org/static/community_logos/python-logo-generic.svg)
![repl.it Logo](https://cdn.freebiesupply.com/logos/large/2x/replit-logo-png-transparent.png)

## Importing into repl.it

We will be using [repl.it](https://repl.it/) as our coding platform. It's free,
and you don't have to install anything on your computer. This makes it super easy
for us to get started!

To start with, go to the link above, and then click on the **Start Coding** button:

![Start Coding](start_coding.png)

Select the **Import from GitHub** tab and then type in **`darrenkidd/coah-python-bootcamp`**:

![Import from GitHub](import_from_github.png)

This should set everything up for you.

## Layout

1. Each **lesson folder** will contain all of the individual (working) steps we
will progress through during the lesson. Feel free to go have a look if you get
stuck. It also contains the lesson notes.
1. The **`main.py`** file is really just a scratch-pad for you to use in repl.it.
That's where most of the editing and learning will be done.

### Links to Lesson Notes

* [Lesson 1 - The Basics, Weather API and Refactoring :hatched_chick:](./lesson1/LESSON1_NOTES.md)

## Advanced Stuff

:fire: :fire: :fire:

### Running with Docker Locally

If you run a very lean local development environment (as I do), you may find
these Docker commands useful when testing the scripts.

```bash
$ docker build -t coah-bc -<<EOF
FROM python:3.8.2-slim-buster
RUN pip install requests
WORKDIR /usr/src/myapp
EOF
$ MSYS_NO_PATHCONV=1 docker run -it --rm -v "$(pwd)":/usr/src/myapp coah-bc python main.py
```
