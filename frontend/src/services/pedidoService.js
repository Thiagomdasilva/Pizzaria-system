import axios from "axios";

const API = "http://localhost:8000";

export async function listarPedidos() {

    const resposta = await axios.get(`${API}/pedido`);

    return resposta.data;

}

export async function criarPedido(pedido) {

    const resposta = await axios.post(
        `${API}/pedido`,
        pedido
    );

    return resposta.data;

}

export async function atualizarPedido(id, pedido) {

    const resposta = await axios.put(
        `${API}/pedido/${id}`,
        pedido
    );

    return resposta.data;

}

export async function deletarPedido(id) {

    const resposta = await axios.delete(
        `${API}/pedido/${id}`
    );

    return resposta.data;

}