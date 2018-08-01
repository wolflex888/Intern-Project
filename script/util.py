#!/Users/juichanglu/anaconda3/bin/python3
import os
import random
def quote_process(path_raw, path_write):
    
    file = open(path_raw, "r")
    write = open(path_write, "w")
    i = 0
    for line in file:
        if line != "\n":
            line = line.rstrip()
            write.write(line)
        else:
            write.write("\t")
            i+=1
    file.close()
    write.close()
    return i
def print_random_quote(path_read, quote_numb):
    data_f = open(path_read, "r")
    rand = random.randint(0, quote_numb-1)
    for line in data_f:
        quotes = line.split("\t")
    print(quotes[rand])
if __name__ == "__main__":
    quote_numb = quote_process("../data/quotes.txt", "../data/quotes_ready.tab")
    print_random_quote("../data/quotes_ready.tab", quote_numb)

