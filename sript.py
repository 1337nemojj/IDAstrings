#find offset
import colorama
data = []
parsed_data = []

colorama.init()
RED = colorama.Fore.RED
GREEN = colorama.Fore.GREEN
GRAY = colorama.Fore.LIGHTBLACK_EX
RESET = colorama.Fore.RESET
YELLOW = colorama.Fore.YELLOW
#init colors

file = input()
with open(f"{file}.txt", "r") as file1:
    for line in file1:
        #print(line.strip())
        data.append(line.strip())

#string ananana/lolol/nama
def colored_text(str_line, f):
    start_mark = str_line.find(f)
    ending_mark = start_mark + len(f)
    if start_mark > 0:
        return f"{str_line[:start_mark]}{GREEN}{str_line[start_mark:ending_mark]}{RESET}{str_line[ending_mark:]}"
    else:
        return str_line


while(True):
    inp = input("[?] Enter starting string pattern: ")
    f = input("[?] Enter finding in word pattern: ")
    ending = len(inp)
    count = 0
    for str in data:
        
        sep = str.split('\t')
        #print(sep[-1])
        str_line = sep[-1]
        parsed_data.append(sep)
        if str_line[:ending] == inp and f in str_line:
            print(sep[0], "\t" ,sep[1], "\t" , colored_text(str_line,f))
            count+=1
            

    print("[+] ALL FOUND: ",count)

