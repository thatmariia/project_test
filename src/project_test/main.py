"""Runtime entry point for ``python -m project_test``.

This module provides a tiny package-level command for quick smoke tests. Keep
larger runtime interfaces in dedicated modules.
"""

from project_test.services.processing import process_text


def main(text: str = "My awesome project") -> None:
    """Run the package entry point.

    Parameters
    ----------
    text : str, default="My awesome project"
        Text to process.
    """
    # Delegate to the service layer so the entry point stays small and
    # testable.
    result = process_text(text)
    print(result.output_text)


if __name__ == "__main__":
    main()
