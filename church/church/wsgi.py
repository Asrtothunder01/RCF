import os
import sys
from django.core.wsgi import get_wsgi_application

# Debug: Print the Python path
print("Python Path:", sys.path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'church.settings')

application = get_wsgi_application()
