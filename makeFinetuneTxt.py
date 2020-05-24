import random
import os

xmlfilepath = 'data/finetune_anns'
txtsavepath = 'data/ImageSets'

total_xml = os.listdir(xmlfilepath)
list = range(len(total_xml))

fft = open('data/ImageSets/finetune.txt','w')

for i in list:
    name = total_xml[i][:-4] + '\n'

    fft.write(name)

fft.close()


