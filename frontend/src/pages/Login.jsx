function Login() {

    return (

        <div className="container mt-5">

            <div className="card shadow">

                <div className="card-body">

                    <h2>Login</h2>

                    <input
                        className="form-control mb-3"
                        placeholder="Usuário"
                    />

                    <input
                        className="form-control mb-3"
                        type="password"
                        placeholder="Senha"
                    />

                    <button className="btn btn-primary">

                        Entrar

                    </button>

                </div>

            </div>

        </div>

    );

}

export default Login;