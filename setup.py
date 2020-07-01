import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name="gsbuild",
    version="1.0",
    author="Muda42",
    author_email="polak.daniel05@outlook.com",
    description="Compiler for Google's Product Sans font",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Muda42/gsbuild",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
