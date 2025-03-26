import './App.css';
import axios from 'axios';
import React from 'react';

class App extends React.Component {
    state = {
    details: [],
    isConnected: false,
    }

    componentDidMount(){
        let data;
        axios.get('http://localhost:8000/services/usuarios/')
        .then(res => {
            data = res.data;
            this.setState({
                details:data,
                isConnected:true,//se a conexão estiver OK
                });
            })
        .catch(err => {
            console.error(err);
            this.setState({
                isConnected:false,
                });
            });
        }

    render(){
        return(
            <div>
                <header>Dados dos usuários:</header>
                <hr></hr>
                {/* Exibe a mensagem se a conexão for bem-sucedida */}

                {this.state.isConnected && (
          <div>
              <p>CONEXAO BEM SUCEDIDA</p>
          </div>
        )}

        {/* Exibe os dados se a conexão for bem-sucedida */}
        {this.state.isConnected && this.state.details.length > 0 ? (
          this.state.details.map((output, id) => (
            <div key={id}>
              <h2>{output.name}</h2>
              <h2>{output.cpf}</h2>
            </div>
          ))
        ) : (
          <p>Falha na conexão ou não há dados para exibir.</p>
        )}
      </div>
    );
  }
}

export default App;