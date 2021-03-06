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

An example of how to use the script is provided in the examples folder. For additional details of theory, implementation and use, please see the reference below.

## Support

Please [open an issue](https://github.com/bjorntsv/tempmom/issues/new) for support.

## Contributing

Please contribute using [Github Flow](https://guides.github.com/introduction/flow/).
Create a branch, add commits, and
[open a pull request](https://github.com/bjorntsv/tempmom/compare/).

## References
[1] Bjørn T. Svendsen, Gunnstein T. Frøseth, Anders Rönnquist, "Damage Detection Applied to a Full-Scale Steel Bridge Using Temporal Moments", Shock and Vibration, vol. 2020, Article ID 3083752, 16 pages, 2020. https://doi.org/10.1155/2020/3083752