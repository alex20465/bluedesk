
from .default import DefaultCommandHandler
from ..desks import DefaultDesk

def factory(desk: DefaultDesk):
    if isinstance(desk, DefaultDesk):
        return DefaultCommandHandler(desk)
    else:
        raise Exception("No command handler for desk instance: ", type(desk))