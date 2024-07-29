# Selenium-Oxide

A Selenium boilerplate for automating web exploits. Use responsibly and ethically.

Selenium Oxide is a web exploitation automation framework designed
around the needs of penetration testers and attack/defense CTF players
alike! Whether you need to quickly make an automated
exploit for web apps, a stealthy automation tool for attack/defense,
or a springboard for other exploit development, this is the tool for you!

The module offers a slimmer API than standard Selenium, and has
multiple handy features, such as:

* Stealth functionality
* Builder pattern exploit writing
* Automatic browser binary configuration
* Cookie dumping and manipulation
* Proxy support
* Chrome support
* Arbitrary selector support
* Alert waiting
* User generation
* API interface
* JavaScript execution

## Why the Name?

When making this module I initially struggled with
what to call it. I happened to look at another module,
named Selenium Wire, and decided yeah, you know what,
using Selenium in the name is fair game. Selenium Oxide
sounded cool, and when I looked up information on the
chemical it read that it was at least somewhat dangerous.

A dangerous version of Selenium. Checks out for an offsec
platform.

## Getting Started

Like regular Selenium, you're going to need a browser binary
and geckodriver.

NOTE: ***Selenium Oxide Chrome support is currently untested. Proceed at your own risk.***

Selenium Oxide supports both Firefox and Chrome.

### Firefox

To simplify things, I've provided an install script for Firefox that will download compatible
versions of Firefox and Geckodriver. These *should* work for most cases, however I recommend
submitting an issue in the event you find a use case for older or more modern versions.

```bash
sudo ./install_firefox.sh
```

Otherwise, you can manually install versions of Firefox and Geckodriver at your own discretion.
If you ever find yourself needing to do that, I'm assuming you don't need instructions for that.

### Chrome

Chrome installation is currently undocumented, however you will need the Chrome Webdriver as well as the Chrome binary itself.

### Final Steps

Next, just install from Pip!

```bash
    pip install selenium-oxide
```

If that doesn't work, you may have an outdated version of Selenium (this library needs a version compatible with 4.1.0).
If so:

```bash
    pip install selenium~=4.1.0
```

That should install everythng you need.

## Using Selenium Oxide

Selenium Oxide is a builder-pattern exploit automation
framework, designed to provide a more immediately usable
method of exploit automation before resorting
to using the network tab. The ability to use proxies
makes the tool extremely useful as a ground layer for
API-focused exploit development as well.

### The Basics

First, import the module:

```python
from selenium_oxide import ExploitBuilder
```

The ExploitBuilder constructor can take something as simple as a URL to test, or you can add additional options:

```python
exploit = ExploitBuilder(
    base_url="https://juice-shop.herokuapp.com",
    stealth=False, # if True, enable Stealth Mode
    browser="firefox", # either "firefox" or "chrome"
    use_proxy=False, # if you want to use a proxy, enable this
    proxy_address="127.0.0.1:8080", # defaults to 127.0.0.1:8080
    headless=False, # if you want headless Selenium enable this
    **options       # other options, see ExploitBuilder docs
)
```

Stealth mode is interesting, allowing the user to avoid alerting blue teams with multiple rapid requests. As of 2.0.0, it uses the length of user inputs to determine how long its sleep time is before writing text in input boxes. There is some randomness thrown in as well, to really throw off blue teams. However, this may be painfully slow while you're waiting on the input to appear, so do keep an eye on your terminal for crashes.
Adjustable stealth timings may appear in a future release.

Proxy support is a 1.0.0 addition, allowing the user to use proxies (such as ZAP or Burp Suite) to track their HTTP requests and responses. This is handy for mapping out APIs and finding potential additional vulnerabilities.

To start building exploits, you can chain functions together!

```python
(
    exploit.get("/")
        .login("/#/login", "admin' OR 1=1;--", "password", '//*[@id="email"]', '//*[@id="password"]', '//*[@id="loginButton"]')
        .type_entry('//*[@id="mat-input-0"]', "<img src=\"http://url.to.file.which/not.exist\" onerror=alert(document.cookie);>")
        .send_enter('//*[@id="mat-input-0"]')
)
```

However, some functions, like `get_cookies` or `get_cookie_by_name` cannot be chained into
other functions, and further exploitation must begin on a new line.
