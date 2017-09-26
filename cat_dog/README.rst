===============================
cat_dog
===============================

An api for cat_dog


## Installation instruction

```
virtualenv env -p python3
source env/bin/activate
pip install -r requirements.txt
```


## Running the application

Do not LEAVE the api on as using 0.0.0.0 will be able to receive incoming information.

```
export FLASK_APP=application.py
flask run --host=0.0.0.0 -port=8000
```

Now for some React Native
