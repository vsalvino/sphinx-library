from setuptools import setup

with open("README.rst", encoding="utf8") as readme_file:
    readme = readme_file.read()

setup(
    name="sphinx-library",
    version="1.1.1",
    description="Typography-centric Sphinx theme that reads like a good book.",
    long_description=readme,
    long_description_content_type="text/x-rst",
    author="Vince Salvino",
    author_email="salvino@coderedcorp.com",
    url="https://vsalvino.github.io/sphinx-library/",
    license="MIT",
    packages=["sphinx_library"],
    include_package_data=True,
    entry_points={"sphinx.html_themes": ["library=sphinx_library"]},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Sphinx",
        "Framework :: Sphinx :: Theme",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Documentation",
        "Topic :: Software Development :: Documentation",
    ],
)
