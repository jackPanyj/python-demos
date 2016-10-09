import os
import re
def method1(file_path):
    with open(file_path, 'r') as f:
        print len(f.read().split())

def method2(file_path):
    print os.popen('wc -w {0}'.format(file_path)).read()

def method3(file_path):
    with open(file_path, 'r') as f:
        words = re.findall(r'[a-zA-Z0-9]+', f.read())
        print len(words)

if __name__ == '__main__':
    file_path = 'english.txt'
    method1(file_path) 
    method2(file_path)
    method3(file_path)
