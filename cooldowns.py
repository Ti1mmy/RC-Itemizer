inputs = []
while True:
    a = input()
    if a:
        inputs.append(a)
    else:
        break
for thing in inputs:
    if "cooldown=" in thing:
        print(f'{thing.split("=")[1][:-1]}=54325332323')