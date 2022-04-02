import enum
import pathlib
import sys


class ExitCode(enum.IntEnum):
    GOOD = 0
    I837_FAILED = 1
    P837_FAILED = 2
    I837_AND_P837_FAILED = 3


EXIT_CODE = ExitCode.GOOD

root = pathlib.Path(r"X:\precombine")
i837 = root / "837i"
p837 = root / "837p"

# https://docs.python.org/3/tutorial/errors.html
try:
    for file in i837.iterdir():
        with file.open() as file_handle:
            first_line = file_handle.readline()

        if "837p" in first_line:
            file.unlink()
# except:
# except FileNotFoundError:
# except (Exception, FileNotFoundError):
# except Exception as err:
except FileNotFoundError as err:
    print(f"837i deletion failed: {err.strerror}")
    EXIT_CODE = ExitCode.I837_FAILED

try:
    for file in p837.iterdir():
        with file.open() as file_handle:
            first_line = file_handle.readline()

        if "837i" in first_line:
            file.unlink()
except FileNotFoundError as err:
    print(f"837p deletion failed: {err.strerror}")

    if EXIT_CODE is ExitCode.I837_FAILED:
        EXIT_CODE = ExitCode.I837_AND_P837_FAILED
    else:
        EXIT_CODE = ExitCode.P837_FAILED

sys.exit(EXIT_CODE)
