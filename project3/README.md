# AI Image Classifier

An intelligent image classification tool powered by Google's MobileNetV2 deep learning model. Upload an image and instantly get AI-powered predictions of what's in the image!

## Features

- **Fast Image Recognition**: Uses MobileNetV2, a lightweight and efficient neural network
- **Accurate Predictions**: Pre-trained on ImageNet dataset with access to 1000+ object classes
- **Top 3 Predictions**: Displays the three most likely classifications with confidence scores
- **Multiple Format Support**: Works with JPG, JPEG, and PNG image formats
- **User-Friendly Interface**: Built with Streamlit for an intuitive web-based experience
- **Optimized Performance**: Model caching for faster subsequent classifications

## Prerequisites

- Python 3.8 or higher
- TensorFlow/Keras
- Streamlit
- OpenCV
- PIL (Pillow)

## Installation

1. Clone or download this project
2. Navigate to the project directory
3. Install the required dependencies:

```bash
pip install streamlit opencv-python numpy pillow tensorflow
```

Or using `uv`:

```bash
uv add streamlit opencv-python numpy pillow tensorflow
```

## Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

Or with `uv`:

```bash
uv run streamlit run app.py
```

The app will open in your default browser. Then:

1. Click "Choose an image..." to upload an image (JPG, JPEG, or PNG)
2. View a preview of your uploaded image
3. Click "Classify Image" to run the AI classification
4. View the top 3 predictions with confidence percentages

## How It Works

1. **Image Upload**: User uploads an image through the web interface
2. **Preprocessing**: The image is resized to 224x224 pixels and normalized for the model
3. **Classification**: MobileNetV2 processes the image and generates predictions
4. **Results**: Top 3 predictions are decoded and displayed with confidence scores

## Model Details

- **Architecture**: MobileNetV2 (lightweight, efficient CNN)
- **Training Data**: ImageNet dataset (1000+ object classes)
- **Input Size**: 224x224 pixels
- **Output**: Top predictions with confidence scores

## Project Structure

- `app.py` - Main Streamlit application
- `README.md` - This file

## Dependencies

- **streamlit** - Web app framework
- **tensorflow** - Deep learning framework with Keras
- **opencv-python** - Image processing library
- **numpy** - Numerical computing library
- **pillow** - Image processing library

## Performance Notes

- First run takes longer as the MobileNetV2 model is downloaded (~50-100MB)
- Subsequent runs are fast due to model caching
- Model runs efficiently even on CPU
- Best results with clear, well-lit images

## Troubleshooting

**"No module named 'tensorflow'"**
- Install TensorFlow: `pip install tensorflow`
- This may take a few minutes on first install

**"Image format not supported"**
- Only JPG, JPEG, and PNG formats are supported
- Convert your image to one of these formats

**"Error in classifying image"**
- Ensure the image file is valid and not corrupted
- Try uploading a different image
- Check console for detailed error messages

**App is slow on first load**
- This is normal - TensorFlow is initializing and downloading the model
- Subsequent predictions will be much faster

**Out of memory error**
- MobileNetV2 is lightweight but still requires RAM
- Close other applications to free up memory
- Try restarting the app

## Supported Object Classes

The model can classify objects from 1000+ ImageNet categories including:
- Animals (dogs, cats, birds, insects, etc.)
- Vehicles (cars, trucks, bicycles, airplanes, etc.)
- Household items (furniture, appliances, utensils, etc.)
- Nature (plants, flowers, trees, landscapes, etc.)
- Sports and equipment
- Food items
- And many more!

## Limitations

- Works best with clear, well-lit images
- May struggle with very small or partially obscured objects
- Trained on ImageNet, so may not recognize objects outside its training dataset
- Confidence scores reflect model confidence, not accuracy guarantees

## Future Enhancements

Possible improvements:
- Support for multiple image upload and batch classification
- Real-time camera/webcam classification
- Image comparison feature
- Custom model training on user-specific datasets
- Export classification results as reports
- Confidence score filtering
- Image preprocessing options (brightness, contrast adjustment)

## Tips for Best Results

- Use clear, well-lit images
- Ensure the main object is centered in the image
- Use high-quality images when possible
- Avoid heavily edited or blurry images
- For best results, use natural lighting

## License

This is a simple project for learning purposes.
