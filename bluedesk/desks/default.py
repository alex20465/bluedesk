import struct
from time import sleep
from bluepy.btle import Scanner, Peripheral, ADDR_TYPE_RANDOM, DefaultDelegate

class DefaultDesk:

    MAX_POSITION = 6500

    SECURE_STOP_POSITION = 100

    def __init__(self, peripheral: Peripheral, addr: str):
        self._addr = addr
        self._peripheral = peripheral

    def up(self):
        current_position = self.position

        if current_position > (self.MAX_POSITION - self.SECURE_STOP_POSITION):
            return # secure stop

        while current_position == self.position:
            self.__up()
            sleep(0.3)

    def __up(self):
        self._peripheral.writeCharacteristic(0x0010, bytes.fromhex("4700"))

    def down(self):
        current_position = self.position

        if current_position < self.SECURE_STOP_POSITION:
            return # secure stop

        while current_position == self.position:
            self.__down()
            sleep(0.3)

    def __down(self):
        self._peripheral.writeCharacteristic(0x0010, bytes.fromhex("4600"))

    def move_to(self, percentage):
        current_percentage = self.position_percentage
        if percentage < current_percentage:
            while percentage < self.position_percentage:
                self.__down()
                sleep(0.1)
        elif percentage > current_percentage:
            while percentage > self.position_percentage:
                self.__up()
                sleep(0.1)
        else:
            pass
    
    def is_supported(self):
        if self.has_service_characteristic(
            "99fa0020-338a-1024-8a49-009c0215f78a", 26) is False:
            return False

        if self._addr[0:8] != "e4:d1:a7":
            return False

        return True

    def has_service_characteristic(self, service_uuid, handle):
        service = self._peripheral.getServiceByUUID(service_uuid)
        handlers = [ char.getHandle() for char in  service.getCharacteristics() ]

        if handle in handlers:
            return True
        else:
            return False

    @property
    def position(self):
        data = self._peripheral.readCharacteristic(26)
        return struct.unpack('<H', data[0:2])[0]

    @property
    def position_percentage(self):
        return self.position / (self.MAX_POSITION / 100)
