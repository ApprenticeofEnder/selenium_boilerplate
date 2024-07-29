API
===

Class ``ExploitBuilder``
------------------------
``selenium_oxide.exploit_builder.ExploitBuilder``

The ExploitBuilder, the bread and butter of Selenium Oxide.

``ExploitBuilder(protocol, hostname, **options)``

Parameters:
    * protocol (str): The protocol to use (either "http" or "https" in most cases)
    * hostname (str): The hostname of the application to access
    * \*\*options

Options:
    * stealth (bool): Whether or not to engage stealth mode (Default: False)
    * browser (str): Which browser to use ("firefox" or "chrome", default: "firefox")
    * use_proxy (bool): Whether or not to use a proxy (Default: False)
    * proxy_address (str): Which proxy address to use (Default: "127.0.0.1:8080")

Methods
#######

Methods for ``selenium_oxide.exploit_builder.ExploitBuilder``

``api``
~~~~~~~
``api(self, req_method: Callable, endpoint: str, api_protocol: str = None, api_hostname: str = None, **kwargs)``

Wrapper for Python's Requests library, enabling automatic proxy usage and cookie sharing when interfacing with APIs. 
kwargs supports same options as Requests.

Parameters:
    * req_method (Callable): requests function to use (requests.get, requests.posts, etc.)
    * endpoint (str): the API endpoint to request
    * api_protocol (str): the protocol to use for the API. Effectively defaults to the same protocol used in the ExploitBuilder
    * api_hostname (str): the hostname to use for the API. Effectively defaults to the same hostname used in the ExploitBuilder
    * \*\*kwargs: interoperable with Python Requests (e.g. headers parameter will be passed into the requests call)

Returns:
requests.Response

``api_get``
~~~~~~~~~~~
``api_get(self, endpoint: str, api_protocol: str = None, api_hostname: str = None, **kwargs)``

Wrapper for ExploitBuilder.api(requests.get, ...).

Parameters:
    * endpoint (str): the API endpoint to request
    * api_protocol (str): the protocol to use for the API. Effectively defaults to the same protocol used in the ExploitBuilder
    * api_hostname (str): the hostname to use for the API. Effectively defaults to the same hostname used in the ExploitBuilder
    * \*\*kwargs: interoperable with Python Requests (e.g. headers parameter will be passed into the requests call)

Returns:
requests.Response

``api_post``
~~~~~~~~~~~~
``api_post(self, endpoint: str, api_protocol: str = None, api_hostname: str = None, **kwargs)``

Wrapper for ExploitBuilder.api(requests.post, ...).

Parameters:
    * endpoint (str): the API endpoint to request
    * api_protocol (str): the protocol to use for the API. Effectively defaults to the same protocol used in the ExploitBuilder
    * api_hostname (str): the hostname to use for the API. Effectively defaults to the same hostname used in the ExploitBuilder
    * \*\*kwargs: interoperable with Python Requests (e.g. headers parameter will be passed into the requests call)

Returns:
requests.Response

``api_put``
~~~~~~~~~~~
``api_put(self, endpoint: str, api_protocol: str = None, api_hostname: str = None, **kwargs)``

Wrapper for ExploitBuilder.api(requests.put, ...).

Parameters:
    * endpoint (str): the API endpoint to request
    * api_protocol (str): the protocol to use for the API. Effectively defaults to the same protocol used in the ExploitBuilder
    * api_hostname (str): the hostname to use for the API. Effectively defaults to the same hostname used in the ExploitBuilder
    * \*\*kwargs: interoperable with Python Requests (e.g. headers parameter will be passed into the requests call)

Returns:
requests.Response

``api_delete``
~~~~~~~~~~~~~~
``api_delete(self, endpoint: str, api_protocol: str = None, api_hostname: str = None, **kwargs)``

Wrapper for ExploitBuilder.api(requests.delete, ...).

Parameters:
    * endpoint (str): the API endpoint to request
    * api_protocol (str): the protocol to use for the API. Effectively defaults to the same protocol used in the ExploitBuilder
    * api_hostname (str): the hostname to use for the API. Effectively defaults to the same hostname used in the ExploitBuilder
    * \*\*kwargs: interoperable with Python Requests (e.g. headers parameter will be passed into the requests call)

Returns:
requests.Response

``click``
~~~~~~~~~~~~~~~~
``click(self, button: str, by: SelectBy = SelectBy.XPATH)``

