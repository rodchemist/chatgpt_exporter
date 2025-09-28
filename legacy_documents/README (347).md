# Empiric Presentation Modular

**Objetivo:** Cada slide es *autocontenida* (HTML, CSS, JS y vendors locales), y `index.html` carga todas las slides listadas en `assets/config/slides_config.json`.

## Cómo ejecutar
- Servir en local (recomendado):
  ```bash
  npx http-server -p 8080
  # Abrir http://localhost:8080
  ```
  O con Python:
  ```bash
  python -m http.server 8080
  ```

## Estructura
- `slides/slide_XX/slide.html`  → contiene `<link ./slide.css>` y `<script ./slide.js>`.
- Librerías copiadas por slide en `slides/slide_XX/vendor/` (ej.: Chart.js).
- `assets/config/slides_config.json` → orden de carga.
- `assets/js/slide-loader.js` y `assets/js/navigation.js` → cargan y navegan sin acoplar estilos o lógicas de cada slide.

## Añadir/ocultar slides
1. Crear nueva carpeta `slides/slide_15/` con `slide.html`, `slide.css`, `slide.js`.
2. (Opcional) Copiar librerías a `vendor/` y referenciarlas en `slide.html`.
3. Editar `assets/config/slides_config.json` y agregar `\"slide_15\"` en `slides`.

## Documentación Adicional

Para información sobre el desarrollo de agentes AI y las directrices de repositorio, consulte la documentación principal en [../QWEN_CONTEXT.md](../QWEN_CONTEXT.md).

## Notas
- Las rutas externas (`http(s)://`) se mantienen.
- Las rutas locales se copian a `vendor/` cuando es posible.
