# Humanos contra meteoros

Para esta prueba tecnica se desarrollo un juego el cual consiste en una nave espacial, la última sobreviviente con seres humanos y esta se encuentra amenazada por una serie de meteoritos asesinos los cuales quieren aniquilarla. Para esto usando un arma lazer con el que cuenta la nave y controlando a esta debe exquivar o aniquilar a los meteoritos. La nave cuenta con un escudo protector que le permite sobrevivir a diez impactos de meteoros ¡la especie humana esta en tus manos!

## Construcción del Juego

Para la creación de los elementos del juego se hizo uso de clases con funciones o métodos especiales, se contruyeron las clases:
- Player (Jugador) con los métodos de inicialización (init), actualización de posición (update) y disparo (shoot).

- Meteor (Meteoro) con los métodos de inicialización (init) y actualización de posición (update).

- Bullet (Disparo) con los métodos de inicialización (init) y actualización de posición (update).

Con estas clases se crearon los tres personajes que interactuan en el juego la cual es la nave, los meteoros y los lazers o disparos.
Por otro lado, se construyeron diferentes funciones que permiten dibujar texto en pantalla (draw_text) para mostrar el menu inicial con indicaciones o el puntaje a lo largo del juego, también la función que dibuja la barra de vida (draw_shield_bar) y la función para el menu inicial (show_go_screen).

Por último el Juego se corre en un Loop hasta que se cierre con la x o pierda el jugador, en este loop se crean los meteoritos, se realizan los disparos, se mueve el jugador y todas las acciones correspondientes al juego.

Es de anotar, que las imagenes utilizadas al rededor del juego se encuentran en la carpeta Obje
