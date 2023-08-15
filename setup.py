from setuptools import setup, find_packages


with open("README.markdown", "r", encoding="utf-8") as readme_file:
    long_description = readme_file.read()


setup(
    name="smpp.twisted",
    version="0.4",
    author="Roger Hoover",
    author_email="roger.hoover@gmail.com",
    description="SMPP 3.4 client built on Twisted",
    license="Apache License 2.0",
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="smpp twisted",
    url="https://github.com/eaitelecom/smpp.twisted",
    py_modules=["smpp.twisted"],
    include_package_data=True,
    package_data={"smpp.twisted": ["README.markdown"]},
    zip_safe=False,
    install_requires=[
        'twisted',
        'pyOpenSSL'
    ],
    tests_require=[
        'mock',
    ],
    test_suite='smpp.twisted.tests',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Twisted",
        "Topic :: System :: Networking",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
