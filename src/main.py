"""Główny plik programu"""

import pyspark
import sys
import numpy as np
import matplotlib.pyplot as pyplot
from matplotlib.animation import FuncAnimation

from mesh import mesh


TempL=300
TempR=900
size=1
elem_num=200
max_iter=100

def main():
    print ("Witaj w świecie klałd kopjutingu")

    # Kontekst sparka
    context = pyspark.SparkContext('local[*]')
    context.addPyFile("src/point.py")

    my_mesh = mesh(size, elem_num, TempL, TempR)
    
    print("Proba numpy\n", a)
    for step in range(100):
        my_mesh.step_mesh(0.1, context)
        my_mesh.update_mesh()
    print(my_mesh)
    sys.exit()




if __name__ == "__main__":
    main()

# vvv ten syf zostawiam do wglądu

sc = pyspark.SparkContext('local[*]')

txt = sc.textFile('file:////usr/share/doc/python3.8/copyright')
print(txt.count())

python_lines = txt.filter(lambda line: 'python' in line.lower())
print(python_lines.count())
