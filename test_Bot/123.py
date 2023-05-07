import os

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        print(f'{filename[:-3]}')