<h1>DJANGO FOR TG BOT</h1>
<h2>HOW TO START</h2>

<h3>IF YOU ON OS FOR HUMANS (MACOS OR LINUX) WHICH SUPPORTS TWO PACKAGES USE PYTHON3 INSTEAD OF PYTHON</h3>
  
Create venv & activate if you needed:
  
```bash
python -m venv env
source env/bin/activate // MAC OR LINUX
cd env\Scripts
activate // WINDOWS
```

Load requirements:
```bash
pip install -r requrements.txt
```

Init django:
```bash
cd schedule
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

<h2>APIs</h2>

api/set_data:
Method: POST

Requires chatId, groupId, degree, studyForm, course in body of Request:

# choices:

degree:

'bachelor', 'magister'

studForm:

'full-time', 'part-time'

example:

```
{
  "chatId": "test_chatId",
  "groupId": "test_groupId",
  "degree": "bachelor",
  "studyForm": "full-time",
  "course": 1
}
```


api/get_group:
Method: GET
Requires chatId in get request:

```
http://127.0.0.1:8000/api/get_group/?chatId=123
```



api/delete_data:
Method: GET
Requires chatId in get request:

```
http://127.0.0.1:8000/api/delete_group/?chatId=123
```