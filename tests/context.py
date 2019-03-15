import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import sepulcrum  # noqa

from sepulcrum.cli import main  # noqa
from sepulcrum.log import get_logger  # noqa
