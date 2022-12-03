def file_readlines_stripped(path):
    with open(path, "r") as file:
        return map(lambda line: line.strip(), file.readlines())
