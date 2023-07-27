import os, sys
from glob import glob
import time
from datetime import datetime
import numpy as np

# Import the function for extractig volumes from the output files.
# path should be where the other script is saved
sys.path.append("/home/qnt/tchem05/g16/final_project/")                            #!!!
from extract_vol import extrct_vol_from_output as extract

# return the date and time in format: d-m-y HH:MM
def get_time(file_name = False):
    now = datetime.now()
    if not file_name:
        formatted_date = now.strftime('%d-%m-%Y %H:%M')
    else:
        formatted_date = now.strftime('%d-%m-%Y_%H-%M')
    return formatted_date

# refs should be the list of the names of the files
refs = glob("*_vol.gjf")                                                             #!!!
refs = [ref.split(".")[0] for ref in refs]

# open new csv file for results
results_filename = "results_"+get_time(True)+".csv"
with open(results_filename,"w") as f1:
    f1.write("refcode, mean, STD, min, max, median\n")

# loop that iterates over the the input files
for ref in refs:
    # this list will hold all of the results from the Monte-Carlo for this input
    vols = []
    
    # loop that operate gaussian calculation 100 time
    for i in range(10):
        os.system("runqc g16 "+ref)
        # Very optional - writing file for tracking how many calculations has been done until that time 
        with open("Huang_vol.log","a") as f2:                                                                       #!!!
            f2.write(ref+" started calculation at "+get_time()+"\n")    
        time.sleep(3)
        # waiting for a second and checking if the log file still exist. If not, we will break out of the infinity loop 
        while True:
            time.sleep(1)
            if not os.path.exists(ref+'.log'):
                if not os.path.exists(ref+'.log'):
                    break
        with open("Huang_vol.log","a") as f2:
            f2.write(ref+" Has done calculation at "+get_time()+"\n")
        # adding the results to the list of volumes results
        vols.append(extract(ref))
    # after 100 calculations - write summary of the results in the results file 
    with open(results_filename,"a") as f1:
        f1.write(ref+","+str(np.mean(vols))+","+str(np.std(vols))+","+str(np.min(vols))+","+str(np.max(vols))+","+str(np.median(vols))+"\n")


