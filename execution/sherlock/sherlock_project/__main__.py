#! /usr/bin/env python3

"""
Sherlock: Find Usernames Across Social Networks Module

This module contains the main logic to search for usernames at social
networks.
"""

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append('/var/task/execution')
sys.path.append('/execution')
sys.path.append('/execution/sherlock')
sys.path.append('/execution/sherlock/sherlock_project')

if __name__ == "__main__":
    # Check if the user is using the correct version of Python
    python_version = sys.version.split()[0]

    if sys.version_info < (3, 8):
        print(f"Sherlock requires Python 3.8+\nYou are using Python {python_version}, which is not supported by Sherlock.")
        sys.exit(1)
        
    from execution.sherlock.sherlock_project import sherlock
    sherlock.main()
