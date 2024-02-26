from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='tea_AI',
    version='0.1.3',
    packages=find_packages(),
    author_email="nkenyor@gmail.com",
    description="This is a simple package for the Tea Airdrops and development.",
    url = "https://github.com/NtemKenyor/tea_AI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    entry_points={
        'console_scripts': [
            'make_tea=tea_AI.tea:make_tea'
        ]
    }
)
