from setuptools import setup
import re

#requirements = []
#with open('requirements.txt') as f:
#    requirements = f.read().splitlines()

version = '2.4.4'
if not version:
    raise RuntimeError('version is not set')

if version.endswith(('a', 'b', 'rc')):
    # append version identifier based on commit count
    try:
        import subprocess

        p = subprocess.Popen(['git', 'rev-list', '--count', 'HEAD'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        if out:
            version += out.decode('utf-8').strip()
        p = subprocess.Popen(['git', 'rev-parse', '--short', 'HEAD'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        if out:
            version += '+g' + out.decode('utf-8').strip()
    except Exception:
        pass

readme = ''
try:
    with open('README.rst') as f:
        readme = f.read()
except: pass

extras_require = {
    'voice': ['PyNaCl>=1.3.0,<1.6'],
    'docs': [
        'sphinx==4.4.0',
        'sphinxcontrib_trio==1.1.2',
        'sphinxcontrib-websupport',
        'typing-extensions>=4.3,<5',
    ],
    'speed': [
        'orjson>=3.5.4',
        'aiodns>=1.1',
        'Brotli',
        'cchardet==2.1.7; python_version < "3.10"',
    ],
    'test': [
        'coverage[toml]',
        'pytest',
        'pytest-asyncio',
        'pytest-cov',
        'pytest-mock',
        'typing-extensions>=4.3,<5',
    ],
}

packages = [
    'discord',
    'discord.types',
    'discord.ui',
    'discord.webhook',
    'discord.app_commands',
    'discord.ext.commands',
    'discord.ext.tasks',
]

setup(
    name='disdick',
    author='cop-discord',
    url='https://github.com/cop-discord/disdick',
    project_urls={
        'Documentation': 'https://discordpy.readthedocs.io/en/latest/',
        'Issue tracker': 'https://github.com/cop-discord/disdick/issues',
    },
    version=version,
    packages=packages,
    license='MIT',
    description='A Python wrapper for the Discord API',
    long_description=readme,
    long_description_content_type='text/x-rst',
    include_package_data=True,
    install_requires=['aiohttp','aiodns','orjson','typing_extensions','psutil','durations_nlp','rust_requests','fast_string_match'],
    extras_require=extras_require,
    download_url='https://github.com/cop-discord/disdick/archive/refs/tags/2.4.1.tar.gz',
    python_requires='>=3.8.0',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        'Typing :: Typed',
    ],
)
