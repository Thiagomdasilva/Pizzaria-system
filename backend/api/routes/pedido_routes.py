from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import status

from factories.repository_factory import RepositoryFactory

from schemas.pedido_request import PedidoRequest
from schemas.pedido_response import PedidoResponse

from use_cases.criar_pedido import CriarPedido
from use_cases.listar_pedidos import ListarPedidos
from use_cases.buscar_pedido import BuscarPedido
from use_cases.atualizar_pedido import AtualizarPedido
from use_cases.deletar_pedido import DeletarPedido


router = APIRouter()

repository = RepositoryFactory.criar_repository()


# Criar pedido
@router.post(
    "/pedido",
    response_model=PedidoResponse,
    status_code=status.HTTP_201_CREATED
)
def criar_pedido(
        pedido: PedidoRequest):

    novo_pedido = CriarPedido(repository).executar(
        pedido.cliente,
        pedido.pizza,
        pedido.quantidade
    )

    return novo_pedido


# Listar todos os pedidos
@router.get(
    "/pedido",
    response_model=list[PedidoResponse]
)
def listar_pedidos():

    pedidos = ListarPedidos(repository).executar()

    return pedidos


# Buscar pedido por ID
@router.get(
    "/pedido/{id}",
    response_model=PedidoResponse
)
def buscar_pedido(id: int):

    pedido = BuscarPedido(repository).executar(id)

    if pedido is None:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Pedido não encontrado"
        )

    return pedido


# Atualizar pedido
@router.put(
    "/pedido/{id}",
    response_model=PedidoResponse
)
def atualizar_pedido(
        id: int,
        pedido: PedidoRequest):

    pedido_atualizado = AtualizarPedido(repository).executar(
        id,
        pedido.cliente,
        pedido.pizza,
        pedido.quantidade
    )

    if pedido_atualizado is None:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Pedido não encontrado"
        )

    return pedido_atualizado


# Excluir pedido
@router.delete(
    "/pedido/{id}",
    status_code=status.HTTP_200_OK
)
def deletar_pedido(id: int):

    pedido = DeletarPedido(repository).executar(id)

    if pedido is None:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Pedido não encontrado"
        )

    return {
        "mensagem": "Pedido removido com sucesso"
    }