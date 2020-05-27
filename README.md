# redis-demo

## Start Redis for Dev
Get redis docker image: `docker pull redis`  
Start redis: `docker run -d -p 6379:6379 redis`  
Find container id: `docker ps`    
Stop redis: `docker kill <container id>`   

## Redis Queue Management
Start the redis queue worker: `rq worker`  
Empty all redis queues: `rq empty --all`





