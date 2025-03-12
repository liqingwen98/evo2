from setuptools import setup, find_packages

def parse_requirements(filename):
    requirements = []
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                requirements.append(line)
    return requirements

with open('evo2/version.py') as infile:
    exec(infile.read())

with open('README.md') as f:
    readme = f.read()

setup(
    name='evo2',
    version=version,
    packages=find_packages(include=["evo2",]),
    package_data={'evo2': ['evo2/configs/*.yml']},
    include_package_data=True,
    python_requires='>=3.10',
    license="Apache-2.0",
    description='Genome modeling across all domains of life',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Team Evo 2',
    url='https://github.com/arcinstitute/evo2',
)