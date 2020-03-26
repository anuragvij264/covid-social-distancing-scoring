# covid-social-distancing-scoring
Repository for building a social distancing scoring API.
 
### Objective: 
Given a number of images of a certain location, computing a social distancing score for that location using the images. 

### Preliminary approaches
- Count the people/objects in the image and compute proximity and give a score.
  - Haar cascade, face detection to compute the objects, count th
### Resources 
- https://github.com/leeyeehoo/CSRNet-pytorch
- https://www.cv-foundation.org/openaccess/content_cvpr_2016/papers/Zhang_Single-Image_Crowd_Counting_CVPR_2016_paper.pdf
- https://github.com/gjy3035/C-3-Framework
### Datasets to test(to be added further) 
- Shanghai Tech Dataset(Part A and Part B) 


### Instructions

Download pretrained csr-net model (https://drive.google.com/file/d/1KY11yLorynba14Sg7whFOfVeh2ja02wm/view?usp=sharing) and place it in checkpoints directory.
```
pip install -r requirements.txt
python app.py 
```
