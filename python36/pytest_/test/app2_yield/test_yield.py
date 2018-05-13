import pytest
import os
import shutil

tmp_dir_path = "tmp"


@pytest.fixture
def jam_tmp_dir():
    """
    Fixture that creates a tmp directory and leaves it in place for the main tmp_dir to clean up.  This
    test fixture is only created to drive code coverage of the tmp_dir test fixture.
    :return: None
    """
    if not os.path.exists(tmp_dir_path):
        os.mkdir(tmp_dir_path)

@pytest.fixture
def tmp_dir():
    """
    Fixture to setup and teardown a temporary directory.
    :return: path to temporary directory
    """
    # Delete the directory if it exists.
    if os.path.exists(tmp_dir_path):
        shutil.rmtree(tmp_dir_path)

    # Make the temporary directory
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


def test_tmp_exists(jam_tmp_dir, tmp_dir):
    pass