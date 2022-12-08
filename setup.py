from setuptools import setup, find_packages

setup(
    name="bibledatadb",
    version="1.0.0",
    description="Bible Data Database Generator",
    url="",
    author="Elliot Dronebarger",
    author_email="elliot.dronebarger@gmail.com",
    packages=find_packages(),
    install_requires=[
        'SQLAlchemy>=1.4.0',

    ],
    entry_points={
        'console_scripts': [
            'bibledatadb = bibledatadb.main:internal_main',
        ],
    }
)
