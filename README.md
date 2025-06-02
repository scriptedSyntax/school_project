```markdown
# 🎓 School Platform – Django Project

Welcome to **School Platform**, a Django-based web application built to simulate a multi-user school system with roles like **Super Admin**, **Admin**, **Teacher**, and **Student**.

This project is great for learning Django with practical, real-world examples of authentication, dashboards, templates, and models.

![Dashboard Preview](dashboard_preview.png)

---

## 📦 Project Structure

```

school\_platform/
├── accounts/            # User management
├── core/                # Core app
├── school\_platform/     # Main settings & routing
├── templates/           # HTML templates
├── db.sqlite3           # SQLite DB
└── manage.py            # Django project manager

````

---

## 🚀 Getting Started

Follow these easy steps to run the project on your local machine.

### 🔧 Prerequisites

- Python 3.10+ installed
- Git installed
- A code editor (VS Code recommended)

---

## 📥 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/school_project.git
cd school_project/school_platform
````

### 2. Create a Virtual Environment

```bash
python -m venv env
```

### 3. Activate the Virtual Environment

* **Windows:**

  ```bash
  env\Scripts\activate
  ```

* **macOS/Linux:**

  ```bash
  source env/bin/activate
  ```

### 4. Install Dependencies

```bash
pip install django
```

---

## 🛠️ Running the Project

### 5. Run Database Migrations

```bash
python manage.py migrate
```

### 6. Create Superuser (Admin Login)

```bash
python manage.py createsuperuser
```

Follow the prompt to set a username and password.

### 7. Start the Development Server

```bash
python manage.py runserver
```

Now open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser!

---

## 🔐 Login Roles

You can log in as:

* **Super Admin**
* **School Admin**
* **Teacher**
* **Student**

> Make sure to register or create users using the Django admin panel at `/admin/`.

---

## 📁 Key Templates

* `registration/login.html`
* `registration/register.html`
* `dashboards/superadmin.html`
* `dashboards/schooladmin.html`
* `dashboards/teacher.html`
* `dashboards/student.html`
* 
---

## 🙋‍♂️ Author & Socials

Made with ❤️ by **@scriptedSyntax**

[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=flat\&logo=twitter\&logoColor=white)](https://twitter.com/scriptedSyntax)
[![GitHub](https://img.shields.io/badge/GitHub-000?style=flat\&logo=github\&logoColor=white)](https://github.com/scriptedSyntax)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat\&logo=linkedin\&logoColor=white)](https://www.linkedin.com/in/scriptedsyntax)

---

## 📝 License

This project is licensed under the [GNU GPLv3 License](LICENSE).

---

Happy coding! 💻✨

```
```
