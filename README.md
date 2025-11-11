# Retail Recommendation System

A Flask web application that provides personalized product recommendations using machine learning and rule-based approaches.

## Features

- Personalized product recommendations using k-nearest neighbors algorithm
- Interest-based discovery recommendations
- Clean and responsive web interface
- Product catalog display
- Confidence scores for recommendations
- Visual distinction between recommendation types



## Installation

1. Clone this repository
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Train the ML model (optional, pre-trained model included):

```bash
python train_model.py
```

## Usage

1. Run the Flask application:

```bash
python app.py
```

2. Open your web browser and navigate to `http://127.0.0.1:5000/`
3. Enter a User ID (1-4) to get personalized product recommendations

## How It Works

The recommendation system uses three approaches:

1. **ML-based Recommendations**: Uses a k-nearest neighbors model trained on product features to find similar items based on what the user has previously liked
2. **Rule-based Recommendations**: Pre-defined recommendations based on user preferences
3. **Discovery Recommendations**: Additional products that match the user's interests but aren't in their primary recommendations

When a user ID is entered, the system:
1. Retrieves recommendations from all three sources
2. Assigns confidence scores to each recommendation
3. Displays them sorted by confidence score

## Project Structure

- `app.py`: Main Flask application with recommendation logic
- `train_model.py`: Script to train the ML recommendation model
- `recommender_model.pkl`: Pre-trained ML model
- `user_item_matrix.pkl`: User-item interaction data
- `templates/index.html`: HTML template for the web interface
- `requirements.txt`: List of required Python packages

## Machine Learning Model

The recommendation system uses a k-nearest neighbors model from scikit-learn:

- **Algorithm**: k-nearest neighbors (k=3)
- **Features**: Product attributes encoded as binary vectors
- **Training Data**: Synthetic user-item interactions and product features
- **Prediction**: Finds similar products based on feature similarity

## Limitations

- Currently supports only 4 predefined users (IDs 1-4)
- Uses a simplified ML approach with synthetic data
- Limited product catalog (10 items)

## Future Improvements

- Add user registration and login functionality
- Implement collaborative filtering for more accurate recommendations
- Add product images and detailed descriptions
- Allow users to rate products to improve future recommendations
- Train the model on real user interaction data

## Author

[Muhammad Zain](https://github.com/Zayn-Qureshi)

## License

This project is licensed under the MIT License - see the LICENSE file for details. 
