import streamlit as st
import easyocr
import numpy as np
from PIL import Image
import re 

# Load EasyOCR Reader for Hindi and English
reader = easyocr.Reader(['hi', 'en'],gpu=False)

# Function to perform OCR on the image
def ocr_image(uploaded_image):
    image = Image.open(uploaded_image)
    image_np = np.array(image)

    # Perform OCR using EasyOCR
    result = reader.readtext(image_np, detail=0, paragraph=True)
    return " ".join(result)

# Function to search for keywords and highlight them
def highlight_keywords(text, keyword):
    keyword_escaped = re.escape(keyword)
    
    highlighted_text = re.sub(f"({keyword_escaped})", r'<mark>\1</mark>', text, flags=re.IGNORECASE)
    
    return highlighted_text

# Streamlit Page Configuration
st.set_page_config(page_title="OCR & NLP Web App", page_icon="📄", layout="centered")

# Title Section with Custom Styling
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>OCR & Keyword Search Web App</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: grey;'>Upload an image, extract text, and search for keywords with highlights</p>", unsafe_allow_html=True)

# Upload Image Section
st.markdown("### Upload an Image (JPEG, PNG)")
uploaded_image = st.file_uploader("Drag and drop your file here", type=["jpg", "jpeg", "png"])

if uploaded_image:
    # Display the uploaded image with caption
    st.image(uploaded_image, caption='Uploaded Image', use_column_width=True)

    # Add a progress spinner while extracting text
    with st.spinner('Extracting text from the image...'):
        extracted_text = ocr_image(uploaded_image)

    # Display the extracted text in an expander (collapsible section)
    st.markdown("### Extracted Text")
    with st.expander("Click to view the extracted text"):
        st.write(extracted_text)

    # Keyword Search Section
    st.markdown("### Search for a Keyword in the Extracted Text")
    keyword = st.text_input("Enter a keyword to search:")
    if keyword:
        # Progress indicator while searching
        with st.spinner(f'Searching for "{keyword}"...'):
            # Highlight the keyword in the extracted text
            highlighted_text = highlight_keywords(extracted_text, keyword)
        
        # Display the extracted text with highlighted keyword
        st.markdown("### Search Results with Highlighted Keyword")
        st.markdown(highlighted_text, unsafe_allow_html=True)

# Add a horizontal line separator before footer
st.markdown("<hr>", unsafe_allow_html=True)

# Footer Section with Developer Information
st.markdown("""
<div style="text-align: center;">
    <p style="color: grey;">© 2024 Developed by <strong>Syed Naqi Abbas</strong></p>
</div>
""", unsafe_allow_html=True)
