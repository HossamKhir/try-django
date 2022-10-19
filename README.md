# Try-Django

Learn Django bit by bit in this series.

```sh
source .env/bin/activate
mkdir src
cd src
django-admin startproject trydjango .
python3 manage.py createsuperuser
```

---

```sh
python3 manage.py migrate
python3 manage.py startapp products
```

---

```sh
python3 manage.py makemigrations
python3 manage.py migrate
```

---

```py
from products.models import Product
Product.objects.all() # query all products in database
Product.objects.create(
    title="",
    description="",
    price=0.0,
    summary="",
    featured=True
)
```

---

```sh
mkdir templates
cd templates
touch base.html home.html about.html contact.html navbar.html
cd ../
```
