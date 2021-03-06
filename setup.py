from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name = 'pygasflow',
    version = '0.9.0',
    description = 'Ideal Gasdynamics utilities for Python 3.6+',
    long_description = readme(),
    classifiers=[
        'Development Status :: 1 - Alpha',
        'License :: GNU GPL v3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Engineering :: Propulsion',
    ],
    keywords='gasdynamic shockwave fanno rayleigh isentropic flow',
    url = 'https://github.com/Davide-sd/pygasflow',
    author = 'Davide Sandona',
    author_email = 'sandona.davide@gmail.com',
    license='GNU GPL v3',
    packages = [
        'pygasflow',
        'pygasflow.nozzles',
        'pygasflow.solvers',
        'pygasflow.utils',
    ],
    include_package_data=True,
    zip_safe = False,
    install_requires = [
        "numpy",
        "scipy",
        "matplotlib"
    ]
)
