def calculate_structure_sum(data):
    def process_element(element):
        total = 0
        if isinstance(element, int):
            total += element
        elif isinstance(element, str):
            total += len(element)
        elif isinstance(element, (list, tuple)):
            for item in element:
                total += process_element(item)
        elif isinstance(element, dict):
            for value in element.values():
                total += process_element(value)
        return total

    return process_element(data)


data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello",
                  ((), [{(2, 'Urban', ('Urban2', 35))}]), 58]

result = calculate_structure_sum(data_structure)
print(result)