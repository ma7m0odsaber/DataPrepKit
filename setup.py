from setuptools import setup, find_packages

Description = """The DataPrepKit package is a comprehensive toolkit for preprocessing datasets in Python.
It simplifies and streamlines common data preparation tasks, providing efficient functions for
reading data from various file formats, generating data summaries, handling missing values,
and encoding categorical variables.

Key Features:

1. Data Reading: Read data effortlessly from CSV, Excel, and JSON files using Pandas,
                 facilitating seamless integration with diverse datasets.

2. Data Summary: Obtain key statistical summaries of the dataset,including average values and
                 the most frequent values. Gain quick insights into the central tendencies and
                 prevalent categories within the data.

3. Handling Missing Values: Robust functions for handling missing values, offering flexibility with
                            strategies such as removal or imputation based on mean or median.

4. Categorical Data Encoding: Efficiently encode categorical variables into numerical representations
                              using Pandas' get_dummies function. Simplify the process of preparing data for machine learning models.

5. Package Deployment: The DataPrepKit package is easily accessible through PyPI,
                       allowing the broader Python community to integrate these powerful data preprocessing
                       tools seamlessly into their projects."""

# Setting up
setup(
    name="DataPrepKit",
    version='0.1',
    author="Mahmoud Saber(ma7m0od_saber)",
    author_email="<rodomahmoud121@gmail.com>",
    description=Description,
    packages=find_packages(),
    install_requires=['pandas', 'numpy'],
    keywords=['python', 'Data Reading', 'Data Summary',
              'Handling Missing Values', 'Categorical Data Encoding',],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)