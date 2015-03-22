# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 17:38:38 2015

@author: shokoryu
"""

from count_module import *
import sys
import csv 

def main():
    argv = sys.argv
    mypath = argv[1]
    saveto_count = argv[2]
    saveto_median = argv[3]
    
    path = get_file_path(mypath)
    flag = 0
    
    for i in path:
        if flag == 0: 
            store_length, count, med = process_words(i)
            flag += 1
        else: #file > 1
            store_length, count, med = process_words(i, count = count, array = store_length, med = med)

    # save count
    with open(saveto_count,'wb') as tosave_count:
        write = csv.writer(tosave_count, delimiter = '\t', )
        for key in sorted(count):
            write.writerow((key, count[key]))
    
    # save mean 
    np.savetxt(saveto_median, med, fmt = '%.1f', )

        
        
    

    
    
if __name__ == "__main__":
    main()