from __future__ import division
import ast
import datetime
import os
import logging
import random
from multiprocessing import Pool
from tqdm import *
import time
import matplotlib.pyplot as plt
import numpy as np

grid = []
multiprocessing_grid = []
grid_key = []
grid_setting = []


def fibonacci_sequence(n):
    # This function returns the fibonacci number sequence.
    # "n" specifies how long the list should be.

    fibonacci_list = []
    a = 0
    b = 1

    for i in range(0, n):
        fibonacci_list.append(a)

        c = a + b
        a = b
        b = c

    return fibonacci_list


def prime_numbers(n):
    # This function returns a list of prime numbers.
    # "n" specifies how long the list should be.

    prime_numbers_list = []
    start = 0
    num = 0
    while start != n:

        if num > 1:  # all prime numbers are greater than 1
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                prime_numbers_list.append(num)
                start += 1
        num += 1

    return prime_numbers_list


def generate_grid_setting(number_of_lists_in_grid, length_of_message, list_step, ):

    start_time = time.time()
    logging.info("Start Time: " + str(start_time))

    number_of_constants = 13

    # COMPILING GRID SETTING:
    # -------------------------------------------------------------------------
    # for i in tqdm(range(number_of_lists_in_grid), desc="Compiling Grid Setting... "):
    for i in range(number_of_lists_in_grid):
        # If you want to include the fibonacci_sequence and prime_numbers function.
        # Then change the 2 to a 0. This will make the list of numbers more random, but
        # will require more processing power and you will not be abel to draw a table/graph.
        list_constant_num = random.randint(0, number_of_constants - 1)  # <<<<<<@@@@@@@@@@@@@@@@@@@@@@@@@

        new_list_step = random.randint(0, list_step)
        new_length_of_message = length_of_message + new_list_step

        num = i

        grid_setting.append([num, list_constant_num, new_list_step, new_length_of_message, number_of_lists_in_grid])

    logging.info("grid_setting: " + str(grid_setting))
    # -------------------------------------------------------------------------

    return grid_setting


