import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf
from tensorflow.keras.models import load_model
from matplotlib import pyplot as plt

# Create a title
st.title('SignLingual - A Machine Learning Translator App for ASL')

@st.cache_resource()
def load_model():
  model=tf.keras.models.load_model('../model/my_models/VGG_fine_tuned.h5')
  return model

model = load_model()

alphabet = ['a','b','c','d','e','f','g','h','i','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y']
# Add custom CSS to control camera feed size

img_file_buffer = st.camera_input("ASL Letter:")  
if img_file_buffer is not None:

       # Display uploaded image
    image = Image.open(img_file_buffer)
    
    # Resize and center crop the image to make it 64x64
    width, height = image.size
    aspect_ratio = width / height
    if aspect_ratio > 1:  # Landscape orientation
        new_width = int(64 * aspect_ratio)
        img_resized = image.resize((new_width, 64))
        left = (new_width - 64) // 2
        img_resized = img_resized.crop((left, 0, left + 64, 64))
    else:  # Portrait or square orientation
        new_height = int(64 / aspect_ratio)
        img_resized = image.resize((64, new_height))
        top = (new_height - 64) // 2
        img_resized = img_resized.crop((0, top, 64, top + 64))
    
    # Convert PIL image to numpy array
    img_array = np.array(img_resized)
    st.image(img_array)
    # Expand dimensions to create a batch of size 1
    img_array = np.expand_dims(img_array, axis=0)

    # bytes_data = img_file_buffer.getvalue()
    # img_tensor = tf.io.decode_image(bytes_data, channels=3)
    
    # # To read image file buffer as a 3D uint8 tensor with TensorFlow:

    # st.write(img_tensor.shape)
    # img_tensor =np.expand_dims(img_tensor, axis = 0)

    # img_resized = tf.image.resize(img_tensor, size=[64, 64])
    # img_resized_padded = tf.image.resize_with_pad(img_tensor, 64, 64)
    # #img_resized = tf.cast(img_resized_padded[0], tf.uint8).numpy()     


    pred_y = np.argmax(model.predict(img_array))
    st.write(f'Predicted Letter:\n{alphabet[pred_y].upper()}')