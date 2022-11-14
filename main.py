from meters import AverageValueMeter
from meters import MeterInterface, Storage

meters = MeterInterface(default_focus="tra")
with meters.focus_on("test"):
    meters.register_meter("loss", AverageValueMeter())
with meters.focus_on("test"):
    meters["loss"].add(2)
    meters["loss"].add(4)

print(list(meters.statistics()))

storage = Storage("123")
storage.add_from_meter_interface(epoch=1, tra=dict(meters.statistics()))
