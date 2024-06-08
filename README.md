# Sewer


```python
from sewer.config import Task
from sewer.workflows import workflow

t1 = Task(
    name="Example 1",
    module="sewer.dummy",
    parameters_and_flags=dict(
        verbose=True,
        name="My momma"
    )
)

t2 = Task(
    name="Example 2",
    module="sewer.dummy",
    parameters_and_flags=dict(
        verbose=False,
        name="My momma not"
    )
)


@workflow
def generate_data_workflow():
    (t1 >> t2).run()


def main():
    generate_data_workflow()


if __name__ == "__main__":
    main()
```