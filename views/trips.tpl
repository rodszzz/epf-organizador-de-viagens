% rebase('layout.tpl', title='Minhas Viagens')

<style>
    .trip-card {
        border: 1px solid #dbdbdb;
        border-radius: 8px;
        margin-bottom: 1.5rem;
        padding: 1.5rem;
        box-shadow: 0 4px 8px rgba(0,0,0,0.05);
    }
    .trip-header {
        border-bottom: 2px solid #333;
        padding-bottom: 1rem;
        margin-bottom: 1rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .trip-leg {
        margin-bottom: 1rem;
    }
    .columns {
        display: flex;
        justify-content: space-between;
    }
    .column {
        flex: 1;
        padding: 0 1rem;
    }
    .has-text-weight-bold {
        font-weight: bold;
    }
    .mt-2 {
        margin-top: 0.5rem;
    }
</style>

<div class="container">
    <h1 class="title">Minhas Viagens Reservadas</h1>

    % if not trips:
        <div class="notification is-info">
            Você ainda não reservou nenhuma viagem.
            <a href="/search">Encontre a sua próxima aventura!</a>
        </div>
    % else:
        % for i, trip in enumerate(trips):
            <div class="trip-card">
                <div class="trip-header">
                    <div>
                        <h3 class="title is-4">Preço Total: R$ {{trip['preco_total']}}</h3>
                        <p class="subtitle is-6">Duração Total da Viagem: {{trip['duracao_total_viagem']}}</p>
                    </div>
                    <div>
                        <a href="/trips/delete/{{i}}" class="button is-danger" onclick="return confirm('Tem a certeza que quer apagar esta viagem?');">
                            Apagar Viagem
                        </a>
                    </div>
                </div>

                <div class="columns">
                    <div class="column">
                        <h4 class="title is-5">✈️ Ida</h4>
                        <div class="trip-leg">
                            <p><span class="has-text-weight-bold">De:</span> {{trip['ida']['partida']}}</p>
                            <p><span class="has-text-weight-bold">Para:</span> {{trip['ida']['chegada']}}</p>
                            <p><span class="has-text-weight-bold">Duração:</span> {{trip['ida']['duracao_total']}}</p>
                            <p><span class="has-text-weight-bold">Preço:</span> R$ {{trip['ida']['preco']}}</p>
                            <a href="https://www.google.com/flights#flights-booking-step?t={{trip['ida']['booking_token']}}" target="_blank" class="button is-link is-small mt-2">Reservar Ida</a>
                        </div>
                    </div>

                    <div class="column">
                        <h4 class="title is-5">↩️ Volta</h4>
                        <div class="trip-leg">
                            <p><span class="has-text-weight-bold">De:</span> {{trip['volta']['partida']}}</p>
                            <p><span class="has-text-weight-bold">Para:</span> {{trip['volta']['chegada']}}</p>
                            <p><span class="has-text-weight-bold">Duração:</span> {{trip['volta']['duracao_total']}}</p>
                            <p><span class="has-text-weight-bold">Preço:</span> R$ {{trip['volta']['preco']}}</p>
                            <a href="https://www.google.com/flights#flights-booking-step?t={{trip['volta']['booking_token']}}" target="_blank" class="button is-link is-small mt-2">Reservar Volta</a>
                        </div>
                    </div>
                </div>
            </div>
        % end
    % end
</div>