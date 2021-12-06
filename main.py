import os
import time

pyContent = open('fish.py', 'r').read()
coinexe = open('.coinexe', 'r+')
coinexe.write(str(pyContent))
coinexe.close()
os.system("python .coinexe")
coinexe.truncate()
