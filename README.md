# covid-social-distancing-scoring
Repository for building a social distancing scoring API.
 
### Objective: 
Given a number of images of a certain location, computing a social distancing score for that location using the images. 

### Preliminary approaches
- Count the people/objects in the image and compute proximity and give a score.
  - Haar cascade, face detection to compute the objects, count th
  - CSRNet (http://openaccess.thecvf.com/content_cvpr_2018/papers/Li_CSRNet_Dilated_Convolutional_CVPR_2018_paper.pdf) (SOTA)
- Get Social distance score from distances between humans present in Image/Video
  - Identify Humans/Pedestrian from Image that is nothing but boundary boxes
  - Map boundry boxes, corresponding aspect ratios and the fact of average height/width  of human being to calculate actual distances between boundary boxes
  - Use these distances to calculate score
  - Possible benefits:
    - Only Humans will be considered while calculating score
    - Lot of real time human detectors available
### Resources 
- https://github.com/leeyeehoo/CSRNet-pytorch 
- https://www.cv-foundation.org/openaccess/content_cvpr_2016/papers/Zhang_Single-Image_Crowd_Counting_CVPR_2016_paper.pdf
- https://github.com/gjy3035/C-3-Framework
- https://github.com/CommissarMa/Crowd_counting_from_scratch
- https://medium.com/@madhawavidanapathirana/real-time-human-detection-in-computer-vision-part-2-c7eda27115c6
- https://www.pyimagesearch.com/2015/11/09/pedestrian-detection-opencv/
### Datasets to test(to be added further) 
- Shanghai Tech Dataset(Part A and Part B) 


### Instructions

Download pretrained csr-net model (https://drive.google.com/file/d/1KY11yLorynba14Sg7whFOfVeh2ja02wm/view?usp=sharing) and place it in checkpoints directory.
```
pip install -r requirements.txt
python app.py 
```


