#!/usr/bin/env python3
import os
import sys
from shutil import copyfile

if len(sys.argv) > 1:
    file = sys.argv[1]
else:
    file = 'Test.ipynb'

if len(sys.argv) > 2:
    number_of_users = sys.argv[2]
else:
    number_of_users = 4


file_path = '/home/ec2-user/ml-crash-course/{}'.format(file)
for i in range(1, number_of_users + 1):
    copy_path = '/home/user{}/{}'.format(i, file)
    try:
        os.remove(copy_path)
        print('Deleted {}'.format(copy_path))
    except OSError:
        pass

    copyfile(file_path, copy_path)
    print('Copied {} to {}'.format(file_path, copy_path))



