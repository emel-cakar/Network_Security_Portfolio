# malicious1.py
# FAKE malicious example — does nothing real

import os

def pretend_to_do_bad_things():
    code = "print('totally safe!')"
    eval(code)  # <--- flagged by your scanner

pretend_to_do_bad_things()
