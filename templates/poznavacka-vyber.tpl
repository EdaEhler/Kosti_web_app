<!DOCTYPE html>
<html>
<body>

<h1>Poznávačka kostí</h1>

<p>Zde si můžete vyzkoušet vaše znalosti a schopnosti poznat jednotlivé kosti z naší databáze podle fotek. Níže si zvolte, jestli chcete přímo psát názvy kostí k zobrazeným fotkám, nebo chcete vybírat názvy kostí z několika předložených možností. Možné jsou varianty testu s českým, tak i s latinským názvosloví.</p>

<br>

<form action="/poznavacka-volba" method="POST">
  <input type="radio" id="latinsky_psat" name="poznavacka_typ" value="latinsky_psat">
  <label for="latinsky_psat">Psát latinsky názvy kostí</label><br>
  
  <input type="radio" id="cesky_psat" name="poznavacka_typ" value="cesky_psat" checked="checked">
  <label for="cesky_psat">Psát česky názvy kostí</label><br>
  
  <input type="radio" id="latinsky_vybrat" name="poznavacka_typ" value="latinsky_vybrat">
  <label for="latinsky_vybrat">Vybrat latinský název kosti</label><br>
  
  <input type="radio" id="cesky_vybrat" name="poznavacka_typ" value="cesky_vybrat">
  <label for="cesky_vybrat">Vybrat český název kosti</label><br>
  
  <br>
  <input type="submit" value="Submit">
</form>

<br>
<p>Vrátit se <a href="/index">zpět na hlavní stránku</a>.</p>

</body>
</html>
