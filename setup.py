from setuptools import setup
import os

readme = ""
if os.path.exists("README.rst"):
    with open("README.rst") as f:
        readme = f.read()

setup(name="xcat",
      version="0.8",
      author="Tom Forbes",
      license="MIT",
      author_email="tom@tomforb.es",
      package_dir={'xcat': 'xcat'},
      packages=["xcat"],
      install_requires=["aiohttp", "docopt", 'colorama', 'ipgetter'],
      entry_points={
          'console_scripts': [
              'xcat = xcat.run:run'
          ]
      },
      description="A command line tool to automate the exploitation of blind XPath injection vulnerabilities",
      long_description=readme,
      url="https://github.com/orf/xcat",
      classifiers=[
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.2',
          'License :: OSI Approved :: MIT License',
      ])
