import os
from flask import Flask

app = Flask(__name__)
@app.route("/")
def home():
    return template("""
	<head>
		<meta charset="utf-8">
		<link rel="stylesheet" href="/static/main.css" />
		<title>Hasarfréttir - VEFÞ2VF05CU Verkefni 3</title>


	</head>
	<body>
		<header class="header">
		<h1></h1>
		<nav><a href="/">Fréttir</a> 
		| <a href="http://jinja.pocoo.org/docs/2.10/">Jinja Templates</a>	|	<a href="https://github.com/vefthroun/vefthroun.github.io/wiki">Bjargir</a>	 |  <a href="/kvikmyndir">Kvikmyndir í Bíó</a> <!-- þessi síða er ekki til ennþá -->
		</nav>
	</header>

		<main>
		<div class="row">
			<section>
				<h1 class="imp">Fellibylurinn "Florence" veldur óreiðu í Flórída</h1>
				<img src="/static/mynd0.jpg">
			</section>
			<section class="top">
				<h3>Hasarfréttir dagsins</h3>
				<ul>			

					<li><a href="/frett1"> Fellibylurinn "Florence" veldur óreiðu í Flórída </a></li>

					<li><a href="/frett2"> Veiðin er dræm þetta haustið </a></li>

					<li><a href="/frett3"> Ólafía stendur sig vel </a></li>

					<li><a href="/frett4"> Ísland dottið úr leik </a></li>

				</ul>
			</section>
		</div>
	</main>

		<footer class="footer">
		<h5>hasarfrettir.is - aðalstræti 1 - 101 reykjavík - hasar@frettir.is</h5>
		<h6>&copy; Copyright 2019 by <a href="https://gjg.github.io/">GJG</a>.
	</footer>    
	</body>
	</html>""")


@app.route("/frett1")
def frett1():
    return """
	<head>

		<meta charset="utf-8">
		<link rel="stylesheet" href="/static/styles.css" />
		<title> Fellibylurinn "Florence" veldur óreiðu á Flórída  - VEFÞ2VF05CU</title>

	</head>
	<body>
		<header class="haus">
		<h1 >VEFÞ2VF05CU</h1>
		<nav><a href="/">Fréttir</a> 
		| <a href="http://jinja.pocoo.org/docs/2.10/">Jinja Templates</a> 
		| <a href="https://github.com/vefthroun/vefthroun.github.io/wiki">Bjargir</a>
		| <a href="/kvikmyndir">Kvikmyndir í Bíó</a> <!-- þessi síða er ekki til ennþá -->
		</nav>
	</header>

		<main>
		<div class="row">
			<section>
				<h1>Fellibylurinn "Florence" veldur óreiðu á Flórída</h1>
				<img src="/static/mynd0.jpg">
			</section>
			<section class="top">
				<p>Það er bara helv... vesen á fellibylnum og allt í klessu í Flórída.  Milljónir manna þurftu að yfirgefa heimili sin vegna yfirvofandi eyðileggingar fellibylsins "Florence"...<p>
				<p>dsg@frettir.is</p>
				<h5><a href="/">Forsíða</a></h5>
			</section>
		</div>
	</main>

		<footer class="footer">
		<h5>hasarfrettir.is - aðalstræti 1 - 101 reykjavík - hasar@frettir.is</h5>
		<h6>&copy; Copyright 2019 by <a href="https://gjg.github.io/">GJG</a>.
	</footer>    
	</body>
	</html>
	"""


