import pytest
import os
import shutil

@pytest.fixture
def tmp_dir():
    """
    Fixture to setup and teardown a temporary directory.
    :return: path to temporary directory
    """
    tmp_dir_path = "tmp"

    # Make the temporary directory
    if os.path.exists(tmp_dir_path):
        shutil.rmtree(tmp_dir_path)

    os.mkdir(tmp_dir_path)

    # Return the name to the as output from the fixture.
    yield tmp_dir_path

    # Remove the temporary directory when the test is complete.
    shutil.rmtree(tmp_dir_path)


def test_tmp_dir(tmp_dir):
    """
    Check to see if the temporary directory was created.

    :param tmp_dir: Path to the temporary directory.

    :return: None
    """
    assert os.path.exists(tmp_dir)


def test_non_empty(tmp_dir):
    # Write a file to temporary directory to make sure that non-empty directories are deleted.
    f = open(os.path.join(tmp_dir, "junk.txt"), 'w').close()

