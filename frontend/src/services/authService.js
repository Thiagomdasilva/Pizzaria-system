import axios from "axios";

const API = "http://localhost:8000";

export async function login(usuario, senha) {

    const resposta = await axios.post(
        `${API}/login`,
        {
            usuario,
            senha
        }
    );

    return resposta.data;

}