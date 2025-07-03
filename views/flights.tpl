<h1>Ofertas Ida &amp; Volta</h1>

% if offers:
  % for o in offers:
    <div class="offer">
      <div class="logos">
        <img src="{{o['ida'].airline_logo}}" alt="Logo Ida">
        <img src="{{o['volta'].airline_logo}}" alt="Logo Volta">
      </div>
      <p><strong>Preço total:</strong> R$ {{o['total_price']}}</p>
      <p><strong>Duração total:</strong> {{o['total_duration']}} min</p>

      <h3>Ida</h3>
      <ul>
        % for leg in o['ida'].legs:
          <li>{{leg.departure_airport_code}} {{leg.departure_time}} → {{leg.arrival_airport_code}} {{leg.arrival_time}} ({{leg.airline}} {{leg.flight_number}})</li>
        % end
      </ul>

      <h3>Volta</h3>
      <ul>
        % for leg in o['volta'].legs:
          <li>{{leg.departure_airport_code}} {{leg.departure_time}} → {{leg.arrival_airport_code}} {{leg.arrival_time}} ({{leg.airline}} {{leg.flight_number}})</li>
        % end
      </ul>

      <form action="/flights/book" method="post">
        <input type="hidden" name="offer_idx" value="{{o['idx']}}">
        <button type="submit">Reservar Ida &amp; Volta</button>
      </form>
    </div>
    <hr>
  % end
% else:
  <p>Nenhuma oferta disponível.</p>
% end
