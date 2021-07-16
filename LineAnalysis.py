def LineAnalysis(line):
    if line[0] == '*' and line[-1] == '*':
        
        if len(line)==1:
            return True
        
        if '.' not in line:
            return True
        
        pattern_line = line[0]
        for i in range(1, len(line)):
            if line[i] != '*':
                pattern_line += line[i]
            else:
                break
        
        line = line.split(pattern_line)
        str_line = [x for x in line if x != '']
        
        return len(str_line) == 1