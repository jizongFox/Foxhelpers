import torch

from foxhelpers.foxMetrics import AverageValueMeter
from foxhelpers.foxMetrics import MeterInterface, Storage

mdf = AverageValueMeter()
mdf.add(1)

meters = MeterInterface(default_focus="tra")
with meters.focus_on("test"):
    meters.register_meter("loss", AverageValueMeter())
with meters.focus_on("test"):
    cur_meter: AverageValueMeter = meters["loss"]
    meters["loss"].add()
    meters["loss"].add(torch.tensor(4))

print(list(meters.statistics()))

storage = Storage("123")
storage.add_from_meter_interface(epoch=1, tra=dict(meters.statistics()))
