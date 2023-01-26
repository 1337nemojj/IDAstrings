#find offset
data = []
parsed_data = []

file = input()
with open(f"{file}.txt", "r") as file1:
    for line in file1:
        #print(line.strip())
        data.append(line.strip())
def colored_text(string, color_it):
    pass

while(True):
    inp = input("[?] Enter starting string pattern: ")
    f = input("[?] Enter finding in word pattern: ")
    ending = len(inp)
    count = 0
    for str in data:
        
        sep = str.split('\t')
        #print(sep[-1])
        parsed_data.append(sep)
        if sep[-1][:ending] == inp and f in sep[-1]:
            print(sep[0], "\t" ,sep[1], "\t" ,sep[-1])
            count+=1
    print("[+] ALL FOUND: ",count)