@app.route("/frett2")
def frett2():
    return """
	<head>

    <meta charset="utf-8">
    <link rel="stylesheet" href="/static/styles.css" />
    <title> Veiðin er dræm þetta haustið  - VEFÞ2VF05CU</title>

	</head>
	<body>
	    <header class="header">
			<h1 >VEFÞ2VF05CU</h1>
				<nav><a href="/">Fréttir</a> 
					| <a href="http://jinja.pocoo.org/docs/2.10/">Jinja Templates</a> 
					| <a href="https://github.com/vefthroun/vefthroun.github.io/wiki">Bjargir</a>
					| <a href="/kvikmyndir">Kvikmyndir í Bíó</a> <!-- þessi síða er ekki til ennþá -->
				</nav>
		</header>
    <main>
	<div class="row">
		<section>
			<h1>Veiðin er dræm þetta haustið</h1>
			<img src="/static/mynd1.jpg">
		</section>
		<section class="top">
			<p>Veiðin hefur heldur verið döpur þetta haustið þrátt fyrir ágætis rigninar upp á síðkastið...<p>
			<p>est@frettir.is</p>
			<h5><a href="/">Forsíða</a></h5>
		</section>
	</div>
	</main>    
   	<footer class="footer">
		<h5>hasarfrettir.is - aðalstræti 1 - 101 reykjavík - hasar@frettir.is</h5>
		<h6>&copy; Copyright 2019 by <a href="https://gjg.github.io/">GJG</a>.
	</footer>    
	</body>
	</html>
	"""


@app.route("/frett3")
def frett3():
    return """
	<head>
    	<meta charset="utf-8">
    	<link rel="stylesheet" href="/static/styles.css" />
    	<title> Ólafía stendur sig vel  - VEFÞ2VF05CU</title>

	</head>
	<body>
		<header class="header">
			<h1>VEFÞ2VF05CU</h1>
			<nav><a href="/">Fréttir</a> 
				| <a href="http://jinja.pocoo.org/docs/2.10/">Jinja Templates</a> 
				| <a href="https://github.com/vefthroun/vefthroun.github.io/wiki">Bjargir</a>
				| <a href="/kvikmyndir">Kvikmyndir í Bíó</a> <!-- þessi síða er ekki til ennþá -->
			</nav>
		</header>

	<main>
		<div class="row">
			<section>
				<h1>Ólafía stendur sig vel</h1>
				<img src="/static/mynd2.jpg">
			</section>
			<section class="top">
				<p>Ólafía er komin í 65 sæti peningalistans og hefur því tryggt sér keppnisrétt á LPG mótaröðinni á komandi keppnistimabili...<p>
				<p>htg@frettir.is</p>
				<h5><a href="/">Forsíða</a></h5>
			</section>
		</div>
	</main>

    <footer class="footer">
		<h5>hasarfrettir.is - aðalstræti 1 - 101 reykjavík - hasar@frettir.is</h5>
		<h6>&copy; Copyright 2019 by <a href="https://gjg.github.io/">GJG</a>.
	</footer>   
	"""


@app.route("/frett4")
def frett4():
    return """
	<head>
    <meta charset="utf-8">
    <link rel="stylesheet" href="/static/styles.css" />
    <title> Ísland dottið úr leik  - VEFÞ2VF05CU</title>

	</head>
	<body>
    	<header class="header">
		<h1> VEFÞ2VF05CU </h1>
			<nav><a href="/">Fréttir</a> 
				| <a href="http://jinja.pocoo.org/docs/2.10/">Jinja Templates</a> 
				| <a href="https://github.com/vefthroun/vefthroun.github.io/wiki">Bjargir</a>
				| <a href="/kvikmyndir">Kvikmyndir í Bíó</a> <!-- þessi síða er ekki til ennþá -->
			</nav>
		</header>
    <main>
		<div class="row">
			<section>
				<h1>Ísland dottið úr leik</h1>
				<img src="/static/mynd3.jpg">
			</section>
			<section class="top">
				<p>Íslenska karlalandsliðið í körfubolta er dottið úr leik a Eurobasket þrátt fyrir ágætis spretti inn a milli.  Ísland spilaði lokaleik sinn á mótinu fyrir troðfullri höll gegn heimamönnum Finnum..<p>
				<p>dsg@frettir.is</p>
				<h5><a href="/">Forsíða</a></h5>
			</section>
		</div>
	</main>
    <footer class="footer">
		<h5>hasarfrettir.is - aðalstræti 1 - 101 reykjavík - hasar@frettir.is</h5>
		<h6>&copy; Copyright 2019 by <a href="https://gjg.github.io/">GJG</a>.
	</footer>   
	"""


@app.errorhandler(404)
def page_not_found(e):
    return """<h1>Error 404, vefsíða ekki fundin eða ekki til.</h1>""", 404


if __name__ == "__main__":
    #    app.run(debug=True, use_reloader=True)
    app.run()