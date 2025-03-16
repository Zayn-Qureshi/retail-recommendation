# Retail Recommendation System

A simple Flask web application that provides product recommendations based on user preferences.

## Features

- User-based product recommendations
- Simple and intuitive web interface
- Product catalog display
- Confidence scores for recommendations

## Installation

1. Clone this repository
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Run the Flask application:

```bash
python app.py
```

2. Open your web browser and navigate to `http://127.0.0.1:5000/`
3. Enter a user ID (1-4) to get personalized product recommendations

## Project Structure

- `app.py`: Main Flask application with recommendation logic
- `templates/index.html`: HTML template for the web interface
- `requirements.txt`: List of required Python packages

## How It Works

The recommendation system uses predefined user preferences to suggest products. Each user has associated interests and recommended items. When a user ID is entered, the system retrieves the appropriate recommendations and displays them with confidence scores.

## Limitations

- Currently supports only 4 predefined users (IDs 1-4)
- Uses a simplified recommendation approach rather than a machine learning model 