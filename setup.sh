#!bin/bash
sudo apt-get install python3-pip

pip install -r requirements.txt

python -m spacy download en_core_web_sm
