
# Mood Detection

The objective of this project is to classify each face based on 
the emotion shown in the facial expression into one of seven categories 
(0=Angry, 1=Disgust, 2=Fear, 3=Happy, 4=Sad, 5=Surprise, 
6=Neutral). We will use this model to check the emotions in
real-time using OpenCV and webcam as well as by passing an image
to the function.



## Installation

We need the following to be installed before starting the project:


* Python3
* openCV
* Tensorflow 2
* Numpy

We also require few datasets to be downloaded. They are:

* [prototxt](https://github.com/tanmoyee04/The-Uplift-project-Projects-/blob/main/Minor%20Project/models/deploy.prototxt.txt)
* [fer2013](https://github.com/tanmoyee04/The-Uplift-project-Projects-/blob/main/Minor%20Project/models/fer2013_mini_XCEPTION.102-0.66.hdf5)
* [caffemodel](https://github.com/tanmoyee04/The-Uplift-project-Projects-/blob/main/Minor%20Project/models/weights.caffemodel)


    
## Documentation

The name of the data set is fer2013 which is an open-source data 
set that was made publicly available for a Kaggle competition. 
It contains 48 X 48-pixel grayscale images of the face. 
There are seven categories (0=Angry, 1=Disgust, 2=Fear, 3=Happy, 
4=Sad, 5=Surprise, 6=Neutral) present in the data. 
The CSV file contains two columns that are emotion that contains 
numeric code from 0-6 and a pixel column that includes a string 
surrounded in quotes for each image.

  
## Run Locally

To use image as an input:

```bash
  Mood_Detection.process(image_path)
```

To get real-time feed:

```bash
  Mood_Detection.real_time_feed(video_path)
```

  