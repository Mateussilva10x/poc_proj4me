# s3/s3_client.py

import boto3
import os

def download_files_from_s3(bucket, prefix, local_dir, user, mock=False):
    if mock:
        print(f"[MOCK] Simulando download do S3 bucket={bucket}, prefix={prefix}")
        return
    """
    Baixa todos os arquivos de um prefixo no bucket S3 para um diretório local.
    """
    print(f"[INFO] Conectando ao S3 como {user}...")
    s3 = boto3.client('s3')  # Requer configuração prévia do perfil (AWS CLI ou variáveis de ambiente)

    os.makedirs(local_dir, exist_ok=True)

    paginator = s3.get_paginator('list_objects_v2')
    for page in paginator.paginate(Bucket=bucket, Prefix=prefix):
        for obj in page.get('Contents', []):
            key = obj['Key']
            if key.endswith('/'):  # Ignora "pastas"
                continue

            local_path = os.path.join(local_dir, os.path.basename(key))
            print(f"[DOWNLOAD] {key} => {local_path}")
            s3.download_file(bucket, key, local_path)

    print(f"[OK] Arquivos do S3 baixados para: {local_dir}")
