#!/usr/bin/env python3

if __name__ == '__main__':

    import sys
    import gunicorn.app.wsgiapp

    sys.argv = ["gunicorn", "-b", "0.0.0.0:8080", "wsgi:application"]
    gunicorn.app.wsgiapp.run()

