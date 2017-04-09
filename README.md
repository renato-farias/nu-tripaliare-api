# nu-tripaliare-api
nu-tripaliare-api



curl -XPUT http://33.33.33.43:8081/api/schedule -d '{"name": "", "img": ""}' -H 'Content-Type: application/json'

curl -XPUT http://33.33.33.43:8080/api/schedule -d '{"name": "", "img": "", "date": "14/10/2017", "time": "10:30", "envs": {"env1": "valor"}}' -H 'Content-Type: application/json'


docker run -d -p 27017:27017 mongo:latest

docker run -d -p 27017:27017 --expose 27017 mongo:latest

docker run -d -p 27017:27017 --net=host --name=mongo mongo:latest
docker run -ti -p 8080:8080 -p 3000:3000/udp --net=host --name=nu-tripaliare-api-8080 nu-tripaliare-api


docker run -ti --env APP_PORT=8081 -p 8081:8081 -p 3000:3000/udp --net=host nu-tripaliare-api

docker run -ti -p 8080:8080 -p 3000:3000/udp --net=host nu-tripaliare-api


docker run -ti -p 8080:8080 -p 3000:3000/udp --link=mongo nu-tripaliare-api -- bash
