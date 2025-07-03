<h1>Buscar Voos</h1>
<form action="/search" method="post">
  <label>Origem (código IATA):<br>
    <input type="text" name="departure_id" required>
  </label><br><br>

  <label>Destino (código IATA):<br>
    <input type="text" name="arrival_id" required>
  </label><br><br>

  <label>Data de Ida:<br>
    <input type="date" name="outbound_date" required>
  </label><br><br>

  <label>Data de Volta:<br>
    <input type="date" name="return_date" required>
  </label><br><br>

  <button type="submit">Buscar</button>
</form>
