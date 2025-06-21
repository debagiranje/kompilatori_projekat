from antlr4 import *
from sintaksni_analizator.RubyParser import RubyParser
from leksicki_analizator.RubyLekser import RubyLekser
from .analizator import Analizator
from antlr4.tree.Tree import ParseTreeWalker

def main(fajl):
    input_stream = FileStream(f"/home/ng/Documents/kompilatori_projekat/primjeri/{fajl}.rb", encoding='utf-8')
    lexer = RubyLekser(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = RubyParser(token_stream)
    tree = parser.prog()

    listener = Analizator()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    return listener.broj_gresaka()
