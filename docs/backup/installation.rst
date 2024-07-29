Installation
============

Installation of Selenium Oxide requires Selenium. Hope you saw that coming.

For the sake of convenience, though, I'll lay out the steps to get Selenium 
up and running in addition to Selenium Oxide.

==========
Unix/macOS
==========

Selenium Oxide supports both Firefox and Chrome.

Firefox
~~~~~~~

First, you'll want to grab a binary of Firefox. I recommend the following flow
for installing on UNIX systems. Once you've downloaded a version of firefox you 
like (for that, the official download page is usually sufficient): ::

    tar -xjf your_firefox_archive.tar.bz2
    sudo mv firefox /opt

This way, your Firefox binary will be in ``/opt/firefox/firefox``, which is the
default location the module looks at. Perfect.

If you already have a Firefox binary on hand (maybe you already used Selenium),
then you can just specify the location in the exploit builder constructor. 

Alternatively, if you want to use your existing installation of Firefox, you can
locate the binary and create a symlink from it to ``/opt/firefox/firefox``: ::

    for b in $(find / -name "firefox*" 2>/dev/null); do file $b; done | grep ELF
    
(Note the path to the binary the search found) ::

    sudo ln -s [absolute_path_to_binary] /opt/firefox/firefox

Then, you'll need Geckodriver. You can grab that from `here.`_ ::

    tar -xzf your_geckodriver_archive.tar.gz
    sudo mv geckodriver /usr/bin

.. _here.: https://github.com/mozilla/geckodriver/releases

So long as Geckodriver is in your path, you should be golden.

Chrome
~~~~~~

Installing Chrome for Seleniumis usually even easier than installing Firefox. Install Chrome normally
through your preferred package manager, then grab a copy of Chromedriver. Extract it and move 
it into /opt like so: ::

    sudo mv chromedriver /opt

Also for reference, you can find your Chrome binary with the ``which`` command: ::

    which google-chrome

Final Steps
~~~~~~~~~~~

Next, just install from Pip! ::

    python3 -m pip install selenium-oxide

If that doesn't work, you may have an outdated version of Selenium (this library needs 4.1.0 or greater).
If so: ::

    pip install --upgrade selenium

=======
Windows
=======

Documentation on that is definitely a work in progress.

===============
Getting Started
===============

There you go! Now, let's get started. Head on over to :ref:`First Strike`.

