import csv
with open('combinedall.csv', 'rb') as f, open('combined_filtered.csv', 'wb') as out:
    writer = csv.writer(out)
    count = 1
    # Write the count, total time only once. The current file has multiple
    # entries due to concat from multiple files.
    for row in csv.reader(f):
        fir = row
        sec = f.next()
        thir = f.next()
        four = f.next()
        writer.writerow([count, 60])
        writer.writerow([sec])
        writer.writerow([thir])
        writer.writerow([four])
        count += 1
