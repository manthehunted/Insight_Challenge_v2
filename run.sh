#!/usr/bin/env bash

# example of the run script for running the word count

# first I'll load all my dependencies
apt-get install python-numpy

# next I'll make sure that all my programs (written in Python in this example) have the proper permissions
chmod a+x ./src/execute.py
chmod a+x ./src/count_module.py

# finally I'll execute my programs, with the input directory wc_input and output the files in the directory wc_output
python ./src/execute.py ./wc_input ./wc_output/wc_result.txt ./wc_output/med_result.txt



