# py-todo-list
>Project for Django Practice

## Technological stack

>* python 3.11.8
>* django 5.0.3
>* crispy-bootstrap 2024.1
>* django-crispy-forms 2.1


## Installation instructions

Firstly, you need to install Python3+ 

In terminal write down following commands:

```shell
git clone https://github.com/MaxymChyncha/py-todo-list.git
python -m venv venv
source venv/bin/activate  # for Windows use: venv\scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Also for testing you can load already prepared data:
```shell
python manage.py loaddata todo_list_db_data.json
```
