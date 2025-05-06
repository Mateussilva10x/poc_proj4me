# fileops/file_manager.py

import os
import shutil
from datetime import datetime

def organize_files(source_dir, target_dir, mock=False):
    if mock:
        print(f"[MOCK] Organizando arquivos de {source_dir} para {target_dir}")
        return
    """
    Move e renomeia arquivos do source_dir para target_dir organizando por data.
    """
    os.makedirs(target_dir, exist_ok=True)

    for filename in os.listdir(source_dir):
        source_path = os.path.join(source_dir, filename)
        if not os.path.isfile(source_path):
            continue

        # Gera novo nome com data e hora
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        new_name = f"{timestamp}_{filename}"
        target_path = os.path.join(target_dir, new_name)

        print(f"[MOVER] {filename} => {new_name}")
        shutil.move(source_path, target_path)

    print(f"[OK] Arquivos organizados em: {target_dir}")
