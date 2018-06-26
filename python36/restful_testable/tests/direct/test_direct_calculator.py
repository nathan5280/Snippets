import subprocess


def test_direct_calculator():
    argv = ["python", "calculator_direct.py"]
    result = subprocess.run(argv, stdout=subprocess.PIPE)

    assert "result=3" in str(result.stdout)