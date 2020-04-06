import random
import os
from PIL import Image,ImageFilter,ImageDraw
import numpy as np
import h5py
from PIL import ImageStat
import cv2
from scipy.io import loadmat

def load_data(img_path,train = True):
    gt_path = img_path.replace('.jpg','.mat').replace("IMG","GT_IMG").replace('images','ground_truth')
    img = Image.open(img_path).convert('RGB')
    # gt_file = h5py.File(gt_path)

    gt_file = loadmat(gt_path)

    target = gt_file['image_info'][0][0][0][0][0]
    # if train:
    #     crop_size = (img.size[0]/2,img.size[1]/2)
    #     if random.randint(0,9)<= -1:
    #
    #
    #         dx = int(random.randint(0,1)*img.size[0]*1./2)
    #         dy = int(random.randint(0,1)*img.size[1]*1./2)
    #     else:
    #         dx = int(random.random()*img.size[0]*1./2)
    #         dy = int(random.random()*img.size[1]*1./2)
    #     img = img.crop((dx,dy,crop_size[0]+dx,crop_size[1]+dy))
    #     target = target[dy:crop_size[1]+dy,dx:crop_size[0]+dx]
    #
    #     if random.random()>0.8:
    #         target = np.fliplr(target)
    #         img = img.transpose(Image.FLIP_LEFT_RIGHT)

    
    
    print(target.shape)

    target = cv2.resize(target,(int(target.shape[1]/2),int(target.shape[0]/2)),interpolation = cv2.INTER_CUBIC)*4

    print(target.shape)
    target = np.expand_dims(target,axis=3)
    
    return img,target