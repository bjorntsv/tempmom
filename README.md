# Temporal Moments

Implementation of temporal moments in Python.
Temporal moments statistically characterizes transient dynamic signals and describe how the energy of a signal is distributed over time.

[![DOI](https://zenodo.org/badge/233225416.svg)](https://zenodo.org/badge/latestdoi/233225416)

## Installation
These scripts can be used directly, or downloaded as a Python package. Utilizing this as a Python package can be done by downloading
the repository and install, e.g. by **pip**

```
pip install .
```
or directly from [anaconda cloud](https://anaconda.org/bjorntsv/tempmom)

```sh
conda install -c bjorntsv tempmom
```

## Content
The package provides the algorithms for establishing the temporal moments of time series. All moments of order 2 and higher are calculated
about the central time, *T*.

An example of how to use the script is provided in the examples folder.

## Support

Please [open an issue](https://github.com/bjorntsv/tempmom/issues/new) for support.

## Contributing

Please contribute using [Github Flow](https://guides.github.com/introduction/flow/).
Create a branch, add commits, and
[open a pull request](https://github.com/bjorntsv/tempmom/compare/).
