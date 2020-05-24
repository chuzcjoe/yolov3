import os
import random

finetune = ['birdCall_1','blueSunglasses_1','brownDie_1','cloudSign_1','eyeball_1','gClamp_1','gyroscope_1','hairClip_1','lavenderDie_1','metalKey_1']

xmlfilepath = 'data/Annotations'
txtsavepath = 'data/ImageSets'
total_xml = os.listdir(xmlfilepath)

ftrain = open('data/ImageSets/train.txt', 'w')
ftune = open('data/ImageSets/finetune.txt', 'w')

for xml in total_xml:
    name = xml[:-4]

    flg = False
    for finetune_name in finetune:
        if finetune_name in name and finetune_name.split('_')[1] == name.split('_')[1]:
            ftune.write(name+'\n')
            flg = True
            break

    if not flg:
        ftrain.write(name+'\n')


ftrain.close()
ftune.close()
