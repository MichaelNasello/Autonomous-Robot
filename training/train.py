import matplotlib.pyplot as plt
import os

from data import build_dataset
from model import model_v1, convert_model


def train():
    """
    Trains ML model
    """

    x_train, x_test, y_train, y_test = build_dataset()

    neural_net = model_v1()
    neural_net.compile(loss = 'sparse_categorical_crossentropy', metrics = ['sparse_categorical_accuracy'],
                       optimizer = 'adam')

    history = neural_net.fit(x = x_train, y = y_train, epochs = 10, validation_data = (x_test, y_test), shuffle = True)

    save_path = os.path.join('/Users/michaelnasello/PycharmProjects/Autonomous-Robot/trained_models', 'model_v1')
    if not os.path.exists(save_path):
        os.mkdir(save_path)

    neural_net.save(os.path.join(save_path, 'model.h5'))
    convert_model(save_path)

    plt.title('Validation Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss Value')
    plt.plot(history.history['val_loss'])
    plt.savefig(os.path.join(save_path, 'val_loss'))

    plt.close()

    plt.title('Validation Accuracy')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.plot(history.history['val_sparse_categorical_accuracy'])
    plt.savefig(os.path.join(save_path, 'val_sparse_categorical_accuracy'))


if __name__ == '__main__':

    train()
