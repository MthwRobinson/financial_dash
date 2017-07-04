from setuptools import setup, find_packages
# To upload to PyPi run python setup.py sdist upload -r pypi
setup(
    name='financial_dash',
    version='0.0.1',
    author='Matt Robinson',
    author_email='mthw.wm.robinson@gmail.com',
    packages=find_packages(),
    scripts=[],
    license='LICENSE.txt',
    install_requires=[
        "dash==0.17.7",
        "dash-renderer==0.7.3",
        "dash-html-components==0.6.2",
        "dash-core-components==0.5.1",
        "plotly==2.0.11",
        "pandas",
        "quandl"
    ]
)
