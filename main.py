import re
import os
import sys
from rules_lexer import rules
import cyk_parser as parser
import tokenizer as display
import time

input_file = str(sys.argv[1])

# Printing hasil file setelah selesai dibuat menjadi token
# print(display.tokenizer(input_file))

file_path = './' + input_file
file = open(file_path, 'r')
text = file.read()

class LexerError(Exception):
    def __init__(self, pos):
        self.pos = pos


class Lexer(object):
    def __init__(self, rules, skip_whitespace=True):
        idx = 1
        regex_parts = []
        self.group_type = {}

        for regex, type in rules:
            groupname = 'GROUP' + str(idx)
            regex_parts.append('(?P<' + groupname + '>' + regex + ')')
            self.group_type[groupname] = type
            idx += 1

        self.regex = re.compile('|'.join(regex_parts))
        self.skip_whitespace = skip_whitespace
        self.re_ws_skip = re.compile('\S')

    def input(self, buffer):
        self.buffer = buffer
        self.pos = 0

    def token(self):
        if self.pos >= len(self.buffer):
            return None
        else:
            if self.skip_whitespace:
                m = self.re_ws_skip.search(self.buffer, self.pos)

                if m:
                    self.pos = m.start()
                else:
                    return None

            m = self.regex.match(self.buffer, self.pos)
            if m:
                groupname = m.lastgroup
                tkn_type = self.group_type[groupname]
                tkn = tkn_type
                self.pos = m.end()
                if (tkn == 'WHITESPACE') :
                    return ''
                return tkn
            raise LexerError(self.pos)

    def tokens(self):
        while 1:
            tkn = self.token()
            if tkn is None: 
                break
            yield tkn

CYK = parser.Parser('grammar.txt', " COMMENT ")

def process(sentence) :
    CYK.__call__(sentence)
    CYK.parse()
    return CYK.print_tree()

if __name__ == '__main__':
    start = time.time()

    # Import regex ke dalam classnya dan set skip whitespace
    lx = Lexer(rules, skip_whitespace=False)
    # Memasukkan text ke lexer
    lx.input(text)
    output = ''

    try:
        # Melakukan looping semua token yang ad di lexer
        for tkn in lx.tokens():
            if tkn != '':
                output += tkn + ' '
    except LexerError as err:
        # Apabila terjadi error
        print('LexerError at position:', err.pos)
    
    # String ini merupakan token, tapi displit berdasarkan \n
    string_container = output.split('NEWLINE')

    if_toggle = 0
    multiline_checker = False
    total_string = len(string_container)
    total_success = 0
    total_error = 0
    line_counter = 0
    print('Memulai parsing pada ' + str(total_string) + ' baris kode')
    error_output = []
    for text in string_container :
        line_counter += 1
        # Hidupkan fitur triple quote
        if text.find('TRIPLEQUOTE') != -1 and multiline_checker == False :
                multiline_checker = True
                total_success += 1
        # Matikan fitur triple quote
        elif (text.find('TRIPLEQUOTE') != -1) and multiline_checker == True :
                multiline_checker = False
                total_success += 1
        else :
            # Melakukan pengecekan apakah textnya whitespace atau kosong
            if (text == ' ' or text == ''):
                print("",end='')
                total_success += 1
            # Apabila tidak didalam triple quote
            elif multiline_checker == False :
                # Apabila text merupakan IF
                if text.find(' IF') != -1 :
                    if_toggle += 1
                    if process(text) :
                        total_success += 1
                    else :
                        error_output.append('Error pada line ' + str(line_counter) + '.')
                        total_error += 1
                elif text.find('ELIF') != -1 :
                    if if_toggle > 0 :
                        text = 'ELIFTKN' + text
                    if process(text) :
                        total_success += 1
                    else :
                        error_output.append('Error pada line ' + str(line_counter) + '.')
                        total_error += 1
                elif text.find('ELSE') != -1 :
                    if if_toggle > 0 :
                        text = 'ELIFTKN' + text
                    if_toggle -= 1
                    if process(text) :
                        total_success += 1
                    else :
                        error_output.append('Error pada line ' + str(line_counter) + '.')
                        total_error += 1
                else :
                    if process(text) :
                        total_success += 1
                    else :
                        error_output.append('Error pada line ' + str(line_counter) + '.')
                        total_error += 1
    
    if (total_error == 0) :
        print("Parsing telah selesai")
        print("Tidak ada error yang ditemukan")
    else :
        print("Terdeteksi " + str(total_error) + ' buah Error pada file')
        print("Detail kesalahan:")
    for error in error_output:
        print("    ", error)
    end = time.time()
    delta = end - start
    delta = round(delta,3)
    print("Waktu yang dibutuhkan untuk melakukan parsing adalah ", delta, "detik")
