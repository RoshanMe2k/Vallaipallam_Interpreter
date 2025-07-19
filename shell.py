from lexer import Lexer
from parser import Parser
from interpreter import Interpreter
from data import Data
from tokens import Token
from errors import Error
root=Data()

def main_shell(b):
    if b :
        tokens=Lexer(b)
        a=tokens.tokenize()
        tree=Parser(a,root)
        trees=tree.parse()
        output=Interpreter(trees,root)
        return Token.display_output,Error.display_error
