from setuptools import setup, find_packages


def read_requirements():
    with open('requirements.txt') as f:
        return f.read().splitlines()


setup(
    name="clank",
    version="0.1",
    description="CLI Example",
    python_requires=">=3.7.0",
    license='MIT',
    pacakges=find_packages("clank"),
    install_requires=read_requirements(),
    classifiers=[
        "Natural Language :: English",
    ],
    entry_points={
        "console_scripts": [
            "clankcli=clank:cli"
        ]
    }
)
