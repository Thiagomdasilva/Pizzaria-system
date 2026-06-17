from services.pagamentos.pix_pagamento import PixPagamento
from services.pagamentos.cartao_pagamento import CartaoPagamento
from services.pagamentos.dinheiro_pagamento import DinheiroPagamento


class PagamentoFactory:

    @staticmethod
    def criar_pagamento(tipo):

        if tipo == "pix":
            return PixPagamento()

        if tipo == "cartao":
            return CartaoPagamento()

        if tipo == "dinheiro":
            return DinheiroPagamento()

        raise Exception("Forma de pagamento inválida")