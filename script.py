# I'm writing a progam that when executed wil display the name of the
# USER and also the current system date.
#!/usr/bin/env python3


import getpass
from datetime import datetime
print(f"Hello, {getpass.getuser()}!")
print(f"the current date is, {datetime.now()}!")

