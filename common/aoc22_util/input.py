def file_readlines_stripped(path):
    with open(path, "r") as file:
        return map(lambda line: line.strip(), file.readlines())

def file_readlines_no_newlines(path):
    with open(path, "r") as file:
        return map(lambda line: line.replace("\n", ""), file.readlines())
