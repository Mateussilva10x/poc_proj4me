import argparse
from db.mysql_client import get_data
from excel.report_generator import generate_excel_report
from s3.s3_client import download_files_from_s3
from fileops.file_manager import organize_files



def parse_args():
    parser = argparse.ArgumentParser(description="Batch S3 Excel MySQL Processor")
    parser.add_argument('--db-host', required=True)
    parser.add_argument('--db-port', type=int, default=3306)
    parser.add_argument('--db-user', required=True)
    parser.add_argument('--db-password', required=True)
    parser.add_argument('--db-name', required=True)
    parser.add_argument('--s3-user', required=True)
    parser.add_argument('--s3-bucket', required=True)
    parser.add_argument('--s3-prefix', required=True)
    parser.add_argument('--mock', action='store_true', help="Executa em modo simulado")
    return parser.parse_args()


def main():
    args = parse_args()

    data = get_data(
        host=args.db_host,
        port=args.db_port,
        user=args.db_user,
        password=args.db_password,
        database=args.db_name,
        mock=args.mock
    )

    generate_excel_report(data, output_path="output/report.xlsx", mock=args.mock)

    download_files_from_s3(
        bucket=args.s3_bucket,
        prefix=args.s3_prefix,
        local_dir="downloads",
        user=args.s3_user,
        mock=args.mock
    )

    organize_files(source_dir="downloads", target_dir="arquivos_organizados", mock=args.mock)


if __name__ == "__main__":
    main()
