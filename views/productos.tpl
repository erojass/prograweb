<!DOCTYPE html>
<html>

    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>Lista de productos</title>
        <meta name="description" content="Una guía interactiva de primeros pasos para Brackets.">
        <link rel="stylesheet" href="/main.css">
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
    </head>
    <body class="container">
        <table class="table table-striped">
            <tr>
                <th>id</th>
                <th>nombre</th>
                <th>precio</th>
                <th>imagen</th>
                <th>ficha</th>
            </tr>
            % for producto in locals['productos']:
            <tr>
                <td>{{producto['id']}}</td>
                <td>{{producto['nombre']}}</td>
                <td>{{producto['precio']}}</td>
                <td><img src="{{producto['imagen']}}" alt="" height="50" width="50"></td>
                <td><a href="{{producto['ficha']}}" target="_blank">Ver ficha</a></td>
            </tr>
            % end
        </table>
    </body>
</html>
