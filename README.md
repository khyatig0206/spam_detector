# Spam Detector Web App

Welcome to the **Spam Detector Web App**! This application is designed to detect spam comments using a K-Nearest Neighbors (KNN) classifier with TF-IDF vectorization. The web app is built using Django and HTMX, and it allows users to register, create comments, and detect spam within those comments.

## Features

- **User Registration**: Users can create an account to access the app's features.
- **Comment Creation**: Registered users can create and post comments on the platform.
- **Spam Detection**: Users can click the "Detect Spam" button to identify spam comments.
- **Spam Highlighting**: After detecting spam, the comments flagged as spam will be highlighted in red.
- **Admin Management**: Admin users have the ability to delete any comments, including spam.

## Technologies Used

- **Django**: The web framework used to build the application.
- **HTMX**: A modern web framework used for enhancing user interaction.
- **K-Nearest Neighbors (KNN) Classifier**: The machine learning algorithm used for spam detection.
- **TF-IDF Vectorizer**: The technique used to convert text into numerical features for spam detection.
- **Dataset**: The spam detection model is trained using the dataset available [here](https://www.kaggle.com/datasets/karthickveerakumar/spam-filter).

## Installation and Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/spam-detector-webapp.git
   cd spam-detector-webapp
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Create a Superuser (Admin)**:
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the App**:
   Open your web browser and go to `http://127.0.0.1:8000`.


![Screenshot (107)](https://github.com/user-attachments/assets/c0e7d515-7193-43bf-ba48-5e449bc70f4e)

![Screenshot (105)](https://github.com/user-attachments/assets/f5b28863-a628-4977-9ba6-474842c58e17)

![Screenshot (109)](https://github.com/user-attachments/assets/16c4f628-d39c-491f-b407-6c4804310b3b)

![Screenshot (106)](https://github.com/user-attachments/assets/26fcf16b-bdba-41f6-87b8-0ceb0f51b6ae)

![Screenshot (101)](https://github.com/user-attachments/assets/c84cca5c-c8b0-4d8c-ba38-28a7aa708f29)

![Screenshot (102)](https://github.com/user-attachments/assets/d42eb8ca-4fb4-44dd-bb9f-d59ea601e842)

![Screenshot (104)](https://github.com/user-attachments/assets/5e6814c3-b013-45ca-a9d6-4ef4c473e9d7)
