# cloud-computing
Cloud computing project. Authors: [Juliusz Neuman](https://github.com/superjulek) [Arkadiusz Rybski](https://github.com/arybs)

## Introduction

Project is focussing o using AWS clusters to perform numerical computation.

## Problem
The idea comes from the Olympic problem, published [here](http://www.kgof.edu.pl/archiwum/69/of69-1-2.pdf). 
description will be pubslished soon...

## Installation (Linux)
Downloading files
```bash
git clone https://github.com/superjulek/cloud-computing 
cd cloud-computing
```

In order to use this project, following tools are required:
* [python](https://www.python.org/)
* [pip packache](https://packages.debian.org/stable/python-pip)
* [pip-tools](https://pypi.org/project/pip-tools/1.8.0/)
</br>...

All dependencies could be installed followin fruther instuctions. </br>
Installing python, pip package.
```bash
sudo apt install python3.8
sudo apt-get install python3-pip
```
Getting and installing virutalenv
```bash
python3.8 -m pip install --user virtualenv
python3.8 -m venv PATH/TO/CHOSEN/LOCATION/venv
```
Activate virtual environment
```
bash
PATH/TO/CHOSEN/LOCATION/venv/bin/activate
```
Dowloading pip-tools
```
bash
pip install pip-tools
```
Getting needed libraries for python scripts.
```
bash
pip-compile requirements.in
pip-syc requirements.txt
```
For further compiling it is posiible to use:
```
bash
pip-compile
````
Deactivate virutal environment
```
bash
deactivate
```

## Preparing Pyspark

* TBD
