from bluepy.btle import Peripheral

from .default import DefaultDesk

supported_desks = [
    DefaultDesk
]

def factory(peripheral: Peripheral, device_addr: str):
    for desk_cls in supported_desks:
        desk = desk_cls(peripheral, device_addr)
        if desk.is_supported():
            return desk
    else:
        return None