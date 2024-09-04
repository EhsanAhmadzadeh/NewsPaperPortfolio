# News Paper APP - Django Learning Project

Welcome to my Django Twitter Clone project! 🚀 This project is a work in progress as I learn and explore Django. I'm building a simple Blog App with continuously added features to enhance my learning experience.

## 🚧 Project Status
**Current Status**: In development 🛠️ (continuously improving)

This project started as a way for me to learn Django, and I'm adding features as I go. It might still lack polish, but I'm committed to refining it and adding new features regularly.

## 🌟 Features
So far, the app includes the following features:
- User authentication (sign-up, login, logout)
- Create, delete, and edit articles
- Like and commenting functionality
- Basic tweet feed
- Responsive design (in progress)


## 🛠️ Technologies Used
- **Django**: For backend and handling user authentication.
- **HTML/CSS**: Basic UI structure and design.
- **SQLite**: Default database (easy to set up for development).
- **Bootstrap** : To make the app responsive (in progress).

## 📋 How to Install and Run Locally

If you want to clone this project and try it out locally, follow these steps:

### Prerequisites
- Python 3.x
- [Pipenv](https://pipenv.pypa.io/en/latest/)

### Step-by-step instructions:

1. Clone the repository:
   ```bash
   git clone https://github.com/EhsanAhmadzadeh/NewsPaperPortfolio.git
   ```

2. Install dependencies:
    ```bash 
    pipenv install
    ```

3. Run migrations:
    ```bash
    pipenv run python manage.py migrate
    ```
4. Create a superuser to access the Django admin(Optional):
    ```bash
    pipenv run python manage.py createsuperuser
    ```
5. Run the development server:
    ```bash
    pipenv run python manage.py runserver
    ```
6. Open your browser and go to http://127.0.0.1:8000 to see the project.