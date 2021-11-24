# Yang pasti tidak ada
# finally
# lambda
# try
# nonlocal
# del
# global
# yield
# assert
# async
# except
# await

# Asumsikan tidak ada range dalam looping
# Asumsikan tidak ada type casting
# Asumsikan tidak ada penggunaan built-in len

rules = [
    (r'\"\"\"', 'TRIPLEQUOTE'),
    (r'\'\'\'', 'TRIPLEQUOTE'),    
    (r'from\s', 'FROM'),
    (r'import\s', 'IMPORT'),
    (r'as\s', 'AS'),
    (r'class\s', 'CLASS'),
    (r'def\s', 'DEF'),
    (r'return\s', 'RETURN'),
    (r'pass', 'PASS'),
    (r'raise\s', 'RAISE'),
    (r'continue\n', 'CONTINUE'),
    (r'break\w', 'BREAK ERR'),
    (r'break\n', 'BREAK NEWLINE'),
    (r'if\s', ' IF'),
    (r'if\(', ' IF LP'),
    (r'elif', 'ELIF'),
    (r'elif\(', 'ELIF LP'),
    (r'else', 'ELSE'),
    (r'for\s', 'FOR'),
    (r'in\s', 'IN'),
    (r'while', 'WHILE'),
    (r'None', 'NONE'),
    (r'True', 'TRUE'),
    (r'False', 'FALSE'),
    (r'not', 'NOT'),
    (r'and', 'AND'),
    (r'\sor\s', 'OR'),
    (r'is\s', 'IS'),
    (r'with\s', 'WITH'),
    (r'print', 'PRINT'),
    (r'bool', 'BOOL'),
    (r'abs', 'ABS'),
    (r'round', 'ROUND'),
    (r'pow', 'POW'),
    (r'\#.*', 'COMMENT'),

    # https://stackoverflow.com/questions/41067866/raw-strings-python-and-re-normal-vs-special-characters
    # 2 di bawah tidak menggunakan raw karena alasan di atas.
    ('\".*\"', 'STRING'),
    ('\'.*\'', 'STRING'),

    (r'\.', 'WITH_METHOD'),
    (r':', 'COLON'),
    (r';', 'SEMICOLON'),
    (r',', 'COMA'),
    (r'\n', 'NEWLINE'),
    (r'\s', 'WHITESPACE'),
    (r'\d+[\da-zA-Z_0-9]*', 'NOT_VAR'),
    (r'\d+','NUMBER'),
    (r'\d+.+\d','FLOAT'),
    (r'[a-zA-Z_]+[\da-zA-Z_0-9]*','IDENTIFIER'),

    # Operasi matematik
    (r'\+','PLUS'),
    (r'\-','MINUS'),
    (r'\*\*','POWER'),
    (r'\*','MULTIPLY'),
    (r'\/','DIVIDE'),
    (r'\%', 'MOD'),
    (r'\[', 'LB'),
    (r'\]', 'RB'),
    (r'\(','LP'),
    (r'\)','RP'),
    (r'\{', 'LC'),
    (r'\}', 'RC'),
    
    # Checking
    (r'==','DOUBLEEQUAL'),
    (r'=','EQUALS'),
    (r'!=', 'NOT_EQUAL'),
    (r'>=', 'GREATER_OR_EQUAL_THAN'),
    (r'>', 'GREATER_THAN'),
    (r'<=', 'LESS_OR_EQUAL_THAN'),
    (r'<', 'LESS_THAN'),

    # Selain yang dideklarasi pada bagian di atas
    # Atau melanggar asumsi
    (r'\w', 'NULL'),
]