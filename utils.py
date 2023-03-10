def multi_replace(text, replaces) -> (str, dict):
    for key in replaces.keys():
        text = text.replace(key, replaces[key])
    return text
