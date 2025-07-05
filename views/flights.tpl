%# views/flights.tpl

<h1>Ofertas de Ida &amp; Volta</h1>

% if offers:
  % for o in offers:
    <div class="offer-card" style="border:1px solid #ccc; padding:16px; margin-bottom:24px; border-radius:8px;">

      <!-- Cabeçalho: logos + preço/duração -->
      <header style="display:flex; justify-content:space-between; align-items:center;">
        <div>
          <img src="{{o['ida'].airline_logo}}" alt="Logo Ida" style="height:32px; margin-right:8px;">
          <img src="{{o['volta'].airline_logo}}" alt="Logo Volta" style="height:32px;">
        </div>
        <div style="text-align:right;">
          <div style="font-size:1.25em; font-weight:bold;">R$ {{o['total_price']}}</div>
          <div style="color:#555;">Duração total: {{o['total_duration_hm']}}</div>
        </div>
      </header>

      <!-- Seção Ida -->
      <section style="margin-top:16px;">
        <h3>Ida ({{o['ida'].total_duration_hm}})</h3>
        <table style="width:100%; border-collapse:collapse;">
          <thead>
            <tr style="background:#f5f5f5;">
              <th style="padding:8px; border:1px solid #ddd;">Origem</th>
              <th style="padding:8px; border:1px solid #ddd;">Partida</th>
              <th style="padding:8px; border:1px solid #ddd;">Destino</th>
              <th style="padding:8px; border:1px solid #ddd;">Chegada</th>
              <th style="padding:8px; border:1px solid #ddd;">Companhia</th>
              <th style="padding:8px; border:1px solid #ddd;">Duração</th>
            </tr>
          </thead>
          <tbody>
            % for leg in o['ida'].legs:
            <tr>
              <td style="padding:8px; border:1px solid #ddd;">{{leg.departure_airport_code}}</td>
              <td style="padding:8px; border:1px solid #ddd;">{{leg.departure_time}}</td>
              <td style="padding:8px; border:1px solid #ddd;">{{leg.arrival_airport_code}}</td>
              <td style="padding:8px; border:1px solid #ddd;">{{leg.arrival_time}}</td>
              <td style="padding:8px; border:1px solid #ddd;">{{leg.airline}} {{leg.flight_number}}</td>
              <td style="padding:8px; border:1px solid #ddd;">{{leg.duration_hm}}</td>
            </tr>
            % end
          </tbody>
        </table>
      </section>

      <!-- Seção Volta -->
      <section style="margin-top:16px;">
        <h3>Volta ({{o['volta'].total_duration_hm}})</h3>
        <table style="width:100%; border-collapse:collapse;">
          <thead>
            <tr style="background:#f5f5f5;">
              <th style="padding:8px; border:1px solid #ddd;">Origem</th>
              <th style="padding:8px; border:1px solid #ddd;">Partida</th>
              <th style="padding:8px; border:1px solid #ddd;">Destino</th>
              <th style="padding:8px; border:1px solid #ddd;">Chegada</th>
              <th style="padding:8px; border:1px solid #ddd;">Companhia</th>
              <th style="padding:8px; border:1px solid #ddd;">Duração</th>
            </tr>
          </thead>
          <tbody>
            % for leg in o['volta'].legs:
            <tr>
              <td style="padding:8px; border:1px solid #ddd;">{{leg.departure_airport_code}}</td>
              <td style="padding:8px; border:1px solid #ddd;">{{leg.departure_time}}</td>
              <td style="padding:8px; border:1px solid #ddd;">{{leg.arrival_airport_code}}</td>
              <td style="padding:8px; border:1px solid #ddd;">{{leg.arrival_time}}</td>
              <td style="padding:8px; border:1px solid #ddd;">{{leg.airline}} {{leg.flight_number}}</td>
              <td style="padding:8px; border:1px solid #ddd;">{{leg.duration_hm}}</td>
            </tr>
            % end
          </tbody>
        </table>
      </section>

      <!-- Botão de Reserva (temporariamente removido o deep-link) -->
      <div style="margin-top:16px; text-align:right;">
        <button
          style="padding:8px 16px; border:none; border-radius:4px; background:#0078D4; color:white; cursor:not-allowed;"
          disabled>
          Reservar Ida &amp; Volta
        </button>
      </div>

    </div>
    <hr>
  % end
% else:
  <p>Nenhuma oferta disponível.</p>
% end
