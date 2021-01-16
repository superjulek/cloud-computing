"""Główny plik programu"""

import pyspark
import sys
import numpy as np
import matplotlib.pyplot as pyplot
from matplotlib.animation import FuncAnimation

from mesh import mesh
from visualization import animation


TempL=300
TempR=900
size=1
elem_num=200
max_iter=int(5e04)
time_delta=0.1

def main():
    print ("Witaj w świecie klałd kopjutingu")

    # Kontekst sparka
    context = pyspark.SparkContext()
    context.addPyFile("src/point.py")

    my_mesh = mesh(size, elem_num, TempL, TempR)

    data=[]
    temp, _ = np.meshgrid(my_mesh.data_return(), my_mesh.data_return())
    data.append(temp)
    for step in range(max_iter):
        my_mesh.step_mesh(time_delta, context)
        my_mesh.update_mesh()
        temp, _ = np.meshgrid(my_mesh.data_return(), my_mesh.data_return())
        data.append(temp)
    
    context.stop()
    animation(data)
    print(my_mesh)
    sys.exit()




if __name__ == "__main__":
    main()

# vvv ten syf zostawiam do wglądu

sc = pyspark.SparkContext()

txt = sc.textFile('file:////usr/share/doc/python3.8/copyright')
print(txt.count())

python_lines = txt.filter(lambda line: 'python' in line.lower())
print(python_lines.count())
sc.stop()