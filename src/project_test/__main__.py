"""Executable module for ``python -m project_test``.

Python runs this file when the package is executed as a module. The real entry
logic lives in ``main.py`` so it can also be imported and tested directly.
"""

from project_test.main import main

if __name__ == "__main__":
    main()
