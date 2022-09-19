#/usr/bin/python3.7
def tofloat(s):
    """
    In our dataset we can meet a variable like '-.9', 
    this function converts this variable to a float 
    """

    integer, mantissa = s.split('.')
    if integer is ('-' or '+' or ''):
        integer += '0'
    return float(integer + '.' + mantissa)


def convert(line):
    """ Convert all variables from int and specific type to float """
    
    return ','.join(str(float(x)) if x.isdigit()
                 else str(tofloat(x)) for x in line.strip().split(','))


def merge_datasets(list_names_datasets, file_to_fill):
    for name_dataset in list_names_datasets:
        with open(name_dataset, "r") as dataset:
            for line in dataset:
                if '?' not in line:
                    file_to_fill.write(convert(line) + '\n')


if __name__ == '__main__':

    with open("new_dataset.data", "w") as new_dataset:
        list_of_datasets_names = [
            "processed.hungarian.data",
            "processed.switzerland.data",
            "processed.va.data",
            "processed.cleveland.data"
        ]
        
        merge_datasets(list_of_datasets_names, new_dataset)
