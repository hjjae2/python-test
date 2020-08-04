## Testing python2

1. Error: socket.error: [Errno 99] Cannot assign requested address
- jupyter notebook --ip=0.0.0.0 --port=8888 --allow-root

2. pip install test
- pip install pip-install-test
- `import pip_install_test`

3. pip install (force reinstall)
- `pip install django==2.2 --force-reinstall`

4. pip install list
- django, flask, gunicorn (default)
- numpy, pandas
- openpyxl, xlrd
- pytest

5. Django port 
- `python manage.py runserver 0.0.0.0:8080`



## Testing python3

2. pip install test
- pip install pip-install-test
- import pip_install_test

5. Django port
- `python manage.py runserver 0.0.0.0:8080`

6. Run `Tutorial-DRF` project

7. Install jupyter notebook
- `pip install jupyter notebook`
- `jupyter notebook --generate-config`
- `jupyter notebook password`
- https://brunch.co.kr/@mapthecity/16
- https://jupyter-notebook.readthedocs.io/en/stable/public_server.html

8. Using gunicorn
- `gunicorn --bind 0.0.0.0:8000 장고프로젝트이름.wsgi:application`
- https://soyoung-new-challenge.tistory.com/62


## PIP install list
- django, flask, gunicorn (default)
- numpy, pandas
- openpyxl, xlrd
- pytest
- jupyter notebook
