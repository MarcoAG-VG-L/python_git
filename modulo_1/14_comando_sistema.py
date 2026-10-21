import os
import subprocess


comando = ["cmd", "/c", "dir"] if os.name == "nt" else ["ls"]
resultado = subprocess.run(
    comando,
    check=True,
    capture_output=True,
    text=True,
)
print(resultado.stdout)
