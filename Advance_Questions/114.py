list_comprehension = [x * 2 for x in range(5)]
print(f"List comprehension: {list_comprehension}")

generator_expression = (x * 2 for x in range(5))
print(f"Generator expression:")
for item in generator_expression:
    print(item)
