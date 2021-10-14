from flask import blueprints, render_template, request

main = blueprints.Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/login/')
def login():
    return render_template('login.html')


@main.route('/login/', methods=['GET', 'POST'])
def dashAdmin():
    if(request.method == 'POST'):
        return render_template('dashAdmin.html')
    else:
        render_template('login.html')


@main.route('/olvideContraseña/')
def registro():
    return render_template('recuperarContraseña.html')


@main.route('/productos/')
def dashProductos():
    return render_template('dashProducto.html')


@main.route('/listaProductos/')
def listaProductos():
    return render_template('listaProductos.html')


@main.route('/verProducto/')
def verProducto():
    return render_template('verProducto.html')



@main.route('/nuevoProducto/')
def nuevoProducto():
    return render_template('crearProducto.html')


@main.route('/buscarProducto/')
def buscarProducto():
    return render_template('buscarProducto.html')


@main.route('/indexProveedor/')
def indeProveedor():
    return render_template('dashProveedor.html')


@main.route('/listaProveedores/')
def listaProveedor():
    return render_template('listarProveedores.html')


@main.route('/crearProveedor/')
def crearProveedor():
    return render_template('crearProveedor.html')


@main.route('/buscarProveedor/')
def buscarProveedor():
    return render_template('buscarProveedor.html')


@main.route('/editarProveedorL/')
def editarProveedorL():
    return render_template('editarProveedores.html')


@main.route('/editarProveedorB/')
def editarProveedorB():
    return render_template('editarProveedores.html')


@main.route('/cancelar/')
def cancelar():
    return render_template('dashProveedor.html')


@main.route('/editarB-P/')
def editarB_P():
    return render_template('editarProducto.html')


@main.route('/editarL-P/')
def editarL_P():
    return render_template('editarProductoLista.html')


@main.route('/cancelarL_P/')
def cancelarL_P():
    return render_template('verProducto.html')



@main.route('/cancelarE_B_P/')
def cancelar_E_BP():
    return render_template('buscarProducto.html')


@main.route('/crearUsuario/')
def crearUsuario():
    return render_template('crearUsuario.html')

@main.route('/crearUsuarioU/')
def crearUsuarioU():
    return render_template('crearUsuario.html')


@main.route('/miPerfil/')
def miPerfil():
    return render_template('miPerfil.html')


@main.route('/usuarios/')
def usuarios():
    return render_template('dashUsuario.html')


@main.route('/nuevoUsuario/')
def nuevoUsuario():
    return render_template('nuevosUsuarios.html')


@main.route('/listaUsuarios/')
def listaUsuarios():
    return render_template('listaUsuarios.html')


@main.route('/editarDatos/')
def editarDatos():
    return render_template('editarDatos.html')

@main.route('/cambiarContraseña/')
def cambiarContraseña():
    return render_template('cambiarContraseña.html')


@main.route('/nuevoProducto/', methods=['GET', 'POST'])
def crearProducto():
    if(request.method == 'POST'):
        return render_template('dashProducto.html')
    else:
        render_template('crearProducto.html')


@main.route('/crearProveedor/', methods=['GET', 'POST'])
def crearProv():
    if(request.method == 'POST'):
        return render_template('dashProveedor.html')
    else:
        return render_template('crearProveedor.html')


@main.route('/editarProveedorL/', methods=['GET', 'POST'])
def editarrProvL():
    if(request.method == 'POST'):
        return render_template('listarProveedores.html')
    else:
        return render_template('editarProveedores.html')


@main.route('/editarProveedorB/', methods=['GET', 'POST'])
def editarrProvB():
    if(request.method == 'POST'):
        return render_template('buscarProveedor.html')
    else:
        return render_template('editarProveedores.html')


@main.route('/editarB-P/', methods=['GET', 'POST'])
def editarProducB():
    if(request.method == 'POST'):
        return render_template('buscarProducto.html')
    else:
        return render_template('editarProducto.html')


@main.route('/crearUsuario/', methods=['GET', 'POST'])
def crearUsu():
    if(request.method == 'POST'):
        return render_template('index.html')
    else:
        return render_template('crearUsuario.html')


@main.route('/olvideContraseña/', methods=['GET', 'POST'])
def enviarOlvideContraseña():
    if(request.method == 'POST'):
        return render_template('recuperarContraseña.html')
    else:
        return render_template('login.html')


@main.route('/editarL-P/', methods=['GET', 'POST'])
def editarProducL():
    if(request.method == 'POST'):
        return render_template('verProducto.html')
    else:
        return render_template('editarProducto.html')

