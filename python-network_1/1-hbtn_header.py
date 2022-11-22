#!/usr/bin/python3
"""Import urllib and sys modules"""

import urllib.request
import sys


"""Display the value of X-Request_Id in the header"""
if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        html = response.info()
        print(html.get("X-Request-Id"))
