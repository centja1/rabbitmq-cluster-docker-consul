import pika, time

connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq.localhost',5672))
channel = connection.channel()

channel.queue_declare(queue='hello',durable=True,arguments={"x-queue-type":"quorum"})

inx = 0
while inx <= 100000:
    channel.basic_publish(exchange='',
                        routing_key='hello',
                        body='Hello World!')
    print(" [x] Sent 'Hello World!'")
    inx += 1
    #time.sleep(0.05)