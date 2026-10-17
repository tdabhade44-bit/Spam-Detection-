# Spam Detection System

## About
Spam Detection System is a Python-based web application that identifies whether a text message is spam or not spam. It provides a login system, a dashboard for message analysis, spam keyword highlighting, detection history, and PDF report generation.

## Technologies Used
- **Python** – Core application logic
- **Flask** – Web application framework
- **SQLite** – Database for storing detection history
- **HTML** – Web page structure
- **CSS** – User interface styling
- **FPDF** – PDF report generation

## Detection Technique
- Keyword-based spam detection
- Predefined spam keyword matching
- Rule-based classification using a probability threshold
- Spam keyword highlighting

## Features
- Admin login and session management
- Interactive spam detection dashboard
- Spam and not-spam classification
- Spam keyword highlighting
- Confidence percentage display based on the keyword ratio
- Detection history stored in SQLite
- PDF report generation
- Logout functionality

## Project Structure
- `app3.py` – Main Flask application and detection logic
- `templates/login.html` – Login page
- `templates/dashboard.html` – Detection dashboard
- `spam.txt` – Sample spam and non-spam messages
- `data.db` – SQLite database
- `report.pdf` – Generated PDF report

## How to Run
1. Install Python.
2. Install the required packages:
   `pip install flask fpdf`
3. Open a terminal in the project directory.
4. Run:
   `python app3.py`
5. Open `http://127.0.0.1:5000/` in your browser.
6. Log in using the credentials configured in `app3.py`.

## Future Improvements
- Integrate a machine-learning model for spam classification
- Train a model using a labelled spam-message dataset
- Improve prediction accuracy using text preprocessing and feature extraction
- Add secure user authentication

## Project Purpose
This project was developed to practice Python programming, Flask web development, database management, text classification, and report generation.
