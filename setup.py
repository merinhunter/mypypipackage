import setuptools

setuptools.setup(
    name="mypypipackage",
    version="0.0.1",
    author="Sergio Merino Hernández",
    author_email="sergiohdez94@gmail.com",
    description="A small example package",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
