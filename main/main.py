import subprocess
from semanticki_analizator import analiza
from uml import diagram_gen, uml_gen
import sys

def generate_lexer():
    gramlex ='leksicki_analizator/RubyLekser.g4'
    output_lex='leksicki_analizator'

    cmd_lex = [
        'antlr4',             
        '-Dlanguage=Python3',
        gramlex
    ]

    try:
        result = subprocess.run(cmd_lex, capture_output=True, text=True, check=True)
        print("lekser generisan uspjeno")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("err")
        print(e.stderr)

def generate_parser():
    grampar ='sintaksni_analizator/RubyParser.g4'
    output_parser='sintaksni_analizator/'
    tokenloc = 'leksicki_analizator/'

    cmd_par = [
        'antlr4',             
        '-Dlanguage=Python3',
        '-lib', tokenloc,
        grampar
    ]

    try:
        result = subprocess.run(cmd_par, capture_output=True, text=True, check=True)
        print("parser generisan uspjesno")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("err")
        print(e.stderr)

def all(naziv_fajla="prvi"):

    # pokrenuti sljedece 2 met samo pri prvom pokretanju/izmjeni
    #generate_lexer()
    #generate_parser()

    rezultat_analize = analiza.main(naziv_fajla)
    print(rezultat_analize)
    
    if rezultat_analize == 0:
        uml_code = uml_gen.codegen(naziv_fajla)
        diagram_gen.generate_uml(uml_code, naziv_fajla)
    else:
        print("Kod ima greske, vise info u konzoli")



if __name__ == "__main__":
    all(sys.argv[1])


