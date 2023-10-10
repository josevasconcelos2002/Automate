from pathlib import Path
import os
import shutil

src_dir = Path("../Downloads/")
out_dir = Path("../Documents/")


downloaded_files = os.listdir(src_dir)


for file in downloaded_files:
    
    file_path = src_dir / file
    sufixo = file_path.suffix
    nomePasta = sufixo.lstrip(".")
    nomePastaCompleto = out_dir / nomePasta
    
    if(os.path.exists(nomePastaCompleto)):
        try:
            shutil.move(file_path, nomePastaCompleto / file)
        except Exception as e:
             print(f"Erro ao mover o ficheiro: {str(e)}\n")
             
    else:
        try:
            os.mkdir(nomePastaCompleto)
        except Exception as e:
             print(f"Erro ao criar a pasta: {str(e)}\n")
        try:
            shutil.move(file_path, nomePastaCompleto / file)
        except Exception as e:
             print(f"Erro ao mover o ficheiro: {str(e)}\n")