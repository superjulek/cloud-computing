# cloud-computing
Cloud computing project. Authors: [Juliusz Neuman](https://github.com/superjulek) [Arkadiusz Rybski](https://github.com/arybs)

## Introduction

Project is focussing o using AWS clusters to perform numerical computation.

## Problem
The idea comes from the Olympic problem, published [here](http://www.kgof.edu.pl/archiwum/69/of69-1-2.pdf). 
description will be pubslished soon...

## Installation (Linux)

In order to use this project, following tools are required:
* [python](https://www.python.org/)
* [pip packache](https://packages.debian.org/stable/python-pip)
...

All dependencies could be installed followin fruther instuctions.
Installing python, pip package.
```bash
sudo apt install python3.8
sudo apt-get install python3-pip
```

* Należy pobrać pythona _sudo apt install python3.8_.
* Należy pobrać pip _sudo apt-get install python3-pip_.
* Należy pobrać narzędzie do wirtualnych środowisk _python3.8 -m pip install --user virtualenv_.
* Należy w wybranej lokalizacji zainstalować witualne środowisko pythona: _python3.8 -m venv ./venv_.
* Aktywować środowisko _source ./venv/bin/activate_.
* Pobrać narzędzia _pip install pip-tools_.
* Przejść do katalogu z projektem i skompilować zależności _pip-compile requirements.in_.
* Przy następnych kompilacjach można użyć tylko _pip-compile_.
* Zsynchronizować zależności _pip-sync requirements.txt_.
* Środowisko można dezaktywować _deactivate_.

## Preparing Pyspark

* TBD