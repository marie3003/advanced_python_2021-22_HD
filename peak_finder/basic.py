#
# The first version of our function!
# Write doc strings 
#
def find_peaks(list_of_intensities):
    """Find peaks

    Find local maxima for a given list of intensities or tuples
    Intensities are defined as local maxima if the
    intensities of the elements in the list before and after
    are smaller than the peak we want to determine.

    For example given a list:
        1 5 [6] 4 1 2 [3] 2

    We expect 6 and 3 to be returned.
    

    Args:
        list_of_intensities (list of floats, ints or tuple of ints): a list of
            numeric values

    Returns:
        list of floats or tuples: list of the identified local maxima

    Note:
        This is just a place holder for the TDD part :)

    """
    

    maxima = []
    list_of_intensities_original = list_of_intensities.copy()

    if type(list_of_intensities[0]) == type((0,0,0)):
        for position, tuple in enumerate(list_of_intensities):
            list_of_intensities[position] = tuple[0] + tuple[1] + tuple[2]

    for pos, value in enumerate(list_of_intensities):
        if pos == 0 or pos == len(list_of_intensities) - 1:
            continue
        pre_value = list_of_intensities[pos - 1]
        post_value = list_of_intensities[pos + 1]
        if pre_value < value > post_value:
            maxima.append(list_of_intensities_original[pos])
    return  maxima


    """
    local_maxima = []

    for number in list_of_intensities:
        if number == 0:
            if list_of_intensities[number] == max(list_of_intensities[number:number +2]):
                local_maxima.append(number)
        if number > 0 and number < len(list_of_intensities) - 1:
            if list_of_intensities[number] == max(list_of_intensities[number - 1:number +2]):
                local_maxima.append(number)
        if number == len(list_of_intensities) -1:
            if list_of_intensities[number] == max(list_of_intensities[number:number +2]):
                local_maxima.append(number)
    return local_maxima
    """

