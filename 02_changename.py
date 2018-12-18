import os

os.chdir(r'C:\Users\student\SSJ\SSAFY지원자')

for filename in os.listdir("."):
    os.rename(filename, filename.replace('APPLE', 'SSAFY'))