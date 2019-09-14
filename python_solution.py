
def refine_parameters(data: dict):
    '''Refine the parameters of a dictionary

    Returns:
        Return a dictionary of cleaned input
    '''
    clean_dict = {}

    for key, value in data.items():
        if type(value) is dict:
            clean_dict[key] = refine_parameters(value)
        
        try:
            float(value)
            clean_dict[key] = float(value)
        except:
            pass

        try:
            int(value)
            clean_dict[key] = int(value)
        except:
            pass

        try:
            bool(value)
            clean_dict[key] = bool(value)
        except:
            pass


    return clean_dict
