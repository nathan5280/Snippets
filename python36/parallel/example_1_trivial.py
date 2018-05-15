import time
import functools

from joblib import Parallel, delayed


class Compute:
    def param_iter(self) -> int:
        """
        Iterator to generate the list of work to be performed.

        :return: Integer to be processed.
        """
        # Play around with these parameters.
        # The difference between the controls how many times the process method is called.
        # The size of them controls how much work the process does.
        # range(10000000, 10000016) The multi-process takes about 25% of the time of the single-process
        # on a quad core (8 Thread) 7700HQ processor.  Not a bad improvement if your code is easy to
        # parallelize with joblib.
        for n in range(10000000, 10000016):
            yield n

    @staticmethod
    def process(n: int) -> float:
        """
        Working process that will can be run in a single process or in multiple processes in parallel.

        :param n: Integer to process.
        :return: The sum of the square roots of all numbers between 0 and n.
        """
        # Do some work that is CPU intensive
        return functools.reduce(lambda a, b: a + b**0.5, range(n))

    def run_single_process(self) -> float:
        """
        Process all of the n's returned by param_iter one after another.

        :return: Sum of the sum of the square roots.
        """
        result = functools.reduce(lambda a, b: a + b, [(Compute.process(n)) for n in self.param_iter()])
        return result

    def run_multi_process(self) -> float:
        """
        Process all the n's in 8 processes.  Tune this parameter based on the number of cores/threads
        the CPU has.

        :return: Sum of the sum of the square roots.
        """
        result = functools.reduce(lambda a, b: a + b,
                                  Parallel(n_jobs=8, verbose=0)(delayed(Compute.process)(n) for n in self.param_iter()))
        return result


if __name__ == '__main__':
    processor = Compute()
    st0 = time.time()
    s_result = processor.run_single_process()
    st1 = time.time()
    print(f"Single: Time: {st1-st0:.2f}, Result: {s_result:.0f}")

    processor = Compute()
    mt0 = time.time()
    m_result = processor.run_multi_process()
    mt1 = time.time()
    print(f"Multi: Time: {mt1-mt0:.2f}, Result: {m_result:.0f}")

    # Calculate the percentage of time the multi-process calculation took compared to the single-process.
    print(f"Processing time: {(mt1-mt0)/(st1-st0):.3f}%")
