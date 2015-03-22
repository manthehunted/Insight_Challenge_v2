# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 17:36:20 2015

@author: shokoryu
"""
import numpy as np
import string
import os

# get file path from folder path (mypath)
def get_file_path(mypath):
    path_file = []
    for (dirpath, dirnames, filenames) in os.walk(mypath):
        for name in sorted(filenames): #sort filenames in alphabetic order
            if name[0] != '.': #eliminate loading hidden files
                path = os.path.join(dirpath, name)
                path_file.append(path)
    return path_file
    
    
# count frequency 
def count_word(phrase, count):
    if phrase[0]: #if phrase is not empty
        for word in phrase:
            if word not in count:
                count[word] = 1
            else:
                count[word] += 1
    return count

# find median of array
def find_median(array):
    length_array = len(array)
    mid_index = (length_array-1)/2

    if length_array%2 == 0:
        return float(array[mid_index]+array[mid_index+1])/2
    else:
        return array[mid_index]
    
# track median
def median_word(phrase, array):
    if phrase[0]:
        length_phrase = len(phrase)
    else:
        length_phrase = 0
        
    array = np.sort(np.append(array,length_phrase))

    med = find_median(array) 
    
    #sanity check
#    med = np.median(array)
    
    return med, array


def process_words(path, count = 'None', array = 0, med = 0):
    with open(path) as data:
        if count == 'None':
            count = {}
            
        for line in data:
            phrase = line.translate(None,string.punctuation).lower().strip().split(" ")
            count = count_word(phrase, count)
            
            if not isinstance(array, np.ndarray): #initiation
                m = len(phrase)
                array = np.atleast_1d(m)
                med = array
            else:
                med_value, array = median_word(phrase, array)
                med = np.append(med, med_value)
        return array, count, med