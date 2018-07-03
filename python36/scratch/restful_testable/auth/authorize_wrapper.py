def authorize(web_method, url, *args, auth_token, **kwargs):
    """
    Wrap a FlaskClient test object method call to add the authorization information to the headers dictionary.

    :param web_method: The Web Method to wrap.
    :param url: The URL the method is called against.
    :param args: Any additional positional arguments.
    :param auth_token: The Authorization Token to add to the headers dictionary.
    :param kwargs: Any additional key word arguments.

    :return: The response to the Web Method.
    """
    # Get any headers information that is set in kwargs.
    existing_headers = kwargs.get("headers", {})

    # Add or update the Authorization item in the headers dictionary.
    existing_headers.update({"Authorization": f"JWT {auth_token}"})
    kwargs.update({"headers": existing_headers})

    # Call the web method with the authorization information.
    return web_method(url, *args, **kwargs)