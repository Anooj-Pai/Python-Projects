import time


imdb_file = input("Enter the name of the IMDB file ==> ").strip()
name_list = []
for line in open(imdb_file, encoding = "ISO-8859-1"):
    words = line.strip().split('|')
    name = words[0].strip()
