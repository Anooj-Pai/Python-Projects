def justleft(string, size):
    liststr = string.split()
    print(liststr)
    line = ''
    linelist = []
    while liststr != []:
        for i in liststr:
            if len(line)+len(i) <= size:
                line += i
                line += ' '
                liststr.remove(i)
            else:
                line = line + ' '*(size-len(line))
                linelist.append(line)
                print(linelist)
                break

if __name__ == '__main__':
    justleft("Here is an example of text justification.", 16)