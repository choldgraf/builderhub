from setuptools import setup, find_packages

setup(
    name='builderhub',
    version='0.1',
    install_requires=[
        'kubernetes==1.*',
        'tornado',
        'traitlets'
    ],
    author='Yuvi Panda',
    author_email='yuvipanda@gmail.com',
    license='BSD',
    packages=find_packages(),
    include_package_data=True
)
