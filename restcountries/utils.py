KM2_MILES2_CONVERSION_RATE = 0.386102159


def km2_to_miles2(km2):
    """
    Converts km2 to miles2
    :param km2: area km2
    :return: Converted area in m2
    """
    return km2 * KM2_MILES2_CONVERSION_RATE
