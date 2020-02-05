import click
import redis
import json
from os import system, name 

def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls')   
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

def load_demonstration_data(redis_connection):
    num_users = 100000
    click.echo(f"Loading session data for {num_users} users.")
    session_data = json.dumps({"token": f"arbitrary token for user", "last_logged_in": 3600})
    for i in range(1, num_users): 
        redis_connection.set(f"session:{i}", session_data)

@click.group()
def redis_demonstration():
    pass

@redis_demonstration.command()
@click.option('--rediss', prompt='Rediss Connection String', help='This is the rediss:// connection string.')
def demo(rediss):
    exit = False
    while (exit == False):
        clear()
        redis_conn = redis.Redis.from_url(url=rediss)
        click.echo(f'Connected to redis instance: {rediss}')
        click.echo("Options:\n" + 
            "1. Load demonstration data\n"
            "10. Exit\n"
        )
        option = click.prompt('Please choose an option: ', type=int)
        if option == 1: 
            load_demonstration_data(redis_conn)
            click.confirm('Data loaded. Hit enter to return to main menu.')
        if option == 10:
            exit = True

if __name__ == '__main__':
    redis_demonstration()
