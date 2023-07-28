""" You have a non-empty set s, and you have to execute N commands given in N lines.

The commands will be pop, remove and discard. """

n: int = int(input())
s: set = set(map(int, input().split()))
number_commands: int = int(input())

for i in range(number_commands):
    command: str = input()
    
    if "pop" in command:
        s.pop()
    elif "remove" in command:
        commands: list = command.split()
        s.remove(int(commands[1]))
    else:
        commands: list = command.split()
        s.discard(int(commands[1]))

print(sum(s))

