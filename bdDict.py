bd = {
    'A': "25/12/2000",
    'B': "31/12/2000",
    'C': "30/12/1999"
}
print(">>> Welcome to birthday dictionary. We know the birthday of:")
for k in bd:
    print(k)

while True:
    print(">>> Who's birthday do you want to look up?")
    name = input()
    print(name, "'s birthday is ", bd[name], sep='')
