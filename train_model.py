import numpy as np
import pandas as pd
from sklearn.neighbors import NearestNeighbors
import joblib

# Create synthetic user-item interaction data
# User IDs: 1-4, Item IDs: 1-10

# Create a user-item matrix (1=interaction, 0=no interaction)
user_item_matrix = np.zeros((4, 10))

# User 1 interactions (audio, electronics, portable)
user_item_matrix[0, 0] = 1  # 1: Wireless Headphones
user_item_matrix[0, 3] = 1  # 4: Portable Charger
user_item_matrix[0, 4] = 1  # 5: Bluetooth Speaker

# User 2 interactions (fitness, wearables, health)
user_item_matrix[1, 1] = 1  # 2: Smart Fitness Tracker
user_item_matrix[1, 3] = 1  # 4: Portable Charger
user_item_matrix[1, 9] = 1  # 10: Smart Watch

# User 3 interactions (reading, productivity, storage)
user_item_matrix[2, 2] = 1  # 3: E-Reader
user_item_matrix[2, 6] = 1  # 7: Laptop Sleeve
user_item_matrix[2, 8] = 1  # 9: USB Flash Drive

# User 4 interactions (computing, accessories, office)
user_item_matrix[3, 6] = 1  # 7: Laptop Sleeve
user_item_matrix[3, 7] = 1  # 8: Wireless Mouse
user_item_matrix[3, 8] = 1  # 9: USB Flash Drive

# Create item features matrix
item_features = np.array([
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

# Train a k-nearest neighbors model on item features
model = NearestNeighbors(n_neighbors=3, algorithm='ball_tree')
model.fit(item_features)

# Save the model and data
joblib.dump(model, 'recommender_model.pkl')
joblib.dump(user_item_matrix, 'user_item_matrix.pkl')

print("Model and data saved successfully!")

# Test the model
for user_id in range(1, 5):
    user_idx = user_id - 1
    user_items = np.where(user_item_matrix[user_idx] == 1)[0]
    
    # Get items the user has interacted with
    user_items_real_ids = [item_idx + 1 for item_idx in user_items]
    
    # Find similar items based on features
    all_recommendations = []
    
    for item_idx in user_items:
        # Get item features
        item_features_vector = item_features[item_idx].reshape(1, -1)
        
        # Find similar items
        distances, indices = model.kneighbors(item_features_vector)
        
        # Convert to real item IDs and add to recommendations
        for idx in indices[0]:
            if idx not in user_items:  # Don't recommend items the user already has
                all_recommendations.append(idx + 1)
    
    # Remove duplicates and limit to top 3
    unique_recommendations = list(dict.fromkeys(all_recommendations))[:3]
    
    print(f"User {user_id} liked items {user_items_real_ids}")
    print(f"Recommended items: {unique_recommendations}")
    print() 