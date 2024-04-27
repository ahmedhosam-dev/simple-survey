# Simple survey project (MVP)

* There is no register
    * Just outh with GitHub
    * Login 

### Setup env and run server
First install **venv** and active it.
```bash
pip install venv
```

Clone project
```bash
git clone https://github.com/ahmedhosam-dev/simple-survey.git

cd simple-survey
```

Install project requirments
```bash
pip install -r requirements.txt
```
Migrate all data
```bash
python manage.py migrate
```
Create super user
```bash
python manage.py createsuperuser
```

Run project
```bash
python manage.py runserver
```