from setuptools import setup, find_packages

setup(
    name="project",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "pandas==1.0.3",
        "Flask==1.1.1",
        "SQLAlchemy==1.3.13",
        "Flask-SQLAlchemy==2.4.1",
        "Flask-Cors==3.0.8",
        "Flask-Bootstrap4==4.0.2",
        "Flask-WTF==0.14.3",
        "python-dateutil==2.8.1",
        "python-dotenv==0.10.5",
        "treelib",
    ],
)
