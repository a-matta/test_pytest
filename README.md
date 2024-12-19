# test_pytest

A short description of the project

---


---

## Development

* Requirements:
  * [Poetry](https://python-poetry.org/)
  * Python 3.12+
  * [Install Allure Report](https://allurereport.org/docs/install/)
* Create a virtual environment and activate it
  ```sh
  poetry shell
  ```
* Install the dependencies
  ```sh
  poetry install
  ```
* Running the tests
  ```sh
  # Uses PyInvoke
  inv tests
  ```
* To view the allure reports.
  ```sh
  allure serve allure-results
  ```
## Run Tests
pytest filename -rA 
* view test results in xml formate -> dump to xml file  &   see test suites and test cases

  ```sh
  pytest filename -rA --junitxml="Report.xml"
  ```
* view test results -> install pytest-html(Open in live server)
  ```sh
  pytest --html nameoffile.html
  ```
* Run mark - regression
  ```sh
  pytest filename -m smoke/regression
  ```

