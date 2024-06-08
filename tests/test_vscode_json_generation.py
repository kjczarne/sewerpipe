import unittest
from rich.console import Console
from sewerpipe.vscode import generate_launch_json
from sewerpipe.task import Task


class TestVSCodeJsonGeneration(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.t1 = Task(name="Example 1",
                      module="sewer.dummy",
                      parameters_and_flags=dict(verbose=True, name="My momma"))
        cls.t2 = Task(name="Example 2",
                      module="sewer.dummy",
                      parameters_and_flags=dict(verbose=False,
                                                name="My momma not"))

    def test_generate_vscode_json(self):
        console = Console()
        launch_json_dict = generate_launch_json(self.t1,
                                               return_or_write='return')
        exp = {
            'version':
            '0.2.0',
            'configurations': [{
                'name': 'Example 1',
                'type': 'python',
                'request': 'launch',
                'module': 'sewer.dummy',
                'args': ['--name', 'My momma', '--verbose'],
                'console': 'integratedTerminal'
            }]
        }
        # console.print(launch_json_dict)
        self.assertDictEqual(launch_json_dict, exp)


if __name__ == "__main__":
    unittest.main()
