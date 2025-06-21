import os
import subprocess


def generate_uml(plantuml_code, naziv):

    output_file = f"output/{naziv}_dijagram.png"

    with open("temp.uml", "w") as f:
        f.write(plantuml_code)

    subprocess.run(["java", "-jar", "/home/ng/Documents/kompilatori_projekat/uml/plantuml-1.2025.3.jar", "-tpng", "temp.uml"], check=True)

    os.rename("temp.png", output_file)
    os.remove("temp.uml")
    
    print(f"dijagram generisan u : {output_file}")

