import sys 
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
        print("MATRIX STATUS: You're still plugged in")
        print("Current python:", sys.executable )
        print("Virtual Environment: None detected")
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print("To enter the construct, run:")
        print("python3 -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activate # On Windows")
        print("Then run this program again.")
    else:
         print("MATRIX STATUS: Welcome to the Matrix")
         print("Current python ", sys.executable)
         print("Environnement_path" ,venv_path)
         print("SUCCESS, You’re in an isolated environment!")
         print("Safe to install packages without affecting")
         print("the global system.")s
         print("Package installation path:")

        


if __name__ == "__main__":
    main()