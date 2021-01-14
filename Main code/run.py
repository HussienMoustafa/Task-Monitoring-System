import subprocess
import sys
import os

result = subprocess.run(
    [sys.executable, "-m", "pip", "install", "-U",
        "Django", "django-crispy-forms", "Pillow"],
    check=True
)
result = subprocess.run(
    [sys.executable, "manage.py", "runserver"],
    check=True
)
