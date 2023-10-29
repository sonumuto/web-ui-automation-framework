<h1 align="center"> WebUI Page Object Model Framework </h1>

This is a WebUI Page Object Model Framework using Selenium WebDriver, Python and pytest.
There are some example pages and tests in the project to help you get started.

## Getting Started

To be able to run the tests, you need to install followings:
1. Python3 (3.11 is recommended)
2. chromedriver or geckodriver (depending on the browser you want to use)
3. Required packages using the following command:

    ```bash
    pip install -r requirements.txt
    ```

## Running the tests

To run the tests, you can use the following command:

```bash
pytest
```

If you do not specify the browser it will run the tests on Firefox by default. You can specify the browser using the following command:

```bash
pytest --browser-name chrome
```

You can also choose to run the tests in headless mode using the following command:

```bash
pytest --headless True
```

Or you can run the tests on different view size using the following command:

```bash
pytest --device-view tablet
```

There are markers for the tests. You can run the tests with specific markers using the following command:

```bash
pytest -k login
```

Keep that in mind if you want to add new markers to the tests, you need to add them to the pytest.ini file as well.
