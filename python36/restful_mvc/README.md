# RESTful API example.

This snippet focus on testing of models, controllers and the REST API.  SQLAlchemy is used throughout this 
example as the backend for the model.  Session management is handled outside of the controller to allow
switching between using straight SQLAlchemy for the model or switching to Flask-SQLAlchemy with sesison management
handled at the resource layer.

Note how the flask testing client is used to develop unit tests at he RESTful API layer.  This is nice because
the http server runs in the same process as client tests and simplifies debugging.