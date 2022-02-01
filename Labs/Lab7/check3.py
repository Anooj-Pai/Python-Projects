def parse_line(line):
    count = 0
    len_line = len(line)
    for i in range(len_line - 1, 0, -1):
        if line[i] == "/":
            count = count + 1
            if count == 3:
                break
    if count <= 2:
        return "None"
    text = line[0:i]
    num = line[i + 1:len_line]
    num_list = num.split("/")
    final_list = []
    for i in range(0, len(num_list), 1):
        if num_list[i].isdigit():
            final_list.append(int(num_list[i]))
        else:
            return "None"
    final_list.append(text)
    return final_list

def get_line(fname, parno, lineno):
    with open(fname, encoding='utf8') as f:
        count_parno = 1
        count_lineno = 1
        lines = f.readlines()
        for par, line in enumerate(lines):
            if not line.strip():
                if par > 0 and not lines[par - 1].strip():
                    continue
                count_parno += 1
                continue
            if count_parno == int(parno) and int(lineno) == count_lineno:
                return line.strip()
            if count_parno == int(parno):
                count_lineno += 1
            if count_parno > int(parno):
                return None

def line_spaces(fname, parno, lineno):
    with open(fname, encoding='utf8') as f:
        count_parno = 1
        count_lineno = 1
        lines = f.readlines()
        for par, line in enumerate(lines):
            if not line.strip():
                if par > 0 and not lines[par - 1].strip():
                    continue
                count_parno += 1
                continue
            if count_parno == int(parno) and int(lineno) == count_lineno:
                return line
            if count_parno == int(parno):
                count_lineno += 1
            if count_parno > int(parno):
                return None

if __name__ == "__main__":
    fname = input("Please enter the file number => ").strip()
    print(fname)
    fname = fname + '.txt'
    parno = input("Please enter the paragraph number => ").strip()
    print(parno)
    lineno = input("Please enter the line number => ").strip()
    print(lineno)

    y = open("program.py", "w")
    while get_line(fname, parno, lineno) != 'END/0/0/0':
        line = parse_line(get_line(fname, parno, lineno))
        linenospace = line[-1]
        linespace = line_spaces(fname,parno,lineno)
        finalline = ' ' * ((len(linespace)-len(line[-1]))-11) + linenospace
        fname = str(line[0]) + '.txt'
        parno = line[1]
        lineno = line[2]
        y.write(finalline+'\n')