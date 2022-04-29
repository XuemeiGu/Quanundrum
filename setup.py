from setuptools import setup, find_packages


# This reads the __version__ variable from quanundrum/_version.py
exec(open('quanundrum/_version.py').read())

# Readme file as long_description:
long_description = open('README.md').read()

# Read in requirements.txt
with open('requirements.txt', 'r') as f_requirements:
    requirements = f_requirements.readlines()
requirements = [r.strip() for r in requirements]

setup(
    name='quanundrum',
    version=__version__,
    author='quanundrum',
    author_email='jangnurgin@gmail.com,simon.mathis@gmail.com,',
    url='https://github.com/jangnur/Quanundrum',
    description=('quanundrum - '
                 'An open source software framework for simulating quantum thought experiments'),
    long_description=long_description,
    install_requires=requirements,
    zip_safe=False,
    license='MIT License',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3.7',
    ],
    python_requires='>=3.6',
)