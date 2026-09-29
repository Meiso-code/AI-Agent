# IA Agent – Estructura Inicial

Un agente de IA básico desarrollado en Python, diseñado para ser extensible y fácil de configurar.

## 📁 Estructura del proyecto

```
AI-Agent/
├── main.py              # Clase base del agente
├── requirements.txt     # Dependencias del proyecto
├── .env.example         # Variables de entorno de ejemplo
├── README.md            # Documentación del proyecto
└── .env                # (no versionado) Configuración local
```

## 🚀 Instalación

1. Clona este repositorio o crea la estructura de archivos anterior.
2. Crea un entorno virtual (recomendado):
   ```bash
   python -m venv venv
   source venv/Scripts/activate   # Windows
   # . venv/bin/activate          # macOS / Linux
   ```
3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
4. Copia el archivo de ejemplo de variables de entorno:
   ```bash
   copy .env.example .env
   ```
5. Agrega tu clave de API de OpenAI en el archivo `.env`:
   ```
   OPENAI_API_KEY=sk-tu-clave-aqui
   ```

## 🛠️ Uso

Ejemplo básico de creación y ejecución de un agente:

```python
from main import Agent

agent = Agent(name="Asistente", model="gpt-4o-mini")
response = agent.think("¿Cuál es la capital de Francia?")
print(response)  # Output: Thinking about: ¿Cuál es la capital de Francia?
```

Para implementar lógica propia, hereda de la clase `Agent` y sobreescribe el método `run`.

## ⚙️ Configuración

Las variables de entorno se leen desde el archivo `.env` (no incluido en el repositorio). Puedes añadir más variables según sea necesario (por ejemplo, `MAX_TOKENS`, `TEMPERATURE`, etc.).

## 🤝 Contribuir

1. Fork el repositorio.
2. Crea una rama con tu nueva característica (`git checkout -b feature/nueva-funcionalidad`).
3. Commit tus cambios (`git commit -m 'Añadir nueva funcionalidad'`).
4. Push a la rama (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Ver el archivo `LICENSE` para más detalles.