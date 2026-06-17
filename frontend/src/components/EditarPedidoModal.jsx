import { useState, useEffect } from "react";

function EditarPedidoModal({
    pedidoSelecionado,
    salvarEdicao,
    fecharModal
}) {

    const [cliente, setCliente] = useState("");
    const [pizza, setPizza] = useState("");
    const [quantidade, setQuantidade] = useState("");

    useEffect(() => {

        if (pedidoSelecionado) {

            setCliente(pedidoSelecionado.cliente);
            setPizza(pedidoSelecionado.pizza);
            setQuantidade(pedidoSelecionado.quantidade);

        }

    }, [pedidoSelecionado]);

    function enviar(event) {

        event.preventDefault();

        salvarEdicao({
            cliente,
            pizza,
            quantidade
        });

    }

    if (!pedidoSelecionado) {

        return null;

    }

    return (

        <div className="card shadow mt-4">

            <div className="card-body">

                <h3>Editar Pedido</h3>

                <form onSubmit={enviar}>

                    <input
                        className="form-control mb-3"
                        value={cliente}
                        onChange={(e) =>
                            setCliente(e.target.value)
                        }
                    />

                    <input
                        className="form-control mb-3"
                        value={pizza}
                        onChange={(e) =>
                            setPizza(e.target.value)
                        }
                    />

                    <input
                        className="form-control mb-3"
                        value={quantidade}
                        onChange={(e) =>
                            setQuantidade(e.target.value)
                        }
                    />

                    <button className="btn btn-success me-2">
                        Salvar
                    </button>

                    <button
                        type="button"
                        className="btn btn-secondary"
                        onClick={fecharModal}
                    >
                        Cancelar
                    </button>

                </form>

            </div>

        </div>

    );

}

export default EditarPedidoModal;