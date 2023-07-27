import cclib
import os, sys
from glob import glob
import numpy as np
from matplotlib import pyplot as plt
import time
from datetime import datetime

def get_time(file_name = False):
    now = datetime.now()
    if not file_name:
        formatted_date = now.strftime('%d-%m-%Y %H:%M')
    else:
        formatted_date = now.strftime('%d-%m-%Y_%H-%M')
    return formatted_date

refs = glob("*_pka1.out")                                                             #!!!
out_file_list = [ref for ref in refs]
#out_file_list = ['yourfile.out', 'yourotherfile.out', …] # adjust file names

# open new csv file for results
results_filename = "results_pka"+get_time(True)+".csv"
with open(results_filename,"w") as f1:
    f1.write("refcode, delta G\n")


for filename in out_file_list:
    data = cclib.io.ccread(filename)
    # Read using cclib package the output file - all the data save in var "data"
    # The data object above contains all the information cclib was able to parse
    # from the output file, available as attributes on the object:
    #plt.title("SCF energy ")
    #plt.xlabel("Optimization Step Number")
    #plt.ylabel("SCF energies [kcal/mol]")
    delta_g = min(data.scfenergies)*627.509

    with open(results_filename,"a") as f1:
        f1.write(filename.split(".")[0]+","+delta_g+"\n")
