<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{title}} - Organizador de Viagens</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.9.4/css/bulma.min.css">
    <style>
        body {
            background-color: #f5f7fa; /* Um fundo um pouco mais suave */
        }
        .main-content {
            padding: 2rem 1.5rem;
        }
    </style>
</head>
<body>
    <nav class="navbar is-info" role="navigation" aria-label="main navigation">
        <div class="container">
            <div class="navbar-brand">
                <a class="navbar-item has-text-weight-bold is-size-4" href="/dashboard">
                    ✈️ Organizador de Viagens
                </a>
            </div>

            <div id="navbarBasicExample" class="navbar-menu">
                <div class="navbar-start">
                    <a class="navbar-item" href="/dashboard">
                        Dashboard
                    </a>
                    <a class="navbar-item" href="/trips">
                        Minhas Viagens
                    </a>
                </div>

                <div class="navbar-end">
                    <div class="navbar-item">
                        <div class="buttons">
                            <a class="button is-light" href="/logout">
                                Logout
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </nav>

    <main class="main-content">
        {{!base}}
    </main>

</body>
</html>