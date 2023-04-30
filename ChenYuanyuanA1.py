import csv

def main():
    print("Travel Tracker 1.0 - by Lindasy Ward")
    print(count_file(),"places loaded from places.csv")
    show_menu()
    user_input = input(">>> ").upper()
    while user_input != "Q":
        if user_input == "L":
            show_list()
            show_menu()
            user_input = input(">>> ").upper()
        elif user_input == "A":
            add_new_place()
            show_menu()
            user_input = input(">>> ").upper()
        elif user_input == "R":
            recommend_place()
            show_menu()
            user_input = input(">>> ").upper()
        elif user_input == "M":
            mark_visited_place()
            show_menu()
            user_input = input(">>> ").upper()

    print(count_file(),"places saved in places.csv")
    print("Have a nice day :)")
    sort_csv_file()



def show_menu():
    print("Menu:\nL - List place\nR - Recommend random place"
          "\nA = Add new place\nM - Mark a place as visited\nQ - Quit")


def count_file():
    import csv
    with open('places.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        row_count = sum(1 for row in reader)
    return row_count

def show_list():
    with open("places.csv","r") as csvfile:
        reader = csv.reader(csvfile)

        csv_list = [row for row in reader]

        # calculate the max length of each column
        max_column1 = int(max(len(row[0]) for row in csv_list))
        max_column2 = int(max(len(row[1]) for row in csv_list))
        max_column3 = int(max(len(row[2]) for row in csv_list))

        csvfile.seek(0)
        # sort the list in the Arabic number
        sorted_city = sorted(csv_list, key=lambda row: (row[3], int(row[2])))

        row_count = len(sorted_city)
        total_number_of_n = sum(1 for row in sorted_city if row[3] == 'n')
        count = 0
        for row in sorted_city:
            count += 1
            if row[3] == "n":
                city_sign = "*"
            else:
                city_sign = " "
            print(f"{city_sign}{count}. {row[0]:<{max_column1}} in {row[1]:<{max_column2}} {row[2]:>{max_column3}}")

        if total_number_of_n == 0:
            print(f"{row_count} Places. No places left to visit. Why not add a new place?")
        else:
            print(f"{row_count} Places. You still want to visit {total_number_of_n} places.")


def add_new_place():
    city = input("Name: ")
    while city.strip() == "": # error checking
        print("Input can not be blank")
        city = input("Name: ")

    country = input("Country: ")
    while country.strip() == "": # error checking
        print("Input can not be blank")
        country = input("Country: ")

    priority = input("Priority: ")
    while priority.strip() == "": # error checking
        print("Input can not be blank")
        priority = input("Priority: ")

    with open("places.csv", "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([city, country, priority, "n"])

    print(f"{city} in {country} (priority {priority}) added to Travel Tracker")


def recommend_place():
    with open("places.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        # Reverse the order since by default sorted method is in the increasing order
        # But here I want to recommend user has the highest priority place
        sorted_place = sorted([row for row in reader if row[3] == "n"], key=lambda row: int(row[2]), reverse=True)

        if len(sorted_place) > 0:
            print("Not sure where to visit next?")
            recommend_place = sorted_place[0]
            print(f"How about... {recommend_place[0]} in {recommend_place[1]}?")
        else:
            print("No places left to visit")

def mark_visited_place():
    show_list()
    csvfile = open("places.csv","r")
    reader = csv.reader(csvfile)
    csv_list = [row for row in reader]
    csvfile.close()

    unvisited_cities = [row for row in csv_list if row[3] == "n"]
    if len(unvisited_cities) == 0:
        print("No unvisited place.")
        return

    while True:
        user_input = input("Enter the number of a place to mark as visited\n>>> ")
        if not user_input.isnumeric() or int(user_input) not in range(1,len(csv_list)+1):
            print("Invalid input. Please enter a valid number.")
        elif csv_list[int(user_input)-1][3] == "v":
            print(f"You have already visited {csv_list[int(user_input)-1][0]}.")
        else:
            break

    city_index = int(user_input) - 1
    city_name = unvisited_cities[city_index][0]
    country_name = unvisited_cities[city_index][1]
    csv_list[csv_list.index(unvisited_cities[city_index])][3] = 'v'

    with open("places.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        sorted_list = sorted(csv_list, key=lambda row: ('n' if row[3] == 'n' else 'v', int(row[2])))
        writer.writerows(sorted_list)

    print(f"{city_name} in {country_name} visited")

def sort_csv_file():
    with open("places.csv","r") as csvfile:
        reader = csv.reader(csvfile)
        sorted_list = sorted(reader, key=lambda row:(row[3], int(row[2])))

    with open("places.csv", "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(sorted_list)


main()


