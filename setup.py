from setuptools import setup, find_packages

with open("requirements.txt") as f:
    required = f.read().splitlines()

with open("README.md", "r", encoding="utf-8") as readme_file:
    long_description = readme_file.read()

setup(
    name="navigator",
    version="1.0.1",
    packages=find_packages(),
    install_requires=required,
    entry_points={
        "console_scripts": [
            "operate=operate.main:main_entry",
        ],
    },
    package_data={
        "operate.models.weights": ["best.pt"],
    },
    long_description=long_description,
    long_description_content_type="text/markdown",
)
