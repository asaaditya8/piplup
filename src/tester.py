import pytest
import sys

if __name__ == "__main__":
    retcode = pytest.main(["--tb", "native", "--json-report", "-n", "auto"])
    print('retcode', retcode)
    sys.exit(retcode)