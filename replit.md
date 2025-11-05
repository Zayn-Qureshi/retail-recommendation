# Retail Recommendation System

## Overview
A Flask-based web application providing personalized product recommendations using machine learning (k-nearest neighbors) and rule-based approaches. The app features a clean, responsive Bootstrap interface where users can get product recommendations by entering their user ID.

## Project State
- **Status**: Fully functional and running on Replit
- **Last Updated**: November 5, 2025
- **URL**: Accessible via Replit webview on port 5000

## Technology Stack
- **Backend**: Flask 3.1.0 (Python web framework)
- **ML**: scikit-learn 1.5.2 (k-nearest neighbors algorithm)
- **Data Processing**: NumPy 1.26.4, joblib 1.4.2
- **Frontend**: Bootstrap 5.3.0, HTML/CSS
- **Python Version**: 3.11

## Project Structure
```
.
├── app.py                      # Main Flask application
├── train_model.py              # ML model training script
├── requirements.txt            # Python dependencies
├── templates/
│   └── index.html             # Web interface template
├── recommender_model.pkl       # Trained ML model
├── user_item_matrix.pkl        # User-item interaction data
└── mini_recommender.pkl        # Original model file (from import)
```

## Features
1. **ML-based Recommendations**: Uses k-nearest neighbors on product features
2. **Rule-based Recommendations**: Pre-defined recommendations per user
3. **Discovery Recommendations**: Interest-based product suggestions
4. **Confidence Scoring**: Each recommendation shows confidence level
5. **Visual Distinction**: Color-coded badges for different recommendation types (ML=blue, Rule=green, Discovery=purple)

## How It Works
- Supports 4 pre-defined users (IDs 1-4)
- 10 product catalog items with feature vectors
- Combines ML similarity matching with rule-based logic
- Displays recommendations sorted by confidence score

## Replit Configuration
- **Workflow**: `flask-app` running `python app.py`
- **Port**: 5000 (bound to 0.0.0.0 for Replit proxy)
- **Output Type**: webview

## Development Notes
- The app is configured to work with Replit's proxy environment
- ML models are pre-trained and loaded from pickle files
- Debug mode is enabled for development
- All dependencies are managed via requirements.txt

## Deployment Notes
- The app uses Flask's development server
- For production deployment, consider using Gunicorn or uWSGI
- Port 5000 is required for Replit's webview functionality

## User Preferences
None specified yet.

## Recent Changes
- November 5, 2025: Major UI/UX improvements and Replit setup
  - **Design Overhaul**: Implemented modern gradient design with purple theme
  - **Enhanced Layout**: Added responsive cards, better spacing, and visual hierarchy
  - **Improved Badges**: Color-coded recommendation types with confidence percentages
  - **Better Typography**: Integrated Inter font and improved readability
  - **Deployment Ready**: Added Gunicorn for production deployment
  - Initial Replit environment setup:
    - Configured Flask to bind to 0.0.0.0:5000 for Replit proxy
    - Generated ML model files (recommender_model.pkl, user_item_matrix.pkl)
    - Set up workflow for automatic server start
    - Added .gitignore for Python projects
    - Updated requirements.txt with all dependencies
