import subprocess


def test_direct_calculator_pass():
    """Invoke the model functionality directly."""
    argv = ['python', 'direct.py']
    result = subprocess.run(argv, stdout=subprocess.PIPE)

    assert "result=3" in str(result.stdout)