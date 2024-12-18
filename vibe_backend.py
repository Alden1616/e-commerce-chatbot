import os
import random
from datetime import datetime
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from faker import Faker
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy import func

# Configuration
class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///vibe.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True

# Initialize Flask and Extensions
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
CORS(app)

# Database Models
class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(100), nullable=False)
    image_url = db.Column(db.String(500))
    tags = db.Column(JSON)  # Mood and style tags
    stock = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'category': self.category,
            'image_url': self.image_url,
            'tags': self.tags
        }

class Recommendation(db.Model):
    __tablename__ = 'recommendations'

    id = db.Column(db.Integer, primary_key=True)
    mood = db.Column(db.String(50), nullable=False)
    products = db.Column(JSON)  # Store product IDs
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Utility Functions for Database Population
def generate_product_tags(category):
    mood_tags = ['happy', 'calm', 'energetic', 'relaxed']
    style_tags = ['modern', 'classic', 'trendy', 'minimalist']
    
    return random.sample(mood_tags, 2) + random.sample(style_tags, 2) + [category.lower()]

def populate_database():
    # Clear existing data
    db.session.query(Product).delete()
    db.session.query(Recommendation).delete()
    
    # Create Fake Data
    fake = Faker()
    categories = [
        'Electronics', 'Fashion', 'Home & Living', 
        'Sports & Outdoors', 'Beauty', 'Gifts'
    ]

    products = []
    for _ in range(100):
        category = random.choice(categories)
        product = Product(
            name=fake.catch_phrase(),
            description=fake.paragraph(nb_sentences=3),
            price=round(random.uniform(10, 500), 2),
            category=category,
            image_url=f"https://via.placeholder.com/300x400?text={category.replace(' ', '+')}",
            tags=generate_product_tags(category),
            stock=random.randint(10, 200)
        )
        products.append(product)

    db.session.add_all(products)
    db.session.commit()
    print(f"Populated database with {len(products)} products!")

# API Routes
@app.route('/api/search', methods=['GET'])
def search_products():
    query = request.args.get('q', '').lower()
    mood = request.args.get('mood', '')
    category = request.args.get('category', '')

    # Base query
    products_query = Product.query

    # Filter by query
    if query:
        products_query = products_query.filter(
            func.lower(Product.name).contains(query) | 
            func.lower(Product.description).contains(query)
        )

    # Filter by category
    if category:
        products_query = products_query.filter(Product.category == category)

    # Filter by mood tag
    if mood:
        products_query = products_query.filter(Product.tags.contains(mood))

    # Limit and randomize results
    products = products_query.limit(10).all()
    
    return jsonify([product.to_dict() for product in products])

@app.route('/api/mood-recommendations', methods=['GET'])
def get_mood_recommendations():
    mood = request.args.get('mood', '')
    
    # Predefined mood to category mapping
    mood_category_map = {
        'happy': ['Fashion', 'Beauty', 'Gifts'],
        'shopping': ['Electronics', 'Sports & Outdoors'],
        '🎁': ['Gifts', 'Home & Living'],
        '💡': ['Electronics', 'Home & Living'],
        '😄': ['Fashion', 'Beauty', 'Gifts'],
        '🛍️': ['Electronics', 'Sports & Outdoors']
    }

    categories = mood_category_map.get(mood, [])
    
    # If no specific categories, use all
    if not categories:
        recommendations = Product.query.order_by(func.random()).limit(5).all()
    else:
        recommendations = Product.query.filter(Product.category.in_(categories)) \
                                       .order_by(func.random()) \
                                       .limit(5).all()

    # Create or update recommendation record
    rec = Recommendation(
        mood=mood,
        products=[product.id for product in recommendations]
    )
    db.session.add(rec)
    db.session.commit()

    return jsonify([product.to_dict() for product in recommendations])

# Health Check Route
@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy', 
        'total_products': Product.query.count()
    })

# Application Entry Point
if __name__ == '__main__':
    # Create database tables
    with app.app_context():
        db.create_all()
        
        # Check if database is empty, if so populate
        if Product.query.count() == 0:
            populate_database()
    
    # Run the application
    app.run(debug=True, port=5000)
