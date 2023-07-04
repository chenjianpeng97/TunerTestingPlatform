#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

from PyAutoTest.auto_test.auto_system.service.socket_link.socket_user_redis import SocketUserRedis
from script.nuw_logs import __nuw_dir

__nuw_dir()

SocketUserRedis().all_delete()


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PyAutoTest.settings')
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
