from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Product catalog
products = {
    101: "Wireless Headphones",
    102: "Smart Fitness Tracker",
    103: "E-Reader",
    104: "Portable Charger",
    105: "Bluetooth Speaker",
    106: "Smartphone Case",
    107: "Laptop Sleeve",
    108: "Wireless Mouse",
    109: "USB Flash Drive",
    110: "Smart Watch"
}

# Simple recommendation system based on user preferences
user_preferences = {
    1: {
        "interests": ["audio", "electronics", "portable"],
        "recommended_items": [101, 105, 104]
    },
    2: {
        "interests": ["fitness", "wearables", "health"],
        "recommended_items": [102, 110, 104]
    },
    3: {
        "interests": ["reading", "productivity", "storage"],
        "recommended_items": [103, 109, 107]
    },
    4: {
        "interests": ["computing", "accessories", "office"],
        "recommended_items": [108, 107, 109]
    }
}

# Product features for similarity-based recommendations
product_features = {
    101: ["audio", "wireless", "electronics"],
    102: ["fitness", "wearable", "health"],
    103: ["reading", "electronics", "entertainment"],
    104: ["power", "portable", "electronics"],
    105: ["audio", "wireless", "portable"],
    106: ["protection", "accessories", "smartphone"],
    107: ["protection", "accessories", "laptop"],
    108: ["computing", "wireless", "accessories"],
    109: ["storage", "portable", "data"],
    110: ["wearable", "smart", "fitness"]
}

@app.route('/', methods=['GET', 'POST'])
def recommend():
    if request.method == 'POST':
        try:
            user_id = int(request.form['user_id'])
            
            if user_id < 1 or user_id > 4:
                return render_template('index.html', 
                                      products=products,
                                      error="User ID must be between 1 and 4")
            
            # Get pre-defined recommendations for this user
            recommendations = []
            for item_id in user_preferences[user_id]["recommended_items"]:
                # Generate a confidence score between 0.7 and 0.99
                confidence = round(random.uniform(0.7, 0.99), 2)
                recommendations.append((item_id, confidence))
            
            # Sort by confidence score
            recommendations = sorted(recommendations, key=lambda x: x[1], reverse=True)
            
            return render_template('index.html',
                                  products=products,
                                  recommendations=recommendations)
                                  
        except Exception as e:
            return render_template('index.html', 
                                  products=products,
                                  error=f"Error: {str(e)}")

    return render_template('index.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)