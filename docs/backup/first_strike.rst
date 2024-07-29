First Strike
============

Now it's time to get cracking. For now, the only part of Selenium 
Oxide that is accessible is the Exploit Builder, so let's play with that.

=========================
Cracking Juice Shop Admin
=========================

To start, let's import the builder. ::

    from selenium_oxide.exploit_builder import ExploitBuilder

The ``ExploitBuilder`` constructor takes a few options, but the only two mandatory
ones are the protocol and hostname. Protocol is either ``http`` or ``https`` in most 
cases, and the hostname is either a domain, a domain and port number, an IP address,
or an IP address and port number. This is all dependent on your situation and what 
you're attacking. For the sake of example, let's say we have a live `Juice Shop`_ instance 
to attack::

    first_exploit = ExploitBuilder("https", "juice-shop.herokuapp.com")

.. _Juice Shop: https://github.com/juice-shop/juice-shop

In that line, Selenium Oxide does a lot of the work for us. It sets up the Selenium driver 
and saves our protocol and domain to its state. It also can tell whether we want stealth 
mode from the constructor, but we'll talk about that later.

Next, let's make our very first exploit! If you don't want spoilers for Juice Shop's Admin 
login challenge, turn away now!

Like now.

Seriously.

I'm warning you.

Okay, you've had enough warning. This challenge is really just an SQL injection into the username
field of the login page. Luckily, Selenium Oxide has a function pre-built for username-password 
login pages. More advanced login pages will need some tinkering, but you can always check the API 
for reference.

We can use ``admin' OR 1=1;--`` for the username and literally anything for the password. For the 
other three arguments to the function, we'll need to dig into the HTML source and copy the XPaths of
the username and password fields, as well as the submit button. ::

    first_exploit.login("/#/login", "admin' OR 1=1;--", "password", '//*[@id="email"]', '//*[@id="password"]', '//*[@id="loginButton"]')

Save the program and run it. You should see a Firefox browser pop up and in a few seconds, you'll 
be logged in as Admin.

Congrats! You just built your first exploit with Selenium Oxide! How easy was that?

================
A Note on XPaths
================

XPaths are the default method of selecting stuff in Selenium Oxide because it's the most reliable method,
and can be done without worrying about whether something has an ID, class name, or anything else.

To copy the XPath of an element, you can right click on it in the inspector and select Copy -> XPath. 

=====================
Stealthy Exploitation
=====================

One of the key features of Selenium Oxide is the exploit builder's stealth mode. This opens up viability
for use in Attack/Defense CTF competitions where a bunch of requests in quick succession will fire off 
blue team alerts like there's no tomorrow.

In essence, the Stealth mode is a sleep timer that scales with the length of your inputs. This may 
become adjustable in future releases, but for now the formula is::
    
    len(text_input) / 5 + random.uniform(0.2, 1)

In essence, a constant factor is applied, along with a bit of floating point randomness for good 
measure.

Try out the same exploit code, but replacing the constructor with the following::

    first_exploit = ExploitBuilder("https", "juice-shop.herokuapp.com", stealth=True)

Save it, and run it again. Notice the difference? The stealth factor is applied with each 
text input, so the delay is much more noticable. This can save you in an attack/defense 
scenario, and can throw off blue teams. That is, of course, assuming you're not obvious with 
your exploits and file names.

Now that you've got a grasp of the module, head over to :ref:`API` for more.