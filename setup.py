from setuptools import setup, find_packages

setup(
    name='systeminfo',
    version='0.0.1',
    url='https://github.com/ridhima-singh-dev/systeminfo.git',
    author='ridhima-singh-dev',
    author_email='ridhimasingh217@gmail.com',
    description='My system Info',
    packages=find_packages(),
    install_requires=[
        'dependency1',
        'dependency2',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
    entry_points={
        'console_scripts': [
            'my_project_script=systeminfo:main',
        ],
    },
)

