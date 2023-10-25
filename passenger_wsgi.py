import sys, os
INTERP = os.path.expanduser("~/venv310/bin/python3")

if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)

from admin_panel.wsgi import application