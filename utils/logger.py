import logging


class Logger:
    """Logger class that holds the logging decorators for the project"""

    @staticmethod
    def interaction_logger(func):
        """Logging decorator for browser interactions.

        Args:
            func: Function to be decorated
        """
        def wrapper(*args, **kwargs):
            page_name = args[0]
            func_name = func.__name__.replace("_", " ").capitalize()
            locator_name = (args[1] if len(args)>1 else kwargs.get("locator")).replace("_", " ").title()

            try:
                # Try to execute the function
                _function = func(*args, **kwargs)
                logging.info("%s: %s on %s", func_name, locator_name, page_name)
                return _function
            except Exception as exception:
                # If function fails, log an error
                logging.error("%s: %s on %s", func_name, locator_name, page_name)
                logging.error(exception)
                raise

        return wrapper


    @staticmethod
    def matcher_logger(func):
        """Logging decorator for matcher functions.

        Args:
            func: Function to be decorated
        """

        def wrapper(*args, **kwargs):
            page_name = args[0]
            func_name = func.__name__.replace("_", " ").capitalize()

            try:
                # Try to execute the function
                _function = func(*args, **kwargs)
                if len(args) > 2:
                    logging.info("%s with argument '%s' on %s: %s",
                                func_name, args[1], page_name, _function)
                else:
                    logging.info("%s on %s: %s",
                                func_name, page_name, _function)

                return _function
            except Exception as exception:
                # If function fails, log an error
                logging.error("%s on %s", func_name, page_name)
                logging.error(exception)
                raise

        return wrapper
