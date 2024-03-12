from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Persona
from app.forms import PersonaForm
from flask_paginate import Pagination, get_page_args
@app.route('/')
def index():
    """Ruta principal para mostrar todas las personas, además de las acciones disponibles."""
      # Obtener los parámetros de la paginación desde la solicitud HTTP
    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')

    # Obtener todas las personas de la base de datos
    personas = Persona.query.order_by(Persona.id).offset(offset).limit(per_page).all()

    # Crear la instancia de paginación
    pagination = Pagination(page=page, per_page=per_page, total=Persona.query.count())

    return render_template('index.html', personas=personas, pagination= pagination)

@app.route('/agregar', methods=['GET', 'POST'])
def agregar():
    """Ruta para agregar una nueva persona."""
    form = PersonaForm(request.form)
    if request.method == 'POST' and form.validate():
        try:
         nueva_persona = Persona(nombre=form.nombre.data, 
                                apellido=form.apellido.data, 
                                edad=form.edad.data, 
                                direccion=form.direccion.data, 
                                correo=form.correo.data)
         db.session.add(nueva_persona)
         db.session.commit()
         return redirect(url_for('index'))
        except Exception as e:
            return render_template('error.html', error=str(e)), 500

    return render_template('agregar_persona.html', form=form)

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    """Ruta para editar una persona existente."""
    persona = Persona.query.get_or_404(id)
    if request.method == 'POST':
        try:
         persona.nombre = request.form['nombre']
         persona.apellido = request.form['apellido']
         persona.edad = request.form['edad']
         persona.direccion = request.form['direccion']
         persona.correo = request.form['correo']
        
         db.session.commit()
        
         return redirect(url_for('index'))
        except Exception as e:
           return render_template('error.html', error=str(e)), 500
        
    return render_template('editar_persona.html', persona=persona)

@app.route('/eliminar/<int:id>')
def eliminar(id):
    """Ruta para eliminar una persona."""
    try:
     persona = Persona.query.get_or_404(id)
     db.session.delete(persona)
     db.session.commit()
     return redirect(url_for('index'))
    except Exception as e:
        return render_template('error.html', error=str(e)), 500