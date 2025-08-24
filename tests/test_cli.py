import subprocess


def test_help_flag():
    """Test that the --help flag works correctly."""
    result = subprocess.run(["reddit-export", "--help"], capture_output=True, text=True)

    assert result.returncode == 0
    assert "usage:" in result.stdout.lower() or "reddit-export" in result.stdout.lower()
    assert len(result.stdout) > 0
