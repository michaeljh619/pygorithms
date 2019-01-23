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

## Contributing
If you wish to contribute, feel free to fork a copy and get started. However, there are a few things to do before you contribute:

### pytest
This project uses many pytest modules and a git pre-commit hook to ensure bugs are caught before any commits are made. You will need to have [pytest installed](https://docs.pytest.org/en/latest/getting-started.html) on your machine.

### pycodestyle
This project follows the code style guidelines in pycodestyle. You will need to have [pycodestyle installed](https://pypi.org/project/pycodestyle/) on your machine.

### validate
An executable file called *validate* comes in the root directory of this repo. To make sure any code changes pass pytest and pycodestyle, you can simply run this executable to check all the code for you.

### Setup Git Hooks
As mentioned before, a pre-commit hook is used to validate all code passes pytest and pycodestyle before any commits are accepted. Essentially, this hook will run the *validate* executable for you and reject the commit if *validate* comes back with any error messages.

To set up this git hook, simply run the *setup* executable file in the root directory of this repo and it will create a file to automatically validate the code against pytest and pycodestyle before any commits are made.
