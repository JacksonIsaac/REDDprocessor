# coding: utf-8
import csv
import os
import sys
import numpy as np
import datetime
import operator
import re
#from nilmtk.dataset_converters import convert_redd

path = 'SmartHome/sorted/'
dest = 'list_test_mins_channel/'

def processData():
    for root, dirs, files in os.walk(path):
        for name in files:
            if name.startswith("channel"):
                #print root
                current = os.path.join(root, name)
                print "Processing ", current

                data = []

                with open(current, 'rb') as f: #, open('test.csv', 'wb') as out:
                    for line in f:
                        fields = line.split()[1].split()
                        rowdata = map(float, fields)
                        data.extend(rowdata)
                    avg = sum(data)/float(len(data))
                    thres = avg * 30/100
                    thres_min = avg - thres
                    thres_max = avg + thres
                    print avg
                    print thres
                    print thres_min
                    print thres_max

                initial_line = 0

                #print os.path.basename(os.path.normpath(root))

                #ofile = os.path.join((root), name)
                #print "Writing to ", ofile
                ofile = os.path.join(dest, os.path.basename(os.path.normpath(root)), name)

                if not os.path.exists(os.path.dirname(ofile)):
                    try:
                        os.makedirs(os.path.dirname(ofile))
                    except OSError as exc: # Guard against race condition
                        if exc.errno != errno.EEXIST:
                            raise
                # Calculate the mean for every file and pass the threshold
                # according to which the values will be filtered out from raw data.
                filterData(current, ofile, thres_min, thres_max)

# This function converts the time points to time intervals with continous
# range with a constant difference.
# Output is of the form
# <number of example> <total time>
# <starting minute>
# <duration>
def filterData(current, ofile, thres_min, thres_max):
    # print type(ofile)
    # print os.path.basename(ofile[:-4]).split('_')[2]
    channel_no = os.path.basename(ofile[:-4]).split('_')[2]
    timethres = 6
    print channel_no
    with open(current, 'rb') as f, open(ofile, 'wb') as out:
        writer = csv.writer(out)
        #st_time = f.readline().split()[0]
        #end_time = f.readline().split()[0]
        frst = f.readline().split()
        sec = f.readline().split()
        f.seek(0)
        diff = long(sec[0])-long(frst[0])
        #inp = csv.reader(f)
        #f = sorted(inp, key=operator.itemgetter(0))
        s_comb_range = []
        dur_comb_range = []
        chann_range = []
        count = 1
        p_hour = datetime.datetime.fromtimestamp(long(frst[0])).strftime('%Y-%m-%d %H')
        for row in csv.reader(f):
            #fields = row[0].split()
            #if float(fields[1]) > start: # and long(fields[0]) >= prev+1:
            #    writer.writerow(row)     # write (Start_Time <space> End_Time)
            #print row
            s_range = row[0].split()                       # Starting Row
            #print s_range
            s_time = long(s_range[0])   # Starting range time
            s_voltage = float(s_range[1])   # Starting range voltage
            if s_voltage > thres_min and s_voltage < thres_max:
                try:
                    e_range = f.next().split()                  # End time row
                    e_time = long(e_range[0])   # End range time
                    e_voltage = float(e_range[1]) # End range voltage
                    cnt = diff
                    bool = 0
                    while e_time == s_time+cnt+timethres and (e_voltage > thres_min and e_voltage < thres_max):
                        e_min_1 = e_range
                        e_prev_time = long(e_range[0])   # End range time
                        e_range = f.next().split()                  # End time row
                        e_time = long(e_range[0])   # End range time
                        e_voltage = float(e_range[1]) # End range voltage
                        cnt += diff
                        bool = 1
                    if e_time > s_time and bool == 1:
                        #print s_time, "---", e_time
                        s_range[0] = datetime.datetime.fromtimestamp(s_time).strftime('%Y-%m-%d %H:%M:%S')
                        e_min_1[0] = datetime.datetime.fromtimestamp(e_time).strftime('%Y-%m-%d %H:%M:%S')
                        duration = (e_time - s_time) * 1.0 / 60.0
                        duration = round(duration, 2)
                        # e_min_1[0] = duration
                        # print duration
                        # print s_range, "---", e_min_1
                        c_hour = datetime.datetime.fromtimestamp(e_time).strftime('%Y-%m-%d %H')
                        # print p_hour
                        # print c_hour
                        # if duration > 0.05:
                        if (p_hour == c_hour):
                            # print "Inside if"
                            chann_range = chann_range + [channel_no]
                            s_comb_range = s_comb_range \
                            + [datetime.datetime.fromtimestamp(s_time).strftime('%M')]
                            dur_comb_range = dur_comb_range + [duration]
                        else:
                            # print "Inside else"
                            p_hour = c_hour
                            chann_range = chann_range + [channel_no]
                            s_comb_range = s_comb_range \
                            + [datetime.datetime.fromtimestamp(s_time).strftime('%M')]
                            dur_comb_range = dur_comb_range + [duration]
                            if s_comb_range and dur_comb_range:
                                # print "s_comb_range is not empty"
                                writer.writerow(chann_range)
                                writer.writerow(s_comb_range)
                                writer.writerow(dur_comb_range)
                                s_comb_range = []
                                dur_comb_range = []
                                chann_range = []
                        # writer.writerow([count,"60"])
                        # writer.writerow([channel_no])
                        # writer.writerow([datetime.datetime.fromtimestamp(s_time).strftime('%M')])
                        # writer.writerow([duration])
                        # count += 1
                            #writer.writerow(["duration", duration])
                except(StopIteration):
                    print "Done Processing ", current

def main():
    processData()

if __name__ == "__main__":
    main()
