from checkio_referee import RefereeBase
from checkio_referee.covercode import py_unwrap_args
from checkio_referee.validators import FloatEqualValidator

import settings
import settings_env
from tests import TESTS

FloatEqualValidator.PRECISION = 8


class Referee(RefereeBase):
    TESTS = TESTS
    EXECUTABLE_PATH = settings.EXECUTABLE_PATH
    CURRENT_ENV = settings_env.CURRENT_ENV
    FUNCTION_NAME = "chase"
    VALIDATOR = FloatEqualValidator
    ENV_COVERCODE = {
        "python_2": py_unwrap_args,
        "python_3": py_unwrap_args,
        "javascript": None
    }
