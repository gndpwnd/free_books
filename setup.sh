#!/bin/bash

# sudo apt-get install build-essential libssl-dev libffi-dev python3-dev
# pip3 install -r requirements.txt
python3 index_generator.py
git-lfs track *.pdf
git add -A
git commit -m "update"
git push --set-upstream origin $(git branch | grep "*" | cut -f2 -d " ")