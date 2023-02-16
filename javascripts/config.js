function login()
{
    var password = prompt( "Veuillez entrer le mot de passe pour accéder à cette page", "" );
    // si un mot de passe a été entré
    if ( password != null )
    {
    	// on le compare à celui attendu
    	if ( hex_md5( password ) == "b96cfb81257b023c7fe5f87029bacc33" )
    	{
    	    // on construit un nom de page à partir du mot de passe et on l'ouvre
    	    document.location.href = password + ".html";
        }
        else
        {
            alert( "Mot de passe incorrecte!", "Erreur" );
        }
    }
}

app.location$.subscribe(function() {
  var tables = document.querySelectorAll("article table")
  tables.forEach(function(table) {
    new Tablesort(table)
  })
})

window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"]],
    displayMath: [["\\[", "\\]"]],
    processEscapes: true,
    processEnvironments: true
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex"
  }
}