def math_constants_list(constant, n):

    # LIST OF CONSTANTS:
    # -----------------------------------------------------------------
    # "twin_prime_constant"
    # "pi"
    # "degree"
    # "base_of_natural_logarithm"
    # "golden_ratio"
    # "eulers_constant"
    # "catalans_constant"
    # "aperys_constant"
    # "khinchins_constant"
    # "glaishers_constant"
    # "mertens_constant"
    # -----------------------------------------------------------------

    try:
        # import version included with old SymPy
        from sympy.mpmath import mp
    except ImportError:
        # import newer version
        from mpmath import mp

    mp.dps = n  # set number of digits

    if constant == "twin_prime_constant":
        n1 = n
        while True:
            mp.dps = n1
            mc = str(mp.twinprime)
            mc = mc[0: 1:] + mc[1 + 1::]  # Takes comma out
            mc = list(mc)
            mc = mc[:n1]

            if len(mc) >= n:

                while True:

                    if len(mc) == n:
                        return mc
                    del mc[len(mc) - 1]
            n1 += 1

    elif constant == "pi":

        n1 = n

        while True:

            mp.dps = n1
            mc = str(mp.pi)
            mc = mc[0: 1:] + mc[1 + 1::]  # Takes comma out
            mc = list(mc)
            mc = mc[:n1]

            if len(mc) >= n:

                while True:

                    if len(mc) == n:
                        return mc
                    del mc[len(mc) - 1]
            n1 += 1

    elif constant == "degree":

        n1 = n

        while True:

            mp.dps = n1
            mc = str(mp.degree)
            mc = mc[0: 1:] + mc[1 + 1::]  # Takes comma out
            mc = list(mc)
            mc = mc[:n1]

            if len(mc) >= n:

                while True:

                    if len(mc) == n:
                        return mc
                    del mc[len(mc) - 1]
            n1 += 1

    elif constant == "base_of_natural_logarithm":

        n1 = n

        while True:

            mp.dps = n1
            mc = str(mp.e)
            mc = mc[0: 1:] + mc[1 + 1::]  # Takes comma out
            mc = list(mc)
            mc = mc[:n1]

            if len(mc) >= n:

                while True:

                    if len(mc) == n:
                        return mc
                    del mc[len(mc) - 1]
            n1 += 1

    elif constant == "golden_ratio":

        n1 = n

        while True:

            mp.dps = n1
            mc = str(mp.phi)

            mc = mc[0: 1:] + mc[1 + 1::]  # Takes comma out
            mc = list(mc)
            mc = mc[:n1]

            if len(mc) >= n:

                while True:

                    if len(mc) == n:
                        return mc
                    del mc[len(mc) - 1]
            n1 += 1

    elif constant == "eulers_constant":

        n1 = n

        while True:

            mp.dps = n1
            mc = str(mp.euler)
            mc = mc[0: 1:] + mc[1 + 1::]  # Takes comma out
            mc = list(mc)
            mc = mc[:n1]

            if len(mc) >= n:

                while True:
                    if len(mc) == n:
                        return mc
                    del mc[len(mc) - 1]
            n1 += 1

    elif constant == "catalans_constant":

        n1 = n

        while True:

            mp.dps = n1
            mc = str(mp.catalan)
            mc = mc[0: 1:] + mc[1 + 1::]  # Takes comma out
            mc = list(mc)
            mc = mc[:n1]

            if len(mc) >= n:

                while True:
                    if len(mc) == n:
                        return mc
                    del mc[len(mc) - 1]
            n1 += 1

    elif constant == "aperys_constant":

        n1 = n

        while True:

            mp.dps = n1
            mc = str(mp.apery)
            mc = mc[0: 1:] + mc[1 + 1::]  # Takes comma out
            mc = list(mc)
            mc = mc[:n1]

            if len(mc) >= n:

                while True:
                    if len(mc) == n:
                        return mc
                    del mc[len(mc) - 1]
            n1 += 1

    elif constant == "khinchins_constant":

        n1 = n

        while True:
            mp.dps = n1
            mc = str(mp.khinchin)
            mc = mc[0: 1:] + mc[1 + 1::]  # Takes comma out
            mc = list(mc)
            mc = mc[:n1]

            if len(mc) >= n:

                while True:
                    if len(mc) == n:
                        return mc
                    del mc[len(mc) - 1]
            n1 += 1

    elif constant == "glaishers_constant":

        n1 = n

        while True:

            mp.dps = n1
            mc = str(mp.glaisher)
            mc = mc[0: 1:] + mc[1 + 1::]  # Takes comma out
            mc = list(mc)
            mc = mc[:n1]

            if len(mc) >= n:

                while True:
                    if len(mc) == n:
                        return mc
                    del mc[len(mc) - 1]
            n1 += 1

    elif constant == "mertens_constant":

        n1 = n

        while True:
            mp.dps = n1
            mc = str(mp.mertens)
            mc = mc[0: 1:] + mc[1 + 1::]  # Takes comma out
            mc = list(mc)
            mc = mc[:n1]

            if len(mc) >= n:

                while True:
                    if len(mc) == n:
                        return mc
                    del mc[len(mc) - 1]
            n1 += 1

    else:
        logging.warning("Error: math_constants_list")
        return "Error: math_constants_list"


