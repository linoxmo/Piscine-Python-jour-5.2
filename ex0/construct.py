from struct import pack
import sys 
import os
import site
from typing import Optional, Tuple


def verify() -> Tuple[bool, Optional[str]] :
    in_environnement: bool = False
    venv_path = sys.prefix
    if hasattr(sys, "base_prefix") and sys.prefix != sys.base_prefix:
        in_environnement = True
        return in_environnement, venv_path
    else:
        return in_environnement, None


def main():
    venv, venv_path = verify()
    if not (venv):
        print("MATRIX STATUS: You're still plugged in\n")
        print("Current python:", sys.executable )
        print("Virtual Environment: None detected\n")
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")
        print("To enter the construct, run:")
        print("python3 -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activate # On Windows\n")
        print("Then run this program again.")
    else:
         base_name = os.path.basename(venv_path) if venv_path else "unknown"
         package = site.getsitepackages()
         print("MATRIX STATUS: Welcome to the Matrix\n")
         print("Current python: ", sys.executable)
         print("Virtual Environment: " + base_name)
         print("Environnement_path:" ,venv_path)
         print("\nSUCCESS, You’re in an isolated environment!")
         print("Safe to install packages without affecting")
         print("the global system.\n")
         print("Package installation path:")
         print(package[0])

        


if __name__ == "__main__":
    main()
