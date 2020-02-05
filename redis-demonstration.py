import click

@click.group()
def redis_demonstration():
    pass

@redis_demonstration.command()
def cmd1():
    '''Command on redis_demonstration'''
    click.echo('redis_demonstration cmd1')

@redis_demonstration.command()
def cmd2():
    '''Command on redis_demonstration'''
    click.echo('redis_demonstration cmd2')

if __name__ == '__main__':
    redis_demonstration()
