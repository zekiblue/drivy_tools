import csv
import time
from typing import List

from drivy_tools.state import state


def save_csv(*, results_dir, header: List[str] = None, results: List[dict], name_of_csv: str):
    if not header:
        header = results[0].keys()

    directory = f"{results_dir}/{name_of_csv}.csv"
    with open(directory, "w") as handle:
        dict_writer = csv.DictWriter(handle, header)
        dict_writer.writeheader()
        dict_writer.writerows(results)
    print(f"Csv saved to the {directory}")


def time_it(func):
    if state.verbose:

        def inner_(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            elapsed = time.perf_counter() - start
            print(f"Execution for {func.__name__} took: {elapsed}")
            return result

        return inner_
    else:

        def inner_(*args, **kwargs):
            result = func(*args, **kwargs)
            return result

        return inner_
