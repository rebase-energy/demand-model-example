from setuptools import find_packages, setup


# # get the dependencies and installs
requires = []
with open("requirements.txt", encoding="utf-8") as f:
    requires = [line.strip() for line in f.readlines()]


setup(
    name="demand_model_example",
    version="0.1",
    packages=find_packages(),
    #entry_points=entry_points,
    install_requires=requires
)
