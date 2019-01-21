# pygorithms
Algorithms written in python.  This repository contains common algorithms learned in CS classes, from sorting to searching and more.


## Getting Started
Since the project is still small enough, simply clone the repository and write any code in a python file in the repo's root directory. For example, if you wish to use the merge sort algorithm from the sorting folder, you could create a python file in the repository's root directory:

*merge_sort_example.py*

	from sorting.merge_sort import MergeSort

	unsorted_list = [5, 3, 4, 1, 2]
	sorted_list = MergeSort.sort(unsorted_list)

	print("Unsorted: " + str(unsorted_list))
	print("Sorted: " + str(sorted_list))


##  Automated Testing
This project comes complete with its own automated tests, as well as code style checks. In the root directory, there is an executable file called *validate*. Simply run validate from the command line and it will run pytest and pycodestyle for you. You will need both [pytest](https://docs.pytest.org/en/latest/getting-started.html) and [pycodestyle](https://pypi.org/project/pycodestyle/) installed to run *validate*.

If you change any code, you will need to run *validate* to ensure that you did not break anything and that the code style is still preserved.

### Code Style
This project's code is compliant with [pycodestyle](https://pypi.org/project/pycodestyle/). 

### Running the Tests
Simply run pytest from command prompt at the root directory of the repository and it will run all the tests available:

	$ pytest
	============================= test session starts =============================
	platform win32 -- Python 2.7.15, pytest-4.1.1, py-1.7.0, pluggy-0.8.1
	rootdir: F:\Michael\Programming\Algorithms\pygorithms, inifile:
	collected 12 items

	sorting\test_sorting.py ............                                     [100%]

	========================== 12 passed in 0.06 seconds ==========================
Of course, you can also run pytest from a sub-directory and it will only run the tests in that folder and any of its sub-directories.

### Sorting Algorithm Tests
Since the sorting algorithms all extend *BaseClass*, these tests are parameterized to take all the sub-classes of *BaseClass*. In other words, all the sorting algorithms are put through these same tests:
- Trivial Case: An empty list or a list with one element
- Least to Greatest: Test a valid list, sorting from least to greatest
- Greatest to Least: Test a valid list, sorting from greatest to least
- Not a List: Test that the sorting algorithm fails gracefully when passed a non-list type
