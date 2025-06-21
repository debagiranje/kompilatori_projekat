from antlr4 import *
from RubyLekser import RubyLekser

def proba(input):
    input_stream = InputStream(input)
    lekser = RubyLekser(input_stream)
    
    token_stream = CommonTokenStream(lekser)
    token_stream.fill() 

    for token in token_stream.tokens:  
        if token.type != Token.EOF:
            token_name = lekser.symbolicNames[token.type]
            print(f"Token: '{token.text}'\tTip: {token_name}")


p = """class Person
  def initialize(name, age)
    @name = name
    @age = age
  end
end"""

proba(p)
