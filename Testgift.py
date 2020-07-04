with open("Test Files/menusPortingShop.conf", "r", encoding="utf8") as File1:
    file_contents = File1.read().split(sep="\n")
with open("Test Files/menusPortingShopStacks.conf", "r", encoding="utf8") as File2:
    file_contents2 = File2.read().split(sep="\n")
gifts = []
for thing in file_contents:
    if ("cost=" in thing or "commodity=" in thing) and thing.split(":")[1] not in gifts and thing.split(":")[1] != "rcoin":
        gifts.append(thing.split(":")[1])
for thing in file_contents2:
    if ("cost=" in thing or "commodity=" in thing) and thing.split(":")[1] not in gifts and thing.split(":")[1] != "rcoin":
        gifts.append(thing.split(":")[1])
gifts.sort()
for gift in gifts:
    if gift[-1] == '"':
        print(f'        {gift[:-1]} ' + "{")
        print('            "0" {')
        print(f'                reward="COMMAND:giftplayer %p% {gift[:-1]} 150"')
        print('            }')
        print('        }')
    else:
        print(f'        {gift} ' + "{")
        print('            "0" {')
        print(f'                reward="COMMAND:giftplayer %p% {gift} 150"')
        print('            }')
        print('        }')