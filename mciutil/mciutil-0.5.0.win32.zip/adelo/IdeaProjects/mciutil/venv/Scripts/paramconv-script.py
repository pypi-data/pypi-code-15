#!C:\Users\adelo\IdeaProjects\mciutil\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'mciutil==0.5.0','console_scripts','paramconv'
__requires__ = 'mciutil==0.5.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('mciutil==0.5.0', 'console_scripts', 'paramconv')()
    )
