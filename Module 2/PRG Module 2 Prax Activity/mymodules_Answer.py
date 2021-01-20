from time import *
import random


def create_time():
    return time()


def output_local_time(the_time):
    return strftime("%X", localtime(the_time))


def calculate_difference(first_time, second_time):
    return second_time - first_time


def generate_random(max_value):
    return random.sample(range(1, max_value), 1)[0]

