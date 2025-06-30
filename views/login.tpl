<!DOCTYPE html>
<html lang="pt-br">

<head>
  <meta charset="UTF-8" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <link rel="stylesheet" href="static/css/paginaLogin.css" />
  <title>Sistema Bottle - Login</title>
</head>

<body>
  <div class="main-box">
    <div class="logo-div">
      <div class="logo-box">
        <!--<img src="algumaLogo.png" alt="logo do projeto" class="logo-image" /> -->
        <p class="logo-text">Organizador de Viagens</p>
      </div>
      <p class="image-credit">
        <!-- Photo by -->
        <!-- <a href="https://unsplash.com/@mrbrodeur?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Matthew -->
        <!--   Brodeur</a> -->
        <!-- on -->
        <!-- <a -->
        <!--   href="https://unsplash.com/backgrounds/things/weed?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a> -->
        Photo by
        <a
          href="https://unsplash.com/@haliewestphoto?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Ross
          Parmly</a>
        on
        <a
          href="https://unsplash.com/photos/aerial-photography-of-airliner-rf6ywHVkrlY">Unsplash</a>
      </p>
    </div>

    <div class="right-box">
      <p class="top-boilerplate boilerplate-first main-text">
        Crie aqui a sua conta!!!
      </p>

      <p class="top-boilerplate boilerplate-second main-text">
         Logue <em>agora</em> para começar
      </p>

      <!-- <p class="top-boilerplate main-text">You <em>know</em> you want to.</p> -->

      <form action="#" method="get">
        <div class="form-section">
          <p class="main-text">Crie sua conta!</p>

          <div class="form-section-right">
            <div class="form-div">
              <label for="first_name">NOME</label> <br>
              <input type="text" id="first_name" name="first_name" required />
            </div>

            <!-- <div class="form-div"> -->
              <!-- <label for="last_name">LAST NAME</label> <br> -->
              <!-- <input type="text" id="last_name" name="last_name" required /> -->
            <!-- </div> -->

            <div class="form-div">
              <label for="email">EMAIL</label> <br>
              <input type="email" id="email" name="email" required />
            </div>

            <!-- <div class="form-div"> -->
              <!-- <label for="phone">PHONE NUMBER</label> <br> -->
              <!-- <input type="tel" id="phone" name="phone" required /> -->
            <!-- </div> -->

            <div class="form-div">
              <label for="password">SENHA</label> <br>
              <input class="error" type="password" id="password" name="password" minlength="8" required /> <br>
              <span>* senhas não iguais</span>
            </div>

            <div class="form-div">
              <label for="password_confirm">CONFIRME SENHA</label> <br>
              <input class="error" type="password" id="password_confirm" name="password_confirm" minlength="8"
                required />
            </div>

          </div>
        </div>
        <div><button type="submit">Criar Conta</button></div>
      </form>

      <p class="account">Já tem uma conta? <a class="account" href="#">Log in</a></p>
    </div>
</body>

</html>
