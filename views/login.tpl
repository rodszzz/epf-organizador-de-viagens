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
        <img src="odinLogo.png" alt="Odin Project logo" class="logo-image" />
        <p class="logo-text">ODIN</p>
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
          href="https://unsplash.com/@haliewestphoto?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Halie
          West</a>
        on
        <a
          href="https://unsplash.com/photos/25xggax4bSA?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
      </p>
    </div>

    <div class="right-box">
      <p class="top-boilerplate boilerplate-first main-text">
        This is not a real online service! You know you need something like
        this in your life to help you realize your deepest dreams.
      </p>

      <p class="top-boilerplate boilerplate-second main-text">
        Sign up <em>now</em> to get started.
      </p>

      <p class="top-boilerplate main-text">You <em>know</em> you want to.</p>

      <form action="#" method="get">
        <div class="form-section">
          <p class="main-text">Let's do this!</p>

          <div class="form-section-right">
            <div class="form-div">
              <label for="first_name">FIRST NAME</label> <br>
              <input type="text" id="first_name" name="first_name" required />
            </div>

            <div class="form-div">
              <label for="last_name">LAST NAME</label> <br>
              <input type="text" id="last_name" name="last_name" required />
            </div>

            <div class="form-div">
              <label for="email">EMAIL</label> <br>
              <input type="email" id="email" name="email" required />
            </div>

            <div class="form-div">
              <label for="phone">PHONE NUMBER</label> <br>
              <input type="tel" id="phone" name="phone" required />
            </div>

            <div class="form-div">
              <label for="password">PASSWORD</label> <br>
              <input class="error" type="password" id="password" name="password" minlength="8" required /> <br>
              <span>* Passwords do not match</span>
            </div>

            <div class="form-div">
              <label for="password_confirm">CONFIRM PASSWORD</label> <br>
              <input class="error" type="password" id="password_confirm" name="password_confirm" minlength="8"
                required />
            </div>

          </div>
        </div>
        <div><button type="submit">Create Account</button></div>
      </form>

      <p class="account">Already have an account? <a class="account" href="#">Log in</a></p>
    </div>
</body>

</html>
