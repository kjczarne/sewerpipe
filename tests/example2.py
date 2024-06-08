from sewerpipe.config import Config, Task
from sewerpipe.workflows import workflow

t1 = Task(
    name="Data Generation",
    module="uarr.generation",
    parameters_and_flags=dict(
        config="configs/0_gen/gen_chi_squared.toml"
    )
)

t2 = Task(
    name="Data Noising",
    module="uarr.noising",
    parameters_and_flags=dict(
        config="configs/0_noising/noising_cfg_synth.toml"
    )
)


@workflow
def generate_data_workflow():
    (t1 >> t2).run()


def main():
    generate_data_workflow()


if __name__ == "__main__":
    main()
