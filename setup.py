from distutils.core import setup
from setuptools import find_packages

setup(
    name='jitterbit-plugin',
    version='0.1',
    url='https://github.com/ju55i/jitterbit-plugin',
    license='EUPL',
    author='Jussi Talaskivi',
    author_email='jptalask@gmail.com',
    description='Jitterbit plugin SDK for Python',
    classifiers=["Programming Language :: Python"],
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    install_requires=["setuptools", "lxml"]
)
