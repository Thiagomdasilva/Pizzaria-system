from domain.interfaces.pagamento_interface import (
    PagamentoInterface
)


class CartaoPagamento(PagamentoInterface):

    def pagar(self, valor):

        return {
            "tipo": "Cartão",
            "valor": valor,
            "mensagem": "Pagamento realizado via Cartão"
        }