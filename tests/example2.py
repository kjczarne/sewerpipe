from pathlib import Path
from sewerpipe.workflows import workflow
from sewerpipe.utils import load_module
from sewerpipe.task import get_task_from_module

module = load_module(Path("tests/example.py"))
t1 = get_task_from_module(module, "Example 1")
t2 = get_task_from_module(module, "Example 2")


@workflow
def generate_data_workflow():
    (t1 >> t2).run()


def main():
    generate_data_workflow()


if __name__ == "__main__":
    main()
