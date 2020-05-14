import os
from time import sleep

from picamera import PiCamera


def gather_dataset():
    """
    Builds dataset for ML model training.
    """

    root_folder = '/home/pi/Projects/Autonomous-Robot'

    left_images = os.path.join(root_folder, 'left')
    right_images = os.path.join(root_folder, 'right')
    forward_images = os.path.join(root_folder, 'forward')
    stay_images = os.path.join(root_folder, 'stay')

    camera = PiCamera()
    camera.start_preview()

    camera.resolution = (256, 256)
    camera.rotation = 180
    camera.exposure_mode = 'backlight'

    for folder in [left_images, right_images, forward_images, stay_images]:

        print('Starting gather for {} in 10 seconds...'.format(folder))
        sleep(10)
        print('Gathering...')

        if not os.path.exists(folder):
            os.mkdir(folder)

        for i in range(100):

            sleep(0.5)

            camera.capture(os.path.join(folder, 'image_{}.jpg'.format(i)))

        print('Done gathering for {}\n'.format(folder))

    camera.stop_preview()


def capture_picture(filename):
    """
    Takes picture and saves it in filename.
    """

    camera = PiCamera()
    camera.start_preview()

    camera.resolution = (256, 256)
    camera.rotation = 180
    camera.exposure_mode = 'backlight'

    sleep(0.5)

    camera.capture(filename)
    camera.stop_preview()


if __name__ == '__main__':

    #capture_picture('/home/pi/Desktop/test_image.jpg')
    gather_dataset()
