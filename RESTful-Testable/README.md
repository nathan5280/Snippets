# RPN Calculator (RESTful and Testable)
Demonstrate through a number of incremental stages how to implement a RESTful API that incorporates
the following capabilities.
* RESTful API using Flask-RESTful
* Testability of:
    * Direct invocation of the model from Python script.
    * Unit testing of the model using PyTest.
    * Client server invocation of the model functionality.
    * Unit testing of the RESTful API using PyTest.
* Storing state in DB across method invocations using SQLAlchemy.
* Java Web Tokens using Flask-JWT for simple user authentication.
* (Future) Managing long running jobs outside the request/response and http server process leveraging Celery.

# Stages
The example is broken down into several stages were each stage demonstrating a new piece of the
overall functionality.
* **Stage 1:** "Hello, World!" - Simple Flask Application used to add two numbers together.  Leverage
this application to demonstrate all four modes of testing.
* **Stage 2:** Rework the simple add calculator to an RPN calculator that tracks the state of the
stack between invocations.  This stage just manages the state in a list in memory.  It isn't 
suitable for a multi-client environment, but it lets us work out the API that can be expanded to a
 multi-client, multi-server environment.
* **Stage 3:** Fully functional multi-client, multi-server model with state stored in the DB
* **Stage 4:** User authentication to make sure only valid users can use the calculator.

### Environment
The environment is python 3.6 and is managed with PipEnv.

```commandline
pipenv python 3.6

pipenv install coverage pytest requests flask flask-restful sql-alchemy flask-jwt celery
```

## Stage-1: "Hello, World!" 
This Stage implements a simple server that adds two numbers together and returns the results.  It
is a good starting point to make sure that we can automate the testing of all for testing modes 
in a scalable and understandable manner.

* **Direct:** 

   Run 
   ```commandline
   $ export PYTHONPATH=.
   $ cd stage-1-hello-world
   $ python direct.py
   ```
   or run from the pytest.
   ```commandline
   pytest -k 'direct'
   ```

   *Notes:*
   * The unit test runs direct.py in a subprocess and checks to see that the correct
   response is sent to stdout.
   
* **Model:** 
   ```commandline
   pytest -k 'models'
   ```
   
* **Client/Server:** 
   Run the server and client in different shells.
   ```commandline
   $ cd stage-1-hello-world
   $ python server.py
   $ python client.py
   ```
   or
   ```commandline
   $ pytest -k 'client'
   ```

   
* **RESTful API:**

   This is the money case.  Flask exposes an in process version of the server through flask.testing.FlaskClient.
   By coding the unit tests against this client a number of benefits are realized.
   * No need to spin up subprocesses and manage their life cycles and timing issues.
   * Debug both the client (unit test) and server in the same PyCharm process.
   * Run code coverage on the server along with the tests.
   
   ```commandline
   $ pytest -k 'rest'
   ```

###Results
The output of PyTest when run from stage-1-hello-world shows that all 4 of the test models were run successfully.

```commandline
Testing started at 3:45 PM ...
/home/nathan/.virtualenvs/RESTful-Testable-21eBrR1d/bin/python3.6 /home/nathan/bin/pycharm-2018.1.3/helpers/pycharm/_jb_pytest_runner.py --path /home/nathan/projects/Snippets/RESTful-Testable/stage-1-hello-world
Launching py.test with arguments /home/nathan/projects/Snippets/RESTful-Testable/stage-1-hello-world in /home/nathan/projects/Snippets/RESTful-Testable/stage-1-hello-world

============================= test session starts ==============================
platform linux -- Python 3.6.5, pytest-3.6.3, py-1.5.4, pluggy-0.6.0
rootdir: /home/nathan/projects/Snippets/RESTful-Testable/stage-1-hello-world, inifile:
plugins: celery-4.2.0collected 4 items

tests/client-server/test_client_server.py .                              [ 25%]
tests/direct/test_direct.py .                                            [ 50%]
tests/models/test_add_calculator.py .                                    [ 75%]
tests/restful/test_rest_calculator.py .                                  [100%]

=========================== 4 passed in 0.93 seconds ===========================
Process finished with exit code 0
```
That isn't bad.  1 second to know that everything is working.  Actually it is only 0.5 seconds to run the tests
as there is a 0.5 second sleep in the client-server test to give the server time to startup.
   
###Summary
This stage has demonstrated how to test the model with PyTest directly as well as how to invoke the model with
a standalone application.  Similarly the RESTful API was tested with standalone server applications and with
PyTest leveraging the FlaskClient.  Developing models and RESTful APIs to support the PyTest methodologies for
unit and integration testing brings all the benefits of testing to the party.  Moving forward only the PyTest
methodologies for testing the model and the RESTful API will be used.  The Direct and Client/Server models
are really deployment scenarios.  They may need additional test for these depolyments, but it will be limited
to deployment and not model implementation.

