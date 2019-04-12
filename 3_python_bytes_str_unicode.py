"""
Two types that represent sequence of char: str and bytes(Python3), unicode and str(Python2)
Python3:
    str: Unicode character
    bytes: 8 bits raw data
Python2:
    unicode: Unicode character
    str: 8 bits raw data
"""

import sys
version = sys.version_info[0]

if version is 3:
    #encoding will take unicode str to bytes
    #where decoding will take bytes to unicode str
    def to_str(bytes_or_str):
        if isinstance(bytes_or_str, bytes):
            value = bytes_or_str.decode('utf-8')
        else:
            value = bytes_or_str
        return value

    def to_bytes(bytes_or_str):
        if isinstance(bytes_or_str, str):
            value = bytes_or_str.encode('utf-8')
        else:
            value = bytes_or_str
        return value

if version is 2:
    def to_str(str_or_unicode):
        if isinstance(bytes_or_str, unicode):
            value = bytes_or_str.encode('utf-8')
        else:
            value = bytes_or_str
        return value
    
    def to_unicode(bytes_or_str):
        if isinstance(bytes_or_str, str):
            value = bytes_or_str.decode('utf-8')
        else:
            value = bytes_or_str
        return value


