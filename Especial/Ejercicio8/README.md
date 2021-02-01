### Primero se crea una red de docker:

* sudo docker network create mongo-net

### Para crear el contenedor de mongo se ejecuta el siguiente comando:

* sudo docker run --name mongo -d -p 27017:27017 --network mongo-net mongo

### Para crear el contenedor de redis

* sudo docker run --name redis --network mongo-net -d -p 6379:6379 redis
