from django.db import models

# Create your models here.

class Asociaciones(models.Model):
    asociacionesid = models.AutoField(db_column='AsociacionesID', primary_key=True)  # Field name made lowercase.
    dpto = models.IntegerField(db_column='Dpto')  # Field name made lowercase.
    ctacontable = models.FloatField(db_column='CtaContable')  # Field name made lowercase.
    ctapresupuestaria = models.CharField(db_column='CtaPresupuestaria', max_length=255, blank=True, null=True)  # Field name made lowercase.
    descripcionctapresu = models.CharField(db_column='DescripcionCtaPresu', max_length=255, blank=True, null=True)  # Field name made lowercase.
    a = models.IntegerField(db_column='A', blank=True, null=True)  # Field name made lowercase.
    b = models.IntegerField(db_column='B',blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Asociaciones'

class CodigoFactura(models.Model):
    tipo = models.IntegerField(db_column='Tipo', primary_key=True)  # Field name made lowercase.
    factura = models.CharField(db_column='Factura', max_length=50, blank=True, null=True)  # Field name made lowercase.
    codcomprobante = models.CharField(db_column='CodComprobante', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Codigo Factura'


class Codigocajachica(models.Model):
    codcajachica = models.IntegerField(db_column='CodCajaChica', primary_key=True)  # Field name made lowercase.
    concepto = models.CharField(db_column='Concepto', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CodigoCajaChica'


class Condicioniva(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    condicioniva = models.CharField(db_column='CondicionIVA', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CondicionIVA'


class CuentasContables(models.Model):
    n·mero_de_cuenta = models.FloatField(db_column='N·mero de Cuenta', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ctapresu = models.IntegerField(db_column='CtaPresu', blank=True, null=True)  # Field name made lowercase.
    descripción = models.CharField(db_column='Descripción', max_length=70, blank=True, null=True)  # Field name made lowercase.
    dpto = models.SmallIntegerField(db_column='Dpto', blank=True, null=True)  # Field name made lowercase.
    número = models.SmallIntegerField(db_column='Número', blank=True, null=True)  # Field name made lowercase.
    nivel2 = models.CharField(db_column='Nivel2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    suma = models.CharField(db_column='Suma', max_length=50, blank=True, null=True)  # Field name made lowercase.
    descripcionsuma = models.CharField(db_column='DescripcionSuma', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Cuentas Contables'


class CuentasPresupuestaria(models.Model):
    ctapresu = models.CharField(db_column='CtaPresu', primary_key=True, max_length=50)  # Field name made lowercase.
    descripcionctapresu = models.CharField(db_column='DescripcionCtaPresu', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subcuenta = models.FloatField(db_column='SubCuenta')  # Field name made lowercase.
    descripcion_subcuenta = models.CharField(db_column='Descripcion Subcuenta', max_length=70, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cuenta = models.FloatField(db_column='Cuenta', blank=True, null=True)  # Field name made lowercase.
    descripcion_cuenta = models.CharField(db_column='Descripcion Cuenta', max_length=70, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Cuentas Presupuestaria'
        unique_together = (('ctapresu', 'subcuenta'),)


class ErogacionesPresupuestarias(models.Model):
    coddpto = models.IntegerField(db_column='CodDpto', primary_key=True)  # Field name made lowercase.
    cuenta = models.CharField(db_column='Cuenta', max_length=7, blank=True, null=True)  # Field name made lowercase.
    departamento = models.CharField(db_column='Departamento', max_length=50, blank=True, null=True)  # Field name made lowercase.
    suma = models.CharField(db_column='Suma', max_length=7, blank=True, null=True)  # Field name made lowercase.
    cuentaiva = models.CharField(db_column='CuentaIva', max_length=8, blank=True, null=True)  # Field name made lowercase.
    subcentaiva = models.CharField(db_column='SubCentaIva', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ctapercib = models.CharField(db_column='CtaPercIB', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tem = models.CharField(db_column='TEM', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Erogaciones Presupuestarias'


class Estados(models.Model):
    estadoid = models.AutoField(db_column='EstadoID', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Estados'


class Excepciones(models.Model):
    excepcionid = models.AutoField(db_column='ExcepcionID', primary_key=True)  # Field name made lowercase.
    sectorid = models.IntegerField(db_column='SectorID')  # Field name made lowercase.
    creado = models.DateField(db_column='Creado')  # Field name made lowercase.
    modificado = models.DateField(db_column='Modificado')  # Field name made lowercase.
    usuarioid = models.IntegerField(db_column='UsuarioID')  # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Excepciones'


class Fechacierre(models.Model):
    idfechacierre = models.AutoField(db_column='idFechaCierre', primary_key=True)  # Field name made lowercase.
    fechacierre = models.DateField(db_column='FechaCierre')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FechaCierre'


class Habilitocajachica(models.Model):
    codsector = models.IntegerField(db_column='CodSector', primary_key=True)  # Field name made lowercase.
    fechacajachica = models.DateTimeField(db_column='FechaCajaChica')  # Field name made lowercase.
    montoasignado = models.DecimalField(db_column='MontoAsignado', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rendido = models.DecimalField(db_column='Rendido', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    encaja = models.DecimalField(db_column='EnCaja', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    estadoid = models.IntegerField(db_column='EstadoID', blank=True, null=True)  # Field name made lowercase.
    usuariocambioestado = models.IntegerField(db_column='UsuarioCambioEstado', blank=True, null=True)  # Field name made lowercase.
    fechacambioestado = models.DateTimeField(db_column='FechaCambioEstado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HabilitoCajaChica'
        unique_together = (('codsector', 'fechacajachica'),)


class Maestro(models.Model):
    n·mero_de_cuenta = models.FloatField(db_column='N·mero de Cuenta', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    código_de_integración = models.CharField(db_column='C¾digo de Integraci¾n', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cuenta_en_que_suma = models.FloatField(db_column='Cuenta en que suma', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    number_1 = models.FloatField(db_column='1', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2 = models.FloatField(db_column='2', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3 = models.FloatField(db_column='3', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4 = models.FloatField(db_column='4', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_5 = models.FloatField(db_column='5', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    crÚdito = models.FloatField(db_column='CrÚdito', blank=True, null=True)  # Field name made lowercase.
    descripción = models.CharField(db_column='Descripci¾n', max_length=70, blank=True, null=True)  # Field name made lowercase.
    total_comprometido = models.FloatField(db_column='Total Comprometido', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    total_crÚdito = models.FloatField(db_column='Total CrÚdito', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cuenta_contable = models.FloatField(db_column='Cuenta Contable', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    n·mero = models.SmallIntegerField(db_column='N·mero', blank=True, null=True)  # Field name made lowercase.
    balance = models.SmallIntegerField(db_column='BALANCE', blank=True, null=True)  # Field name made lowercase.
    pp = models.CharField(db_column='PP', max_length=10, blank=True, null=True)  # Field name made lowercase.
    control = models.BooleanField(db_column='Control', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Maestro'


class Movimientos(models.Model):
    idmovimiento = models.AutoField(db_column='IdMovimiento', primary_key=True)  # Field name made lowercase.
    codsector = models.IntegerField(db_column='CodSector', blank=True, null=True)  # Field name made lowercase.
    coddpto = models.IntegerField(db_column='CodDpto', blank=True, null=True)  # Field name made lowercase.
    fechagrabacion = models.DateTimeField(db_column='FechaGrabacion', blank=True, null=True)  # Field name made lowercase.
    fechacajachica = models.DateTimeField(db_column='FechaCajaChica', blank=True, null=True)  # Field name made lowercase.
    codproveedor = models.IntegerField(db_column='CodProveedor', blank=True, null=True)  # Field name made lowercase.
    proveedor = models.CharField(db_column='Proveedor', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cuit = models.CharField(db_column='CUIT', max_length=13, blank=True, null=True)  # Field name made lowercase.
    tipofactura = models.IntegerField(db_column='TipoFactura', blank=True, null=True)  # Field name made lowercase.
    nrofactura = models.CharField(db_column='NroFactura', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cantidad = models.IntegerField(db_column='Cantidad', blank=True, null=True)  # Field name made lowercase.
    articulo = models.CharField(db_column='Articulo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    neto = models.DecimalField(db_column='Neto', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    netonogravado = models.DecimalField(db_column='NetoNoGravado', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    neto21 = models.DecimalField(db_column='Neto21', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    iva21 = models.DecimalField(db_column='Iva21', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    neto105 = models.DecimalField(db_column='Neto105', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    iva105 = models.DecimalField(db_column='Iva105', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    iva = models.DecimalField(db_column='IVA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    percib = models.DecimalField(db_column='PercIB', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tem = models.DecimalField(db_column='TEM', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    percepcioniva = models.DecimalField(db_column='PercepcionIVA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    otrostrib = models.DecimalField(db_column='OtrosTrib', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ajusteredondeo = models.DecimalField(db_column='AjusteRedondeo', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    total = models.DecimalField(db_column='Total', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cuentacontable = models.FloatField(db_column='CuentaContable', blank=True, null=True)  # Field name made lowercase.
    cuentapresupuestaria = models.IntegerField(db_column='CuentaPresupuestaria', blank=True, null=True)  # Field name made lowercase.
    subcuenta = models.IntegerField(db_column='SubCuenta', blank=True, null=True)  # Field name made lowercase.
    idautorizado = models.IntegerField(db_column='IdAutorizado', blank=True, null=True)  # Field name made lowercase.
    exento = models.BooleanField(db_column='Exento', blank=True, null=True)  # Field name made lowercase.
    estadoid = models.IntegerField(db_column='EstadoID', blank=True, null=True)  # Field name made lowercase.
    usuariocambioestado = models.IntegerField(db_column='UsuarioCambioEstado', blank=True, null=True)  # Field name made lowercase.
    fechacambioestado = models.DateTimeField(db_column='FechaCambioEstado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Movimientos'


class Movimientosproveedores(models.Model):
    idmovimiento = models.AutoField(db_column='IdMovimiento', primary_key=True)  # Field name made lowercase.
    codsector = models.SmallIntegerField(db_column='CodSector', blank=True, null=True)  # Field name made lowercase.
    nro_cuenta = models.FloatField(db_column='Nro cuenta', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    codcajachica = models.IntegerField(db_column='CodCajaChica', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    asiento = models.IntegerField(db_column='Asiento', blank=True, null=True)  # Field name made lowercase.
    observacion = models.CharField(db_column='Observacion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    anulado = models.BooleanField(db_column='Anulado', blank=True, null=True)  # Field name made lowercase.
    fechaanulacion = models.DateTimeField(db_column='FechaAnulacion', blank=True, null=True)  # Field name made lowercase.
    idusuario = models.IntegerField(db_column='IdUsuario', blank=True, null=True)  # Field name made lowercase.
    fechacajachica = models.DateTimeField(db_column='FechaCajaChica', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MovimientosProveedores'


class Proveedores(models.Model):
    cuit = models.CharField(db_column='CUIT', primary_key=True, max_length=12)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=30)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ciudad = models.CharField(db_column='Ciudad', max_length=50, blank=True, null=True)  # Field name made lowercase.
    provincia = models.CharField(db_column='Provincia', max_length=30, blank=True, null=True)  # Field name made lowercase.
    codpostal = models.IntegerField(db_column='CodPostal', blank=True, null=True)  # Field name made lowercase.
    telefono = models.CharField(db_column='Telefono', max_length=15, blank=True, null=True)  # Field name made lowercase.
    condicioniva = models.IntegerField(db_column='CondicionIVA', blank=True, null=True)  # Field name made lowercase.
    alta = models.DateTimeField(db_column='Alta', blank=True, null=True)  # Field name made lowercase.
    modificacion = models.DateTimeField(db_column='Modificacion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Proveedores'


class Sectores(models.Model):
    codsector = models.SmallIntegerField(db_column='CodSector', primary_key=True)  # Field name made lowercase.
    sectorcontable = models.CharField(db_column='SectorContable', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sector = models.CharField(db_column='Sector', max_length=50, blank=True, null=True)  # Field name made lowercase.
    erogacion = models.IntegerField(db_column='Erogacion', blank=True, null=True)  # Field name made lowercase.
    cuentaiva = models.CharField(db_column='CuentaIVA', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subcuentaiva = models.CharField(db_column='SubCuentaIVa', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ctapercib = models.CharField(db_column='CtaPercIB', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tem = models.CharField(db_column='TEM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    contraseña = models.CharField(db_column='Contraseña', max_length=255, blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=255, blank=True, null=True)  # Field name made lowercase.
    montoautorizado = models.DecimalField(db_column='MontoAutorizado', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    idautorizado = models.IntegerField(db_column='IdAutorizado', blank=True, null=True)  # Field name made lowercase.
    tipodepartamento = models.IntegerField(db_column='TipoDepartamento', blank=True, null=True)  # Field name made lowercase.
    cuentanombre = models.CharField(db_column='CuentaNombre', max_length=255, blank=True, null=True)  # Field name made lowercase.
    essucursal = models.BooleanField(db_column='EsSucursal', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Sectores'


class Tiposdepartamentos(models.Model):
    tipodepartamentoid = models.AutoField(db_column='TipoDepartamentoId', primary_key=True)  # Field name made lowercase.
    descripciontipodepartamento = models.CharField(db_column='DescripcionTipoDepartamento', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TiposDepartamentos'


class Usuariosautorizados(models.Model):
    idautorizado = models.AutoField(db_column='IdAutorizado', primary_key=True)  # Field name made lowercase.
    codsector = models.IntegerField(db_column='CodSector', blank=True, null=True)  # Field name made lowercase.
    legajo = models.IntegerField(db_column='Legajo', blank=True, null=True)  # Field name made lowercase.
    usuarioautorizado = models.CharField(db_column='UsuarioAutorizado', max_length=255, blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fechaalta = models.DateTimeField(db_column='FechaAlta', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UsuariosAutorizados'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128)
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)


class Usuarios(models.Model):
    usuarioid = models.AutoField(db_column='UsuarioID', primary_key=True)  # Field name made lowercase.
    usuariolegajo = models.IntegerField(db_column='UsuarioLegajo', blank=True, null=True)  # Field name made lowercase.
    usuariodescripcion = models.CharField(db_column='UsuarioDescripcion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    usuariocontraseña = models.CharField(db_column='UsuarioContraseña', max_length=255, blank=True, null=True)  # Field name made lowercase.
    usuarioestado = models.CharField(db_column='UsuarioEstado', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usuarios'