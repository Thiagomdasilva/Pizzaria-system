from domain.interfaces.pagamento_interface import PagamentoInterface


class PixPagamento(PagamentoInterface):

    def pagar(self, valor):

        return {
            "tipo": "Pix",
            "valor": valor,
            "mensagem": "Pagamento realizado via Pix"
        }