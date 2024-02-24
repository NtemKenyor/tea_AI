from setuptools import setup, find_packages

setup(
    name='tea_AI',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'make_tea=tea_AI.tea:make_tea'
        ]
    }
)
