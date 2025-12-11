def read_csv_manual(filename):
    data = []
    with open(filename, 'r') as file:
        for line in file:
            row = []
            current = ""
            inside_quotes = False

            for ch in line.strip():
                if ch == '"' :
                    inside_quotes = not inside_quotes
                elif ch == ',' and not inside_quotes:
                    row.append(current)
                    current = ""
                else:
                    current += ch

            row.append(current)
            data.append(row)

    return data

def display_first_ten():
    line_count = 0
    try:
        with open('titanic.csv', 'r') as file:
        
            for line in file:
                row = line.strip().split(',')
                print(row)
                line_count += 1
                if line_count >= 11:
                    break

    except FileNotFoundError:
        print("Error: 'titanic.csv' file not found.")


def calculate_survival_rate(data):
    header = data[0]
    survived_index = header.index("Survived")

    total_passengers = 0
    total_survived = 0

    for row in data[1:]:  
        total_passengers += 1
        if row[survived_index] == '1':
            total_survived += 1

    survival_rate = (total_survived / total_passengers) * 100
    return survival_rate

titanic_data = read_csv_manual('titanic.csv')

rate = calculate_survival_rate(titanic_data)
print(f"Overall survival rate: {rate:.2f}%")


def gender_survival_rate(data):
    header = data[0]
    survived_index = header.index("Survived")
    sex_index = header.index("Sex")

    male_total = 0
    male_survived = 0
    female_total = 0
    female_survived = 0

    for row in data[1:]:
        sex = row[sex_index].lower()
        survived = row[survived_index]

        if sex == "male":
            male_total += 1
            if survived == "1":
                male_survived += 1
        
        elif sex == "female":
            female_total += 1
            if survived == "1":
                female_survived += 1


    male_rate = (male_survived / male_total) * 100
    female_rate = (female_survived / female_total) * 100


    print(f"Male survival rate: {male_rate:.2f}%")
    print(f"Female survival rate: {female_rate:.2f}%")


    if female_rate > male_rate:
        print("Females had a higher survival rate.")
    elif male_rate > female_rate:
        print("Males had a higher survival rate.")
    else:
        print("Both genders had the same survival rate")

    males = round(male_rate, 2)
    females = round(female_rate, 2)

    return males, females


def age_statistics(data):
    header = data[0]
    age_index = header.index("Age")
    survived_index = header.index("Survived")

    ages = []
    survived_ages = []
    not_survived_ages = []

    for row in data[1:]:
        age = row[age_index]


        if age == "" or age.lower() == "nan":
            continue

        age = float(age)
        ages.append(age)


        if row[survived_index] == "1":
            survived_ages.append(age)
        else:
            not_survived_ages.append(age)


    overall_avg = sum(ages) / len(ages) if ages else 0
    survived_avg = sum(survived_ages) / len(survived_ages) if survived_ages else 0
    not_survived_avg = sum(not_survived_ages) / len(not_survived_ages) if not_survived_ages else 0


    youngest = min(ages)
    oldest = max(ages)

    print(f"Average age (all passengers): {overall_avg:.2f}")
    print(f"Average age (survivors): {survived_avg:.2f}")
    print(f"Average age (non-survivors): {not_survived_avg:.2f}")
    print(f"Youngest passenger: {youngest}")
    print(f"Oldest passenger: {oldest}")

    return overall_avg, survived_avg, not_survived_avg, youngest, oldest



def class_statistics(data):
    header = data[0]
    pclass_index = header.index("Pclass")
    survived_index = header.index("Survived")
    fare_index = header.index("Fare")


    

    class1_survived = 0
    class1_total = 0
    class1_fare = 0
    class1_fares_collected = 0

    class2_survived = 0
    class2_total = 0
    class2_fare = 0
    class2_fares_collected = 0

    class3_survived  = 0
    class3_total = 0
    class3_fare = 0
    class3_fares_collected = 0

    for row in data[1:]:
        pclass = row[pclass_index]
        survived = row[survived_index]
        fare = float(row[fare_index])

        if pclass == '1':
            class1_total += 1
            class1_fare += fare
            class1_fares_collected += 1
            if survived == '1':
                class1_survived +=1
        elif pclass == '2':
            class2_total += 1
            class2_fare += fare
            class2_fares_collected += 1
            if survived == '1':
                class2_survived +=1
        elif pclass == '3':
            class3_total += 1
            class3_fare += fare
            class3_fares_collected += 1
            if survived == '3':
                class3_survived += 1 
    class1fare = (class1_fare/class1_fares_collected)*100
    class2fare = (class2_fare/class2_fares_collected)*100
    class3fare = (class3_fare/class3_fares_collected)*100

    faree1 = f"${class1fare:.2f}"
    faree2 = f"${class2fare:.2f}"
    faree3 = f"${class3fare:.2f}"


    print('CLASS 1 STATS')
    print(f'the survival rate for first class passengers is', (class1_survived/class1_total)*100)
    print(f'the average fare of second class passengers was',faree1)
        
    print('CLASS 2 STATS')
    print(f'the survival rate for second class passengers is''', (class2_survived/class2_total)*100)
    print(f'the average fare of second class passengers was', faree2)
    
    print('CLASS 3 STATS')
    print(f'the survival rate for third class passengers is''', (class3_survived/class3_total)*100)
    print(f'the average fare of third class passengers was', faree3,)



        
        
    


def main():
    while True:
        choice = input('''
        1. Display first 10 lines: 
        2. Calculate survival rate
        3. gender survival rate
        4. age stats
        5. class stats
        - ''')
        if choice == '1':
            display_first_ten()
        elif choice == '2':
            rate = calculate_survival_rate(titanic_data)
            print(f"survival rate: {rate:.2f}%")
        elif choice == '3':
            gender_survival_rate(titanic_data)
        elif choice == '4':
            age_statistics(titanic_data)
        elif choice == '5':
            class_statistics(titanic_data)
            


main()



