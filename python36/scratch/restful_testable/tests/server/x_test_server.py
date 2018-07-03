import subprocess
import time


def test_server():
    server_argv = ["python", "calculator_server.py"]
    client_argv = ["python", "calculator_client.py"]
    server_process = None
    try:
        pass
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
