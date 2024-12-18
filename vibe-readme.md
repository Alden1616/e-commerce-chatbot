# Vibe Shopping Companion 🌞🛍️

## Project Overview

Vibe is an innovative shopping companion web application that provides personalized product recommendations based on user mood and interaction. The application combines a sleek frontend with a robust backend, offering an intuitive and engaging shopping experience.

### Key Features
- 🎭 Mood-based Product Recommendations
- 🔍 Dynamic Product Search
- 📱 Responsive Web Design
- 🤖 AI-Powered Product Matching

## Technology Stack

### Frontend
- HTML5
- CSS3 (with CSS Variables)
- Vanilla JavaScript

### Backend
- Python 3.8+
- Flask
- SQLAlchemy
- Faker (for data generation)

### Database
- SQLite (Development)
- PostgreSQL (Production)

## Project Structure

```
vibe-shopping-companion/
│
├── frontend/
│   └── vibe-shop-chatbot.html       # Main frontend application
│
├── backend/
│   ├── vibe_backend.py               # Flask backend server
│   └── requirements.txt              # Python dependencies
│
├── database/
│   └── vibe.db                       # SQLite database (generated)
│
├── tests/
│   ├── test_backend.py               # Backend unit tests
│   └── test_frontend.js              # Frontend integration tests
│
├── docs/
│   └── technical_documentation.md    # Detailed project documentation
│
├── .env.example                      # Environment configuration template
├── .gitignore
├── LICENSE
└── README.md
```

## Prerequisites

### Frontend
- Modern web browser (Chrome, Firefox, Safari, Edge)
- No additional dependencies required

### Backend
- Python 3.8+
- pip (Python Package Manager)

## Setup and Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/vibe-shopping-companion.git
cd vibe-shopping-companion
```

### 2. Backend Setup
```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

# Install dependencies
pip install -r backend/requirements.txt

# Set environment variables
cp .env.example .env
# Edit .env with your configuration
```

### 3. Run Backend Server
```bash
cd backend
python vibe_backend.py
```

### 4. Run Frontend
- Open `frontend/vibe-shop-chatbot.html` in your web browser

## Configuration

### Environment Variables
- `SECRET_KEY`: Flask application secret key
- `DATABASE_URL`: Database connection string
- `DEBUG`: Enable/disable debug mode

## Available Endpoints

### Backend API Endpoints
- `/api/search`: Product search
- `/api/mood-recommendations`: Get recommendations by mood
- `/api/health`: Application health check

## Testing

### Run Backend Tests
```bash
python -m pytest tests/test_backend.py
```

## Deployment

### Local Deployment
- Ensure all prerequisites are met
- Run backend server
- Open frontend HTML in browser

### Production Deployment
- Use gunicorn or uwsgi for Flask backend
- Configure PostgreSQL database
- Set up CORS and security headers
- Use environment-specific configuration

## Contribution Guidelines

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

### Contribution Areas
- Frontend UI/UX improvements
- Backend recommendation algorithm
- Additional product categories
- Performance optimization

## Known Limitations
- Mock data generation
- Simplified recommendation engine
- No persistent user sessions

## Future Roadmap
- [ ] User authentication
- [ ] Machine learning recommendation system
- [ ] Expanded product database
- [ ] Real-time mood tracking

## License
This project is licensed under the MIT License.

## Authors
- Your Name <your.email@example.com>

## Acknowledgments
- Flask Documentation
- SQLAlchemy ORM
- Faker Library

## Support
For issues or questions, please open a GitHub issue or contact support.

---

**Happy Shopping with Vibe! 🛒✨**
