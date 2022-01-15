"""
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:

Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)
"""


def get_when_user_turn_100(age, birthday, copies):

    year_now = 2022

    birth_year = year_now - int(age)

    turn_hundred_year = birth_year + 100

    if birthday == "nej":
        turn_hundred_year = turn_hundred_year - 1

    count = 0
    while count < int(copies):
        print(f"Hej {name}, du kommer fylla 100 år {turn_hundred_year} \n")
        count += 1


if __name__ == "__main__":
    name = input("Vad heter du? ")
    age = input("Hur gammal är du? ")
    birthday = input("Har du firat din födelsedag i år? (ja/nej). ")
    copies = input("Hur många gånger vill du att jag ska meddela dig? ")

    get_when_user_turn_100(age, birthday, copies)
