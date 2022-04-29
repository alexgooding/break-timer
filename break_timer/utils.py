def round_to_nearest_second(minutes):
    """
    Round to the nearest second and return milliseconds
    :param minutes: user inputted minutes
    :return: minutes in milliseconds rounded to the nearest second
    """
    seconds = minutes*60
    rounded_seconds = round(seconds)
    return rounded_seconds*1000

# TODO: format time appearing in toast