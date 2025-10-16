
movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]
add_count = int(input("How many movies do you want to add? "))
for i in range(add_count):
    name = input(f"Enter name of movie {i+1}: ")
    budget = int(input(f"Enter budget of '{name}': "))
    movies.append((name, budget))

total_budget = sum(budget for _, budget in movies)
average_budget = total_budget / len(movies)
print(f"\nAverage budget: ${average_budget:,.0f}\n")

above_avg = []
for name, budget in movies:
    if budget > average_budget:
        diff = budget - average_budget
        print(f"'{name}' spent ${diff:,.0f} more than average")
        above_avg.append(name)
print(f"\nNumber of movies above average: {len(above_avg)}")

