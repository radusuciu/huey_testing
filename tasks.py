from huey import RedisHuey
from redis import ConnectionPool

pool = ConnectionPool(
    host='redis',
    port=6379,
    max_connections=100
)

huey = RedisHuey(
    blocking=True,
    connection_pool=pool,
)

@huey.task()
def check_bean_count(num):
    if num > 0:
        print('We have beans!')
        return True
    
    print('No beans :(')
    return False

@huey.task()
def count_beans(num):
    result = check_bean_count(num)
    result.get(blocking=True)
    print(f'-- counted {num} beans --')
