<img width="1920" height="1080" alt="Screenshot (1153)" src="https://github.com/user-attachments/assets/62bb456b-6624-4a88-a665-f25c5de910be" />

# 🛒 E-Commerce Website using Django (with Razorpay Payment)

A full-stack **E-commerce web application** built using **Python & Django**, featuring **product management, cart system, Razorpay payment gateway integration, and bill/invoice management**.

This project simulates a **real-world online shopping platform** used in production systems.

---

## 📌 Project Overview

This application allows users to browse products, add items to the cart, complete secure online payments using **Razorpay**, and generate **order bills/invoices** after successful payment.

It is designed to demonstrate **backend logic, payment workflows, and order lifecycle management** in Django.

---
## 🎥 Project Demo

Below is a walkthrough of the E-commerce website, showcasing UI, navigation, and shopping flow including checkout and billing.

![E-commerce Project Demo](project_demo_lightweight.gif)


## 🎯 Features

### 🛍️ Core E-commerce

* Product listing & product detail pages
* Add to cart & cart quantity management
* User authentication (login / register)
* Order placement & tracking
* Admin dashboard for managing products & orders

### 💳 Payment Integration (Razorpay)

* Secure online payments using **Razorpay Payment Gateway**
* Dynamic order amount creation
* Payment verification using Razorpay signature
* Handling payment success & failure callbacks
* Order status update after payment confirmation

### 🧾 Bill / Invoice Management

* Automatic bill generation after successful payment
* Stores:

  * Order ID
  * User details
  * Product list
  * Total amount
  * Payment ID
  * Payment status
* Downloadable invoice (future-ready)
* Admin access to order bills

---

## 🛠️ Tech Stack

* **Backend:** Python, Django
* **Frontend:** HTML, CSS, Bootstrap
* **Database:** SQLite
* **Payment Gateway:** Razorpay
* **Tools:** Git, GitHub
* **Architecture:** Django MVT (Model-View-Template)

---

## 🖼️ Project Demo


(![project_demo_lightweight](https://github.com/user-attachments/assets/0aae3d4d-5822-45c5-9d7c-fc9eb1d040d2)


<img width="1920" height="1080" alt="Screenshot (1147)" src="https://github.com/user-attachments/assets/55b58a4b-8591-4918-881f-2160eec578ba" />


---<img width="1920" height="1080" alt="Screenshot (1148)" src="https://github.com/user-attachments/assets/930e9909-403b-497f-bc46-cb019d3bf8d4" />

<img width="1920" height="1080" alt="Screenshot (1149)" src="https://github.com/user-attachments/assets/4605414f-25b3-4473-84ff-d7354ed6de82" />
<img width="1920" height="1080" alt="Screenshot (1150)" src="https://github.com/user-attachments/assets/a1058219-9cee-4f14-98e1-0cc35e3b6498" />
<img width="1920" height="1080" alt="Screenshot (1151)" src="https://github.com/user-attachments/assets/ccfbcc2f-cf87-4071-a132-81e9407c2782" />
<img width="1920" height="1080" alt="Screenshot (1151)" src="https://github.com/user-attachments/assets/0fdd1837-ac31-4ce3-89d4-0edb1165b41b" />

<img width="1920" height="1080" alt="Screenshot (1152)" src="https://github.com/user-attachments/assets/6ac84d29-ef0a-4af8-bd9c-2cbb337dee97" />

<img width="1920" height="1080" alt="Screenshot (1153)" src="https://github.com/user-attachments/assets/497fea29-dd10-4133-bd12-327e6b49532e" />

<img width="1920" height="1080" alt="Screenshot (1154)" src="https://github.com/user-attachments/assets/e6c5c037-e17c-4c37-a35d-f86b9a6cdee9" />




## 📂 Project Structure

```
E-Commerce-Django/
│
├── ecommerce/          # Project settings
├── store/              # Products & cart
├── orders/             # Orders & billing
├── payments/           # Razorpay integration
├── templates/          # HTML templates
├── static/             # CSS, JS, images
├── media/              # Product images
├── db.sqlite3
├── manage.py
```

---

## 💳 Razorpay Payment Flow (How It Works)

1️⃣ User adds products to cart
2️⃣ Proceeds to checkout
3️⃣ Razorpay order is created dynamically
4️⃣ User completes payment securely
5️⃣ Razorpay returns **payment_id & signature**
6️⃣ Server verifies payment authenticity
7️⃣ Order status updated to **PAID**
8️⃣ Bill/Invoice generated and stored

---

## 🧾 Billing Logic (Database Level)

Each successful order stores:

* Order ID
* User ID
* Product details
* Quantity & price
* Total amount
* Razorpay payment ID
* Payment status
* Timestamp

This enables:
✔ Invoice generation
✔ Order history
✔ Admin reporting

---

## 🚀 Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Dipanshu712/E-Commerce-Django.git
cd E-Commerce-Django
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install django razorpay
```

### 4️⃣ Razorpay Setup

Create `.env` or add in `settings.py`:

```python
RAZORPAY_KEY_ID = "your_key_id"
RAZORPAY_KEY_SECRET = "your_key_secret"
```

### 5️⃣ Run migrations

```bash
python manage.py migrate
```

### 6️⃣ Start server

```bash
python manage.py runserver
```

Open:

```
http://127.0.0.1:8000/
```

---

## 🔐 Admin Panel

```bash
python manage.py createsuperuser
```

Access:

```
http://127.0.0.1:8000/admin/
```

Admins can:

* Manage products
* View orders
* Check payment status
* Access bills/invoices

---

## 📚 Learning Outcomes

* Django project structuring
* Cart & order lifecycle management
* Razorpay payment integration
* Secure payment verification
* Invoice & bill data modeling
* Real-world backend workflows

---

## 🔮 Future Enhancements

* PDF invoice generation
* Email invoice to users
* Django REST Framework APIs
* Payment refunds handling
* Deployment on cloud (Render / AWS)

---

## 👨‍💻 Developer

**Name:** Dipanshu Mishra
**GitHub:** [https://github.com/Dipanshu712](https://github.com/Dipanshu712)
