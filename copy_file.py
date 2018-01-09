#!/usr/bin/env python3

import os
import sys
from shutil import copyfile

if len(sys.argv) > 1:
    file = sys.argv[1]
else:
    file = 'Test.ipynb'

file_path = '/home/ec2-user/ml-crash-course/{}'.format(file)

for i in range(1, 3):
    copy_path = '/home/user{}/{}'.format(i, file)
    try:
        os.remove(copy_path)
    except OSError:
        pass

    copyfile(file_path, copy_path)



