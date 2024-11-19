from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="wordfilegenerator",
    version="1.0.0",
    description="Generate custom wordlists for brute force testing.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["your_package_name"],
    license="MIT",
)