def run_math_constants(n):

    # n0 = n[0]   # num
    n1 = n[1]  # list_constant_num (Which math constant is chosen)
    n2 = n[2]  # new_list_step
    n3 = n[3]  # new_length_of_message (length_of_message + random_added_stepper[i])
    # n4 = n[4]   # number_of_lists_in_grid

    if n1 == 0:
        grid_key.append(0)
        grid.append(fibonacci_sequence(n3)[n2:])

    elif n1 == 1:
        grid_key.append(1)
        grid.append(prime_numbers(n3)[n2:])

    elif n1 == 2:
        grid_key.append(2)
        grid.append(math_constants_list("twin_prime_constant", n3)[n2:])

    elif n1 == 3:
        grid_key.append(3)
        grid.append(math_constants_list("pi", n3)[n2:])

    elif n1 == 4:
        grid_key.append(4)
        grid.append(math_constants_list("degree", n3)[n2:])

    elif n1 == 5:
        grid_key.append(5)
        grid.append(math_constants_list("base_of_natural_logarithm", n3)[n2:])

    elif n1 == 6:
        grid_key.append(6)
        grid.append(math_constants_list("golden_ratio", n3)[n2:])

    elif n1 == 7:
        grid_key.append(7)
        grid.append(math_constants_list("eulers_constant", n3)[n2:])

    elif n1 == 8:
        grid_key.append(8)
        grid.append(math_constants_list("catalans_constant", n3)[n2:])

    elif n1 == 9:
        grid_key.append(9)
        grid.append(math_constants_list("aperys_constant", n3)[n2:])

    elif n1 == 10:
        grid_key.append(10)
        grid.append(math_constants_list("khinchins_constant", n3)[n2:])

    elif n1 == 11:
        grid_key.append(11)
        grid.append(math_constants_list("glaishers_constant", n3)[n2:])

    elif n1 == 12:
        grid_key.append(12)
        grid.append(math_constants_list("mertens_constant", n3)[n2:])


def run_math_constants_multiprocessing(n):

    n0 = n[0]  # num
    n1 = n[1]  # list_constant_num (Which math constant is chosen)
    n2 = n[2]  # new_list_step
    n3 = n[3]  # new_length_of_message (length_of_message + random_added_stepper[i])
    n4 = n[4]  # number_of_lists_in_grid

    if n1 == 0:
        grid_key.append(0)
        return fibonacci_sequence(n3)[n2:]

    elif n1 == 1:
        grid_key.append(1)
        return prime_numbers(n3)[n2:]

    elif n1 == 2:
        grid_key.append(2)
        return math_constants_list("twin_prime_constant", n3)[n2:]

    elif n1 == 3:
        grid_key.append(3)
        return math_constants_list("pi", n3)[n2:]

    elif n1 == 4:
        grid_key.append(4)
        return math_constants_list("degree", n3)[n2:]

    elif n1 == 5:
        grid_key.append(5)
        return math_constants_list("base_of_natural_logarithm", n3)[n2:]

    elif n1 == 6:
        grid_key.append(6)
        return math_constants_list("golden_ratio", n3)[n2:]

    elif n1 == 7:
        grid_key.append(7)
        return math_constants_list("eulers_constant", n3)[n2:]

    elif n1 == 8:
        grid_key.append(8)
        return math_constants_list("catalans_constant", n3)[n2:]

    elif n1 == 9:
        grid_key.append(9)
        return math_constants_list("aperys_constant", n3)[n2:]

    elif n1 == 10:
        grid_key.append(10)
        return math_constants_list("khinchins_constant", n3)[n2:]

    elif n1 == 11:
        grid_key.append(11)
        return math_constants_list("glaishers_constant", n3)[n2:]

    elif n1 == 12:
        grid_key.append(12)
        return math_constants_list("mertens_constant", n3)[n2:]


def generate_grid(generate_grid_setting):

    start_time = time.time()

    for i in tqdm(generate_grid_setting, desc="Building grid... "):
        run_math_constants(i)

    logging.info("Normal_grid: " + str(grid))

    end_time = time.time() - start_time

    logging.info(f'Building grid took {end_time} time.')

    return grid


def generate_grid_multiprocessing(generate_grid_setting):

    start_time = time.time()

    logging.info("Building Grid...")

    p = Pool(os.cpu_count())
    multiprocessing_grid.append(p.map(run_math_constants_multiprocessing, generate_grid_setting))

    end_time = time.time() - start_time

    logging.info(f'Building grid with multiprocessing took {end_time} time.')
    logging.info("Multiprocessing_grid: " + str(multiprocessing_grid[0]))
    return multiprocessing_grid[0]


