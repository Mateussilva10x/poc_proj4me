import os
import shutil
import json
from datetime import datetime

def organize_files(source_dir: str, target_dir: str, mock: bool = False) -> list[str]:
    os.makedirs(source_dir, exist_ok=True)
    os.makedirs(target_dir, exist_ok=True)

    moved_files = []

    if mock:
        print(f"[MOCK] Organizando arquivos de {source_dir} para {target_dir}")
        for i in range(3):
            filename = f"arquivo_{i+1}.txt"
            path = os.path.join(source_dir, filename)
            with open(path, "w") as f:
                f.write(f"Conteúdo de teste {i+1}\n")
            moved_files.append(path)
    else:
        for filename in os.listdir(source_dir):
            source_path = os.path.join(source_dir, filename)
            if not os.path.isfile(source_path):
                continue

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            new_name = f"{timestamp}_{filename}"
            target_path = os.path.join(target_dir, new_name)

            print(f"[MOVER] {filename} => {new_name}")
            shutil.move(source_path, target_path)
            moved_files.append(target_path)

        print(f"[OK] Arquivos organizados em: {target_dir}")

    print("[RESULTADO] Arquivos processados:")
    print(json.dumps(moved_files, indent=2, ensure_ascii=False))
    return moved_files
