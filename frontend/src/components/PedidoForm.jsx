import { useState } from "react";

import { criarPedido } from "../services/pedidoService";

function PedidoForm({ atualizarLista }) {

    const [cliente, setCliente] = useState("");

    const [pizza, setPizza] = useState("");

    const [quantidade, setQuantidade] = useState("");

    async function salvar(event) {

        event.preventDefault();

        await criarPedido({
            cliente,
            pizza,
            quantidade: Number(quantidade)
        });

        setCliente("");

        setPizza("");

        setQuantidade("");

        atualizarLista();

    }

    return (

        <div className="container mt-4">

            <h2>Novo Pedido</h2>

            <form onSubmit={salvar}>

                <input
                    className="form-control mb-3"
                    placeholder="Cliente"
                    value={cliente}
                    onChange={(e) =>
                        setCliente(e.target.value)
                    }
                />

                <input
                    className="form-control mb-3"
                    placeholder="Pizza"
                    value={pizza}
                    onChange={(e) =>
                        setPizza(e.target.value)
                    }
                />

                <input
                    className="form-control mb-3"
                    placeholder="Quantidade"
                    value={quantidade}
                    onChange={(e) =>
                        setQuantidade(e.target.value)
                    }
                />

                <button className="btn btn-success">

                    Salvar Pedido

                </button>

            </form>

        </div>

    );

}

export default PedidoForm;