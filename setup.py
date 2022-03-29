from setuptools import setup, find_packages

version = "0.1.0"

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt") as f:
    required = f.read().splitlines()
setup(
    name="mkdocs_custom_fences",
    python_requires=">=3.7",
    version=version,
    description=" A series of snippets to create custom fences for mkdocs ",
    author="Mara-Li",
    author_email="mara-li@icloud.com",
    packages=find_packages(),
    install_requires=required,
    license="AGPL",
    keywords="mkdocs, custom_fences, pymdownx, markdown extension, markdown, md",
    classifiers=[
        "Natural Language :: English",
        "Natural Language :: French",
        "Topic :: Text Processing :: Markup :: Markdown",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later"
        " (AGPLv3+)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Mara-Li/mkdocs_custom_fences",
)
