if __name__ == "__main__":

    # Skapa en tom lista
    empty_list = []

    my_family = ["Oliver", "Zacharias", "Richard"]

    # print(my_family[0])
    # print(my_family[1])
    # print(my_family[2])

    # Lägg till objekt till en lista
    empty_list.append("Jennifer")

    for person in my_family:
        print(person)

    # Ta reda på hur lång en lista här
    length = len(my_family)
    print(length)

    for i in empty_list:
        print(i)

    print(len(empty_list))