from flask import Flask, render_template, redirect

app=Flask(__name__)


# Area principal (produtos e tals)

@app.route("/")
def init_page():
    return render_template("index.html")

# Portal do cliente

@app.route("/my-account/auth/")
def auth_page_client():
    return render_template("painel_cliente/auth.html")


@app.route("/my-account/login/")
def login_page_client():
    return render_template("painel_cliente/perfil_login.html")


@app.route("/my-account/register/")
def register_page_client():
    return render_template("painel_cliente/perfil_register.html")


@app.route("/my-account/panel/")
def painel_page_client():
    return render_template("painel_cliente/painel_cliente.html")


# Comprar 

@app.route("/my-account/comprar/")
def comprar_page_client():
    return render_template("painel_cliente/comprar.html")


# Carrinho


@app.route("/my-account/cart/")
def cart_page_client():
    return render_template("painel_cliente/carrinho.html")


# Mais paginas
@app.route("/destaques/")
def destaques_page():
    return render_template("destaques_page.html")


# Finalizar compra



# Portal do ADM
@app.route("/adm_panel/auth/login")
def adm_panelLogin():
    return render_template('admin/login.html')


@app.route("/adm_panel/panel/")
def panel_adm_panel():
    return render_template('admin/init_panel.html')

@app.route("/adm_panel/estoque")
def panel_adm_estoque():
    return render_template('admin/estoque.html')






if "__main__" == __name__:
    app.run(
        debug=True
    )