<h1>Minhas Viagens</h1>
% if trips:
  <ul>
  % for t in trips:
    <li>
      {{t.direction}} — preço: R$ {{t.price}} — duração: {{t.duration}} min
      <ul>
        % for leg in t.legs:
          <li>{{leg.dep_code}} {{leg.dep_time}} → {{leg.arr_code}} {{leg.arr_time}} ({{leg.airline}} {{leg.flight_number}})</li>
        % end
      </ul>
    </li>
  % end
  </ul>
% else:
  <p>Você ainda não selecionou nenhuma passagem.</p>
% end
