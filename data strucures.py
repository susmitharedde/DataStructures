numbers = [1, 2, 3, 4, 5]
print("List:", numbers)

colors = ("red", "blue", "green")
print("Tuple:", colors)

student = {
    "name": "Susmitha",
    "branch": "ECE",
    "year": 4
}
print("Dictionary:", student)

unique_numbers = {1, 2, 3, 3, 4, 4}
print("Set:", unique_numbers)


matrix = [
    [1, 2],
    [3, 4]
]
print("Nested List:", matrix)

employees = {
    "emp1": {"name": "Ram", "salary": 25000},
    "emp2": {"name": "Sam", "salary": 30000}
}
print("Nested Dictionary:", employees)


squares = [x*x for x in range(1, 6)]
print("Squares:", squares)


square_dict = {x: x*x for x in range(1, 6)}
print("Dictionary Comprehension:", square_dict)

data = [1, 2, 2, 3, 4, 4, 5]
cleaned_data = list(set(data))
print("Cleaned Data:", cleaned_data)
