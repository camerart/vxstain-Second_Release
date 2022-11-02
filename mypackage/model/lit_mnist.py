# lit_mnist.py ---
#
# Filename: lit_mnist.py
# Author: Fred Qi
# Created: 2022-02-11 16:51:25(+0800)
#
# Last-Updated: 2022-02-12 17:00:05(+0800) [by Fred Qi]
#     Update #: 57
# 

# Commentary:
#
#
# 

# Change Log:
#
#
#
from torch.nn import functional as F
from torch import nn
from pytorch_lightning.core.lightning import LightningModule
from pytorch_lightning.utilities.cli import MODEL_REGISTRY

       
@MODEL_REGISTRY
class LitMNIST(LightningModule):
    def __init__(self):
        super().__init__()
        self.layer_1 = nn.Linear(28 * 28, 128)
        self.layer_2 = nn.Linear(128, 256)
        self.layer_3 = nn.Linear(256, 10)

    def forward(self, x):
        batch_size, channels, height, width = x.size()
        x = x.view(batch_size, -1)
        x = self.layer_1(x)
        x = F.relu(x)
        x = self.layer_2(x)
        x = F.relu(x)
        x = self.layer_3(x)
        x = F.log_softmax(x, dim=1)
        return x

    def training_step(self, batch, batch_idx):
        x, y = batch
        logits = self(x)
        loss = F.nll_loss(logits, y)
        self.log("loss", loss)
        return loss

# 
# lit_mnist.py ends here
