
#!/usr/bin/env python3
# Created by: Lia Duggan
# Created on: Dec 5th, 2022
# This program prints the users
# mailing address in proper format


def format_address(
    name, street_number, street_name, city, province, postal_code, unit=None
):
    # changes first name to uppercase
    full_name = name.upper()

    # determining if the user lives in an apartment or not
    if unit != None:
        full_name = (
            full_name
            + "\n"
            + unit.upper()
            + "-"
            + street_number.upper()
            + " "
            + street_name.upper()
            + "\n"
            + city.upper()
            + " "
            + province.upper()
            + " "
            + postal_code.upper()
        )
    else:
        full_name = (
            full_name
            + "\n"
            + street_number.upper()
            + " "
            + street_name.upper()
            + "\n"
            + city.upper()
            + " "
            + province.upper()
            + " "
            + postal_code.upper()
        )

    return full_name


def main():
    unit = None

    # Gets the address, postal code and name of the user
    first_name = input("Enter your full name (first and last): ")
    user_housing = input("Do you live in an apartment? (y/n): ")
    if user_housing.upper() == "Y" or user_housing.upper == "YES":
        unit = input("Enter your apartment number: ")
    street_number = input("Enter your street number: ")
    street_name = input("Enter your street name: ")
    city = input("Enter the name of your city: ")
    province = input("Enter the name of your province: ")
    postal_code = input("Enter your postal code: ")

    # Determines what to print depending on if the user lives in an apartment
    if unit != None:
        address = format_address(
            first_name, street_number, street_name, city, province, postal_code, unit
        )
    else:
        address = format_address(
            first_name, street_number, street_name, city, province, postal_code
        )

    print(address)


if __name__ == "__main__":
    main()
