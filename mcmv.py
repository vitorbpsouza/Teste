
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        cidade = request.form['cidade']
        renda = request.form['renda']
        preco_proposta = request.form['preco_proposta']
        valor_avaliacao = request.form['valor_avaliacao']
        prazo_caixa = request.form['prazo_caixa']
        possui_dependente = request.form['possui_dependente']
        fgts = request.form['fgts']
        data_nascimento = request.form['data_nascimento']
        cotista = request.form['cotista']
        
        # Realize a simulação com os dados recebidos
        
        # Exemplo de exibição dos dados de entrada
        return f"""
            <h1>Dados de simulação:</h1>
            <p>Cidade: {cidade}</p>
            <p>Renda: {renda}</p>
            <p>Preço Proposta: {preco_proposta}</p>
            <p>Valor Avaliação: {valor_avaliacao}</p>
            <p>Prazo Caixa: {prazo_caixa}</p>
            <p>Possui Dependente: {possui_dependente}</p>
            <p>FGTS: {fgts}</p>
            <p>Data de Nascimento: {data_nascimento}</p>
            <p>Cotista: {cotista}</p>
        """
        
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
