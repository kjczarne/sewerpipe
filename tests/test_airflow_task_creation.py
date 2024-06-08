import unittest
from airflow.decorators.python import _PythonDecoratedOperator
from sewerpipe.config import Task
from sewerpipe.airflow import create_airflow_task, create_airflow_tasks


class TestAirflowTaskCreation(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.t1 = Task(name="sameid",
                      module="sewer.dummy",
                      parameters_and_flags=dict(verbose=True, name="My momma"))
        cls.t2 = Task(name="sameid",
                      module="sewer.dummy",
                      parameters_and_flags=dict(verbose=False,
                                                name="My momma not"))


    def test_one_airflow_task(self):
        task = create_airflow_task(self.t1)
        self.assertDictEqual(task.kwargs, {'task_id': 'sameid'},
                             "`kwargs` is not equal to `{'task_id': 'sameid'}`")


    def test_two_airflow_tasks(self):
        tasks = create_airflow_tasks([self.t1, self.t2])
        for task in tasks:
            self.assertDictEqual(task.kwargs, {'task_id': 'sameid'}),


if __name__ == "__main__":
    unittest.main()
