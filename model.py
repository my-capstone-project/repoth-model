import tensorflow as tf
from tensorflow.keras.utils import load_img, img_to_array
import numpy as np
from PIL import Image

def load_model():
  # Recreate the exact same model, including its weights and the optimizer
  model = tf.keras.models.load_model('model.h5')

  # Show the model architecture
  # model.summary()

  return model

def predict(model, path):
  # Load image
  # path = 'jalan.jpg'
  img = load_img(path, target_size=(300, 300))

  x = img_to_array(img)
  x /= 255
  x = np.expand_dims(x, axis=0)
  images = np.vstack([x])

  # Predict
  classes = model.predict(images, batch_size=20)
  
  return classes