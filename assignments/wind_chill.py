from emoji import emojize


def return_emoji(temperature):
    if temperature < 5:
        return emojize(":ice:")
    if temperature < 15:
        return emojize(":snowman:")
    if temperature < 32:
        return emojize(":snowflake:")
    if temperature < 40:
        return emojize(":cloud:")
    if temperature < 60:
        return emojize(":fallen_leaf:")
    if temperature < 80:
        return emojize(":palm_tree:")
    if temperature > 81:
        return emojize(":pensive_face:")
    if temperature > 100:
        return emojize(":fire:")


def celsius_to_fahrenheit(temperature):
    return temperature * (9 / 5) + 32


def calculate_wind_chill(temperature, wind_speed):
    return 35.74 + 0.6215 * temperature - 35.75 * (wind_speed ** 0.16) + 0.4275 * temperature * (wind_speed ** 0.16)


def calculate_wind_chill_12(temperature):
    for index in range(12):
        calculated = calculate_wind_chill(temperature, (index + 1) * 5)
        emoji = return_emoji(calculated)
        print(
            f"at a temperature of {temperature}F, and a wind speed of {(index + 1) * 5} mph, the wind chill is: {emoji}{calculated:.2f}")


def get_temperature():
    return float(input("What is the temperature: "))


def get_degree_type():
    return input("Fahrenheit or Celsius (F/C)? ")


def run_program():
    temperature = get_temperature()
    degree_type = get_degree_type().upper()
    if degree_type == "C":
        temperature = celsius_to_fahrenheit(temperature)
    calculate_wind_chill_12(temperature)


run_program()
