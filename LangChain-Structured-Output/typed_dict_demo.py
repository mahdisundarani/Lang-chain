from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int

new_person: Person = {"name": "Alice", "age": 30}

print(new_person)
# Output: {'name': 'Alice', 'age': 30}
print(type(new_person))
print("hello how ar eyou \n\n")
print("I am fine")