This stage was developed using the following workflow:
1. Implement the model.
1. Unit test the model with  tests/models/test_add_calculator.py
1. Implement resources/calculator.py and server/calculator_server.py
1. Integration test the RESTful API with tests/restful/test_rest_calculator.py

All other implementation direct.py, client.py, server.py and their corresponding unit tests were done to show
how the functionality will ultimately be deployed and methods to use PyTest to validate their deployment.

It is recommended the above 4 step process be used for development and testing of Flask based 
RESTful APIs wrapped around fully testable standalone models.


## Stage-2 Building the RPN Calculator Model
The AddCalculator was pretty darn boring, but it provides a foundation for how to test Models and the RESTful
API that wraps around them.  Let's build a more complicated RPNCalculator that has to manage state (Stack of Operands),
the beginning and end of a calculation across multiple operations.  We'll keep it simple by only implementing
the addition and subtraction operations.

### Development Steps
1. Implement the RPNCalculator model.  

   1. Break out the Stack in preparation for moving this functionality to the database in Stage 3.

   1. Factor out the binary_op functionality as writing the add operator and then the sub operator immediately
   showed most of the code was duplicated between them.

   1. Add the concept of the calculation id.  This will allow the persistent storage of the stacks in the 
   db in Stage 3.  It also drives additional lifecycle interactions with the model.
      1. Calculations must call start to get a new stack with a unique id.
      1. All calls to operators for the calculation must pass this id.
      1. The server is still stateful in the sense that it has the stack in memory, but now it is straight 
      forward to move the stack to the DB and completely move the state out of the server.  The start method
      creates the unique id which will be part of the location url returned in the RESTful API.
      
1. Test the model.

   1. The model test fixture needs to return two pieces of information to the tests.  It creates a new 
   RPNCalculator object and calls start on it to get the ID of the calculation.  To allow dotted access
   to this information in the test case a *namedtuple* is used.  This creates a new data only class (ModelData)
   that is returned by the fixture.

   1. The model test cases are written in the same way that the Stage 1 model test cases were developed.  
      1. There are test cases now that test the failure modes on the stack.  These are basically ones
      where the state of the stack is wrong and those where the ID of the calculation is wrong.  The 
      former are captured with the OperandError and the latter with InvalidContextError.
      1. Review the code coverage in the model classes.  This can show where additional tests
      are required.  Code coverage doesn't insure that all paths through the code have been
      tested, but code that hasn't been tested is suspect.
   ```commandline
   $ pytest -k '_rpn'
   ```
1. Implement the Resources and Server.

   1. /calculator - POST is used to create the new calculator.  POST is used when the client
   doesn't know the url of the resource that is being created and the server will generate it.

   1. /calculator/\<int:calc_id> - PUT, data={operator, operand}, operator=(push, add, sub) 
   is used for the operators that change the state of the calculator

   1. /calculator/\<int:calc_id> - GET, returns the result or top most operand in the stack.

   1. /calculator/\<int:calc_id> - DELETE removes the stack from the calculator.  In Stage 3 
   this will be used to clean up the database.  

1. Test the RESTful API

   1. Focus the test on the RESTful interface and not all of the functionality of the model.

   1. Review the code coverage in the two resource files for feedback on where more tests
   are needed.
   ```commandline
   $ pytest -k 'rest'
   ```
   
### Summary
Stage 2 showed how new functionality can be developed by following the 4 step process introduced in Stage 1
to create a more complex model and API.  Unit tests are in place for both the model and the API with good 
separation of concerns for the functionality and unit tests.  100% code coverage for the model and API was 
achieved with 18 tests that run in less than 1/5 of a second.  Not surprisingly there is substantially more 
test code than model or resource code.  The good news is that after the first couple of tests are written
the rest are fairly easy to implement.  There are many PyTest recipes to help reduce the amount of this
code.

| Functionality | Implementation | Test |
|:--------------|---------------:|-----:|
| Model         | 97             | 182  |
| Resources     | 66             | 99   |

On to Stage 3.  Lets see how little code we have to modify to move Stack to the DB.

## Stage-3 Converting the Stack to a DB
Implementing a Stack that holds Operands in the DB using SQLAlchemy to replace the Stack in the RPNCalculator turns out
to be pretty straight forward.  

