from database import create_tables, guardar_interaccion, get_interacciones, insert_recurso, get_recursos, delete_old_interacciones

create_tables()

print("Insertando un recurso...")
insert_recurso(
    categoria="Educación",
    descripcion="Guía para entender términos LGTBI",
    enlace="https://ejemplo.com/guia-lgtbi"
)

print("\nRecursos disponibles:")
recursos = get_recursos()
for recurso in recursos:
    print(recurso)

print("\nGuardando una interacción...")
guardar_interaccion(
    endpoint="/consulta-ejemplo",
    consulta="¿Qué significa queer?",
    respuesta="Es un término inclusivo para identidades no normativas.",
    metadata='{"nivel": "básico"}'
)

print("\nÚltimas interacciones registradas:")
interacciones = get_interacciones(limit=5)
for interaccion in interacciones:
    print(interaccion)

print("\nEliminando interacciones antiguas...")
resultado = delete_old_interacciones(days_old=30)
print(f"Interacciones eliminadas: {resultado['deleted_rows']}")