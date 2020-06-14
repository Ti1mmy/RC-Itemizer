with open("Test Files/ItemizationShop.conf", "r", encoding="utf8") as File1:
    file_contents = File1.read().split(sep="\n")
newlist = []
for thing in file_contents:
    if "reward=" in thing and '"COMMAND:."' not in thing:
        newlist.append(thing.split("Lore:")[0] + 'Lore:[\\"§c§lItemized Gift! Non-functional!\\"]}}"')
    else:
        newlist.append(thing)
with open("outputnew.conf", "a", encoding="utf-8") as output:
    for line in newlist:
        output.write(f'{line}\n')
