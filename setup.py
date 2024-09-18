
import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "CrypeAlbatros",
    version = "1.10.5",
    author = "byt3n33dl3",
    author_email = "byt3n33dl3@proton.me",
    description = " CrypeAlbatros is a handy SMB enumeration tool ",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/byt3n33dl3/CrypeAlbatros",
    project_urls = {
        "Bug Tracker": "https://github.com/byt3n33dl3/CrypeAlbatros/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    packages =[ "CrypeAlbatros" ],
    python_requires = ">=3.6",
    install_requires = [
        'impacket',
        'pyasn1',
        'pycryptodome',
        'configparser',
        'termcolor',
    ],
    entry_points={
        'console_scripts': [
            'CrypeAlbatros=CrypeAlbatros.CrypeAlbatros:main'
        ]
    },
)
