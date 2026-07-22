# Informacion sobre peliculas, series y artistas (Juan Diego Almanza Veloz)

query = input("Ingrese el nombre de la película, serie o artista: ").lower()
match query:
    case "skyfall":
        info = "007 Operación Skyfall es una película de James Bond lanzada en 2012. También puede referirse a la canción de Adele que sirve como tema principal."
    case "queen":
        info = "Queen es una banda de rock británica formada en 1970, conocida por éxitos como 'Bohemian Rhapsody' y 'We Will Rock You'."
    case "dragon ball":
        info = "Dragon Ball es una serie de anime creada por Akira Toriyama que sigue las aventuras de Goku y sus amigos."
    case "stranger things":
        info = "Stranger Things es una serie de ciencia ficción producida por Netflix."
    case "frieren":
        info = "Frieren es un manga y anime de fantasía que sigue la historia de una elfa llamada Frieren."
    case "karol g":
        info = "Karol G es una cantante y compositora colombiana de música urbana, conocida por éxitos como 'Tusa' y 'Bichota'."
    case "radiohead":
        info = "Radiohead es una banda británica de rock alternativo formada en 1985."
    case "hatsune miku":
        info = "Hatsune Miku es una cantante virtual japonesa creada por Crypton Future Media."
    case "kagamine rin":
        info = "Kagamine Rin es una cantante virtual japonesa creada por Crypton Future Media."
    case "kasane teto":
        info = "Kasane Teto es una cantante virtual japonesa originada en la comunidad de UTAU."
    case "siinamota":
        info = "Siinamota fue un productor musical japonés conocido por canciones como 'Young Girl A' y 'Strobe Last'."
    case _:
        info = "No hay información para ese tema."
print(info)