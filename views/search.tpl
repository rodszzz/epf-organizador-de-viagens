%# views/search.tpl

<h1>Buscar Voos</h1>

<form action="/search" method="post">
  <label>
    Origem (IATA):
    <input type="text" name="departure_id" required placeholder="ex: GRU">
  </label><br><br>

  <label>
    Destino (IATA):
    <input type="text" name="arrival_id" required placeholder="ex: JFK">
  </label><br><br>

  <label>
    Data de Ida:
    <input type="date" name="outbound_date" required>
  </label><br><br>

  <label>
    Data de Volta:
    <input type="date" name="return_date" required>
  </label><br><br>

  <button type="submit">Pesquisar</button>
</form>
