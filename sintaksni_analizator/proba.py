from antlr4 import *
import sys
sys.path.append(r"/home/ng/Documents/kompilatori_projekat/leksicki_analizator")
from RubyLekser import RubyLekser
from RubyParser import RubyParser
from antlr4.tree.Tree import TerminalNodeImpl

def print_tree_verbose(node, parser, indent=0):
    prefix = '  ' * indent
    if isinstance(node, TerminalNodeImpl):
        print(f"{prefix}Token: '{node.getText()}'")
    else:
        rule_name = parser.ruleNames[node.getRuleIndex()]
        print(f"{prefix}Rule: {rule_name}")
        for i in range(node.getChildCount()):
            print_tree_verbose(node.getChild(i), parser, indent + 1)

def test_parser(input_code):
    input_stream = InputStream(input_code)
    lexer = RubyLekser(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = RubyParser(token_stream)

    tree = parser.prog() 
    print_tree_verbose(tree, parser) 


code = """class Animal
  #attr_accessor :name, :age

  def initialize(name, age)
    @name = name
    @age = age
  end

  def speak
    puts "#{@name} makes a noise."
  end
end

class Dog < Animal
  def initialize(name, age, breed)
    super(name, age)
    @breed = breed
  end

  def speak
    if @age < 2
      puts "#{@name} barks like a puppy."
    elsif @age < 10
      puts "#{@name} barks loudly."
    else
      puts "#{@name} barks quietly."
    end
  end

  def fetch(item)
    puts "#{@name} fetches the #{item}."
  end
end

class Cat < Animal
  def speak
    puts "#{@name} meows."
  end

  def sleep(hours)
    while hours > 0
      puts "#{@name} is sleeping."
      hours -= 1
    end
  end
end

# Usage example
dog = Dog.new("Rex", 3, "Labrador")
dog.speak
dog.fetch("ball")

cat = Cat.new("Mittens", 5)
cat.speak
cat.sleep(3)

for i in 1..3
  puts "Loop #{i}"
end
"""

test_parser(code)
