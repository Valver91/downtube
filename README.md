# downtube
En este repositorio guardo un pequeño proyecto para descargar el video o el audio de un enlace de YouTube.

Este programa es una aplicación de escritorio que utiliza la biblioteca de Python pytube para descargar videos de YouTube. La aplicación presenta una interfaz gráfica de usuario (GUI) creada con la biblioteca Tkinter.

Al ejecutar el programa, se abre una ventana con una casilla de entrada donde se puede pegar el enlace completo del video de YouTube que se desea descargar. Luego, el usuario debe seleccionar si desea descargar el video completo o solo el audio, haciendo clic en los botones de radio "Audio" o "Video". Después, el usuario hace clic en el botón "Descargar" para iniciar el proceso de descarga.

Cuando se hace clic en el botón "Descargar", se llama a la función accion() que verifica qué botón de radio ha sido seleccionado. Si se selecciona "Audio", el programa utiliza la función get_audio_only() de la biblioteca pytube para descargar el audio del video. Si se selecciona "Video", el programa utiliza la función get_highest_resolution() para descargar el video completo en la máxima resolución disponible.

Después de la descarga, la función accion() borra el contenido de la casilla de entrada y muestra un mensaje emergente que indica que la descarga ha finalizado.

Además de la funcionalidad de descarga, la aplicación también incluye un menú con dos opciones: "Para más información" y "Salir". La primera opción muestra una ventana emergente con información sobre el autor de la aplicación, mientras que la segunda opción cierra la aplicación.
