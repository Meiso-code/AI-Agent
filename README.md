# IA Agent – Estructura Inicial

Un agente de IA básico desarrollado en Python, diseñado para ser extensible y fácil de configurar. Este proyecto incluye agentes especializados para empresas financieras y productoras de contenido.

## 📁 Estructura del proyecto

```
AI-Agent/
├── main.py              # Clase base del agente y agentes especializados
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

### Ejemplo básico de creación y ejecución de un agente:

```python
from main import Agent

agent = Agent(name="Asistente", model="gpt-4o-mini")
response = agent.think("¿Cuál es la capital de Francia?")
print(response)  # Output: Thinking about: ¿Cuál es la capital de Francia?
```

Para implementar lógica propia, hereda de la clase `Agent` y sobreescribe el método `run`.

### Agentes para empresa financiera:

```python
from main import FinancialInstitute

bank = FinancialInstitute("Banco Ejemplo")
result = bank.analyze_opportunity("Invertir en tecnología energética")
print(result)
```

### Agentes para productora de contenido:

```python
from main import ContentProductionHouse

studio = ContentProductionHouse("Estudio Creativo")
result = studio.produce_content("Una campaña sobre sostenibilidad")
print(result)
```

## 🏢 Agentes por dominio

### Empresa Financiera

- **RiskAnalysisAgent** (`RiskAnalyzer`): Evalúa riesgo de mercado, crédito y operativo; calcula métricas de riesgo y recomendaciones.
- **InvestmentAnalysisAgent** (`InvestmentAnalyzer`): Analiza estados financieros, evalúa desempeño de activos y genera recomendaciones de inversión.
- **ComplianceAgent** (`ComplianceOfficer`): Verifica requisitos regulatorios, asegura cumplimiento de políticas y sinaliza problemas de cumplimiento.
- **PortfolioManagementAgent** (`PortfolioManager`): Optimización de carteras, análisis de asignación de activos, perfiles riesgo-retorno y recomendaciones de rebalanceo.
- **MarketResearchAgent** (`MarketResearcher`): Análisis de tendencias industriales, panorama competitivo e indicadores económicos.

**FinancialInstitute** – Compañía contenedora que ejecuta análisis completos integrando todos los agentes financieros para evaluar oportunidades de inversión.

### Productora de Contenido

- **ContentStrategyAgent** (`ContentStrategist`): Análisis de audiencia, definición de pilares de contenido, estrategia de canales y configuración de métricas ROI.
- **ContentCreationAgent** (`ContentCreator`): Redacción de artículos, guiones o guiones; fase de investigación; generación de contenido original.
- **EditingAgent** (`ContentEditor`): Revisión de gramática y estilo, verificación de hechos, alineación de tono y marca, y pulido final.
- **SEOOptimizationAgent** (`SEO specialist`): Investigación de palabras clave, elementos SEO on-page, optimización de metadatos y estructura de legibilidad.
- **DistributionAgent** (`ContentDistributor`): Selección de plataformas, calendario de distribución, sindicación multi-canal y segmentación de audiencia.
- **AnalyticsAgent** (`ContentAnalyst`): Seguimiento de métricas de rendimiento, análisis de engagement del audiencia, cálculo ROI de contenido y recomendaciones de ajuste estratégico.

**ContentProductionHouse** – Compañía contenedora que ejecuta el flujo completo de creación de contenido desde la estrategia hasta la medición de resultados.

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