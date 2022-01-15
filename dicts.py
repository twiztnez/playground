if __name__ == "__main__":
    # Skapa en tom dict
    empty_dict = {}

    user_dict = {"name": "Zacharias",
                 "age": 21,
                 "income_type": "arbetssökande",
                 "income": 0,
                 "number_of_children": 0,
                 "mobile_number": "0736018384",
                 "email": "zacharias@hotmail.com"}

    # Loopa igenom nycklar

    for key in user_dict.keys():
        print(key)

    # Loopa igenom värden

    for value in user_dict.values():
        print(value)

    # Loopa igenom nycklar & värden

    for item in user_dict.items():
        print(item)

    if "bajs" in user_dict.keys():
        print("Hello")
    else:
        print("Not found")

    # Lägg till något till en dict

    user_dict["student"] = True

    print(user_dict)

    # Ta bort en nyckel från en dict
    user_dict.pop("age", None)

    print(user_dict)