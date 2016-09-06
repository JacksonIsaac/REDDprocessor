import csv
import numpy as np

with open('redd-1.dat', 'rb') as f, open('redd-1.txt', 'wb') as out:
    writer = csv.writer(out)
    count = 1
    # Remove the first line with total number of examples.
    for row in csv.reader(f):
        try:
            n_row = [count, "60"]
            e_type = row
            s_time = f.next().split(',')
            dur = f.next().split(',')
            l1 = [int(i) for i in e_type]
            l2 = [int(i) for i in s_time]
            l3 = [float(i) for i in dur]

            index = range(len(l2))
            index.sort(key = l2.__getitem__)

            l1[:] = [e_type[i] for i in index]
            l2[:] = [s_time[i] for i in index]
            l3[:] = [dur[i] for i in index]

            l2 = [x.replace("\r\n","") for x in l2]
            l3 = [x.replace("\r\n","") for x in l3]
            #print l1
            #print l2
            #print l3
            writer.writerow(n_row)
            writer.writerow(l1)
            writer.writerow(l2)
            writer.writerow(l3)
            count += 1
        except(StopIteration):
            break
