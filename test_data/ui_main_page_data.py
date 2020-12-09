"""Данные для тестов главной страницы"""
from UI.locators.locators import MainPageLocators as mpl


# todo можно попробовать спарсить через Driver.getCurrentUrl();
PARAMS_FOR_GO_TO = [
    (mpl.PYTHON, mpl.PYTHON, "Welcome to Python.org"),
    (mpl.PYTHON, mpl.PYTHON_HISTORY, "History of Python - Wikipedia"),
    (mpl.PYTHON, mpl.ABOUT_FLASK, "Welcome to Flask — Flask Documentation (1.1.x)"),
    (mpl.LINUX, mpl.LINUX, "Linux"),
    (mpl.LINUX, mpl.DOWNLOAD_CENTOS_7, "Centos"),
    (mpl.NETWORK, mpl.NETWORK, "Network"),
    (mpl.NETWORK, mpl.WIRESHARK_NEWS, "Wireshark · News"),
    (mpl.NETWORK, mpl.WIRESHARK_DOWNLOAD, "Wireshark · Go Deep."),
    (mpl.NETWORK, mpl.TCPDUMP_EXAMPLES, "Tcpdump Examples"),
    (mpl.WHAT_IS_AN_API, mpl.WHAT_IS_AN_API, "API - Wikipedia"),
    (mpl.FUTURE_OF_INTERNET, mpl.FUTURE_OF_INTERNET, "What Will the Internet Be Like in the Next 50 Years?"),
    (mpl.LETS_TALK_ABOUT_SMTP, mpl.LETS_TALK_ABOUT_SMTP, "SMTP — Википедия")
]

PARAMS_FOR_TEST_ACCORDION_BUTTONS = [
    (mpl.PYTHON, [mpl.PYTHON_HISTORY, mpl.ABOUT_FLASK]),
    (mpl.LINUX, [mpl.DOWNLOAD_CENTOS_7]),
    (mpl.NETWORK, [mpl.WIRESHARK_NEWS, mpl.WIRESHARK_DOWNLOAD, mpl.TCPDUMP_EXAMPLES])
]

MAIN_PAGE_INTERACTIVE_BUTTONS_LIST = [
    value for name, value in vars(mpl).items()
    if type(value) == tuple and name not in ["PANEL", "VK_ID", "LOG_OUT", "LOGGED_AS"]
]
