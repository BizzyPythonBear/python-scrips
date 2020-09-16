import random as rnd

question = input("Ask magic 8 ball a question.")
ans = rnd.randint(1, 8)

if ans == 1:
    print("It is certain")
elif ans == 2:
    print("Outlook good")
elif ans == 3:
    print("You may rely on it")
elif ans == 4:
    print("Ask again later")
elif ans == 5:
    print("Concentrate and ask again")
elif ans == 6:
    print("Reply hazy, try again")
elif ans == 7:
    print("My reply is no")
elif ans == 8:
    print("My sources say no")
else:
    print("That is not a question")
print("The end")