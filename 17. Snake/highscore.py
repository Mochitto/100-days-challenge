

def read_hs():
    with open("high_score.txt", "r") as high_score:
        message = high_score.readline()
    return message


def write_hs(message):
    with open("high_score.txt", "w") as high_score:
        high_score.write(message)
