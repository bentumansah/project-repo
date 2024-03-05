favourite_number = int(input("Provide your favourite number: "))
secret_number = 7
near_below = 6
near_above = 8
if favourite_number == secret_number:
    print("""You got the secret number.
Congratulations!!!
You won!""")
elif favourite_number < near_below or favourite_number > near_above:
    print("""We are sorry. 
Shoot your better shot next time!""")
elif favourite_number == near_below or favourite_number == near_above:
    print("""You nearly got our secret number.
Keep it up!
Better luck next time!!!""")
else:
    print("You failed the number test.")