"""Game 'Words'"""


def read_text(filename):
    """Read text from file."""

    with open(filename) as file:
        text = [line.rstrip() for line in file]
    return text


def write_data_to_file(filename, list_):
    """Write text to file."""

    with open(filename, 'w') as file:
        for city in list_:
            file.write(city)
            file.write('\n')


def combine(cities_list):
    """Combine list of cities."""

    def find_world_for_dict(letter):
        """Create list of worlds started from letter."""

        result_by_letter = []
        for city in cities_list:
            if letter == city[0].lower():
                result_by_letter.append(city)
        return result_by_letter

    """Create dictionary:
       key - letter,
       value - list of cities with first letter same key
    """
    dict_letters = {city[-1]: find_world_for_dict(city[-1]) for city in cities_list}

    def recursion_func(letter, sets):
        """ Create list by city that combine cities so that the next one starts with the last letter of the previous"""

        longer_word = ''
        for city in dict_letters[letter]:
            if city in sets:
                continue
            elif len(longer_word) < len(city):
                longer_word = city
        if longer_word == '':
            return sets
        else:
            sets.append(longer_word)
            return recursion_func(sets[-1][-1], sets)

    result_by_cities = []   # List of lists

    for city in cities_list:
        result_by_cities.append(recursion_func(city[-1], [city]))
        
    main_result = []
    for list_ in result_by_cities:
        if len(list_) > len(main_result):
            main_result = list_

    return main_result


def main():
    #cities = ["London", "Milan", "Stockholm", "Paris"]

    #write_data_to_file('input.txt', cities)    # Create file 'input.txt'

    data = read_text('input.txt')              # It's list of cities with file 'input.txt'

    result = combine(data)
    write_data_to_file('output.txt', result)    # Write result to file 'output.txt'


if __name__ == '__main__':
    main()
