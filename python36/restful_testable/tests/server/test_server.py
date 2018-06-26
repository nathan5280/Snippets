import subprocess


def test_server():
    server_argv = ["python", "calculator_server.py"]
    client_argv = ["python", "calculator_client.py"]
    server_process = None
    try:
        server_process = subprocess.Popen(server_argv)

        result = subprocess.run(client_argv, stdout=subprocess.PIPE)

        assert "result=3" in str(result.stdout)
    finally:
        if server_process:
            server_process.terminate()
