🏆 Models-Hub: A Unified Web Service for ML Predictions
Welcome to Models-Hub, a centralized Flask application designed to deploy and serve multiple machine learning models through a single, clean web interface. This repository currently hosts two distinct prediction services: Spam SMS Classifier and IPL Win Predictor.

✨ Features
Unified Interface: Access all deployed models through a single Flask web application.

Spam SMS Classifier: Predicts whether a given text message is spam or legitimate ("ham").

IPL Win Predictor: Predicts the likely winning team of a live or upcoming IPL cricket match.

Reproducible Environment: Uses requirements.txt for easy environment setup via Conda/pip.

🚀 Getting Started
Follow these steps to get a copy of the project running on your local machine.

Prerequisites
You need Python (3.9+ recommended) and Conda (or Miniconda) installed on your system.

1. Clone the Repository
git clone https://github.com/adityakumar003/Models-Hub.git
cd Models-Hub
2. Create and Activate the Conda Environment
conda create --name models_hub_env python=3.9
conda activate models_hub_env
3. Install Dependencies
pip install -r requirements.txt
4. Run the Application
python app.py

🧠 Deployed Models
The following machine learning assets are integrated into this application (saved as .pkl files).

Model Service	File Name(s)	Function	Libraries Used
Spam SMS Classifier	vectorizer (1).pkl, pipe.pkl	Predicts if a text message is spam (1) or ham (0). The vectorizer transforms text data for the classifier pipeline.	scikit-learn, joblib
IPL Win Predictor	model (1).pkl	Predicts the probability of an IPL team winning based on current game state or pre-match statistics.	scikit-learn, joblib, (and possibly pandas)

📂 Project Structure
The repository is structured following standard Flask conventions:

Models-Hub/
├── templates/
│   ├── m1.html         # UI for one model (e.g., Spam Classifier)
│   ├── m2.html         # UI for the second model (e.g., IPL Predictor)
│   └── page.html       # Landing/Index page
├── app.py              # Main Flask application file and routing logic
├── requirements.txt    # List of project dependencies for deployment
├── model (1).pkl       # IPL Win Predictor Model
├── pipe.pkl            # Spam Classifier Pipeline Model
├── vectorizer (1).pkl  # Text Vectorizer (for Spam Classifier)
└── README.md           # You are here!


🛠️ Tech Stack
Component	Technology	Role
Backend Framework	Flask	Serving the web pages and handling API requests.
Machine Learning	Scikit-learn, joblib	Training, saving, and loading the prediction models.
Data Handling	NumPy, Pandas	Numerical operations and data preprocessing.
Environment	Conda/pip	Dependency and virtual environment management.


🤝 Contributing
Contributions are welcome! If you have suggestions for new models, improvements to the Flask interface, or better deployment strategies, please feel free to open an issue or submit a pull request.
