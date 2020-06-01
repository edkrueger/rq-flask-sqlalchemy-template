# redis-demo

## Setup
Run `pipenv install` to install the env.  
Run `pipenv run pre-commit install` to initialize the git hooks.  
Run `pipenv run pre-commit run --all-files` if there are file that were committed before adding the git hooks.  

## Dev Tools
Activate the shell with: `pipenv shell`  
Lint with: `pylint app/`  

## Start Redis for Dev
Get redis docker image: `docker pull redis`  
Start redis: `docker run -d -p 6379:6379 redis`  
Find container id: `docker ps`    
Stop redis: `docker kill <container id>`   

## Redis Queue Management
Start the redis queue worker: `rq worker`  
Empty all redis queues: `rq empty --all`

## Flask App
Start the flask app on dev server: `export FLASK_APP=app.main:app && flask run --reload`  
Start the flask app in production server: `gunicorn app.main:app`  





