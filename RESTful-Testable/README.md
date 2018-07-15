# RPN Calculator (RESTful and Testable)
Show the steps to build a RPN calculator model through to a RESTful server capable of managing 
multiple concurrent calculations using Flask, SQLAlchemy, and JWT.  Demonstrate how to efficiently 
test along the way using PyTest.

## Step-1 Building the RPN Calculator Model
### Environment
The environment is python 3.6 and is managed with PipEnv.

```commandline
pipenv python 3.6

pipenv install pytest
```

### 
1. Build the RPN calculator model.  (models/rpn.py)
1. Build the model directly into an application.  (direct.py)
1. While the above script can test the capabilities of the model, it isn't a very scalable solution.  Build the
pytest version of the test script.  (tests/models/test_rpn.py)
   *Notes*
   * Test directories are directories not packages. They don't contain a __init__.py.
   PyTest will search them unless explicitly directed not to.
   * Test file names start with "test_".  This is the clue to PyTest
   that a file contains test cases.
   * Common setup code is implemented in test fixtures.  Test fixtures are shared across test files through the
   conftest.py file.
   * The tests can be run from the commandline in the step-1-model directory.  You may need
   to set PYTHONPATH=. in the environment.  Execute the tests by executing "pytest".
   * See how the last test (test_value_add_missing_operand_fail) tests the case where there is a
   missing operand and the add tries to pop off a missing value and throws an IndexError.