def generate_table_and_positive_sin_graph(grid, number_of_lists_in_grid, length_of_message):

    plt.rcParams['figure.figsize'] = ((number_of_lists_in_grid / 2), 4.55)

    x = np.arange(0, length_of_message, 0.1)  # start,stop,step
    y = ((number_of_lists_in_grid / 2) - 1) * (np.sin((x) * np.pi / 20))

    # ---------------------------------------------------------------------------
    # Get x,y coordinates
    # ---------------------------------------------------------------------------
    x_list = []
    y_list = []

    logging.info("Sin Graph:")
    for i in range(length_of_message + 1):
        logging.info("x = " + str(i) + " ; y = " + str(int((number_of_lists_in_grid / 2) - 1) * (np.sin((i) * np.pi / 20))))
        x_list.append(int(i))
        y_list.append(int((number_of_lists_in_grid / 2) - 1) * (np.sin((i) * np.pi / 20)))
    # ---------------------------------------------------------------------------

    # ---------------------------------------------------------------------------
    # Now lets construct the colors array.
    # ---------------------------------------------------------------------------
    length_of_message_colors_list = []
    full_color_list = []
    new_series = []
    for i in range(number_of_lists_in_grid):

        for i in range(length_of_message):
            length_of_message_colors_list.append('w')

        full_color_list.append(length_of_message_colors_list)
        length_of_message_colors_list = []

    for i in range(length_of_message):
        y_position = int(round((number_of_lists_in_grid / 2) - y_list[i]))
        x_position = int(round(x_list[i]))

        logging.info('y_position: ' + str(y_position) + ' x_position: ' + str(x_position))
        full_color_list[y_position - 1][x_position] = '#1ac3f5'

        new_series.append(grid[y_position - 1][x_position])

    logging.info('full_color_list' + str(full_color_list))
    logging.info('\nnew_series: ' + str(new_series))

    # ---------------------------------------------------------------------------

    x_ = []
    for i in range(int(length_of_message / 10)):
        x_.append(((i + 1) * 10))
    logging.info('x_' + str(x_))

    y_ = []
    for i in range(int(number_of_lists_in_grid)):
        y_.append(((i + 1) - 0.5) - (number_of_lists_in_grid / 2))
    logging.info('y_' + str(y_))

    fig, ax = plt.subplots()
    ax.axis('tight')
    ax.axis('on')

    plt.plot(x, y, color='#ff0000')  # The graph was made for testing and will display best if length_of_message == 40 and number_of_lists_in_grid == 23
    the_table = ax.table(cellText=grid, loc='center', cellLoc='center', cellColours=full_color_list)
    plt.yticks(y_)
    plt.xticks(x_)
    plt.show()


def generate_table_and_negative_sin_graph(grid, number_of_lists_in_grid, length_of_message):

    #----------------------------------------------------------------------------------------
    # THIS FUNCTION DOES NOT WORK, STILL TRYING TO FIGURE OUT WHY...
    #----------------------------------------------------------------------------------------

    plt.rcParams['figure.figsize'] = ((number_of_lists_in_grid / 2), 4.55)

    x = np.arange(0, length_of_message, 0.1)  # start,stop,step
    y = (-1*((number_of_lists_in_grid / 2)) - 1) * (np.sin((x) * np.pi / 20))

    # ---------------------------------------------------------------------------
    # Get x,y coordinates
    # ---------------------------------------------------------------------------
    x_list = []
    y_list = []

    logging.info("Sin Graph:")
    for i in range(length_of_message + 1):
        logging.info(
            "x = " + str(i) + " ; y = " + str(int((-1*(number_of_lists_in_grid / 2) - 1)) * (np.sin((i) * np.pi / 20))))
        x_list.append(int(i))
        y_list.append(int((-1*(number_of_lists_in_grid / 2) - 1)) * (np.sin((i) * np.pi / 20)))
    # ---------------------------------------------------------------------------

    # ---------------------------------------------------------------------------
    # Now lets construct the colors array.
    # ---------------------------------------------------------------------------
    length_of_message_colors_list = []
    full_color_list = []
    new_series = []
    for i in range(number_of_lists_in_grid):

        for i in range(length_of_message):
            length_of_message_colors_list.append('w')

        full_color_list.append(length_of_message_colors_list)
        length_of_message_colors_list = []

    for i in range(length_of_message):
        y_position = int(round((number_of_lists_in_grid / 2) - y_list[i]))
        x_position = int(round(x_list[i]))

        logging.info('y_position: ' + str(y_position) + ' x_position: ' + str(x_position))
        full_color_list[y_position - 1][x_position] = '#1ac3f5'

        new_series.append(grid[y_position - 1][x_position])

    logging.info('full_color_list' + str(full_color_list))
    logging.info('\nnew_series: ' + str(new_series))

    # ---------------------------------------------------------------------------

    x_ = []
    for i in range(int(length_of_message / 10)):
        x_.append(((i + 1) * 10))
    logging.info('x_' + str(x_))

    y_ = []
    for i in range(int(number_of_lists_in_grid)):
        y_.append(((i + 1) - 0.5) - (number_of_lists_in_grid / 2))
    logging.info('y_' + str(y_))

    fig, ax = plt.subplots()
    ax.axis('tight')
    ax.axis('on')

    plt.plot(x, y,
             color='#ff0000')  # The graph was made for testing and will display best if length_of_message == 40 and number_of_lists_in_grid == 23
    the_table = ax.table(cellText=grid, loc='center', cellLoc='center', cellColours=full_color_list)
    plt.yticks(y_)
    plt.xticks(x_)
    plt.show()


