import glob
import os
import time
from collections import deque
from typing import List

from joblib import Parallel, delayed


class ClimbTree:
    """
    Processor to count how many files are in a directory tree.  The functionality isn't important.
    It is just something that takes time and lends itself to obvious paralisim.
    """

    def __init__(self):
        """
        Initialize where to start the count.
        """

        self._dirs = 0
        self._queue = deque()

    @property
    def dirs(self) -> int:
        return self._dirs

    def _add_dirs(self, dirs: List[str]) -> None:
        """
        Add the new list of directories to queue.
        :param dirs: List of files to add to the queue.
        :return: None
        """
        for dir_ in dirs:
            self._queue.append(dir_)

        self._dirs += len(dirs)

    def next_dir(self) -> str:
        """
        Get the next dir off the queue.

        :return: Next directory.
        """
        while True:
            try:
                dir_ = self._queue.popleft()
                yield dir_
            except Exception:
                raise StopIteration

    @staticmethod
    def process_dir(dir_: str) -> List[str]:
        """
        Get a list of all the files in the directory and add them to the queue.

        :param dir_: Directory to process the files from.
        :return: List of files in the directory.
        """
        files = glob.glob(os.path.join(dir_, "*"))
        dirs = []
        for file in files:
            if os.path.isdir(file):
                dirs.append(file)

        # print(f"Processing: {dir_}, Files: {len(files)}, Dirs: {len(dirs)}")
        # Do something that hits on the CPU
        # If there isn't enough CPU bound work to do in the process
        # then the overhead of starting the process overwhelms the
        # benefit and you should just stick with single process version.
        _ = [n**0.5 for n in range(50000000)]
        return dirs

    def run_single_process(self, dir_: str) -> None:
        """
        Count all the files using only a single process.

        :param dir_: Directory to start counting files.
        """

        # Initialize the dir queue with the top level directories.
        dirs = ClimbTree.process_dir(dir_)
        self._add_dirs(dirs)

        # Process all the dirs until there are no more in the queue.
        [self._add_dirs(ClimbTree.process_dir(dir_)) for dir_ in self.next_dir()]

    def run_multi_process(self, dir_: str) -> None:
        """
        Count all the files using 8 processes. (Set this to match your cpu)

        :param dir_: Directory to start counting files.
        """
        # Initialize the dir queue with the top level directories.
        flat_dirs = ClimbTree.process_dir(dir_)
        self._add_dirs(flat_dirs)

        while len(flat_dirs):
            dirs = Parallel(n_jobs=8, verbose=0)(delayed(ClimbTree.process_dir)(dir_)
                                                 for dir_ in self.next_dir())
            flat_dirs = ([dir_ for dir_list in dirs for dir_ in dir_list])
            self._add_dirs(flat_dirs)


if __name__ == '__main__':
    processor = ClimbTree()
    st0 = time.time()
    processor.run_single_process(dir_=os.path.expanduser(".."))
    st1 = time.time()
    print(f"Single: Time: {st1-st0:.2f}, Dir: {processor.dirs}")

    processor = ClimbTree()
    mt0 = time.time()
    processor.run_multi_process(dir_=os.path.expanduser(".."))
    mt1 = time.time()
    print(f"Multi: Time: {mt1-mt0:.2f}, Dir: {processor.dirs}")

    print(f"Processing time: {(mt1-mt0)/(st1-st0):.3f}%")