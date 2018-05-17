---
description: The tests/ directory provides unittests for all modules, classes, and methods.
---

# Tests

Basic tests are provided in the `tests/` directory. These should all pass when running the following command from the root package directory.

```bash
python -m unittest discover -s tests/
```

To review test coverage, we use the `coverage` python package. Once installed, you can generate coverage data and view the results via the terminal or an interactive HTML page.

```bash
# generate coverage data (results are placed in the .coverage file)
coverage run --branch -m unittest discover -s tests/

# generate a terminal coverage report
coverage report -m

# generate html files (results are placed in the htmlcov/ directory)
coverage html
```