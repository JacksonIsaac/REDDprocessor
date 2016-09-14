from itertools import izip_longest

outpath = "redd-main/combined/"

dir = "redd-main/house_1/"

with open(dir+'channel_1.dat') as f1, open(dir+'channel_2.dat') as f2, open(dir+'channel_5_6.dat') as f3,\
    open(dir+'channel_6_7.dat') as f4, open(dir+'channel_7_5.dat') as f5, open(dir+'channel_8_5.dat') as f6,\
    open(dir+'channel_9_3.dat') as f7, open(dir+'channel_11_9.dat') as f8, open(dir+'channel_12_10.dat') as f9,\
    open(dir+'channel_15_5.dat') as f12, open(dir+'channel_17_3.dat') as f10, open(dir+'channel_18_3.dat') as f11,\
    open(outpath+'redd-combined-1.dat', 'wb') as res: # open(dir+'channel_12.dat') as f12,
    for l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12 in izip_longest(f1, f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12, fillvalue=""):
        res.write("{},{},{},{},{},{},{},{},{},{},{},{}\n".\
        format(l1.rstrip(), l2.rstrip(),l3.rstrip(), l4.rstrip(),\
        l5.rstrip(), l6.rstrip(),l7.rstrip(), l8.rstrip(),\
        l9.rstrip(), l10.rstrip(),l11.rstrip(),l12.rstrip()))

dir2 = "redd-main/house_2/"

with open(dir2+'channel_1.dat') as f1, open(dir2+'channel_2.dat') as f2, open(dir2+'channel_3_5.dat') as f3,\
    open(dir2+'channel_4_3.dat') as f4, open(dir2+'channel_5_11.dat') as f5, open(dir2+'channel_6_9.dat') as f6,\
    open(dir2+'channel_7_4.dat') as f7, open(dir2+'channel_8_5.dat') as f8, open(dir2+'channel_9_6.dat') as f9,\
    open(outpath+'redd-combined-2.dat', 'wb') as res:
    for l1,l2,l3,l4,l5,l6,l7,l8,l9 in izip_longest(f1, f2,f3,f4,f5,f6,f7,f8,f9, fillvalue=""):
        res.write("{},{},{},{},{},{},{},{},{}\n".\
        format(l1.rstrip(), l2.rstrip(),l3.rstrip(), l4.rstrip(),\
        l5.rstrip(), l6.rstrip(),l7.rstrip(), l8.rstrip(),\
        l9.rstrip()))

dir6 = "redd-main/house_3/"

with open(dir6+'channel_1.dat') as f1, open(dir6+'channel_2.dat') as f2, open(dir6+'channel_5_3.dat') as f3,\
    open(dir6+'channel_7_6.dat') as f4, open(dir6+'channel_9_7.dat') as f5, open(dir6+'channel_10_8.dat') as f6,\
    open(dir6+'channel_11_3.dat') as f7, open(dir6+'channel_15_3.dat') as f8, open(dir6+'channel_16_9.dat') as f9,\
    open(dir6+'channel_17_3.dat') as f10, open(dir6+'channel_19_3.dat') as f11,\
    open(outpath+'redd-combined-3.dat', 'wb') as res:
    for l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11 in izip_longest(f1, f2,f3,f4,f5,f6,f7,f8,f9,f10,f11, fillvalue=""):
        res.write("{},{},{},{},{},{},{},{},{},{},{}\n".\
        format(l1.rstrip(), l2.rstrip(),l3.rstrip(), l4.rstrip(),\
        l5.rstrip(), l6.rstrip(),l7.rstrip(), l8.rstrip(),\
        l9.rstrip(), l10.rstrip(),l11.rstrip()))

dir4 = "redd-main/house_4/"

with open(dir4+'channel_1.dat') as f1, open(dir4+'channel_2.dat') as f2, open(dir4+'channel_3_3.dat') as f3,\
    open(dir4+'channel_4_8.dat') as f4, open(dir4+'channel_5_5.dat') as f5, open(dir4+'channel_7_4.dat') as f6,\
    open(dir4+'channel_8_11.dat') as f7, open(dir4+'channel_13_3.dat') as f8, open(dir4+'channel_14_5.dat') as f9,\
    open(dir4+'channel_18_3.dat') as f10, open(dir4+'channel_19_3.dat') as f11,\
    open(outpath+'redd-combined-4.dat', 'wb') as res:
    for l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11 in izip_longest(f1, f2,f3,f4,f5,f6,f7,f8,f9,f10,f11, fillvalue=""):
        res.write("{},{},{},{},{},{},{},{},{},{},{}\n".\
        format(l1.rstrip(), l2.rstrip(),l3.rstrip(), l4.rstrip(),\
        l5.rstrip(), l6.rstrip(),l7.rstrip(), l8.rstrip(),\
        l9.rstrip(), l10.rstrip(),l11.rstrip()))

dir5 = "redd-main/house_5/"

with open(dir5+'channel_1.dat') as f1, open(dir5+'channel_2.dat') as f2, open(dir5+'channel_3_9.dat') as f3,\
    open(dir5+'channel_6_8.dat') as f4, open(dir5+'channel_14_3.dat') as f5, open(dir5+'channel_16_10.dat') as f6,\
    open(dir5+'channel_18_6.dat') as f7, open(dir5+'channel_19_3.dat') as f8, open(dir5+'channel_20_7.dat') as f9,\
    open(dir5+'channel_23_3.dat') as f10,\
    open(outpath+'redd-combined-5.dat', 'wb') as res:
    for l1,l2,l3,l4,l5,l6,l7,l8,l9,l10 in izip_longest(f1, f2,f3,f4,f5,f6,f7,f8,f9,f10, fillvalue=""):
        res.write("{},{},{},{},{},{},{},{},{},{}\n".\
        format(l1.rstrip(), l2.rstrip(),l3.rstrip(), l4.rstrip(),\
        l5.rstrip(), l6.rstrip(),l7.rstrip(), l8.rstrip(),\
        l9.rstrip(), l10.rstrip()))

dir6 = "redd-main/house_6/"

with open(dir6+'channel_1.dat') as f1, open(dir6+'channel_2.dat') as f2, open(dir6+'channel_3_5.dat') as f3,\
    open(dir6+'channel_4_4.dat') as f4, open(dir6+'channel_5_11.dat') as f5, open(dir6+'channel_7_10.dat') as f6,\
    open(dir6+'channel_8_6.dat') as f7, open(dir6+'channel_12_12.dat') as f8, open(dir6+'channel_13_12.dat') as f9,\
    open(dir6+'channel_14_3.dat') as f10, open(dir6+'channel_15_12.dat') as f11,\
    open(outpath+'redd-combined-6.dat', 'wb') as res:
    for l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11 in izip_longest(f1, f2,f3,f4,f5,f6,f7,f8,f9,f10,f11, fillvalue=""):
        res.write("{},{},{},{},{},{},{},{},{},{},{}\n".\
        format(l1.rstrip(), l2.rstrip(),l3.rstrip(), l4.rstrip(),\
        l5.rstrip(), l6.rstrip(),l7.rstrip(), l8.rstrip(),\
        l9.rstrip(), l10.rstrip(),l11.rstrip()))