def generate_new_series_with_positive_sin_graph(grid, number_of_lists_in_grid, length_of_message):

    # ---------------------------------------------------------------------------
    # Get x,y coordinates
    # ---------------------------------------------------------------------------
    x_list = []
    y_list = []

    logging.info("Sin Graph:")
    for i in range(length_of_message + 1):
        logging.info("x = " + str(i) + " ; y = " + str(int((number_of_lists_in_grid / 2) - 1) * (np.sin((i) * np.pi / 20))))
        x_list.append(int(i))
        y_list.append(int((number_of_lists_in_grid / 2) - 1) * (np.sin((i) * np.pi / 20)))
    # ---------------------------------------------------------------------------

    # ---------------------------------------------------------------------------
    # Generate NEW SERIES
    # ---------------------------------------------------------------------------
    new_series = []

    for i in range(length_of_message):
        y_position = int(round((number_of_lists_in_grid / 2) - y_list[i]))
        x_position = int(round(x_list[i]))

        logging.info('y_position: ' + str(y_position) + ' x_position: ' + str(x_position))

        new_series.append(grid[y_position - 1][x_position])
    # ---------------------------------------------------------------------------

    logging.info('\nnew_series : ' + str(new_series))
    return new_series


def generate_new_series_with_negative_sin_graph(grid, number_of_lists_in_grid, length_of_message):

    #----------------------------------------------------------------------------------------
    # THIS FUNCTION DOES NOT WORK, STILL TRYING TO FIGURE OUT WHY...
    #----------------------------------------------------------------------------------------

    # ---------------------------------------------------------------------------
    # Get x,y coordinates
    # ---------------------------------------------------------------------------
    x_list = []
    y_list = []

    logging.info("Sin Graph:")
    for i in range(length_of_message + 1):
        logging.info(
            "x = " + str(i) + " ; y = " + str(int((-1*(number_of_lists_in_grid / 2) - 1)) * (np.sin((i) * np.pi / 20))))
        x_list.append(int(i))
        y_list.append(int((-1*(number_of_lists_in_grid / 2)) - 1) * (np.sin((i) * np.pi / 20)))
    # ---------------------------------------------------------------------------

    # ---------------------------------------------------------------------------
    # Generate NEW SERIES
    # ---------------------------------------------------------------------------
    new_series = []

    for i in range(length_of_message):
        y_position = int(round((number_of_lists_in_grid / 2) - y_list[i]))
        x_position = int(round(x_list[i]))

        logging.info('y_position: ' + str(y_position) + ' x_position: ' + str(x_position))

        new_series.append(grid[y_position - 1][x_position])
    # ---------------------------------------------------------------------------

    logging.info('\nnew_series : ' + str(new_series))
    return new_series


