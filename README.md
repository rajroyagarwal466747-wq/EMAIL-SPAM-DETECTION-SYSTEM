# Email Spam Detection

A machine learning-powered email spam detector application built with Python and Streamlit.

## Project Overview

This project implements an email spam classification system using **Naive Bayes** machine learning algorithm. The application provides an interactive web interface where users can input email messages and get instant predictions on whether they are spam or legitimate.

## Features

- 🚀 Real-time spam classification
- 📊 Machine learning model trained on labeled email data
- 🎨 User-friendly Streamlit web interface
- 📧 Input validation and error handling
- ✅ Clear visual feedback (spam alerts and success messages)

## Technologies Used

- **Python** - Core language
- **Pandas** - Data manipulation and analysis
- **Scikit-learn** - Machine learning library
  - `CountVectorizer` - Text feature extraction
  - `MultinomialNB` - Naive Bayes classifier
  - `train_test_split` - Data splitting
- **Streamlit** - Web application framework

## Project Structure

```
email-spam-detection/
├── spam.py          # Main application file with ML model and Streamlit UI
├── spam.csv         # Training dataset with email messages and labels
├── main.py          # Placeholder file
└── README.md        # This file
```

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Setup Instructions

1. Clone or download the project:
   ```bash
   cd "email spam detection"
   ```

2. Install required dependencies:
   ```bash
   pip install pandas scikit-learn streamlit
   ```

## Usage

Run the Streamlit application:

```bash
streamlit run spam.py
```

The application will open in your default web browser at `http://localhost:8501`

### How to Use

1. Enter an email message in the text area
2. Click the **"🔍 Analyze Message"** button
3. View the result:
   - ✅ **Not Spam** - Message is legitimate
   - 🚨 **Spam** - Message is flagged as spam

## Model Details

### Dataset

- **Source**: `spam.csv`
- **Labels**: "ham" (legitimate) and "spam"
- **Preprocessing**: 
  - Duplicates removed
  - Labels converted to "Not spam" and "spam"

### Training Process

1. **Data Split**: 80% training, 20% testing
2. **Feature Extraction**: CountVectorizer with English stop words removal
3. **Algorithm**: Multinomial Naive Bayes classifier
4. **Performance**: Model accuracy evaluated on test set

## Files Description

| File | Description |
|------|-------------|
| `spam.py` | Main application containing ML model and Streamlit UI |
| `spam.csv` | Training dataset with email messages and classification labels |
| `main.py` | Placeholder file |
| `README.md` | Project documentation |

## How It Works

1. **Data Loading**: Reads email messages and labels from CSV
2. **Preprocessing**: Cleans data and prepares it for modeling
3. **Feature Extraction**: Converts text to numerical features using CountVectorizer
4. **Model Training**: Trains Naive Bayes classifier on extracted features
5. **Prediction**: Classifies new messages in real-time through the web interface

## Future Enhancements

- Model performance metrics display
- Support for multiple languages
- Batch processing for multiple messages
- Model retraining with new data
- Confidence scores for predictions
- Export results functionality

## Requirements

- `pandas` - Data handling
- `scikit-learn` - ML algorithms
- `streamlit` - Web framework

Install all dependencies at once:

```bash
pip install -r requirements.txt
```

(Note: Create `requirements.txt` with the above packages for easy installation)

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError` | Install missing packages using pip |
| `FileNotFoundError` for spam.csv | Ensure spam.csv is in the same directory as spam.py |
| Port 8501 already in use | Streamlit will automatically use the next available port |

## License

This project is provided as-is for educational purposes.

## Author

Created for email spam detection project.

---

**Note**: This model is trained for demonstration purposes. For production use, consider using more comprehensive datasets and evaluating model performance metrics.
