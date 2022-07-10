from setuptools import find_packages, setup

setup(
    name='coding_interview',
    version='1.0.0',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    zip_safe=False,
    python_requires='>=3.10.*',
    install_requires=[
        'bitarray==2.5.1'
    ]
)
