import { useEffect, useState } from "react";

import Dashboard from "../components/Dashboard";
import BuscaPedido from "../components/BuscaPedido";
import PedidoForm from "../components/PedidoForm";
import PedidoList from "../components/PedidoList";

import { listarPedidos } from "../services/pedidoService";

function Home() {

    const [pedidos, setPedidos] = useState([]);
    const [busca, setBusca] = useState("");

    async function atualizarLista() {

        const dados = await listarPedidos();

        setPedidos(dados);

    }

    useEffect(() => {

        atualizarLista();

    }, []);

    const pedidosFiltrados = pedidos.filter(

        pedido =>

            pedido.cliente
                .toLowerCase()
                .includes(busca.toLowerCase())

            ||

            pedido.pizza
                .toLowerCase()
                .includes(busca.toLowerCase())

    );

    return (

        <div className="container">

            <Dashboard pedidos={pedidos} />

            <BuscaPedido
                busca={busca}
                setBusca={setBusca}
            />

            <PedidoForm atualizarLista={atualizarLista} />

            <PedidoList
                pedidos={pedidosFiltrados}
                atualizarLista={atualizarLista}
            />

        </div>

    );

}

export default Home;