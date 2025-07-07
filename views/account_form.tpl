% rebase('layout.tpl', title='Minha Conta')

<div class="columns is-centered">
    <div class="column is-half">
        <div class="box">
            <h1 class="title">Minha Conta</h1>
            <p class="subtitle">Atualize as suas informações pessoais.</p>
            <hr>

            % if success:
                <div class="notification is-success is-light">
                    As suas informações foram atualizadas com sucesso!
                </div>
            % end

            <form action="/account" method="post">
                <div class="field">
                    <label class="label">Nome</label>
                    <div class="control">
                        <input class="input" type="text" name="name" value="{{user.name}}" required>
                    </div>
                </div>

                <div class="field">
                    <label class="label">Email</label>
                    <div class="control">
                        <input class="input" type="email" name="email" value="{{user.email}}" required>
                    </div>
                </div>

                <div class="field">
                    <label class="label">Data de Nascimento</label>
                    <div class="control">
                        <input class="input" type="date" name="birthdate" value="{{user.birthdate}}" required>
                    </div>
                </div>
                
                <hr>
                <p class="is-size-6 has-text-grey mb-3">
                    Preencha os campos abaixo apenas se desejar alterar a sua senha.
                </p>

                <div class="field">
                    <label class="label">Nova Senha</label>
                    <div class="control">
                        <input class="input" type="password" name="password" placeholder="Deixar em branco para não alterar">
                    </div>
                </div>

                <div class="field is-grouped mt-5">
                    <div class="control">
                        <button type="submit" class="button is-info">
                            Salvar Alterações
                        </button>
                    </div>
                    <div class="control">
                        <a href="/dashboard" class="button is-light">Voltar ao Dashboard</a>
                    </div>
                </div>
            </form>
        </div>
    </div>
</div>
