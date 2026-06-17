function BuscaPedido({ busca, setBusca }) {

    return (

        <div className="mt-4">

            <input
                className="form-control"
                placeholder="Pesquisar cliente ou pizza"
                value={busca}
                onChange={(e) =>
                    setBusca(e.target.value)
                }
            />

        </div>

    );

}

export default BuscaPedido;