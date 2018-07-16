import subprocess
import time


def test_client_server_pass():
    """
    Test the RESTful API by starting both the client and server in subprocesses.
    Check that the client outputs the correct answer to stdout.
    """
    server_argv = ['python', 'server.py']
    client_argv = ['python', 'client.py']

    server_process = None
    try:
        server_process = subprocess.Popen(server_argv, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Give the server some time to start up.
        # If you get errors in this test that include "ConnectionRefusedError: [Errno 111] Connection refused"
        # try increasing this time.
        time.sleep(0.5)

        result = subprocess.run(client_argv, stdout=subprocess.PIPE)

        assert "result=3" in str(result.stdout)

    finally:
        if server_process:
            server_process.terminate()
