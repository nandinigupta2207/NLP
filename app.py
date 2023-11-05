import streamlit as st
import pytesseract
from PIL import Image
import googletrans

def predict_topic(image):
    # Read the image
    img = Image.open(image)

    # Perform OCR
    text = pytesseract.image_to_string(img)

    # Translate the text
    translator = googletrans.Translator()
    translation = translator.translate(text, dest='en')

    # Apply the LDA model
    topic = lda_model.predict([translation.text])

    # Return the predicted topic
    return topic[0]

# Create a Streamlit app
st.title('Topic Prediction App')

# Input image
image = st.file_uploader('Choose an image')

# Predict the topic
if image:
    topic = predict_topic(image)
    st.write('Predicted topic:', topic)

