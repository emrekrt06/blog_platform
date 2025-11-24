# 📝 Blog Platform

A fully functional blog platform built with **Django**, designed to let users create, edit, and manage blog posts easily.  
The project supports authentication, public/private posts, commenting, and a clean responsive UI.

---

## 🚀 Features

- **User Authentication**
  - Register, login, and logout system.
  - Users can only edit or delete their own posts.
  
- **Post Management**
  - Create, edit, delete, and view posts.
  - Posts can be set as *public* or *private*.
  - Public posts appear in the main feed.

- **Comment System**
  - Users can comment on posts.
  - Comments can be deleted by their owners.
  - Comment moderation system marks deleted comments as empty instead of fully removing them.

- **UI / UX**
  - Clean, responsive design using Bootstrap.
  - Optimized for both mobile and desktop screens.

- **Multi-language Support (Optional)**
  - Designed with future multi-language support in mind (English, Dutch, Turkish).

- **Secure Deployment**
  - Environment variables stored safely with `.env`.
  - Static file handling via **Whitenoise**.
  - Ready for deployment on **Render** or **Railway**.

---

## 🛠️ Tech Stack

- **Backend:** Django 4.2
- **Frontend:** HTML5, CSS3, Bootstrap
- **Database:** SQLite (local) / PostgreSQL (for deployment)
- **Server:** Gunicorn + Whitenoise
- **Version Control:** Git & GitHub

---

# Blog Platform Images

## Main Page
<img width="1728" height="1117" alt="Blog Project Home Page" src="https://github.com/user-attachments/assets/1136559a-7327-4d01-9788-115b28aa062a" />

## My Posts Page
<img width="1728" height="1117" alt="Blog Project My Posts Page" src="https://github.com/user-attachments/assets/6d6486a8-5197-4cc5-83fa-0b197fb2e322" />

##Create New Post Page
<img width="1728" height="1117" alt="Blog Project New Post Creating Page" src="https://github.com/user-attachments/assets/bb845f92-42ce-4a8f-95d2-e73f6c45dbbb" />
