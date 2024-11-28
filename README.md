# OCR and Document Search Web Application

## Project Overview

This web application enables users to extract text from images and perform keyword searches within the extracted text. Built with **Streamlit** and **EasyOCR**, it supports **Hindi and English** languages. Users can upload an image, view extracted text, and highlight keywords to streamline information discovery.

## Setup Instructions

1. Clone the repository:
    ```
    git clone https://github.com/naqi72/OCR-and-Document-Search-web-Application-Prototype
    
    ```

2. Install the required dependencies
   ```
   pip install -r requirements.txt
   
   ```

3. Run the web application locally:
    ```
    streamlit run app.py
    ```

## Features

- **Text Extraction (OCR)**: Upload a JPEG or PNG image, and the app extracts all readable text.
 
- **Keyword Search and Highlighting**: Enter a keyword to search within the extracted text, which will be highlighted for better readability.
 
- **User-Friendly Interface**: Streamlit-based UI for seamless interaction.


##  Tech Stack:
- **Streamlit**: Fast and modern web framework for creating data-driven apps.
 
- **EasyOCR**: Optical Character Recognition library supporting multiple languages
 
- **Pillow (PIL)**: Image processing capabilities to handle uploaded image files.
 
- **NumPy**: For image conversion and array manipulation.

- **Regular Expressions (re)**: Enables efficient keyword highlighting.






