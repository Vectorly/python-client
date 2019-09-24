import setuptools

try:  # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError:  # for pip <= 9.0.3
    from pip.req import parse_requirements

with open("README.md", "r") as fh:
    long_description = fh.read()

reqs = parse_requirements("requirements.txt", session=False)
install_requires = [str(ir.req) for ir in reqs]

setuptools.setup(
    name="vectorly",
    version="0.0.1",
    author="Alexander Stepanov",
    author_email="stvalxv+python@gmail.com",
    description="Python library for uploading, compressing and streaming videos using Vectorly's stream product",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/stvalxv/vectorly",
    install_requires=install_requires,
    include_package_data=True,
    packages=setuptools.find_packages(),
    python_requires=">=3.5",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

