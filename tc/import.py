from matplotlib import pyplot as plt
from tubes import pathName

with open(pathName, 'r') as my_file:
    lines = my_file.readlines()
    for line in lines:
        print(line)