standard_questions = {"First Name": "", "Last Name": "", "Email": "",
                      "Phone Number": "", "Job Title": "", "ID Number": ""}
additional_questions = {"Hair color": "", "Eye color": "",
                        "Starting Month": "", "Additional Training": ""}

# Ask for basic information.
for question in standard_questions:
    standard_questions[question] = input("What is your {}? ".format(question))
for question in additional_questions:
    additional_questions[question] = input("{}? ".format(question))

# print the ID card.
print("the ID Card is: ")
print("----------------------------------------")
print('{}, {}'.format(
    standard_questions["Last Name"].upper(), standard_questions["First Name"]))
print('{}'.format(standard_questions["Job Title"].title()))
print('ID: {}'.format(standard_questions["ID Number"]))
print()
print('{}'.format(standard_questions["Email"].lower()))
print('{}'.format(standard_questions["Phone Number"]))
print(
    f'Hair: {additional_questions["Hair color"]:15} Eyes: {additional_questions["Eye color"]}')
print(
    f'Month: {additional_questions["Starting Month"]:14} Training: {additional_questions["Additional Training"]}')
print("----------------------------------------")
