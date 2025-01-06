from pathlib import Path
from copier import Worker

def mkvars():
    with Worker(
        src_path="./mkvars/template",
        dst_path=Path("./inventory"),
        unsafe=True,
        skip_if_exists=["**/playbooks/main.yml", "**/README.md"]
    ) as worker:
        worker.run_copy()
