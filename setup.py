from setuptools import setup, find_packages

setup(
    name='tea_AI',
    version='0.1.2',
    packages=find_packages(),
    author_email="nkenyor@gmail.com",
    description="This is a simple package for the Tea Airdrops and development.",
    url = "https://github.com/NtemKenyor/tea_AI",
    entry_points={
        'console_scripts': [
            'make_tea=tea_AI.tea:make_tea'
        ]
    }
)
