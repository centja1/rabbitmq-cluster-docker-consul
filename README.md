# rabbitmq-cluster-docker-consul

From a terminal, run 
```sh
docker-compose up -d --scale rabbit=xxxx
```
where xxxx is an odd number of RabbitMQ instances to start.

You can then go to `http://rabbitmq.localhost` and see the cluster, `http://consul.localhost` to see the services registering with the Consul instance, and `http://localhost:8080` to see the Traefik dashboard.


# Sending and receiving messages
Test sending 100,000 messages to a Quorum Queue on the cluster
```sh
python3 RabbitMQ.Send.py
```

Test receiving messages from a Quorum Queue on the cluster
```sh
python3 RabbitMQ.Receive.py
```