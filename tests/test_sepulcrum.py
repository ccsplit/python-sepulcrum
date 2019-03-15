from click.testing import CliRunner

from .context import sepulcrum


def test_main():
    runner = CliRunner()
    result = runner.invoke(sepulcrum.cli.main, [])

    assert result.output == "()\n"
    assert result.exit_code == 0
