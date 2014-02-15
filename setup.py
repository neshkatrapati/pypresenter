from setuptools import setup

setup(name='pypresenter',
      version='0.1',
      description='Presentations from the CommandLine',
      url='https://github.com/neshkatrapati/pypresenter',
      author='Ganesh Katrapati',
      author_email='ganesh@swecha.net',
      license='GNU GPL V3+',
      packages=['pypresenter'],
      install_requires = [
        'pyfiglet',
        'python-aalib',
        'colorama',
        'termcolor',
      ],
      zip_safe=False)
