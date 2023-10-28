from splinter import Browser


class BrowserFactory:
    """Browser Factory Class"""
    @staticmethod
    def get_browser(browser_name: str, device_view: str, headless: bool=True) -> Browser:
        """Get browser object from given parameters

        Args:
            browser_name (str): Name of the browser. ["chrome", "firefox", "safari"]
            device_view (str): Device name to size the view. ["desktop", "tablet", "mobile"]
            headless (bool, optional): Headless mode. Defaults to True.

        Raises:
            Exception: If given device_view is invalid.
            Exception: If given browser_name is invalid.

        Returns:
            Browser: Browser object
        """
        match device_view:
            case "desktop":
                view_width = 1920
                view_height = 1080
            case "tablet":
                view_width = 820
                view_height = 1180
            case "mobile":
                view_width = 390
                view_height = 844
            case _:
                raise ValueError("Invalid device view")

        if browser_name in ["chrome", "firefox"]:
            browser = Browser(driver_name=browser_name, headless=headless)
            browser.driver.set_window_size(view_width, view_height)
            return browser

        raise ValueError("Invalid browser name")
