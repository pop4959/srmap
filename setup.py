import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="srmap",
    version="0.0.2",
    author="pop4959",
    author_email="pop4959@gmail.com",
    description="SpeedRunners map editing library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pop4959/srmap",
    packages=setuptools.find_packages()
)
