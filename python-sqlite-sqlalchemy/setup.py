from setuptools import setup, find_packages

setup(
    name="project",
    version="1.0",
    packages=find_packages(),
    install_requires=["SQLAlchemy", "treelib"],
)
