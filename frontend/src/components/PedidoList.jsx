import { useState } from "react";

import PedidoCard from "./PedidoCard";
import EditarPedidoModal from "./EditarPedidoModal";

import {
    deletarPedido,
    atualizarPedido
} from "../services/pedidoService";

function PedidoList({
    pedidos,
    atualizarLista
}) {

    const [pedidoSelecionado, setPedidoSelecionado] = useState(null);

    async function removerPedido(id) {

        await deletarPedido(id);

        atualizarLista();

    }

    async function salvarEdicao(dados) {

        await atualizarPedido(
            pedidoSelecionado.id,
            dados
        );

        setPedidoSelecionado(null);

        atualizarLista();

    }

    return (

        <div className="container mt-4">

            <h2 className="mb-3">

                Pedidos

            </h2>

            {

                pedidos.map(

                    pedido => (

                        <PedidoCard
                            key={pedido.id}
                            pedido={pedido}
                            onExcluir={removerPedido}
                            onEditar={setPedidoSelecionado}
                        />

                    )

                )

            }

            <EditarPedidoModal
                pedidoSelecionado={pedidoSelecionado}
                salvarEdicao={salvarEdicao}
                fecharModal={() =>
                    setPedidoSelecionado(null)
                }
            />

        </div>

    );

}

export default PedidoList;