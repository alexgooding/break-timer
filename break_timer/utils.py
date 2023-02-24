from collections import OrderedDict


def round_to_nearest_second(minutes):
    """
    Round to the nearest second and return milliseconds
    :param minutes: user inputted minutes
    :return: minutes in milliseconds rounded to the nearest second
    """
    seconds = minutes * 60
    rounded_seconds = round(seconds)
    return rounded_seconds * 1000

def format_snooze_length(milliseconds):
    """
    Format given milliseconds as a written string for display in toast
    :param milliseconds: the milliseconds to format
    :rtype: str
    """
    total_seconds = milliseconds / 1000
    seconds = total_seconds % 60
    minutes = (total_seconds - seconds) / 60
    hours = (minutes - (minutes % 60)) / 60

    time = OrderedDict([('hours', int(hours)), ('minutes', int(minutes)), ('seconds', int(seconds))])

    formatted_list = [f"{value} {key}" for key, value in time.items() if value != 0]
    return ', '.join(formatted_list)


class InvalidInputException(Exception):
    """Raise when a user entered input is invalid"""
