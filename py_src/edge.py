import cv2
import os
import sys
import glob
import numpy as np
import matplotlib.pyplot as plt

def get_edge(img):
    img = cv2.GaussianBlur(img,(5,5),0)
    img = cv2.Canny(img, 209, 300)
    return img

def flip_save(img_pth):
    img = cv2.imread(img_pth)
    img = cv2.flip(img,0)
    cv2.imwrite(img_pth,img)
    return img

if __name__ == "__main__":
    
    depth_path = sys.argv[1]
    normal_path = sys.argv[2]
    out_path = sys.argv[3]
    
    for i in range(0,360,15):
       
        dpth = os.path.join(depth_path,"%d.png"%(i))
        npth = os.path.join(normal_path,"%d.png"%(i))
        de = get_edge(flip_save(dpth))
        ne = get_edge(flip_save(npth))
        fe = de+ne
        #_,fe = cv2.threshold(fe,1,255,cv2.THRESH_BINARY)
        
        kernel = np.ones((3,3))
        #fe = cv2.dilate(fe, kernel)
        fe = 255-fe
        opth = os.path.join(out_path,"%d.png"%(i))
        #os.remove(dpth)
        #os.remove(npth)
        cv2.imwrite(opth,fe)
        #cv2.imshow('dst',fe)
        #cv2.waitKey(0)

#img_depth = cv2.imread(imgs_pth[0])
#img_normal = cv2.imread(img_pth[1])_


