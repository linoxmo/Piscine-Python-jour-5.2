try:
    from dotenv import load_dotenv
except ImportError as e:
    print(e)

import os
from typing import Optional


def get_variable(name: str, default: Optional[str] = None) -> str:
    value = os.getenv(name, default)
    if value is None:
        return "Missing"
    return value


def main() -> None:
    load_dotenv()

    mode = get_variable("MATRIX_MODE", "development")
    datab = get_variable("DATABASE_URL")
    api = get_variable("API_KEY")
    log = get_variable("LOG_LEVEL", "DEFAULT")
    zion = get_variable("ZION_ENDPOINT")

    print("ORACLE STATUS: Reading the Matrix...")
    print("Mode:", mode)
    print("Database: ", datab)
    if api != 'Missing':
        print("Authenticated")
    else:
        print("Missing")

    print("Log Level:", log)
    print("Zion Network:",  zion)

    if (
        mode == "Missing"
        or datab == "Missing"
        or api == "Missing"
        or log == "Missing"
        or zion == "Missing"
    ):
        print("\nSome variables are missing")
        return

    print("\nEnvironment security check:\n[OK]")


if __name__ == "__main__":
    main()
