# twitter_project

This project is a simple Twitter clone built with Django. It features two core applications: a **Tweet App** for creating and managing tweets and a **History App** for logging user actions, specifically tweet creations.

## Features

-   **Tweet App**: Create new tweets with user authentication.
-   **History App**: Automatically log every new tweet creation using Django Signals.
-   **Django Signals**: A `post_save` signal creates a history entry for each new tweet.
-   **Django Admin**: Provides an administrative interface to manage and view both tweets and history logs.

---

### Prerequisites

-   Python 3.8+
-   Django 4.0+

---

### Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/turtlefishh/twitter_project
    cd twitter_project
    ```

2.  **Create a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the required dependencies:**

    ```bash
    pip install Django
    ```

4.  **Set up the database:**
    Apply the database migrations to create the necessary tables for the `Tweet` and `History` models.

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5.  **Create a superuser:**
    Create an admin user to access the Django admin panel.

    ```bash
    python manage.py createsuperuser
    ```

6.  **Run the development server:**

    ```bash
    python manage.py runserver
    ```

The application will be accessible at `http://127.0.0.1:8000/`.

---

### Usage

#### Creating a Tweet

1.  Log in to the Django admin panel at `http://127.0.0.1:8000/admin/` with your superuser credentials.
2.  Navigate to `http://127.0.0.1:8000/tweets/create/`.
3.  Fill out the form with your tweet content and submit it.

#### Viewing History

Every time a new tweet is created, a corresponding entry will be logged in the **History** app.

1.  Go to the Django admin panel at `http://127.0.0.1:8000/admin/`.
2.  In the `HISTORY` section, click on **Histories**.
3.  You will see a log of all tweet creation actions, including the user, method, tweet content, and timestamp.

---
