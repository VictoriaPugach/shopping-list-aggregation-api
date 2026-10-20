from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def test_cli_reports_unimplemented_aggregation():
    result = subprocess.run(
        [sys.executable, "-m", "src.main", "data/aggregate-request.json"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 1
    assert result.stdout == ""
    assert "Shopping-list aggregation is not implemented" in result.stderr


def test_cli_rejects_missing_file():
    result = subprocess.run(
        [sys.executable, "-m", "src.main", "missing.json"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 1
    assert "Error:" in result.stderr
