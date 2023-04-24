def generate_control_input(**kwargs):
    string = ""
    for key in kwargs:
        string += key + "=" + str(kwargs[key]) + "\n"
    # print(string)
    return string
        