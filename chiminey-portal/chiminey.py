#!/usr/bin/env python
from __future__ import print_function
import os
import sys


def run():
    custom_settings = 'chiminey.settings'
    custom_settings_file = custom_settings.replace('.', '/') + '.py'
    demo_settings = 'chiminey.settings_changeme'
    if os.path.isfile(custom_settings_file):
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", custom_settings)
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", demo_settings)
        print('Using demo settings in "chiminey/settings_changeme.py",'
              ' please add your own settings file, '
              '"chiminey/settings.py".')

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    from django.core.exceptions import ImproperlyConfigured
    try:
        run()
    except ImproperlyConfigured as e:
        if 'SECRET_KEY' in e.message:
            print(r'''
# execute this wonderful command to have your settings.py created/updated
# with a generated Django SECRET_KEY (required for Mychiminey to run)
python -c "import os; from random import choice; key_line = '%sSECRET_KEY=\"%s\"  # generated from build.sh\n' % ('from chiminey.settings_changeme import * \n\n' if not os.path.isfile('chiminey/settings.py') else '', ''.join([choice('abcdefghijklmnopqrstuvwxyz0123456789\\!@#$%^&*(-_=+)') for i in range(50)])); f=open('chiminey/settings.py', 'a+'); f.write(key_line); f.close()"
''')
        else:
            raise
