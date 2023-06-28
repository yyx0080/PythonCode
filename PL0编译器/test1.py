# PL/0编译器的词法分析部分
class Lexer:
    def __init__(self, source_code):
        self.source_code = source_code
        self.position = 0
        self.current_token = None

    def get_next_token(self):
        if self.position >= len(self.source_code):
            return None

        current_char = self.source_code[self.position]

        if current_char.isdigit():
            value = 0
            while self.position < len(self.source_code) and self.source_code[self.position].isdigit():
                value = value * 10 + int(self.source_code[self.position])
                self.position += 1
            self.current_token = ('NUMBER', value)

        elif current_char == '+':
            self.current_token = ('PLUS', '+')
            self.position += 1

        elif current_char == '-':
            self.current_token = ('MINUS', '-')
            self.position += 1

        # 处理其他词法单元...

        return self.current_token


# PL/0编译器的语法分析部分
class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def parse(self):
        # 解析语法规则...
        pass


# 示例代码
source_code = '3 + 5'
lexer = Lexer(source_code)
parser = Parser(lexer)
parser.parse()
print(parser)
