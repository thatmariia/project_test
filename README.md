# My awesome project

[![CI](https://github.com/thatmariia/project_test/actions/workflows/tests.yml/badge.svg)](https://github.com/thatmariia/project_test/actions/workflows/tests.yml)

[![Documentation](https://img.shields.io/badge/docs-online-blue?labelColor=gray)](https://thatmariia.github.io/project_test/)

[![Usage](https://img.shields.io/badge/usage-guide-blue?labelColor=gray)](https://github.com/thatmariia/project_test/blob/HEAD/docs/usage.md)

[![GitHub release](https://img.shields.io/github/v/release/thatmariia/project_test)](https://github.com/thatmariia/project_test/releases/latest)

[![PyPI](https://img.shields.io/pypi/v/project-test)](https://pypi.org/project/project-test/)

[![License](https://img.shields.io/badge/license-view-blue?labelColor=gray)](https://github.com/thatmariia/project_test/blob/HEAD/LICENSE)

![Tool Type](https://img.shields.io/badge/tool%20type-Command--line%20tool%20%7C%20Library%20%7C%20Script-blue?labelColor=gray)

This is a description of my project

## Purpose Categories

- Data collection & instrumentation
- Data analysis
- Visualization & dissemination

## Research Topics

- [Data visualisation](http://edamontology.org/topic_0092)

## Intended Audience

- Researchers (academia)
- Data stewards / data managers
- Software developers / RSEs

## Installation

Install the published package from PyPI:

```bash
poetry add project-test
```

## Usage

```bash
poetry run python -m project_test
```

## Functions

<details>
<summary>Visualisation, Validation</summary>

```yaml
# biotools-function
operation:
- term: "Visualisation"
  uri: http://edamontology.org/operation_0337
- term: "Validation"
  uri: http://edamontology.org/operation_2428
input:
- data:
    term: "JSON"
    uri: http://edamontology.org/format_3464
```

</details>

## Documentation

Read the [project documentation](https://thatmariia.github.io/project_test/).

- User guide: installation, configuration, usage, and examples
- Deployment notes: environment setup and operational assumptions
- Developer guide: development, tests, contribution, and reference

## Access

**Access type:** free.

## Platform support

- Platform independent

## Related Software

- [matplotlib](https://matplotlib.org) - relationship

## Development

Set up the development environment with:

```bash
poetry install --all-extras
```
Run the configured checks:

```bash
poetry run ruff format --check .
poetry run ruff check .
poetry run mypy src
poetry run python -m pytest
```
See [`CONTRIBUTING.md`](CONTRIBUTING.md) for the contribution and code-review policy.

## Citation

If you use this software, cite it using [`CITATION.cff`](CITATION.cff).

## Legal and Licensing

This project is licensed under `https://spdx.org/licenses/Apache-2.0.html`. See `LICENSE` for the full license text.

<!-- rs-files-templates:README:end -->
<!-- Add project-specific README content below this line; it is preserved when the generated README is refreshed. -->
