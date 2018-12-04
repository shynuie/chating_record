def isname(x):
    return x in ['Allen', 'Tom', 'Marvin'];
def read_file(x = 'filename'):
    lines = [];
    with open(x, 'r', encoding = 'utf-8-sig') as input:
        for line in input:
            line = line.strip()
            lines.append(line);
    return lines;
    print(lines);
def convert(lines):
    record = [];
    name = None;
    for line in lines:
        if isname(line):
            name = line;
            continue;
        if name:
            record.append(name + ': '+line); 
    return record;
def write_file(x, y):
    with open(x, 'w', encoding = 'utf-8-sig') as output:
        for line in y:
            output.write(line + '\n');
def main():
    lines = read_file('input.txt');
    record = convert(lines);
    write_file('output.txt', record);
main()