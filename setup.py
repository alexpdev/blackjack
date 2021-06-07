import setuptools
from setuptools import setup, find_packages
import json

package = json.load(open("package.json", "rt"))

version = package.get("version")

with open("README.md", encoding="UTF-8") as readme:
    long_description = readme.read()



setup(
    name=package.get("name"),
    version=version,
    description=package.get("description"),
    long_description=long_description,
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
    ],
    keywords=package.get("keywords"),
    author=package.get("author"),
    author_email="alexpdev@protonmail.com",
    url="https://github.com/alexpdev/blackjack",
    project_urls={"Source Code": "https://github.com/alexpdev/blackjack"},
    license="GNU GPLv3",
    packages=find_packages(exclude=["env", "docs", "node_modules", ".vscode"]),
    include_package_data=True,
    install_requires=["PyQt6"],
    tests_require=["pytest"],
    setup_requires=["setuptools"],
    zip_safe=False,
    test_suite="tests",
)
