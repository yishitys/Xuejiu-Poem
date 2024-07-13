import json

def pop_and_create_new_json(input_file, num, output_file):
    # Read the input JSON file
    with open(input_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Check if the number to pop is greater than the available objects
    if num > len(data):
        print("Error: The number to pop is greater than the available objects in the JSON file.")
        return

    # Pop out the specified number of objects
    popped_data = [data.pop(0) for _ in range(num)]

    # Write the new JSON file with the popped objects
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(popped_data, file, ensure_ascii=False, indent=4)

    # Write the updated original JSON file back
    with open(input_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    print(f"Successfully popped {num} objects and created a new JSON file '{output_file}'.")

# Example usage
input_file = 'test.json'
output_file = 'perplexity_tester.json'
num = 10
pop_and_create_new_json(input_file, num, output_file)
