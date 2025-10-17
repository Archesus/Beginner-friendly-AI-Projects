import streamlit as st
import cv2
import numpy as np
from PIL import Image
from tensorflow.keras.applications.mobilenet_v2 import (
    MobileNetV2,
    preprocess_input,
    decode_predictions,
)


# Load the pre-trained MobileNetV2 model
def load_model():
    model = MobileNetV2(weights="imagenet")
    return model


# use opencv and numpy to preprocess the image so that it can be fed into the model
def preprocess_image(image):
    img = np.array(image)
    img = cv2.resize(img, (224, 224))
    img = preprocess_input(img)
    img = np.expand_dims(img, axis=0)
    return img


def classify_image(model, image):
    try:
        processed_image = preprocess_image(image)
        predictions = model.predict(processed_image)
        decoded_predictions = decode_predictions(predictions, top=3)[0]
        return decoded_predictions
    except Exception as e:
        st.error(f"Error in classifying image: {str(e)}")
        return None


def main():
    st.set_page_config(
        page_title="AI Image Classifier", page_icon="🤖", layout="centered"
    )
    st.title("🤖 AI Image Classifier")
    st.write("Upload an image, and the AI model will classify it for you!")

    # cache the model loading to improve performance
    @st.cache_resource
    def load_cached_model():
        return load_model()
    
    model = load_cached_model()
    
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        image = st.image(
            uploaded_file, caption="Uploaded image.", use_container_width=True
        )

    btn = st.button("Classify Image")
    
    if btn:
        with st.spinner("Classifying..."):
            image = Image.open(uploaded_file)
            predictions = classify_image(model, image)
            
            if predictions:
                st.subheader("Preedictions:")
                for _, label, score in predictions:
                    st.write(f"**{label}**: {score:.2%}")
                    
if __name__ == "__main__":
    main()
                             
                             

            