import numpy as np
import tensorflow as tf

from PIL import Image

from camera import capture_picture


def run_from_dataset():

    image_path = '/home/pi/PycharmProjects/autonomous-robot/dataset/left/image_50.jpg'
    
    image_big = Image.open(image_path)
    image = np.asarray(image_big.resize((256, 256), Image.BILINEAR)) / 255.0
    image = np.expand_dims(image, axis = 0).astype(np.float32)

    interpreter = tf.lite.Interpreter(model_path = '/home/pi/PycharmProjects/autonomous-robot/trained_models/model_v1/model.tflite')
    interpreter.allocate_tensors()

    input_index = interpreter.get_input_details()[0]["index"]
    output_index = interpreter.get_output_details()[0]["index"]

    interpreter.set_tensor(input_index, image)
    interpreter.invoke()
    predictions = interpreter.get_tensor(output_index)

    result_index = np.argmax(predictions)

    possible_results = ['Left', 'Right', 'Forwards', 'Stay']
    result = possible_results[result_index]

    print(result)


def run_live():

    image_path = '/home/pi/PycharmProjects/autonomous-robot/tmp.jpg'
    
    capture_picture(image_path)

    image_big = Image.open(image_path)
    image = np.asarray(image_big) / 255.0
    image = np.expand_dims(image, axis=0).astype(np.float32)

    interpreter = tf.lite.Interpreter(
    model_path='/home/pi/PycharmProjects/autonomous-robot/trained_models/model_v1/model.tflite')
    interpreter.allocate_tensors()

    input_index = interpreter.get_input_details()[0]["index"]
    output_index = interpreter.get_output_details()[0]["index"]

    interpreter.set_tensor(input_index, image)
    interpreter.invoke()
    predictions = interpreter.get_tensor(output_index)

    result_index = np.argmax(predictions)

    possible_results = ['Left', 'Right', 'Forwards', 'Stay']
    result = possible_results[result_index]

    print(result)


if __name__ == '__main__':

    run_live()