def str_to_ascii(text):
    # This method converts string to a list of each characters corresponding ascii number.

    return [ord(x) for x in [char for char in text]]


def ascii_list_to_string(ascii_list):

    # This function converts a ascii list to a string.

    a = [chr(x) for x in [ord for ord in ascii_list]]
    s = ''
    return (s.join(a))


def rotate_ascii_positive(input_ascii, rotate_x_times):

    # If the ascii table was a circle this code will turn it x times in the positive direction.

    for i in range(rotate_x_times):
        if input_ascii == 255:
            input_ascii = (input_ascii - 255)-1
        input_ascii = input_ascii + 1
    return input_ascii


def rotate_ascii_negative(input_ascii, rotate_x_times):

    # If the ascii table was a circle this code will turn it x times in the negative direction.

    for i in range(rotate_x_times):
        if input_ascii == 0:
            input_ascii = (input_ascii + 255)+1
        input_ascii = input_ascii - 1
    return input_ascii


def datetime_now(datetime_format):
    # Returns date and time in the format you specified

    now = datetime.datetime.now().strftime(datetime_format)

    return now


def immensity(encrypt_or_decript, text_or_file, data_input, num_of_lists, list_step):

    global message, key, decrypt_message

    # --------------------------------------------------------------------------------------------------------------
    # ENCRYPT
    # --------------------------------------------------------------------------------------------------------------

    if encrypt_or_decript == 'encrypt':

        if text_or_file == 'text':
            message = data_input
        elif text_or_file == 'file':
            fr = open(data_input, 'r')
            message = fr.read()
            fr.close()
        else:
            logging.warning("Error: The variable 'text_or_file' did not match 'text' or 'file'.")

        message_ascii_list = str_to_ascii(message)
        logging.info('message_ascii_list' + str(message_ascii_list))

        # make num_of_lists_in_grid uneaven
        number_of_lists_in_grid = num_of_lists  # 23
        length_of_message = len(message)
        list_step = list_step  # 100

        settings = generate_grid_setting(number_of_lists_in_grid, length_of_message, list_step)

        # generate_grid(settings) # This function does not use multi processing.

        grid = generate_grid_multiprocessing(settings)
        new_series = generate_new_series_with_positive_sin_graph(grid, number_of_lists_in_grid, length_of_message) # This will be the key!
        logging.info('new series: ' + str(new_series))

        # Mod new_series to improve computation.
        new_series_mod = []
        for i in range(len(new_series)):
            if int(new_series[i]) > 255:
                new_series_mod.append(new_series[i] % 256)
            else:
                new_series_mod.append(new_series[i])

        logging.info('new_series_mod' + str(new_series_mod))

        encrypted_series = []
        for i in range(length_of_message):
            encrypted_series.append(rotate_ascii_positive(int(message_ascii_list[i]), int(new_series_mod[i])))
        logging.info('encrypted series: ' + str(encrypted_series))

        encrypted_series_json = {'encrypted_list': encrypted_series, 'key': settings}
        logging.info(encrypted_series_json)

        # The below function will draw the graph and function.
        # To use this function number_of_lists_in_grid must be equal to 33 and length_of message needs to equal 40.
        # ---------------------------------------------------------------------------------------------------------
        # generate_table_and_positive_sin_graph(grid, number_of_lists_in_grid, length_of_message)
        # ---------------------------------------------------------------------------------------------------------

        if text_or_file == 'text':
            return encrypted_series_json
        elif text_or_file == 'file':
            now = datetime_now("%d_%m_%Y_%H_%M_%S")
            fw = open('Immensity_Encrypt_' + str(now) + '.txt', 'w')
            fw.write(str(encrypted_series_json))
            fw.close
        else:
            logging.warning("Error: The variable 'text_or_file' did not match 'text' or 'file'.")

    # --------------------------------------------------------------------------------------------------------------
    # DECRYPT
    # --------------------------------------------------------------------------------------------------------------

    elif encrypt_or_decript == 'decrypt':

        if text_or_file == 'text':
            data = data_input
            key = data['key']
            decrypt_message = data['encrypted_list']

        elif text_or_file == 'file':

            fr = open(data_input, 'r')
            data = ast.literal_eval(fr.read())
            fr.close()
            key = data['key']
            decrypt_message = data['encrypted_list']

        else:
            logging.warning("Error: The variable 'text_or_file' did not match 'text' or 'file'.")

        length_of_message_decrypt = len(decrypt_message)
        number_of_lists_in_grid_decrypt = key[0][4]

        grid_decrypt = generate_grid_multiprocessing(key)
        new_series_decrypt = generate_new_series_with_positive_sin_graph(grid_decrypt, number_of_lists_in_grid_decrypt, length_of_message_decrypt)
        logging.info('new_series_decrypt: ' + str(new_series_decrypt))

        # Mod 'key' to improve computation.
        new_series_decrypt_mod = []
        for i in range(len(new_series_decrypt)):
            if int(new_series_decrypt[i]) > 255:
                new_series_decrypt_mod.append(new_series_decrypt[i] % 256)
            else:
                new_series_decrypt_mod.append(new_series_decrypt[i])
        logging.info('new_series_decrypt_mod: ' + str(new_series_decrypt_mod))


        decrypted_series = []
        for i in range(length_of_message_decrypt):
            decrypted_series.append(rotate_ascii_negative(int(decrypt_message[i]), int(new_series_decrypt_mod[i])))
        logging.info('decrypted series: ' + str(decrypted_series))

        final_decrypt_string = ascii_list_to_string(decrypted_series)
        logging.info('final_decrypt_string: ' + str(final_decrypt_string))

        if text_or_file == 'text':
            return final_decrypt_string
        elif text_or_file == 'file':
            now = datetime_now("%d_%m_%Y_%H_%M_%S")
            fw = open('Immensity_Decrypt_' + str(now) + '.txt', 'w')
            fw.write(str(final_decrypt_string))
            fw.close
        else:
            logging.warning("Error: The variable 'text_or_file' did not match 'text' or 'file'.")

    else:
        logging.warning("Error: 'encrypt_or_decrypt' variable does not match 'encrypt' or 'decrypt'.")


