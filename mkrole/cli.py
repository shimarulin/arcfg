from pathlib import Path
from copier import Worker

def mkrole():
    with Worker(
        src_path="./mkrole/template",
        dst_path=Path("./collections/ansible_collections"),
        unsafe=True,
        skip_if_exists=["**/playbooks/main.yml", "**/README.md"]
    ) as worker:
        worker.run_copy()
