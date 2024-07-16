import pyttsx3

engine = pyttsx3.init()

def convert_temperature(temperature, from_unit, to_unit):
    try:
        if from_unit.lower() == "c" and to_unit.lower() == "f":
            return temperature * (9/5) + 32
        elif from_unit.lower() == "f" and to_unit.lower() == "c":
            return (temperature - 32) * (5/9)
        elif from_unit.lower() == "k" and to_unit.lower() == "c":
            return temperature - 273.15
        elif from_unit.lower() == "c" and to_unit.lower() == "k":
            return temperature + 273.15
        elif from_unit.lower() == "f" and to_unit.lower() == "k":
            return (temperature - 32) * (5/9) + 273.15
        elif from_unit.lower() == "k" and to_unit.lower() == "f":
            return (temperature - 273.15) * (9/5) + 32
        else:
            return "Invalid conversion"
    except Exception as e:
        return str(e)

while True:
    # input
    engine.say("Enter the temperature: ")
    engine.runAndWait()
    user = input("Enter the temperature: ")
    try:
        user = float(user)
    except ValueError:
        print("Invalid temperature value. Please enter a number.")
        continue

    # unit
    engine.say("What unit is temperature in? [Celsius(C), Fahrenheit(F), Kelvin(K)]: ")
    engine.runAndWait()
    user_c = input("What unit is temperature in? [Celsius(C), Fahrenheit(F), Kelvin(K)]: ").strip().lower()
    if user_c not in ['c', 'f', 'k']:
        print("Invalid unit. Please enter 'C' for Celsius, 'F' for Fahrenheit, or 'K' for Kelvin.")
        continue

    # convert
    engine.say("Which unit do you want to convert it to?")
    engine.runAndWait()
    con = input("Which unit do you want to convert it to? ").strip().lower()
    if con not in ['c', 'f', 'k']:
        print("Invalid unit. Please enter 'C' for Celsius, 'F' for Fahrenheit, or 'K' for Kelvin.")
        continue

    # output
    converted_temperature = convert_temperature(user, user_c, con)
    if isinstance(converted_temperature, float):
        engine.say(f"{converted_temperature} degrees {con.upper()}")
        print(f"{converted_temperature}°{con.upper()}")
    else:
        engine.say(converted_temperature)
        print(converted_temperature)

    engine.say("Do you want to continue?(yes or no)")
    engine.runAndWait()
    yn = input("Do you want to continue to convert?(y/n)")
    if "n" in yn.lower():
        engine.say("Thank you for using the converter.")
        engine.runAndWait()
        print("Thank you for using the converter.")
        break