# Setting up LOGGER
# -----------------------------------------------------------------------
# logging.basicConfig(level=logging.INFO, format='%(asctime)s: line:%(lineno)d: %(levelname)s: %(message)s')
# -----------------------------------------------------------------------

def run_immensity():

    command = ''
    while command != 'x':

        print('Would you like to ENCRYPT(e) or DECRYPT(d)? Or press "x" to exit.')
        command = input()

        if command.lower() in ['encrypt', 'e']:

            print('Would you like to apply this function to TEXT(t) or a FILE(f)?')
            command = input()

            if command.lower() in ['text', 't']:

                print("Please enter the text you'd like to encrypt.")
                command = input()

                print(immensity('encrypt','text',  command, 23, 0))

            elif command.lower() in ['file', 'f']:
                print("Please enter the file path you'd like to encrypt.")
                command = input()

                immensity('encrypt', 'file', command, 23, 0)
                print("File has been Encrypted.")

            else:
                print("Did not recognise command, please try again.")

        elif command.lower() in ['decrypt', 'd']:

            print('Would you like to apply this function to TEXT(t) or a FILE(f)?')
            command = input()

            if command.lower() in ['text', 't']:
                print("Please enter the text you'd like to decrypt.")
                command = input()
                decrypt_command = ast.literal_eval(command)

                print(immensity('decrypt', 'text', decrypt_command, "none", "none"))

            elif command.lower() in ['file', 'f']:
                print("-> Please enter the file path you'd like to decrypt.")
                command = input()

                immensity('decrypt', 'file', command, "none", "none")

                print("File has been Decrypted.")

            else:
                print("Did not recognise command, please try again.")

        if command.lower() in ['exit', 'x', 'e']:
            break

    print('Immensity - Done!')


if __name__ == '__main__':

    run_immensity()