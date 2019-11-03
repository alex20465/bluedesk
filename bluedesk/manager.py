from time import sleep
from bluepy.btle import Scanner, Peripheral, ADDR_TYPE_RANDOM, DefaultDelegate, ScanEntry, BTLEException

from .config import Config
from .desks import factory, DefaultDesk

class DeskManager:

    MAX_CONNECTION_ATTEMPTS = 5

    def __init__(self):
        self._scanner = Scanner()
        self._peripheral = Peripheral()
        self._desk = None
        self.config = Config()

    def scan_devices(self) -> [ScanEntry]:
        scan_entries = self._scanner.scan()

        return [ entry for entry in scan_entries ]

    def disconnect(self):
        self._peripheral.disconnect()

    def connect(self, device_addr):
        connected = False
        error = None
        for _ in range(self.MAX_CONNECTION_ATTEMPTS):
            try:
                self._peripheral.connect(device_addr, ADDR_TYPE_RANDOM)
            except BTLEException as e:
                print("Connection failed: " + str(e))
                sleep(0.3)
                error = e
                continue
            else:
                connected = True
                break

        if connected is False:
            raise error

        self._desk = factory(self._peripheral, device_addr)

        if self._desk is None:
            raise Exception("Device is not supported")

    @property
    def is_connected(self):
        return self.desk.position is not None if self.desk is not None else False

    @property
    def desk(self) -> DefaultDesk:
        return self._desk