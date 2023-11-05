import streamlit as st
import pytesseract
from PIL import Image
import googletrans
import pickle
from gensim import corpora 

from gensim.corpora import Dictionary

# Assuming you have saved the dictionary as 'my_dictionary.dict' in the same directory


# Load the LDA model
with open('lda_model.pkl', 'rb') as f:
    lda_model = pickle.load(f)

def predict_topic(image):
    # Read the image
    img = Image.open(image)

    # Perform OCR
    text = pytesseract.image_to_string(img)

    # Translate the text
    translator = googletrans.Translator()
    translation = translator.translate(text, dest='en')

    new_text_bow = dictionary.doc2bow(translation.text)

    # Apply the LDA model
    new_dominant_topic = lda_model[new_text_bow.text]
    dominant_topic = max(new_document_topics, key=lambda x: x[1])
    dominant_topic_num = dominant_topic[0]

# Get the topic label
    predicted_topic = topics[dominant_topic_num]

    # Return the predicted topic
    return predicted_topic

# Create a Streamlit app
st.title('Topic Prediction App')

# Input image
image = st.file_uploader('Choose an image')

# Predict the topic
if image:
    topic = predict_topic(image)
    st.write('Predicted topic:', predicted_topic)

