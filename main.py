"""estimator_97a791 - File system operations."""
from pathlib import Path
import json, tempfile
WORKSPACE = "estimator_97a791"
def scan_directory(root: Path) -> dict:
    files = list(root.rglob("*"))
    return {"root": str(root), "total": len(files), "dirs": sum(1 for f in files if f.is_dir()), "files": sum(1 for f in files if f.is_file())}
def create_workspace(base: Path) -> Path:
    ws = base / WORKSPACE
    ws.mkdir(parents=True, exist_ok=True)
    (ws / "config.json").write_text(json.dumps({"workspace": WORKSPACE, "version": "1.0"}))
    return ws
def main():
    with tempfile.TemporaryDirectory() as tmp:
        ws = create_workspace(Path(tmp))
        print(f"[{WORKSPACE}] Created workspace: {ws}")
        stats = scan_directory(Path(tmp))
        print(f"[{WORKSPACE}] Stats: {json.dumps(stats, indent=2)}")
if __name__ == "__main__":
    main()
