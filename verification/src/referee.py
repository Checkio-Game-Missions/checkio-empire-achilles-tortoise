from checkio_referee import RefereeBase
from checkio_referee import covercodes, validators, representations, ENV_NAME


import settings_env
from tests import TESTS

Validator = validators.FloatEqualValidator

Validator.PRECISION = 8


class Referee(RefereeBase):
    TESTS = TESTS
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    DEFAULT_FUNCTION_NAME = "chase"
    VALIDATOR = Validator
    CALLED_REPRESENTATIONS = {
        ENV_NAME.PYTHON: representations.unwrap_arg_representation,
        ENV_NAME.JS_NODE: representations.unwrap_arg_representation
    }
    ENV_COVERCODE = {
        ENV_NAME.JS_NODE: covercodes.js_unwrap_args,
        ENV_NAME.PYTHON: covercodes.py_unwrap_args,
    }
