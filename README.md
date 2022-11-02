# repo-template

A repository template for reproducible research projects.

## Layouts

- `mypackage`: Codes.
    - `model`: Models to be explored.
	- `dataloader`: Data loading modules.
- `exps`: Reproducible experiment configurations.
- `data`: Put data used in this project in this folder, but do NOT commit very large data files. Using Git LFS instead if data are permitted to upload onto servers outside of the campus.
- `docs`: Documentation for this project.
- `tests`: Tests for this project.

## Usage

### Environment

To create the deep learning development environment, please run the following command:
``` bash
conda env create -f environment.yaml
conda activate mypackage
```

### CLI

When creating the conda environment, `pip install -e .` has been executed. So it is ready to run the command line interface (CLI) as:

``` bash
mypackage fit --config exps/config.yaml
```
where `exps/config.yaml` is the configuration file.

### Reproducible experiments

The logs are written to `<config.yaml>.default_root_dir/lightning_logs` with a structure as following:

``` bash
/home/data/lightning_logs/
└── version_0
    ├── checkpoints
    │   └── epoch=5-step=5159.ckpt
    ├── config.yaml
    ├── events.out.tfevents.1644656526.nuchvk.182081.0
    └── hparams.yaml

2 directories, 4 files
```
The `config.yaml` is saved for reproducible results.

To write a new configuration file, one can execute the following command:
``` bash
mypackage fit --print_config=comments > exps/verbose-config.yaml
```
to create a template with documentations.

To use the `tqdm` style progress bar, set `enable_progress_bar: true` in `config.yaml`.

### Customizing model and data loader

It is easy to use customized models and data loaders, Just specify the `class_path` of the customized model and data loader with proper `init_args` in `config.yaml`.

```yaml
data:
  class_path: mypackage.dataloader.MNISTDataModule
  init_args:
    batch_size: 64

model:
  class_path: mypackage.model.LitMNIST
  init_args: {}
```

## References

- [PyTorch tutorial](https://pytorch.org/tutorials/)
- [PyTorch lightning](https://pytorch-lightning.readthedocs.io/en/stable/index.html)
- [LightningCLI](https://pytorch-lightning.readthedocs.io/en/stable/common/lightning_cli.html)
