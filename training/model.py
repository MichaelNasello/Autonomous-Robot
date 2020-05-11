import tensorflow as tf
import tensorflow.keras.layers as kl
import os


def model_v1():

    model = tf.keras.Sequential()

    model.add(kl.Conv2D(filters=30, kernel_size=(5, 5), input_shape=(256, 256, 3), activation='relu'))
    model.add(kl.Conv2D(filters=30, kernel_size=(5, 5), activation='relu'))
    model.add(kl.MaxPool2D())

    model.add(kl.Conv2D(filters=15, kernel_size=(3, 3), activation='relu'))
    model.add(kl.Conv2D(filters=15, kernel_size=(3, 3), activation='relu'))
    model.add(kl.MaxPool2D())

    model.add(kl.Flatten())

    model.add(kl.Dense(units=128, activation='relu'))
    model.add(kl.Dropout(0.5))
    model.add(kl.Dense(units=50, activation='relu'))
    model.add(kl.Dropout(0.5))
    model.add(kl.Dense(units=4, activation='softmax'))

    return model


def convert_model(model_path):

    model = tf.keras.models.load_model(os.path.join(model_path, 'model.h5'))

    converter = tf.lite.TFLiteConverter.from_keras_model(model)
    converter.optimizations = [tf.lite.Optimize.DEFAULT]
    converter.target_spec.supported_types = [tf.float16]

    tflite_model = converter.convert()
    open(os.path.join(model_path, 'model.tflite'), 'wb').write(tflite_model)


if __name__ == '__main__':

    convert_model('/Users/michaelnasello/PycharmProjects/Autonomous-Robot/trained_models/model_v1')
