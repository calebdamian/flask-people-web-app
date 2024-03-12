from app import app, db

from app.models import Persona

# Función para agregar personas de ejemplo
def agregar_personas_ejemplo():
    with app.app_context():
     personas = []

     for i in range(30): 
            personas.append({"nombre": f"Persona_{i+1}", "apellido": "Apellido", "edad": 30, "direccion": f"Dirección_{i+1}", "correo": f"persona{i+1}@example.com"})
        
    
    for persona_data in personas:
        nueva_persona = Persona(nombre=persona_data["nombre"], 
                                apellido=persona_data["apellido"], 
                                edad=persona_data["edad"], 
                                direccion=persona_data["direccion"], 
                                correo=persona_data["correo"])
        db.session.add(nueva_persona)
    
    db.session.commit()

# Verificar si ya existen personas en la base de datos
with app.app_context():
 if not Persona.query.all():
    agregar_personas_ejemplo()

if __name__ == '__main__':
    app.run(debug=True)

