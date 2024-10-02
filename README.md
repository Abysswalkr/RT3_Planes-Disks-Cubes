# RT3 Planes Disks and Cubes

## Descripción del Proyecto

Este proyecto implementa un motor de trazado de rayos (raytracer) simple en Python utilizando **pygame**. El motor es capaz de renderizar diferentes formas geométricas, como esferas, discos, cubos (AABB - Axis-Aligned Bounding Box), y planos, con soporte para materiales con texturas y propiedades de reflexión y refracción. El proyecto destaca por la inclusión de texturas, iluminación ambiental y direccional, y un sistema de materiales flexibles que pueden ser opacos, reflectantes o transparentes.

El escenario representado se configura con diferentes objetos y planos que simulan las paredes, piso, y techo de una habitación, con cubos y espejos reflejantes que muestran las propiedades de los materiales.

## Características

- **Formas Soportadas**: Planos, Discos, Cubos (AABB), Esferas.
- **Texturas**: Soporte para imágenes .bmp que se aplican a los objetos como texturas.
- **Materiales**: Los materiales pueden ser opacos, reflectantes o transparentes. Cada material tiene propiedades ajustables como la difusividad, la especularidad y el índice de refracción.
- **Iluminación**: Iluminación direccional y ambiental con ajuste de intensidad.
- **Cámara**: Control de la posición de la cámara para ajustar el ángulo de visión.

## Instalación

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/Abysswalkr/RT3_Planes-Disks-Cubes
   ```

2. Instalar las dependencias necesarias. Se utiliza **pygame** como base:
   ```bash
   pip install pygame
   ```

3. Ejecutar el programa:
   ```bash
   python main.py
   ```

## Estructura del Proyecto

- **gl.py**: Renderizador que se encarga del trazado de rayos, manejo de texturas y generación de la imagen final.
- **figures.py**: Definición de las figuras geométricas soportadas (Planos, Discos, Esferas, Cubos).
- **material.py**: Manejo de materiales aplicados a los objetos (opacos, reflectivos, transparentes).
- **lights.py**: Implementación de la iluminación direccional y ambiental.
- **texture.py**: Carga y aplicación de texturas en los objetos.
- **main.py**: Configuración de la escena, materiales, texturas, luces y ejecución del renderizado.

## Uso

El archivo `main.py` contiene la configuración de la escena que se va a renderizar. Puedes modificar los materiales, agregar o quitar objetos, o cambiar la posición de la cámara según tus necesidades.

Ejemplo de creación de un cubo con textura:
```python
cube_material = Material(texture=Texture('Textures/crafteo.bmp'), spec=64)
rt.scene.append(AABB(position=[-1, -1.5, -5], sizes=[1, 1, 1], material=cube_material))
```


## Captura de Pantalla

![output](https://github.com/user-attachments/assets/cf24cf12-125c-4e6a-8976-f7ed3e141f84)

## Contribuciones

Las contribuciones son bienvenidas. Si tienes ideas para mejorar el proyecto o encontrar errores, por favor abre un "issue" o envía un "pull request" en el repositorio oficial.
