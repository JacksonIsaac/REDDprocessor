import csv
import numpy as np

with open('redd-main.txt', 'rb') as f, open('redd-1.txt', 'wb') as out:
    writer = csv.writer(out)
    # Remove the first line with total number of examples.
    for row in csv.reader(f):
        try:
            fir = row
            sec = f.next().split()
            thir = f.next().split()
            four = f.next().split()
            l1 = [int(i) for i in sec]
            l2 = [int(i) for i in thir]
            l3 = [float(i) for i in four]

            index = range(len(l2))
            index.sort(key = l2.__getitem__)

            l1[:] = [sec[i] for i in index]
            l2[:] = [thir[i] for i in index]
            l3[:] = [four[i] for i in index]

            writer.writerow(row)
            writer.writerow(l1)
            writer.writerow(l2)
            writer.writerow(l3)
        except(StopIteration):
            break
