% rebase('layout.tpl', title='Ofertas de Voo')

<style>
    /* Estilos para melhorar a aparência da página de voos */
    .flight-offer {
        border: 1px solid #dbdbdb;
        border-radius: 8px;
        margin-bottom: 1.5rem;
        padding: 1.5rem;
        box-shadow: 0 4px 8px rgba(0,0,0,0.05);
        transition: box-shadow 0.3s ease-in-out;
    }
    .flight-offer:hover {
        box-shadow: 0 8px 16px rgba(0,0,0,0.1);
    }
    .flight-leg {
        padding-bottom: 1rem;
        margin-bottom: 1rem;
    }
    .flight-leg:not(:last-child) {
        border-bottom: 1px dashed #dbdbdb;
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
    .summary-footer {
        border-top: 2px solid #333;
        margin-top: 1.5rem;
        padding-top: 1rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
</style>

<div class="container">
    <h1 class="title">Ofertas de Voos Disponíveis</h1>

    % if not offers:
        <div class="notification is-warning">
            Nenhuma oferta de voo encontrada. Por favor, faça uma nova busca.
            <a href="/search">Voltar à busca</a>
        </div>
    % else:
        % for offer in offers:
            <div class="flight-offer">
                <div class="columns">
                    <div class="column">
                        <h3 class="subtitle is-4">✈️ Ida</h3>
                        % for leg in offer['ida'].legs:
                            <div class="flight-leg">
                                <p><span class="has-text-weight-bold">De:</span> {{leg.departure_airport_name}} ({{leg.departure_airport_code}})</p>
                                <p><span class="has-text-weight-bold">Para:</span> {{leg.arrival_airport_name}} ({{leg.arrival_airport_code}})</p>
                                <p><span class="has-text-weight-bold">Companhia:</span> {{leg.airline}}</p>
                                <p><span class="has-text-weight-bold">Duração:</span> {{leg.duration_hm}}</p>
                            </div>
                        % end
                        <p class="has-text-weight-bold">Preço Ida: R$ {{offer['ida'].price}}</p>
                    </div>

                    <div class="column">
                        <h3 class="subtitle is-4">↩️ Volta</h3>
                        % for leg in offer['volta'].legs:
                            <div class="flight-leg">
                                <p><span class="has-text-weight-bold">De:</span> {{leg.departure_airport_name}} ({{leg.departure_airport_code}})</p>
                                <p><span class="has-text-weight-bold">Para:</span> {{leg.arrival_airport_name}} ({{leg.arrival_airport_code}})</p>
                                <p><span class="has-text-weight-bold">Companhia:</span> {{leg.airline}}</p>
                                <p><span class="has-text-weight-bold">Duração:</span> {{leg.duration_hm}}</p>
                            </div>
                        % end
                        <p class="has-text-weight-bold">Preço Volta: R$ {{offer['volta'].price}}</p>
                    </div>
                </div>

                <div class="summary-footer">
                    <div>
                        <h4 class="title is-4">Total: R$ {{offer['total_price']}}</h4>
                        <p>Duração total: {{offer['total_duration_hm']}}</p>
                    </div>
                    <div>
                        <a href="/flights/book?offer_idx={{offer['idx']}}" class="button is-primary is-large">
                            Reservar Ida e Volta
                        </a>
                    </div>
                </div>
            </div>
        % end
    % end
</div>