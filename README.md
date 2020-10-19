# cloud-computing
Cloud computing project. Authors: Juliusz Neuman Arkadiusz Rybski

## Wstęp

Projekt ma na celu przeprowadzenie obliczeń numerycznych na klastrze AWS.

## Zagadnienie

Rozważanym zagadnieniem będzie transfer ciepła w [zadaniu numerycznym KGOF z 69. OF](http://www.kgof.edu.pl/archiwum/69/of69-1-2.pdf).

## Przygotowanie środowiska wirtualnego (Linux)

* Należy pobrać pythona _sudo apt install python3.8_.
* Należy pobrać pip _sudo apt-get install python3-pip_.
* Należy pobrać narzędzie do wirtualnych środowisk _python3.8 -m pip install --user virtualenv_.
* Należy w wybranej lokalizacji zainstalować witualne środowisko pythona: _python3.8 -m venv ./venv_.
* Aktywować środowisko _source ./venv/bin/activate_.
* Pobrać narzędzia _pip install pip-tools_.
* Przejść do katalogu z projektem i skompilować zależności _pip-compile_.
* Zsynchronizować zależności _pip-sync requirements.txt_.
* Środowisko można dezaktywować _deactivate_.