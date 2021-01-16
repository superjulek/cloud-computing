"""Program running calculations"""

import pyspark
import sys

from mesh import mesh
from config import constants, initials, simulation, stepping


def run():

    spark = SparkSession\
    .builder\
    .appName("HeatFlow")\
    .getOrCreate()
    
    #context.addPyFile("src/point.py")
    spark.sparkContext.addPyFile("src/point.py")
    spark.sparkContext("src/config.py")

    # pyspark context
    #context = pyspark.SparkContext('local[*]')
    #context.addPyFile("src/point.py")
    #context.addPyFile("src/config.py")

    my_mesh = mesh(constants.length_val, (int)(constants.length_val /  stepping.space_delta))
    data =[]
    for step in range(simulation.max_step_num):
        diff = my_mesh.step_mesh(stepping.time_delta, context)
        if (diff < simulation.expected_diff):
            print('Finished after ' + str(step) + ' steps')
            break
        data.append(my_mesh.data_return())
        my_mesh.update_mesh()

    print(my_mesh)
     with open('Results.txt', 'w') as f:
        for item in data:
            f.write("%s\n" % item)

    if simulation.run_check is True:
        print ('Running check simulation with parameters:')
        return  # TODO: Druga runda dokładniejsza
    sys.exit()

#TODO: zapis do pliku, ładne podsumowanie symulacji z czasem trwania symulacji oraz czasem który wyszedł (+ ewentualnie wyszedł po drugim, dokładniejszym przebiegu)