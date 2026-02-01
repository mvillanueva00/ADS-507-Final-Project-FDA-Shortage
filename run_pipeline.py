#this script will run full FDA ETL pipeline using Github Actions
#The order follwed for ETL steps is
#dowload data
#process data
#load to MYSQL

import subprocess
import sys


def run(cmd: list[str]) -> None:
    """Run a command and stop pipeline if it fails."""
    print(f"Running: {' '.join(cmd)}")
    subprocess.run(cmd, check=True)


def main() -> None:
    try:
        # Download raw data
        run(["python", "scripts/download_data.py"])

        # Process raw data into CSVs
        run(["python", "scripts/process_data.py"])

        # Load CSVs into MySQL
        run(["python", "scripts/load_to_mysql.py"])

        # Run SQL transformations
        run([
            "mysql",
            "-h", "127.0.0.1",
            "-u", "root",
            "-prootpassword",
            "fda_shortage_db",
            "<", "sql/02_transformations.sql"
        ])

        print("ETL pipeline completed successfully.")

    except subprocess.CalledProcessError as e:
        print("ETL pipeline failed.")
        sys.exit(1)


if __name__ == "__main__":
    main()


