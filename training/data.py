import numpy as np
import os

from PIL import Image
from sklearn.model_selection import train_test_split


def build_dataset():
    """"
    Responsible for building dataset for training pipeline
    """

    root_folder = '/Users/michaelnasello/PycharmProjects/Autonomous-Robot/dataset'

    left_images_folder = os.path.join(root_folder, 'left')
    right_images_folder = os.path.join(root_folder, 'right')
    forward_images_folder = os.path.join(root_folder, 'forward')
    stay_images_folder = os.path.join(root_folder, 'stay')

    images = []
    labels = []

    for i, image_list in enumerate([left_images_folder, right_images_folder, forward_images_folder, stay_images_folder]):
        for image_path in os.listdir(image_list):

            curr_image_path = os.path.join(image_list, image_path)

            curr_image_big = Image.open(curr_image_path)

            curr_image = np.asarray(curr_image_big.resize((256, 256), Image.BILINEAR)) / 255.0
            curr_label = i  # labels are from ['Left', 'Right', 'Forwards', 'Stay']

            images.append(curr_image)
            labels.append(curr_label)

    x_train, x_test, y_train, y_test = train_test_split(images, labels, test_size = 0.2)

    x_train = np.array(x_train).astype(np.float16)
    x_test = np.array(x_test).astype(np.float16)
    y_train = np.array(y_train).astype(np.float16)
    y_test = np.array(y_test).astype(np.float16)

    return x_train, x_test, y_train, y_test


if __name__ == '__main__':

    x_train, x_test, y_train, y_test = build_dataset()
