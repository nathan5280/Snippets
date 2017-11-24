# Get a temporary directory from pytest
def test_needs_files(tmpdir):
    print()
    print('----> Temporary directory', tmpdir)
    assert 1