Clicks an element.

Parameters:
    * button (str): The selector for the element to click
    * by (SelectBy): The selector type to use (default: SelectBy.XPATH)

Returns:
``exploit_builder.ExploitBuilder``

``click_by_class``
~~~~~~~~~~~~~~~~~~~~~~~~~
``click_by_class(self, button_class: str)``

Clicks an element based on CSS class name.

Parameters:
    * button_class (str): The element class name

Returns:
``exploit_builder.ExploitBuilder``

``click_by_id``
~~~~~~~~~~~~~~~~~~~~~~
``click_by_id(self, button_id: str)``

Clicks an element based on HTML ID.

Parameters:
    * button_id (str): The element HTML ID

Returns:
``exploit_builder.ExploitBuilder``

``click_by_xpath``
~~~~~~~~~~~~~~~~~~~~~~~~~
``click_by_xpath(self, xpath: str)``

Clicks an element based on XPath.

Parameters:
    * xpath (str): The element XPath

Returns:
``exploit_builder.ExploitBuilder``

``dump_cookies``
~~~~~~~~~~~~~~~~~~~~~~~
``dump_cookies(self)``

Dumps the cookies into the terminal.

Returns:
``exploit_builder.ExploitBuilder``

``execute_script``
~~~~~~~~~~~~~~~~~~
``execute_script(self, script, *args)``

Wrapper for Selenium's webdriver.execute_script().

Parameters:
    script (str): The JavaScript to execute

Returns:
Any: the return value of the JavaScript

``get``
~~~~~~~~~~~~~~
``get(self, endpoint: str)``

Makes a GET request to the specified endpoint in the browser.

Parameters:
    * endpoint (str): The endpoint to which the browser navigates

Returns:
``exploit_builder.ExploitBuilder``

``get_contents``
~~~~~~~~~~~~~~~~~~~~~~~
``get_contents(self, field: str, by: SelectBy = SelectBy.XPATH)``

Get the contents of a specified field.

Parameters:
    * field (str): The selector to extract text from
    * by (SelectBy): The type of selector to use (default: SelectBy.XPATH)

Returns:
str: The text in the given field

``get_contents_by_id``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
``get_contents_by_id(self, field: str)``

Get the contents of a specified field, based on the HTML ID

Parameters:
    * field (str): The HTML ID to extract text from

Returns:
str: The text in the given field

``get_contents_by_class``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
``get_contents_by_class(self, field: str)``

Get the contents of a specified field, based on the CSS class name

Parameters:
    * field (str): The CSS class name to extract text from

Returns:
str: The text in the given field

``get_contents_by_xpath``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
``get_contents_by_xpath(self, xpath: str)``

Get the contents of a specified field, based on the XPath

Parameters:
    * xpath (str): The XPath to extract text from

Returns:
str: The text in the given field

``get_cookie_by_name``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
``get_cookie_by_name(self, name: str)``

Gets a browser cookie by its name.

Parameters:
    * name (str): The name of the cookie

Returns:
Optional(dict): The cookie, or None

``get_cookies``
~~~~~~~~~~~~~~~~~~~~~~
``get_cookies(self)``

Get all cookies in the browser for the current page.

Returns:
list(dict): A list of cookies in the browser

``login``
~~~~~~~~~~~~~~~~
``login(self, endpoint: str, username: str, password: str, username_xpath: str, password_xpath: str, submit_xpath: str)``

Performs a full login process for a given endpoint. Convenience function.

Parameters:
    * endpoint (str): The location of the login page
    * username (str): The username to use
    * password (str): The password to use
    * username_xpath (str): The XPath of the username field
    * password_xpath (str): The XPath of the password field
    * submit_xpath (str): The XPath of the submit button

Returns:
``exploit_builder.ExploitBuilder``

``send_enter``
~~~~~~~~~~~~~~~~~~~~~
``send_enter(self, field: str, by: SelectBy = SelectBy.XPATH)``

Simulates sending the enter key to a particular element.

Parameters:
    * field (str): The selector of the field
    * by (SelectBy): The selector type to use (default: SelectBy.XPATH)

Returns:
``exploit_builder.ExploitBuilder``

``send_enter_by_class``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
``send_enter_by_class(self, field: str)``

Simulates sending the enter key to a particular element selected by CSS class name.

Parameters:
    * field (str): The CSS Class name of the field to send enter in

Returns:
``exploit_builder.ExploitBuilder``

