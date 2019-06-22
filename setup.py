import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="node-buffer",
    version="0.1.0",
    author="Miraculous Owonubi",
    author_email="omiraculous@gmail.com",
    description="A minor rewrite of the NodeJS Buffer Library for efficient memory management",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='Apache-2.0',
    url="https://github.com/miraclx/node-buffer",
    packages=['node_buffer'],
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
    ],
)
