from setuptools import setup, find_packages
setup(
    name="venezuela-economic-impact-database-2024-2025",
    version="1.0.0",
    description="Venezuela Economic Impact Database 2024-2025: Key Indicators and Influencing Factors. DOI: 10.17632/",
    author="de la Serna, Juan Moisés",
    url="https://github.com/juanmoisesd/venezuela-economic-impact-database-2024-2025",
    packages=find_packages(),
    install_requires=["pandas>=1.3.0","requests>=2.26.0"],
    python_requires=">=3.7",
    classifiers=["Programming Language :: Python :: 3","License :: OSI Approved :: MIT License","Topic :: Scientific/Engineering"],
    keywords="zenodo, open-data",
)