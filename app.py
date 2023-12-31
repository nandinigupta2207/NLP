import streamlit as st
import pytesseract
from PIL import Image
import googletrans
import pickle
from gensim import corpora 

from gensim.corpora import Dictionary
# Load the dictionary from the uploaded file
dictionary = Dictionary.load('my_dictionary.dict')

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
    unicode_array = [ord(char) for char in translation.text]
    translated_text = [chr(code_point) for code_point in unicode_array]

    new_text_bow = dictionary.doc2bow(translated_text)

    # Apply the LDA model
    new_document_topics = lda_model[new_text_bow]
    dominant_topic = max(new_document_topics, key=lambda x: x[1])
    dominant_topic_num = dominant_topic[0]

# Get the topic label
    topics = { 0: 'Cafe', 1: 'Hotel', 2: 'Transport', 3: 'Retail', 4: 'Tourist Attraction', 5:'Miscellaneous'}
    predicted_topic = topics[dominant_topic_num]
    # Return the predicted topic
    return predicted_topic

# Create a Streamlit app
st.set_page_config(page_title="NLP Invoice Classification", page_icon="📃", layout="wide", initial_sidebar_state="expanded")
st.markdown("<h1 style='text-align: center; color: orange;'>Invoice CLassification- Topic Modelling</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: orange;'>Using OCR, GoogleTrans and LDA</h1>", unsafe_allow_html=True)

# Input image
image = st.file_uploader('Choose an image')

# Predict the topic
if image:
    topic = predict_topic(image)
    st.write('Predicted topic:', topic)

