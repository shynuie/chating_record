def isname(x):
    return x in ['Allen', 'Tom', 'Marvin'];
def readfile(x = 'filename'):
    y = [];
    name = '';
    with open(x, 'r', encoding = 'utf-8-sig') as input:
        for line in input:
            line = line.strip()
            if isname(line):
                name = line;
                continue;
            line = name + ':' + line;
            y.append(line);
    return y;
def writefile(x, y):
    with open(x, 'w', encoding = 'utf-8-sig') as output:
        for line in y:
            output.write(line + '\n');
record = readfile('input.txt');
writefile('output.txt', record);