Botoman
=======

This bot configured for telegram for sending cat pictures to the user.

Installation
------------

Create install, configure and start virtual environment `venv`_:

.. code-block:: text

    pip install -r requirements.txt
    python -m venv env
    source env/bin/activate

Put images with cats to images folder with filenames cat, only jpg files accepted

Configure
---------
Create file bot_settings.py and add there this settings

.. code-block:: python

    PROXY = {
        'proxy_url': 'socks5://YOUR_SOCKS5PROXY:YOUR_PORT',
        'urllib3_proxy_kwargs': {'username': 'LOGIN',
            'password': 'PASSWORD'}}

    API_KEY = "API KEY generated from BotFather"


    USER_EMOJI = [':mask:', ':poop:', ':hamster:', ':boy:', ':girl:', ':kiss:']

START
-----

.. code-block:: text

    python3 bot.py

.. _venv: https://docs.python.org/3/tutorial/venv.html