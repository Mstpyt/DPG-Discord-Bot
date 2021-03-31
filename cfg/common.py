from messages import examples

def example_none():
    return None


def get_exampe(exam):
    try:
        acExample = getattr(examples, exam, example_none())
        return acExample
    except ValueError:
        return None


def listToStringWithoutBracketsAndAT(list1):
    return str(list1).replace('[', '') \
        .replace(']', '') \
        .replace('(', '') \
        .replace(')', '') \
        .replace("'", '') \
        .replace('@', '') \
        .replace('<', '') \
        .replace('>', '') \
        .replace(',', '') \
        .replace(' ', '')


def listToStringForStatistics(list1):
    return str(list1).replace('[', '') \
        .replace(']', '') \
        .replace('(', '') \
        .replace(')', '\n') \
        .replace("'", '') \
        .replace('<', '') \
        .replace('>', '') \
        .replace(',', '')


def listToStringForStatistics_exam(list1):
    return str(list1).replace('[', '') \
        .replace(']', '') \
        .replace('(', '') \
        .replace(')', '') \
        .replace("'", '') \
        .replace('<', '') \
        .replace('>', '') \
        .replace(',', '\n')