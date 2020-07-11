#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

# update mysql.user set authentication_string = password('mysqlroot') where user ='root' and Host ='localhost';
# grant all privileges on *.* to root@"%" identified by "mysqlroot" with grant option;


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chart_demo.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
