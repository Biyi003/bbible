from setuptools import setup, find_packages

setup(
    name="bbible",
    version="0.2.0",
    author="Biyi Adebayo",
    description="Explore the Bible by verse or by meaning — with multi-version and AI topic search",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Biyi003/bbible",
    project_urls={
        "Documentation": "https://github.com/Biyi003/bbible#readme",
        "Source": "https://github.com/Biyi003/bbible",
        "Bug Tracker": "https://github.com/Biyi003/bbible/issues",
    },
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "bbible": ["data/*.json"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Religion",
    ],
    python_requires=">=3.6",
)
