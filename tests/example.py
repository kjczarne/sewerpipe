from sewerpipe.task import Task
from sewerpipe.workflows import workflow

t1 = Task(
    name="Example 1",
    module="sewerpipe.dummy",
    parameters_and_flags=dict(
        verbose=True,
        name="My momma"
    )
)

t2 = Task(
    name="Example 2",
    module="sewerpipe.dummy",
    parameters_and_flags=dict(
        verbose=False,
        name="My momma not"
    )
)


@workflow
def workflow():
    (t1 >> t2).run()


def main():
    workflow()


if __name__ == "__main__":
    main()
