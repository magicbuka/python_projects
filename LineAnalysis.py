def LineAnalysis(line):

    lst_line = line.split('*')
    if len(lst_line) > 1:
        lst_line = [x for x in lst_line if x != '']

    uniq_elem = set(lst_line)

    return not len(uniq_elem) > 1