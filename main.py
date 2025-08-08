import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myfirstproject.settings')
django.setup()

from accounts.models import User, Role

Role.objects.create(title='admin')