"""Game 'Words'"""


'''def create_file():
    """Create file 'input.txt' with list of cities."""

    

    with open('input.txt', 'w') as file:
        for city in cities:
            file.write(city)
            file.write('\n')'''


def read_text(filename):
    """Read text with file 'input.txt'."""

    with open(filename) as file:
        text = file.read().splitlines()
        #text = [line.rstrip() for line in file]
    return text


def write_data_to_file(filename, list_):
    """Write combine cities to file 'output.txt'."""

    try:
        with open(filename, 'x') as file:
            for word in list_:
                file.write(word)
                file.write('\n')
    except FileExistsError:
        with open(filename, 'a') as file:
            for word in list_:
                file.write(word)
                file.write('\n')


def combine(cities_list):
    """To combine list of cities."""

    def find_world_for_dict(letter):
        result_by_letter = []
        for city in cities_list:
            # print('letter = {}, city = {}'.format(letter, city))
            if letter == city[0].lower():
                # print('letter = {}, city = {}'.format(letter, city))
                result_by_letter.append(city)
        return result_by_letter

    dict_letters = {city[-1]: find_world_for_dict(city[-1]) for city in cities_list}
    #print(dict_letters)

    def recursion_func(letter, sets=[]):

        for key, value in dict_letters.items():
            if letter == key:
                if len(value) == 0:
                    break
                elif len(value) == 1:
                    sets.append(value[0])
                    #print('sets = {}'.format(sets))
                recursion_func(sets[-1][-1], sets)
        return sets

    result_by_cities = []

    for city in cities_list:
        result = [city]
        result += recursion_func(city[-1], sets=[])
        result_by_cities.append(result)
        
    print(result_by_cities)

    main_result = []
    for list_ in result_by_cities:
        if len(list_) > len(main_result):
            main_result = list_

    print(main_result)
    return main_result


def main():
    cities = ["London", "Baiyin", "Aba", "Almetyevsk", "Amol", "Miandoab", "Omsk", "Nacala", "Kalar", "Balashikha",
              "Burgaz", "Zhytomyr", "Radom", "Ladyzin", "Paris", "Stockholm"]

    write_data_to_file('input.txt', cities)    # File 'input.txt' create

    data = read_text('input.txt')              # It's list of cities with file 'input.txt'
    print(data)

    result = combine(data)
    write_data_to_file('output.txt', result)     # Result write to file 'output.txt'


if __name__ == '__main__':
    main()
