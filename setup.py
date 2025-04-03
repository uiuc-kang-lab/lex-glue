from setuptools import setup, find_packages

setup(
    name="lex-glue",
    version="0.1.0",
    packages=find_packages(include=["models", "utils", "scripts", "statistics"]),
    install_requires=[
        "torch>=1.9.0",
        "transformers[torch]>=4.9.0",
        "scikit-learn>=0.24.1",
        "tqdm>=4.61.1",
        "numpy>=1.20.1",
        "datasets>=1.18.1",
        "nltk>=3.5",
        "scipy>=1.6.3",
    ],
    python_requires=">=3.10",
    author="UIUC Kang Lab",
    author_email="kanglab@illinois.edu",
    description="A package for lexical glue tasks",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/uiuc-kang-lab/lex-glue",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    keywords="nlp, machine-learning, transformers",
    license="MIT",
) 