### Development Steps
1. Implemnet the DB Stack model/functionality.

   1. SQLAlchemy and support code 

      1. Implement *db.py* to handle the table creation, connection and session management for the implementation.

      1. Define the declarative base *AppDBBase* used for ORM.

      1. Implement *create_db()* to manage connections to the database.

      1. Implement the *session_scope* Context Manger to make sure all sessions are correctly committed, 
      rolled back and closed.

   1. Implement *db_stack.py*

      1. This is a standard sqlalchemy implementaiton of an Operand class that has a foreign key relationship
      to a table for the Stack.  Stacks are started with a unique ID and all operators are implemented using 
      the ID for that stack.

      1. Currently the client is responsible for cleaning up the stack when the calculation is complete.  There 
      should probably be garbage collection of calculations that are abandoned by the client to keep the DB
      from filling up.
      
1. Test the Stack DB implementation.

   1. For the db test fixture that creates the db before each test, the *autouse=True* is passed to the
   pytest.fixture decorator so that it is run before each test.  
   
      There are other arguments that can control the scope that the fixture is run within.  If the tests are 
      bundled into a class then the fixture could be run once for test class.

   1. For the db test fixture it uses a yield statement to return the calc_id when the calculation has been started.
   After the test completes execution, control is returned to the fixture and the calculation is deleted.  
   This is a good way to make sure that resources are closed and freed as part of the testing process.
   ```commandline
   $ pytest -k 'db_stack'
   ```
1. Modify the implementation of the RPNCalculator.  This worked out pretty well with only a few minor changes.

   1. Update the import so that it points to the new implementation.  We could have skipped this if we had
   named the DBStack the same as the original Stack.

   1. Replace the initialization of the RPNCalculator class scope stack with an instance of the DB Stack.  We only
   need to do this once instead of everytime we created a Calculator.  This is what we want.  Now the 
   RPNCalculator has no state information and can run in a multi-client/multi-server deployment model.

   1. Update the start method.  No need to to manage the state of the internal Stack.

   1. Update the delete method to call delete on the DB Stack.

   1. *Note* No modifications were required in *test_rpn.py* to get the tests to pass.  This is exactly what 
   we want to happen.  We changed the underlying functionality/implementation, but didn't impact the public
   interface or behavior.
   ```commandline
   $ pytest -k 'rpn'
   ```

1. Run the unit tests.   

    1. The RESTful API tests all pass with zero modification. Perfect!

    1. Check the code coverage and implement any additional tests that are needed.
    ```commandline
    $ pytest
    ```

### Comments
I've used SQLAlchemy straight out of the box vs. using the flask-sqlalchemy package.  Flask-sqlalchemy has 
some nice integration features that manage sessions for each invocation of an endpoint, but it also makes it
difficult to do model testing independently of Flask.  The primary problem is that the base class used to 
create ORM classes is different for sqlalchemy and flask-sqlalchemy.  It is possible to use some Python
black magic to change the base class depending on whether the class is used without Flask or with Flask.  In the
end it isn't worth the complexity and you have to manage the session explicitly in the model either way.
 
## Stage-4 JWT Authentication
Wrap the calculator start endpoint with JWT authentication so only authorized users can create a new calculator.

### Development Steps
1. Implement a basic user class.  This would obviously have a more robust and secure implementation with hashing
of passwords and a non-memory based user list.  The simple implementation allows for users to be looked up by
username or ID.

1. Test the User functionality

1. Implement the *authenticate()* and *identity()* functions in *authenticate.py* for Flask-JWT 
to authenticate and identify users.

1. Test the authenticate functionality.

1. Update the server to initialize JWT.  Here again the secret_key needs a better production home.  Initialize
JWT with the above mentioned *authenticate()* and *identity()* functions.

1. Decorate the appropriate methods with '@jwt_required()'. **!!!!!!! Note that the decorator has () at the end.
without this you get a very difficult error to track down. !!!!!!!**  If you get a stack trace that ends with 
something like this,
   ```commandline
     File "/usr/lib/python3.6/json/encoder.py", line 180, in default
       o.__class__.__name__)
     TypeError: Object of type 'function' is not JSON serializable
   ```

   then you probably are missing the ().  If you use flask_jwt_extended then it doesn't required 
   the ().  You've been warned.

1. Leverage *the auth.client.authorize()* wrapper method to simplify adding the authorization to the header 
for all the API calls.
```python
    url = '/calculator/v0'
    response = authorize(client.post, url, auth_token=auth_token, json={})
```
1. Add a pytest.fixture to conftest.py to get that authentication token.
```python
@pytest.fixture
def auth_token(client: FlaskClient):
    url = "auth"

    response = client.post(url, json={"username": "peter", "password": "123"})
    assert 200 == response.status_code
    return response.get_json()["access_token"]
```

### Summary
1. OK, the authentication is pretty minimalist, but it makes it pretty simple after it is setup.  There is clearly
a need for user management, password resets, role based access and operations that are all supported through 
flask_jwt or flask_jwt_extened.
