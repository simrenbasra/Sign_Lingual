import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf
from tensorflow.keras.models import load_model

# Create a title
st.title('SignLingual - A Machine Learning Translator App for ASL')

@st.cache_resource()
def load_model():
  model=tf.keras.models.load_model('../model/my_models/VGG_fine_tuned.h5')
  return model

model = load_model()

alphabet = ['a','b','c','d','e','f','g','h','i','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y']

img_file_buffer = st.camera_input("ASL Letter:")

if img_file_buffer is not None:
    # To read image file buffer as a 3D uint8 tensor with TensorFlow:
    bytes_data = img_file_buffer.getvalue()
    img_tensor = tf.io.decode_image(bytes_data, channels=3)

    img_tensor =np.expand_dims(img_tensor, axis = 0)
    img_resized = tf.image.resize(img_tensor, size=[64, 64])

    # Check the type of img_tensor:
    # Should output: <class 'tensorflow.python.framework.ops.EagerTensor'>
    #st.write(type(img_resized))

    # Check the shape of img_tensor:
    # Should output shape: (height, width, channels)ß
    #st.write(img_resized.shape)

    pred_y = np.argmax(model.predict(img_resized))
    st.write(f'Predicted Letter:\n{alphabet[pred_y].upper()}')