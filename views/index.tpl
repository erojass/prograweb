<!DOCTYPE html>
<html>

    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>PRIMEROS PASOS CON BRACKETS</title>
        <meta name="description" content="Una guía interactiva de primeros pasos para Brackets.">
        <link rel="stylesheet" href="/main.css">
    </head>
    <body>
        <label>nombre  </label>{{locals['nombre']}}
        %if locals['edad'] > 18:
            <h1>eres mayor de edad</h1>
        %else:
            <h1>eres menor de edad</h1>
        %end
        <table>
            <th>
                <td>genero</td>
                <td>nombre</td>
            </th>
            % for juego in locals['juegos']:
            <tr>
                <td>{{juego['genero']}}</td>
                <td>{{juego['nombre']}}</td>
            </tr>
            % end
        </table>

        <form action="/crear" method="POST">
            nombre <input type="text" name="nombre"> <br>
            edad <input type="text" name="edad"> <br>
            <input type="submit" value="enviar">
        </form>
    </body>
</html>
