from InventarioStub import InventarioStub
from UsuarioDummy import UsuarioDummy
from RepositorioFake import RepositorioFake
from EmailDummy import EmailDummy
from unittest.mock import Mock
from InventarioSpy import InventarioSpy

class TicketService:

    def __init__(self, inventario, repositorio, email_service):
        self.inventario = inventario
        self.repositorio = repositorio
        self.email_service = email_service

    def comprar(self, usuario, cantidad):

        disponibles = self.inventario.consultar_disponibilidad()

        if disponibles < cantidad:
            return False

        self.repositorio.guardar(usuario, cantidad)

        self.email_service.enviar_confirmacion(usuario)

        return True

email_mock = Mock()

inventario_spy = InventarioSpy()

service = TicketService(
    #InventarioStub(),
    inventario_spy,
    #UsuarioDummy(),
    RepositorioFake(),
    #EmailDummy()
    email_mock
)

resultado = service.comprar(UsuarioDummy(), 2)

email_mock.enviar_confirmacion.assert_called_once()

print(resultado)

service.comprar(UsuarioDummy(),1)

print(inventario_spy.veces_consultado)