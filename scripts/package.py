#!/usr/bin/env python3
"""Create a directly installable addon ZIP, excluding development assets."""
from pathlib import Path
import re
import zipfile

root = Path(__file__).resolve().parents[1]
addon = root / "SPTouchBars"
version = re.search(r"^## Version: ([\d.]+)$", (addon / "SPTouchBars.toc").read_text(), re.M).group(1)
output = root / "dist" / f"Touchbars-{version}.zip"
output.parent.mkdir(exist_ok=True)
with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED) as archive:
    for name in ("SPTouchBars.toc", "SPTouchBars.lua", "SPTouchBars.tga"):
        archive.write(addon / name, f"SPTouchBars/{name}")
    archive.write(root / "LICENSE", "SPTouchBars/LICENSE")
with zipfile.ZipFile(output) as archive:
    assert archive.testzip() is None
    assert set(archive.namelist()) == {f"SPTouchBars/{name}" for name in
        ("SPTouchBars.toc", "SPTouchBars.lua", "SPTouchBars.tga", "LICENSE")}
print(output)
