<!DOCTYPE html>
<html lang="pt-br">

<head>
  <meta charset="UTF-8" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <link rel="stylesheet" href="/static/css/paginaLogin.css" />
  <title>Organizador de Viagens - Login</title>
</head>

<body>
  <div class="main-box">
    <div class="logo-div">
      <div class="logo-box">
        <p class="logo-text">Organizador de Viagens</p>
      </div>
      <p class="image-credit">
        Photo by
        <a href="https://unsplash.com/@haliewestphoto?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Ross
          Parmly</a>
        on
        <a href="https://unsplash.com/photos/aerial-photography-of-airliner-rf6ywHVkrlY">Unsplash</a>
      </p>
    </div>

    <div class="right-box">
      <p class="top-boilerplate boilerplate-first main-text">
        Bem-vindo de volta!
      </p>

      <p class="top-boilerplate boilerplate-second main-text">
        Faça o login para continuar.
      </p>
      
      <form action="/login" method="post">
        <div class="form-section">
          <p class="main-text">Entrar na sua conta</p>

          % if defined('error') and error:
            <div style="color: red; margin-left: 40px; width: 100%;">{{ error }}</div>
          % end

          <div class="form-section-right">
            <div class="form-div">
              <label for="email">EMAIL</label> <br>
              <input type="email" id="email" name="email" required />
            </div>

            <div class="form-div">
              <label for="password">SENHA</label> <br>
              <input type="password" id="password" name="password" required />
            </div>
          </div>
        </div>
        <div><button type="submit">Entrar</button></div>
      </form>

      <p class="account">Não tem uma conta? <a class="account" href="/register">Crie uma agora</a></p>
    </div>
  </div>
</body>

</html>