import setuptools

with open('requirements.txt') as f:
    required = f.read().splitlines()

setuptools.setup(
    name="aws-cloud-instance-list",
    version="0.0.1",
    description="Aws cloud instance list",
    author="sh.kiruh@gmail.com",
    packages=setuptools.find_packages(where="src"),
    install_requires=required,
    extras_require={
        'dev': [
            'pytest',
        ]
    },
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
    ],
    entry_points={
        "console_scripts": ["get-instance-list=main:run"],
    },
)
