from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='simit',
    version='0.0.1',
    description='Unit Converter using Text Similarity',
    url='https://github.com/naufalafif/simit',
    author='Naufal Afif',
    author_email='naufalafif58@gmail.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development',
    ],
    keywords=['unit converter','text similarity'],
    packages=['simit'],
    install_requires=['pint', 'python-Levenshtein'],
)