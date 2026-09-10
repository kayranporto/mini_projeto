from flask import Flask, render_template

app = Flask(__name__)

CAFETERIAS = [
    {
        "nome": "Canto do Grão",
        "bairro": "Vila Madalena",
        "descricao": "Cafés especiais, bolos caseiros e uma varanda tranquila.",
        "especialidade": "Coado da casa",
        "aberta": True,
    },
    {
        "nome": "Manhã Lenta",
        "bairro": "Pinheiros",
        "descricao": "Um refúgio pequeno para espresso e leitura sem pressa.",
        "especialidade": "Espresso tônica",
        "aberta": True,
    },
    {
        "nome": "Linha 7 Café",
        "bairro": "Liberdade",
        "descricao": "Café brasileiro servido ao lado de doces artesanais.",
        "especialidade": "Latte de gergelim",
        "aberta": False,
    },
]

EVENTOS = [
    {"dia": "Sáb, 12", "evento": "Oficina de métodos filtrados", "local": "Canto do Grão", "horario": "10h"},
    {"dia": "Dom, 20", "evento": "Clube de leitura", "local": "Manhã Lenta", "horario": "15h"},
    {"dia": "Qui, 24", "evento": "Degustação de microlotes", "local": "Linha 7 Café", "horario": "19h"},
]


@app.route("/")
def inicio():
    return render_template("inicio.html", cafeterias=CAFETERIAS[:2])


@app.route("/cafeterias")
def cafeterias():
    return render_template("cafeterias.html", cafeterias=CAFETERIAS)


@app.route("/agenda")
def agenda():
    return render_template("agenda.html", eventos=EVENTOS)


@app.route("/sobre")
def sobre():
    return render_template("sobre.html")


if __name__ == "__main__":
    app.run(debug=True)
