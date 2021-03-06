#!/usr/bin/env python
# This file is Python 2 compliant.

import sys
from app.config import add_stream

class __redirection__:
    def __init__(self):
        self.buff = ''
        self.__console__ = sys.stdout

    def write(self, output_stream):
        if str(output_stream).startswith('    # download-with:'):
            index = str(output_stream).find('=')
            options = str(output_stream)[(index + 1):-6]
            self.buff += '<br><font color=blue>    Option is ' + options + '</p></font>'
            add_stream(options)

        else:
            self.buff += '<br>' + output_stream

    def to_console(self):
        pass
        # sys.stdout = self.__console__
        # print(self.buff)

    def to_file(self, file_path):
        f = open(file_path, 'w')
        sys.stdout = f
        print(self.buff)
        f.close()

    def flush(self):
        self.buff = ''

    def reset(self):
        sys.stdout = self.__console__

    def get_buffer(self):
        return self.buff

    def isatty(self):
        return True


# redirection
r_obj = __redirection__()
sys.stdout = r_obj
tmp = ''
