# запуск kafka
docker run -p 2181:2181 -p 9092:9092 --name kafka --env ADVERTISED_HOST='192.168.100.11' --env ADVERTISED_PORT=9092 spotify/kafka

# список топиков
docker exec -it kafka bash
/opt/kafka_2.11-0.10.1.0/bin/kafka-topics.sh --zookeeper localhost:2181 --list




