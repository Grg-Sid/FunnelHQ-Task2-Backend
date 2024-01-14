# Task 2

## Post Request to Parse a PDF without Uploading it.
![image](https://github.com/Grg-Sid/FunnelHQ-Task2-Backend/assets/106266279/a0548dcf-e8de-4111-800a-6aecb20d73e9)


## Setting Up
- Clone the repositiory
- Create a python virtual environment and activate it
  <br>
  ```shell
  python3 -m venv .venv
  source .venv/bin/activate
  ```
- Give write access to the setup.sh file
  <br>
  ```shell
  chmod +x setup.sh
  ```
- Run setup.sh to install the required packages and set the appropriate paths
  <br>
  ```shell
  ./setup.sh
  ```
-Run the migrate command

```CMD
python manage.py migrate
```

-Run the backend server on localhost:

```CMD
python manage.py runserver
```

You can access the endpoints from your web browser following this url

```url
http://127.0.0.1:8000
```
