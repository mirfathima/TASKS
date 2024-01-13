#File Handling
def capitalize_file_data():
    with open("product_descriptions.txt", "r") as input_file:
        descriptions = input_file.readlines()

    capitalized_descriptions = []
    for description in descriptions:
        capitalized_description = description.title()  # Capitalize first letter of each word
        capitalized_descriptions.append(capitalized_description)

    with open("formatted_descriptions.txt", "w") as output_file:
        output_file.writelines(capitalized_descriptions)

capitalize_file_data()
