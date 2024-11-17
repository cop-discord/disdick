disdick
==========

.. image:: https://discord.com/api/guilds/1054447513794515146/embed.png
   :target: https://discord.gg/r3sSKJJ
   :alt: Discord server invite
.. image:: https://img.shields.io/pypi/v/disdick.svg
   :target: https://pypi.python.org/pypi/disdick
   :alt: PyPI version info
.. image:: https://img.shields.io/pypi/pyversions/disdick.svg
   :target: https://pypi.python.org/pypi/disdick
   :alt: PyPI supported Python versions

A discord.py fork focused on scalability and efficiency, fixing exploitable issues, implementing caching for invalid user IDs, ratelimiting, and more features.

Key Features
-------------

- Modern Pythonic API with ``async`` and ``await``.
- Robust rate limit handling.
- Optimized for speed and memory efficiency.
- Enhanced invalid checking and rate limiting to prevent Cloudflare bans, with optional proxy arguments for heavy API calls.
- Direct message limitations to avoid bot flagging.
- Smart unbanning via ``guild.smart_unban()``.
- Improved speed and reduced thread usage.
- Clustering support with built-in IPC handling.

Installing
----------

**Python 3.8 or higher is required**

To install the library without full voice support, you can just run the following command:

.. code:: sh

    # Linux/macOS
    python3 -m pip install -U git+https://github.com/cop-discord/disdick

    # Windows
    py -3 -m pip install -U git+https://github.com/cop-discord/disdick

Otherwise to get voice support you should run the following command:


To install the development version, do the following:

.. code:: sh

    $ git clone https://github.com/cop-discord/disdick
    $ cd disdick
    $ python3 -m pip install -U .[voice]


Optional Packages
~~~~~~~~~~~~~~~~~~

* `PyNaCl <https://pypi.org/project/PyNaCl/>`__ (for voice support)

Please note that when installing voice support on Linux, you must install the following packages via your favourite package manager (e.g. ``apt``, ``dnf``, etc) before running the above commands:

* libffi-dev (or ``libffi-devel`` on some systems)
* python-dev (e.g. ``python3.8-dev`` for Python 3.8)

Quick Example
--------------

.. code:: py

    import discord

    class MyClient(discord.Client):
        async def on_ready(self):
            print('Logged on as', self.user)

        async def on_message(self, message):
            # don't respond to ourselves
            if message.author == self.user:
                return

            if message.content == 'ping':
                await message.channel.send('pong')

    intents = discord.Intents.default()
    intents.message_content = True
    client = MyClient(intents=intents)
    client.run('token')

Bot Example
~~~~~~~~~~~~~

.. code:: py

    import discord
    from discord.ext import commands

    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix='>', intents=intents)

    @bot.command()
    async def ping(ctx):
        await ctx.send('pong')

    bot.run('token')

You can find more examples in the examples directory.

Links
------

- `Documentation <https://discordpy.readthedocs.io/en/latest/index.html>`_
- `Official Discord Server <https://discord.gg/r3sSKJJ>`_
- `Discord API <https://discord.gg/discord-api>`_
