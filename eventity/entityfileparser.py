import re

# re.sub('[\n]', ' ',entity_file_text)
def parse_entity(file_path, id = None):

    all_components = []
    tempcomponent = {
        "name": None
    }

    with open(file_path) as e_file:
        file_lines = e_file.readlines()

    tokens = [line.rstrip("\n") for line in file_lines]

    for token in tokens:
        if token == "":
            continue

        if token[-1] == ":":
            if tempcomponent["name"] is not None:
                all_components.append(tempcomponent)
            tempcomponent = {
                "name": token[:-1],
                "data": {}
            }
            continue

        if "=" in token:
            handle_assignment(tempcomponent, token)
            continue

    if tempcomponent["name"] is not None:
        all_components.append(tempcomponent)

    return all_components


def handle_assignment(temp, token):

    values = token.split("=")
    data_name = values[0].strip(" \n\t")
    data_value = values[1].strip(" \n\t")

    if data_value.isdigit():
        data_value = int(data_value)

    try:
        if isinstance(temp["data"][data_name], list):
            temp["data"][data_name].append(data_value)
        else:
            temp["data"][data_name] = [
                temp["data"][data_name]
            ]
            temp["data"][data_name].append(data_value)

    except KeyError:
        temp["data"][data_name] = data_value
