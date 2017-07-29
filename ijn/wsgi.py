"""
WSGI config for testforum project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
import sys
import pprint

from django.core.wsgi import get_wsgi_application

prj_path = os.path.normpath(os.path.join(os.path.abspath(__file__), '../../'))
sys.path.insert(0, prj_path)


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ijn.settings")
pprint.pprint(sys.path)

application = get_wsgi_application()
