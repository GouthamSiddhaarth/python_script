"""
This script prints a list of numbers from 1 to 100.
Multiples of 3 are printed as "Three" and multiples of 5 are printed as "Five"
and multiples of 3 & 5 are printed as "ThreeFive"
"""
import logging
logging.basicConfig(level=logging.INFO)


def reformat_list(
    start_num: int = 1,
    end_num: int = 100,
    config_list: list = [(3, "Three"), (5, "Five")]
) -> list:
    """Generates a list of numbers and reformat it based on the logic below

    By Default, this function generates numbers from 1 to 100 and
    replace multiples of 3 as "Three" and replace multiples of 5 as "Five" and
    replace multiples of 3 & 5 as "ThreeFive" instead of the number.

    The replacement number and its value is based on the config_list parameter.

    The order of the tuples inside config_list decides the logic of building
    the combination of the replacement value for the numbers which are divisble
    by two or more numbers in the list.

    Example
    If config_list is [(5,"Five"),(3,"Three")] then multiples of 3 & 5 would
    be replaced by "FiveThree"

    Args:
        start_num: fisrt number Of the list
        end_num: last number of the list
        config_list: list of tuples with replacement values for the number
    """
    if config_list:
        logging.info("Building the reformatting list")
        formatted_data = []
        for i in range(start_num, end_num+1):
            replacement_string = ""
            # Builds the replacement string based on the logic mentioned above
            for mod in config_list:
                if i % mod[0] == 0:
                    replacement_string += mod[1]

            if replacement_string == "":
                formatted_data.append(str(i))
            else:
                formatted_data.append(replacement_string)
        logging.info("Reformatted list built")
        return formatted_data
    else:
        logging.warning("Config_list is empty which means no replacement_value")
        number_list = list(range(start_num, end_num+1))
        converted_list = [str(element) for element in number_list]
        return converted_list


def main():
    """This function will call all the functionality required for the script.
    """
    print(', '.join(reformat_list()))


if __name__ == "__main__":
    main()
