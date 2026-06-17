from tests.fakes.fake_pedido_repository import (
    FakePedidoRepository
)

from use_cases.criar_pedido import CriarPedido

from use_cases.listar_pedidos import ListarPedidos

from use_cases.buscar_pedido import BuscarPedido

from use_cases.atualizar_pedido import AtualizarPedido

from use_cases.deletar_pedido import DeletarPedido


def test_criar_pedido():

    repository = FakePedidoRepository()

    use_case = CriarPedido(repository)

    resultado = use_case.executar(
        "Thiago Marinho",
        "Calabresa",
        2
    )

    assert resultado.cliente == "Thiago Marinho"

    assert resultado.pizza == "Calabresa"

    assert resultado.quantidade == 2


def test_listar_pedidos():

    repository = FakePedidoRepository()

    CriarPedido(repository).executar(
        "Thiago",
        "Portuguesa",
        1
    )

    pedidos = ListarPedidos(repository).executar()

    assert len(pedidos) == 1


def test_buscar_pedido():

    repository = FakePedidoRepository()

    pedido = CriarPedido(repository).executar(
        "Thiago",
        "Frango",
        3
    )

    resultado = BuscarPedido(repository).executar(
        pedido.id
    )

    assert resultado.id == pedido.id


def test_atualizar_pedido():

    repository = FakePedidoRepository()

    pedido = CriarPedido(repository).executar(
        "Thiago",
        "Calabresa",
        2
    )

    resultado = AtualizarPedido(repository).executar(
        pedido.id,
        "Thiago",
        "Portuguesa",
        4
    )

    assert resultado.pizza == "Portuguesa"

    assert resultado.quantidade == 4


def test_deletar_pedido():

    repository = FakePedidoRepository()

    pedido = CriarPedido(repository).executar(
        "Thiago",
        "Frango",
        1
    )

    DeletarPedido(repository).executar(
        pedido.id
    )

    pedidos = ListarPedidos(repository).executar()

    assert len(pedidos) == 0