import { FaEdit, FaTrash } from "react-icons/fa";

function PedidoCard({
    pedido,
    onExcluir,
    onEditar
}) {

    return (

        <div className="card shadow mb-3">

            <div className="card-body">

                <h5 className="card-title">

                    Cliente: {pedido.cliente}

                </h5>

                <p className="card-text">

                    Pizza: {pedido.pizza}

                </p>

                <p className="card-text">

                    Quantidade: {pedido.quantidade}

                </p>

                <button
                    className="btn btn-warning me-2"
                    onClick={() => onEditar(pedido)}
                >
                    <FaEdit /> Editar
                </button>

                <button
                    className="btn btn-danger"
                    onClick={() => onExcluir(pedido.id)}
                >
                    <FaTrash /> Excluir
                </button>

            </div>

        </div>

    );

}

export default PedidoCard;