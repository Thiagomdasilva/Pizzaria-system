from domain.interfaces.pagamento_interface import (
    PagamentoInterface
)


class DinheiroPagamento(PagamentoInterface):

    def pagar(self, valor):

        return {
            "tipo": "Dinheiro",
            "valor": valor,
            "mensagem": "Pagamento realizado em Dinheiro"
        }