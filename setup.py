from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in alfain/__init__.py
from alfain import __version__ as version

setup(
	name="alfain",
	version=version,
	description="document review management",
	author="alfain",
	author_email="admin@alfain.co",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
