import playerClass
pl = playerClass.Player(input("Enter your name: "), input("enter your gender"),input("are u bad?"), input("what race are you?: "))
if "no" in pl.bad:
    pl.bad = False
elif "yes" in pl.bad:
    pl.bad = True

print(pl.bad)