``send_enter_by_id``
~~~~~~~~~~~~~~~~~~~~~~~~~~~
``send_enter_by_id(self, field: str)``

Simulates sending the enter key to a particular element selected by HTML ID.

Parameters:
    * field (str): The HTML ID of the field to send enter in

Returns:
``exploit_builder.ExploitBuilder``

``send_enter_by_xpath``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
``send_enter_by_xpath(self, xpath: str)``

Simulates sending the enter key to a particular element selected by XPath.

Parameters:
    * field (str): The XPath of the field to send enter in

Returns:
``exploit_builder.ExploitBuilder``

``set_cookie``
~~~~~~~~~~~~~~~~~~~~~
``set_cookie(self, name: str, value: str, path: str = "/", secure: bool = False)``

Set a cookie in the browser.

Parameters:
    * name (str): The name of the cookie
    * value (str): The cookie's value
    * path (str): The path to which the cookie belongs
    * secure (bool): Whether or not the cookie has the Secure attribute

Returns:
``exploit_builder.ExploitBuilder``

``type_entry``
~~~~~~~~~~~~~~~~~~~~~
``type_entry(self, field: str, entry: str, by: SelectBy = SelectBy.XPATH)``

Send text to a particular field.

Parameters:
    * field (str): The selector of the field
    * entry (str): The text to enter into the field
    * by (SelectBy): The selector type to use (default: SelectBy.XPATH)

Returns:
``exploit_builder.ExploitBuilder``

``type_by_class``
~~~~~~~~~~~~~~~~~~~~~~~~
``type_by_class(self, field: str, entry: str)``

Send text to a particular field selected by CSS class name.

Parameters:
    * field (str): The CSS class name of the field
    * entry (str): The text to enter into the field

Returns:
``exploit_builder.ExploitBuilder``

``type_by_id``
~~~~~~~~~~~~~~~~~~~~~
``type_by_id(self, field: str, entry: str)``

Send text to a particular field selected by HTML ID.

Parameters:
    * field (str): The HTML ID of the field
    * entry (str): The text to enter into the field

Returns:
``exploit_builder.ExploitBuilder``

``type_by_xpath``
~~~~~~~~~~~~~~~~~~~~~~~~
``type_by_xpath(self, field: str, entry: str)``

Send text to a particular field selected by XPath.

Parameters:
    * field (str): The XPath of the field
    * entry (str): The text to enter into the field

Returns:
``exploit_builder.ExploitBuilder``

``wait_for_alert``
~~~~~~~~~~~~~~~~~~~~~~~~~
``wait_for_stealth(self, entry: str = "")``

Waits for an alert to fire, looking for an optional marker.

Parameters:
    * timeout (int): The amount of time to wait for an alert
    * marker (Optional[str]): A known marker, used to detect XSS attacks

Returns:
bool: whether or not the alert fired

``wait_for_stealth``
~~~~~~~~~~~~~~~~~~~~~~~~~~~
``wait_for_alert(self, timeout: int = 3, marker: Optional[str] = None)``

Waits for a period of time based on the length of the entry.

Parameters:
    * entry (str): The entry to scale by

Returns:
``exploit_builder.ExploitBuilder``

Class ``SelectBy``
------------------
``selenium_oxide.exploit_builder.SelectBy``

A wrapper for Selenium's By enum. Literally only changes the name to avoid confusion with Selenium.

Class ``SeO2User``
------------------------
``selenium_oxide.user_generator.SeO2User``

Generates an individual user for use with Selenium Oxide. Uses Faker.

``SeO2User(self, gen: Faker = None, locale: str = "en_US", **data)``

Parameters:
    * gen (faker.Faker): a Faker generator to use for the user. Defaults to an individually made generator.
    * locale (str): a locale to use for Faker. Defaults to "en_US".
    * \*\*data

All provided data is optional and overrides Faker profile generation.

Data:
    * name (str): The user's name
    * sex (str): The user's sex (usually "M" or "F") determines name gender in lieu of a provided name. Feel free to put "X" for a nonbinary name 
    * username (str): The user's username
    * email (str): The user's email
    * address (str): The user's address
    * birthdate (datetime.date): The user's date of birth

Methods
#######

Methods for ``selenium_oxide.user_generator.SeO2User``

``get_generator``
~~~~~~~~~~~~~~~~~
``get_generator(self)``

Getter method for the user's generator.

Returns:
``faker.Faker``