#pytest

There is a ton of material about why to write unit tests across all programing languages.  For Python, pytest 
seems to be one of the more popular, active and intuitive testing frameworks.   There is good support for it
within PyCharm.  With all that in mind, this will be a pretty short overview.

pytest online documentation: https://docs.pytest.org/en/latest/

## General Notes
1. Why is the module called pytest_ instead of just pytest?  If the module is called pytest it conflicts with the 
pytest module that we need to load to run pytests.  Go ahead and change it to pytest and see if you scratch you 
head the way I did when I tried to sort out that resulting error messages.
2. Test files, cases and classes all start or end with the name 'test'.  This allows pytest to search through
the files in a project and identify the testing code and run it automatically without the need for you to explicitly
call any of the tests yourself.

## app1_basics
**pytest_.app1_basic.wallet.py:** Application code for a simple Wallet that we can add and subract money from.
This is the class that some of the tests will run against.

**pytest_.test.app1_basic:** Module with the tests for the Wallet class.  Note that the tests for the Wallet
class are in a Python package structure that mimics the application code.  This isn't strictly necessary, but
does help simplify the mental mapping and understanding of how the test cases map to the application code.

**test_wallet.py:** This is the most basic way that tests are written against a class.  
1. **@pytest.fixture:** functions get passed into the test cases and are called before / as the test case is being called.
These fixtures define setup code that normally would appear in every test case.  
Test fixtures are a powerful way to dramatically simplify each of the individual test cases.
2. **@pytest.mark.parameterize:** Provides a list of parameters to run a test case multiple times with 
different input.  It is python code that is evaluated like any other piece of python code and allows you
to get pretty creative on how to build the list of parameters for running the test case.
3. The last test case uses a test fixture that is defined outside of the current file and thus can be shared
across multiple test files.  These test fixtures are always in a file called **conftest.py**.

**test_wallet_class.py:** This file shows how to pull the test cases into a test class.  Not only does
this help with organization of test cases, but it allows for resource management and optimization.  An 
example of this is shown **app3_scope**.

**app2_yield:** Demonstrates a test fixture that works as both setup and teardown code
that runs before and after the test case.  In this example the test fixture creates a 
temporary directory and returns the path of the directory to the test case like a norma
test fixture with a yield instead of a return statement.  The **@pytest.fixture** decorator
then calls the test fixture a second time after the test case has complete and execution 
resumes after the yield.  In this example the fixture cleans up the temporary directory.
Every test case gets a new clean temporary directory to execute in and the gets automatically
cleaned up after it has run.

**app3_scope:**  Some tests have expensive setup procedures.  Examples could be establishing
network or database connections.  These resources may be reused across multiple tests and
setting up and tearing them down for each test can significantly extend the time to execute
the test suite.  There are two expensive_setup test fixtures defined in the file and
each of them is passed to the two test cases in the two test classes.  When they run
the first test fixture is always executed.  The second one is only executed once for 
each test class.  This is defined with the scope="class" in the pytest.fixture 
decorator.  