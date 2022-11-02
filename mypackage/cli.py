import flash.image
from pytorch_lightning.core.lightning import LightningModule
from pytorch_lightning.core.datamodule import LightningDataModule
from pytorch_lightning.utilities.cli import LightningCLI
from pytorch_lightning.utilities.cli import MODEL_REGISTRY, DATAMODULE_REGISTRY


def main():
    MODEL_REGISTRY.register_classes(flash.image, LightningModule)
    DATAMODULE_REGISTRY.register_classes(flash.image, LightningDataModule)
    cli = LightningCLI()
