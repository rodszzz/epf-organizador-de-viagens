% rebase('layout.tpl', title='Buscar Voos')

<section class="section">
    <div class="columns is-centered">
        <div class="column is-two-thirds">
            <div class="box">
                <h1 class="title has-text-centered">Para onde vamos? 🌎</h1>
                <p class="subtitle has-text-centered">Preencha os campos para encontrar a sua próxima viagem.</p>
                <hr>

                <form action="/search" method="post">
                    <div class="field is-horizontal">
                        <div class="field-body">
                            <div class="field">
                                <label class="label">Origem (Código IATA)</label>
                                <div class="control has-icons-left">
                                    <input class="input is-medium" type="text" name="departure_id" placeholder="Ex: BSB, GRU" required>
                                    <span class="icon is-small is-left">🛫</span>
                                </div>
                            </div>
                            <div class="field">
                                <label class="label">Destino (Código IATA)</label>
                                <div class="control has-icons-left">
                                    <input class="input is-medium" type="text" name="arrival_id" placeholder="Ex: MIA, LIS" required>
                                    <span class="icon is-small is-left">🛬</span>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="field is-horizontal">
                        <div class="field-body">
                            <div class="field">
                                <label class="label">Data de Ida</label>
                                <div class="control">
                                    <input class="input is-medium" type="date" name="outbound_date" required>
                                </div>
                            </div>
                            <div class="field">
                                <label class="label">Data de Volta</label>
                                <div class="control">
                                    <input class="input is-medium" type="date" name="return_date" required>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <div class="field" style="margin-top: 2rem;">
                        <div class="control">
                            <button type="submit" class="button is-info is-fullwidth is-medium is-focused">
                                Buscar Voos
                            </button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
</section>