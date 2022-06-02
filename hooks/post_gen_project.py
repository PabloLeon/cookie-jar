import os 
os.listdir("./")
os.system("conda env create -f environment.yml")

print("activate the project with 'conda activate {{cokiecutter.name}}")
print("{{cookiecutter.name}} was set up correctly...")
