#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    config_module = os.environ.get("DJANGO_SETTINGS_MODULE", "config.settings.dev")
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", config_module)

    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
