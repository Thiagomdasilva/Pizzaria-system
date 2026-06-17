function Dashboard({ pedidos }) {

    const totalPedidos = pedidos.length;

    const totalPizzas = pedidos.reduce(
        (total, pedido) => total + pedido.quantidade,
        0
    );

    return (

        <div className="row mt-4">

            <div className="col-md-6">

                <div className="card bg-primary text-white">

                    <div className="card-body">

                        <h3>{totalPedidos}</h3>

                        <p>Total de pedidos</p>

                    </div>

                </div>

            </div>

            <div className="col-md-6">

                <div className="card bg-success text-white">

                    <div className="card-body">

                        <h3>{totalPizzas}</h3>

                        <p>Pizzas vendidas</p>

                    </div>

                </div>

            </div>

        </div>

    );

}

export default Dashboard;