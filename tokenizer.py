import re

def tokenizer(filename):
    single_operator = [':', '/', '*', '+', '-', '#', '>', '<', '=', '%', '!', "'", '"', '(', ')', '[', ']' ]
    double_operator = ['//', '**', '>=', '<=', '==', '!=']
    triple_operator = ["'''"]
    with open(filename, "r" , encoding='utf-8') as f:
        lines = f.read().splitlines()
    result = []
    for line in lines:
        temp = ''
        line = line.strip()
        for i in range(len(line)):
            chara = line[i]
            if chara == ' ':
                result.append(temp)
                temp = ''
            if temp == '':
                temp += chara
            elif temp in single_operator:
                if chara in single_operator:
                    temp2 = temp + chara
                    if temp2 ==  "''":
                        temp += chara
                    elif temp2 in double_operator:
                        temp += chara
                    else:
                        result.append(temp)
                        temp = chara
                else:
                    result.append(temp)
                    temp = chara
            elif temp in double_operator:
                result.append(temp)
                temp = chara
            elif temp == "''":
                temp2 =  temp + chara
                if temp2 in triple_operator:
                    temp += chara
                else:
                    result.append(temp)
                    temp = chara
            elif temp in triple_operator:
                result.append(temp)
                temp = chara
            else:
                if chara in single_operator:
                    result.append(temp)
                    temp = chara
                else:
                    temp += chara
        result.append(temp)
    result = [res for res in result if res != ' ' and res != '']
    return result

file = input("Masukkan nama file: ")
print(tokenizer(file))