import os
import numpy as np
import testipynb
import unittest

NBDIR = os.path.sep.join(
    os.path.abspath(__file__).split(os.path.sep)[:-2]
)

IGNORE = [
    "1-magnetic-inversion-raglan-reproduce",
    "3-magnetic-inversion-raglan-lp.ipynb",
    "2-linear-inversion-app.ipynb"
]

Test = testipynb.TestNotebooks(directory=NBDIR, timeout=2800)
TestNotebooks = Test.get_tests()

if __name__ == "__main__":
    unittest.main()
