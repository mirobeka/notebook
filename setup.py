from setuptools import setup

setup(
    name="notebook",
    version='0.1',
    long_description="Client server REST API web application for making notes",
    packages=['notebook'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask==0.10.1'
    ]
)
