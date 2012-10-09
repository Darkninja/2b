'''
Created on Oct 9, 2012

@author: norder
'''
import sys, os
from subprocess import check_call, CalledProcessError

class ConvertedObject():     
    pass

def get_new_filename(input_file, output_type):
    return input_file[:input_file.rfind(".")] + "." + output_type

def convert(input_file, output_type):
    c = ConvertedObject()
    c.input = input_file
    c.type = output_type
    c.path = input_file[:input_file.rfind("/")]
    c.filename = get_new_filename(input_file[input_file.rfind("/"):], output_type)
    if not os.path.exists(c.path+c.filename):
        cmd = ["avconv", "-y", "-i", c.input, "-ar", "22050", "-f", c.type, c.path+c.filename]
        try:
            check_call(cmd)
        except CalledProcessError:
            c.status = 1
            return c
    c.status = 0
    return c

if __name__ == "__main__":
    convert(sys.argv[1], sys.argv[2])