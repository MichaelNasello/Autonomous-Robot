<h1>Autonomous Mini Cart</h1>

The Mini Cart is designed to follow directions without pre-programmed instructions. The end
user can simply point in the desired direction of travel and the robot will react accordingly.

<h3>Raspberry Pi</h3>
<hr>

The Mini Cart is powered by a Raspberry Pi; the Pi is responsible for all ML computations, 
capturing pictures via the Pi camera, and reacting by powering servo motors with GPIO 
(General Purpose Input Output) pins.

![](images/pi.jpg)

<h3>Chassis</h3>
<hr>

The Mini Cart chassis was purchased online. It holds the Pi, Pi-Camera, servo motors, and
breadboard with a circuit supporting drive functionality.

Once the complete Mini Cart is assembled, with custom circuit, pictures
highlighting features will be uploaded.

<h3>Machine Learning</h3>
<hr>

A simple CNN was implemented to generate predictions. One issue specific to this project
was model size. It was impossible to load the original model (~400mB) into memory on the
Raspberry Pi; this is a common problem for ML 'at the edge'. Several steps were taken to 
reduce the model size to ~10mB. The model was quantized to use float16 precision (from
float32). In addition, the model was further compressed using 
<a href = "https://www.tensorflow.org/lite">Tensorflow Lite</a>. 

In addition, images from the dataset were resized to 256 by 256 images (from 512 by 512).
This decreased the size of convolution layer outputs and number of parameters in dense 
ayers later in the network.

I created my own dataset, gathering approximately 400 images of myself pointing in 
various directions. There was a 80 / 20 percent split of training and validation images, 
respectively. On the validation set of 80 images, an eventual accuracy of 100% was 
achieved.

Below you can observe the progress of training...

Validation Loss across Epochs:<br><br>
![](trained_models/model_v1/val_loss.png)

<br>

Validation Accuracy across Epochs: <br><br>

![](trained_models/model_v1/val_sparse_categorical_accuracy.png)

<br>

<h3>Results</h3>
<hr>

A video displaying results will be included upon completion of project.