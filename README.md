This is a test repo for trying to understand some issues I'm encountering with deadlocks. I've packaged it up with docker to make it easy to test in an isolated environment.

To bring up the container and get to a shell

```bash
sudo docker-compose up -d
sudo docker-compose exec web bash
```

Then, start the consumer:

```bash
huey_consumer tasks.huey -w 4
```

And then, separately get yourself a python REPL (might need another `docker-compose exec web bash`):

```python
from tasks import count_beans

count_beans(2) # works fine
count_beans(range(3)) # works fine

count_beans(range(4)) # deadlocks!!
```

To recover from these situations I've restarted the consumer, and ocassionally had to go into `redis-cli` and `DEL huey.redis.app` and then restart the consumer.
