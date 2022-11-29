
file = "life-expectancy.csv"
usable_data = []


def make_dict_from_file():
    with open(file) as f:
        content = f.readlines()

        for index, line in enumerate(content):
            if index > 0:
                line_array = line.rstrip('\n').split(',')
                if (line_array[1] != ''):
                    country = {
                        'Country': line_array[0],
                        'Year': int(line_array[2]),
                        'Expectancy': float(line_array[3])
                    }
                    usable_data.append(country)


make_dict_from_file()


def find_lowest(data):
    lowest = {'Expectancy': 200}
    for each in data:
        if each['Expectancy'] < lowest['Expectancy']:
            lowest = each
    return lowest


def find_lowest_in_year(data, year):
    lowest = {'Expectancy': 200}
    for each in data:
        if each['Year'] == year:
            if each['Expectancy'] < lowest['Expectancy']:
                lowest = each
    return lowest


def find_highest(data):
    highest = {'Expectancy': 0}
    for each in data:
        if each['Expectancy'] > highest['Expectancy']:
            highest = each
    return highest


def find_highest_in_year(data, year):
    highest = {'Expectancy': 0}
    for each in data:
        if each['Year'] == year:
            if each['Expectancy'] > highest['Expectancy']:
                highest = each
    return highest


def find_country_stats(data, country):
    country_data = []
    for each in data:
        if each['Country'] == country.title():
            country_data.append(each)

    highest = find_highest(country_data)
    lowest = find_lowest(country_data)

    print()
    print(f"{country.title()} highest: {highest['Expectancy']}")
    print(f"{country.title()} lowest: {lowest['Expectancy']}")
    print()


def ask_for_country():
    country = input('Interest in a specific country? ')
    if country.title() == 'No':
        return
    if country:
        find_country_stats(usable_data, country)


def ask_for_year():
    year = int(input('Enter the year of interest: '))
    if year < 2020:
        if year > 1750:
            lowest = find_lowest(usable_data)
            highest = find_highest(usable_data)
            lowest_year = find_lowest_in_year(usable_data, year)
            highest_year = find_highest_in_year(usable_data, year)

            print()
            print(
                f"The overall max life expectancy is: {highest['Expectancy']} from {highest['Country']} in {highest['Year']}")
            print(
                f"The overall min life expectancy is: {lowest['Expectancy']} from {lowest['Country']} in {lowest['Year']}")
            print()
            print(f'For the year {year}:')
            print(
                f"The max life expectancy was in {highest_year['Country']} with {highest_year['Expectancy']}")
            print(
                f"The min life expectancy was in {lowest_year['Country']} with {lowest_year['Expectancy']}")
        else:
            print('No data, Year too low.')
    else:
        print('No data, Year too high.')


ask_for_country()
ask_for_year()
