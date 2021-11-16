# web applikace Kosti
# závislosti:  pandas, bottle

import pandas as pd
from bottle import route, request, template, run, TEMPLATE_PATH, static_file


# PROMĚNNÉ #
############
# přidat directory s templatema do cesty
TEMPLATE_PATH.append("./templates/")

kosti = pd.read_csv("kosti_tabulka.csv", sep=";", index_col="id")


# FUNKCE #
##########

@route("/")
@route("/index")
@route("/index.htm")
@route("/index.html")
def index(kosti=kosti):
    # generuj hlavní stránku

    # linky pro kosti lebky
    lebka_links = ""
    for kost in kosti[kosti["topo1"] == "lebka"].itertuples():
        lebka_links += "<a href='/kosti/{0}'>{1} - {2}</a><br>".format(kost.Index, kost.name_cz, kost.name_lat)

    trup_links = ""
    for kost in kosti[kosti["topo1"] == "osový skelet"].itertuples():
        trup_links += "<a href='/kosti/{0}'>{1} - {2}</a><br>".format(kost.Index, kost.name_cz, kost.name_lat)

    horni_k_links = ""
    for kost in kosti[kosti["topo1"] == "kostra horní končetiny"].itertuples():
        horni_k_links += "<a href='/kosti/{0}'>{1} - {2}</a><br>".format(kost.Index, kost.name_cz, kost.name_lat)

    dolni_k_links = ""
    for kost in kosti[kosti["topo1"] == "kostra dolní končetiny"].itertuples():
        dolni_k_links += "<a href='/kosti/{0}'>{1} - {2}</a><br>".format(kost.Index, kost.name_cz, kost.name_lat)

    # vracím template ./templates/index.tpl
    return template("index", lebka_links=lebka_links,
                             trup_links=trup_links,
                             horni_k_links=horni_k_links,
                             dolni_k_links=dolni_k_links)


@route("/poznavacka-vyber")
@route("/poznavacka-vyber.htm")
@route("/poznavacka-vyber.html")
def poznavacka_index():

    # vracím template ./templates/poznavacka-vyber.tpl
    return template("poznavacka-vyber")


@route("/poznavacka-volba", method="POST")  # /poznavacka-volba definované přímo v templatu ve forms
def poznavacka_index_do():
    # funkce, která obsluhuje forms, vyběr typu poznávačky,
    # v templatu ./templates/poznavacka-vyber.tpl
    vyber = request.forms.get("poznavacka_typ")

    return vyber


@route("/kosti/<kost>")
def kosti_detail(kost=""):
    # příprava na template s popisem kosti

    return template("kosti-detail", cesky=kosti.loc[kost].name_cz,
                                    latinsky=kosti.loc[kost].name_lat,
                                    obrazek=kosti.loc[kost].pics)


# obsloužení všech static souborů, v html templátech na ně budu odkazovat takto:
# <link rel='stylesheet' type='text/css' href='/static/css/style.css'>
# ale funguje to i v tagu <img src="/static/pics/DSCN9788kresize.jpg">
# https://stackoverflow.com/questions/10486224/bottle-static-files
@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static/')


@route("/pic")
def obrazekXXX():
    return static_file("DSCN9788kresize.jpg", root="static/pics/")


@route("/test")
def test():
    return template("test")


if __name__ == "__main__":
    print(TEMPLATE_PATH)
    run(reloader=True, debug=True)  # pozor na RELOADER, v ostrém nasazení vypnout
