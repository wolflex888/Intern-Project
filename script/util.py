#!/Users/juichanglu/anaconda3/bin/python3
import os
import random
def quote_process(path_raw, path_write):
    
    file = open(path_raw, "r")
    write = open(path_write, "w")
    for line in file:
        if line != "\n":
            line = line.rstrip()
            write.write(line)
        else:
            write.write("\t")
    file.close()
    write.close()
def print_random_quote(path_read):
    data_f = open(path_read, "r")
    
    for line in data_f:
        quotes = line.split("\t")
    rand = random.randint(0, len(quotes)-1)
    print(quotes[rand])
if __name__ == "__main__":
    quote_process("data/quotes.txt", "data/quotes_ready.tab")
    print_random_quote("data/quotes_ready.tab")

