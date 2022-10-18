from jinja2 import Environment, FileSystemLoader
#Quin template utilitzem
enviroment = Environment(loader=FileSystemLoader("Template/"))
template = enviroment.get_template("laMevaWeb.html")



#Variable que passem al template
info = {"joc":[
    {"titol": "Llista de jocs"},
       {"name": "World of WarCraft: Wrath of the Lich King"},
]}

#Generem el contingut final
contingut = template.render(info)
#Fitxer final on apliquem les dades i agafem la bade de html
file = open("lamevawebfinal.html","w")
#Escrivim el contingut a un fitxer html
file.write(contingut)