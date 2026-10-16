# Releases

`pyproject.toml` is the source of truth for the project version. The metadata workflow validates the software metadata.

| Policy | Value |
| --- | --- |
| Current version | `0.1.0` |
| Versioning scheme | SemVer |
| Expected cadence | Single release - no updates |

## Distribution channels

- PyPI
- Zenodo
- GitHub Releases

## Release process

1. Update `project.version` in `pyproject.toml`.
1. Run the metadata, test, documentation, and release checks configured for the project.
1. Create and push a `v<version>` tag. The distribution workflow checks that the tag matches `project.version` before publishing.

Run the release check locally with:

```bash
python tools/check_release.py
python tools/check_release.py --tag v0.1.0
```

## Channel setup

- **PyPI:** configure a trusted publisher for the GitHub `pypi` environment before the first tagged release.
- **GitHub Releases:** tagged releases are created with source and Python distribution artifacts.
- **External channels:** configure publication separately for Zenodo.
