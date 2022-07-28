import os
import sys

def create_dir(dir):
    for i in range(8):
        os.mkdir(dir + '\\{}'.format(i + 1))

if __name__ == '__main__':
    current_dir = "C:\\Users\\randm\\Desktop"
    create_dir(current_dir)