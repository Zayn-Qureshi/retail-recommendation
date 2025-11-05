from flask import Flask, render_template, request
import random
import numpy as np
import joblib

app = Flask(__name__)

# Load the trained model and user-item matrix
try:
    model = joblib.load('recommender_model.pkl')
    user_item_matrix = joblib.load('user_item_matrix.pkl')
    model_loaded = True
    print("ML model loaded successfully!")
except Exception as e:
    model_loaded = False
    print(f"Error loading ML model: {str(e)}")

# Product catalog - all available products in our store
products = {
    1: "Wireless Headphones",
    2: "Smart Fitness Tracker",
    3: "E-Reader",
    4: "Portable Charger",
    5: "Bluetooth Speaker",
    6: "Smartphone Case",
    7: "Laptop Sleeve",
    8: "Wireless Mouse",
    9: "USB Flash Drive",
    10: "Smart Watch"
}

# Product features for similarity-based recommendations
product_features = {
    1: ["audio", "wireless", "electronics"],
    2: ["fitness", "wearable", "health"],
    3: ["reading", "electronics", "entertainment"],
    4: ["power", "portable", "electronics"],
    5: ["audio", "wireless", "portable"],
    6: ["protection", "accessories", "smartphone"],
    7: ["protection", "accessories", "laptop"],
    8: ["computing", "wireless", "accessories"],
    9: ["storage", "portable", "data"],
    10: ["wearable", "smart", "fitness"]
}

# Item features matrix (same as in train_model.py)
item_features_matrix = np.array([
    [1, 1, 0, 0, 0, 0, 0],  # 1: audio, wireless, electronics
    [0, 0, 1, 1, 0, 0, 0],  # 2: fitness, wearable, health
    [0, 1, 0, 0, 1, 0, 0],  # 3: reading, electronics, entertainment
    [0, 1, 0, 0, 0, 1, 0],  # 4: power, portable, electronics
    [1, 1, 0, 0, 0, 1, 0],  # 5: audio, wireless, portable
    [0, 0, 0, 0, 0, 0, 1],  # 6: protection, accessories, smartphone
    [0, 0, 0, 0, 0, 0, 1],  # 7: protection, accessories, laptop
    [0, 0, 0, 0, 0, 0, 1],  # 8: computing, wireless, accessories
    [0, 0, 0, 0, 0, 1, 0],  # 9: storage, portable, data
    [0, 0, 1, 1, 0, 0, 0],  # 10: wearable, smart, fitness
])

# User preferences database
user_preferences = {
    1: {
        "interests": ["audio", "electronics", "portable"],
        "recommended_items": [1, 5, 4]
    },
    2: {
        "interests": ["fitness", "wearables", "health"],
        "recommended_items": [2, 10, 4]
    },
    3: {
        "interests": ["reading", "productivity", "storage"],
        "recommended_items": [3, 9, 7]
    },
    4: {
        "interests": ["computing", "accessories", "office"],
        "recommended_items": [8, 7, 9]
    }
}

def get_similar_products(user_id, count=1):
    """
    Find additional products similar to user's interests
    but not in their primary recommendations
    """
    if user_id not in user_preferences:
        return []
    
    # Get user interests and already recommended items
    interests = user_preferences[user_id]["interests"]
    already_recommended = user_preferences[user_id]["recommended_items"]
    
    # Score products based on matching features
    product_scores = {}
    for product_id, features in product_features.items():
        # Skip already recommended products
        if product_id in already_recommended:
            continue
        
        # Calculate similarity score based on matching interests
        score = sum(1 for feature in features if feature in interests)
        if score > 0:
            product_scores[product_id] = score
    
    # Get top scoring products
    similar_products = sorted(product_scores.items(), key=lambda x: x[1], reverse=True)[:count]
    return [product_id for product_id, _ in similar_products]

def get_ml_recommendations(user_id, count=3):
    """
    Get recommendations using the trained ML model
    """
    if not model_loaded or user_id < 1 or user_id > 4:
        return []
    
    user_idx = user_id - 1
    user_items = np.where(user_item_matrix[user_idx] == 1)[0]
    
    # Find similar items based on features
    all_recommendations = []
    
    for item_idx in user_items:
        # Get item features from the matrix
        item_features_vector = item_features_matrix[item_idx].reshape(1, -1)
        
        # Find similar items
        try:
            distances, indices = model.kneighbors(item_features_vector)
            
            # Convert to real item IDs and add to recommendations
            for idx in indices[0]:
                if idx not in user_items:  # Don't recommend items the user already has
                    all_recommendations.append(idx + 1)  # +1 because our product IDs start at 1
        except Exception as e:
            print(f"Error getting ML recommendations: {str(e)}")
            continue
    
    # Remove duplicates and limit to top count
    unique_recommendations = list(dict.fromkeys(all_recommendations))[:count]
    return unique_recommendations

@app.route('/', methods=['GET', 'POST'])
def recommend():
    if request.method == 'POST':
        try:
            user_id = int(request.form['user_id'])
            
            if user_id < 1 or user_id > 4:
                return render_template('index.html', 
                                      products=products,
                                      error="User ID must be between 1 and 4")
            
            recommendations = []
            
            # Try to get ML-based recommendations first
            if model_loaded:
                ml_items = get_ml_recommendations(user_id, count=3)
                for item_id in ml_items:
                    # Higher confidence for ML recommendations (0.8-0.99)
                    confidence = round(random.uniform(0.8, 0.99), 2)
                    recommendations.append((item_id, confidence, "ML"))
            
            # If ML recommendations are not available or insufficient, use rule-based
            if not model_loaded or len(recommendations) < 3:
                # Get pre-defined recommendations for this user
                for item_id in user_preferences[user_id]["recommended_items"]:
                    # Only add if not already recommended by ML
                    if item_id not in [r[0] for r in recommendations]:
                        # Generate a confidence score between 0.7 and 0.89
                        confidence = round(random.uniform(0.7, 0.89), 2)
                        recommendations.append((item_id, confidence, "Rule"))
                
                # Add one similar product as a "discovery" recommendation
                similar_products = get_similar_products(user_id, count=1)
                for item_id in similar_products:
                    # Only add if not already recommended
                    if item_id not in [r[0] for r in recommendations]:
                        # Lower confidence for discovery items (0.6-0.75)
                        confidence = round(random.uniform(0.6, 0.75), 2)
                        recommendations.append((item_id, confidence, "Discovery"))
            
            # Sort by confidence score
            recommendations = sorted(recommendations, key=lambda x: x[1], reverse=True)
            
            return render_template('index.html',
                                  products=products,
                                  recommendations=recommendations,
                                  user_id=user_id,
                                  model_loaded=model_loaded)
                                  
        except Exception as e:
            return render_template('index.html', 
                                  products=products,
                                  error=f"Error: {str(e)}",
                                  model_loaded=model_loaded)

    return render_template('index.html', products=products, model_loaded=model_loaded)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)