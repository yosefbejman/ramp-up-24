import redis
import time

r = redis.Redis(host='redis', port=6379)
pubsub = r.pubsub()
pubsub.subscribe('my_channel')

print("Subscriber started, waiting for messages...")

while True:
    message = pubsub.get_message()
    if message and not message['type'] == 'subscribe':
        print(f"Received message: {message['data'].decode('utf-8')}")
    time.sleep(0.1)
