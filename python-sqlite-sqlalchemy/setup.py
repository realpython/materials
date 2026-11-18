from setuptools import find_packages, setup

setup(
    name="project",
    version="1.0",
    packages=find_packages(),
    python_requires=">=3.11",
    install_requires=[
        "pandas==3.1.1",
        "Flask==3.1.3",
        "SQLAlchemy==2.1.9",
        "Flask-SQLAlchemy==3.1.1",
        "Flask-Cors==6.0.5",
        "Flask-Bootstrap4==4.0.2",
        "Flask-WTF==1.3.0",
        "python-dateutil==4.0.0",
        "python-dotenv==1.2.4",
        "treelib==1.8.0",
    ],
)
