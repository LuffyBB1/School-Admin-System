# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------
# AppConfig configuration made easy. Look inside private/appconfig.ini
# Auth is for authenticaiton and access control
# -------------------------------------------------------------------------
from gluon.contrib.appconfig import AppConfig
from gluon.tools import Auth
from gluon import DAL, Field

# -------------------------------------------------------------------------
# This scaffolding model makes your app work on Google App Engine too
# File is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

if request.global_settings.web2py_version < "2.15.5":
    raise HTTP(500, "Requires web2py 2.15.5 or newer")

# -------------------------------------------------------------------------
# if SSL/HTTPS is properly configured and you want all HTTP requests to
# be redirected to HTTPS, uncomment the line below:
# -------------------------------------------------------------------------
# request.requires_https()

# -------------------------------------------------------------------------
# once in production, remove reload=True to gain full speed
# -------------------------------------------------------------------------
configuration = AppConfig(reload=True)

db = DAL(configuration.get('db.uri'),
        pool_size=configuration.get('db.pool_size'),
        migrate_enabled=configuration.get('db.migrate'),
        check_reserved=['all'])

session.connect(request, response, db=db)

# -------------------------------------------------------------------------
# by default give a view/generic.extension to all actions from localhost
# none otherwise. a pattern can be 'controller/function.extension'
# -------------------------------------------------------------------------
response.generic_patterns = []
if request.is_local and not configuration.get('app.production'):
    response.generic_patterns.append('*')

# -------------------------------------------------------------------------
# choose a style for forms
# -------------------------------------------------------------------------
response.formstyle = 'bootstrap4_inline'
response.form_label_separator = ''

auth = Auth(db, host_names=configuration.get('host.names'))

auth.settings.extra_fields['auth_user'] = []
auth.define_tables(username=False, signature=False)

auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True


response.meta.author = configuration.get('app.author')
response.meta.description = configuration.get('app.description')
response.meta.keywords = configuration.get('app.keywords')
response.meta.generator = configuration.get('app.generator')
response.show_toolbar = configuration.get('app.toolbar')


if configuration.get('scheduler.enabled'):
    from gluon.scheduler import Scheduler
    scheduler = Scheduler(db, heartbeat=configuration.get('scheduler.heartbeat'))

db.define_table('salon',
    Field('id', 'integer'),
    Field('cod_salon', 'string', unique=True),
    primarykey=['cod_salon']
)

db.define_table('estudiante',
    Field('documento', 'integer', notnull=True, unique=True),
    Field('nombre', 'string', notnull=True),
    Field('apellido', 'string', notnull=True),
    Field('edad', 'integer', notnull=True),
    Field('fecha_nacimiento', 'date', notnull=True),
    Field('jornada', 'string', notnull=True),
    Field('salon_id', 'reference salon.cod_salon'),
    primarykey=['documento']
)

db.define_table('asistencia',
    Field('id_asistencia', 'id'),
    Field('asiste', 'boolean', default=False),
    Field('ausente', 'boolean', default=False),
    Field('fecha', 'date', notnull=True),
    Field('id_estudiante', 'reference estudiante.documento'),
    Field('cod_salon', 'reference salon.cod_salon'),
)

db.define_table('materia',
    Field('id_materia', 'id'),
    Field('nombre', 'string', notnull=True),
    Field('cod_salon', 'reference salon.cod_salon'),
)
