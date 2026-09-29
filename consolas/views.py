from django.shortcuts import render


data = {"mando-xbox360": {

                            "nombre": "Mando de Xbox 360 Original",
                            "stock": 12,
                            "color": "Negro",
                            "Estado": "Nuevo",
                            "ano": 2005,
                            "pilas":"2",
                            "descripcion": "Mando clásico, compatible con PC para tus emuladores o juegos de Steam, tambien puedes jugar en la consola origial",
                            "precio":"69.000",
                            "imagen":"images/consolas/xbox360.png"
                            },

            "nintendo-switch-oled": {
                            "nombre": "Nintendo Switch Oled",
                            "stock": 6,
                            "color": "Blanco",
                            "Estado": "Nuevo",
                            "ano": 2021,
                            "pilas":"no",
                            "controles":"2",
                            "descripcion": "Consola Familiar de nintendo, penultima generacion de consolas, 2 mandos",
                            "precio":"349.000",
                            "imagen":"images/consolas/nintendo_switch.png"
                            },
            "gameboy-sp": {
                            "nombre": "Nintendo GameBoy Advance SP Pikachu Edition",
                            "stock": 4,
                            "color": "amarillo",
                            "Estado": "Como Nuevo",
                            "ano": 2003,
                            "pilas":"no",
                            "descripcion": "Consola de nintendo, una joya de consola,creada al inicio de 2003, es una edicion especial de pokémon",
                            "precio":"199.000",
                            "imagen":"images/consolas/gameboy-pika.jpg"
                            },
            "play3-slim": {
                           "nombre": "Play Station 3 Slim",
                           "stock": 7,
                           "color": "Negra",
                           "ano": 2009,
                           "Estado": "Poco Usado",
                           "pilas":"no",
                           "controles":"2",
                           "descripcion": "Consola de gamer clasico, 2 mandos, puedes jugar muchos juegos FPS, singleplayer",
                           "precio":"149.000",
                           "imagen":"images/consolas/ps3_slim.png"
                           },
            "virtual-boy": {
                           "nombre": "Virtual Boy",
                           "stock": 6,
                           "color": "Rojo",
                           "Estado": "Como Nuevo",
                           "ano": "1995",
                           "pilas":"6",
                           "controles":"2",
                           "descripcion": "consola muy retro y de nicho de nintendo, como VR pero rojos, no puedes moverte con la cabeza, si no con el control",
                           "precio":"899.000",
                           "imagen":"images/consolas/virtual_boy.png"
                           },
            "play5-d": {
                           "nombre": "Play Station 5 Digital",
                           "stock": 9,
                           "color": "Blanco",
                           "Estado": "Nuevo",
                           "ano": "2020",
                           "pilas":"no",
                           "controles":"2",
                           "descripcion": "Consola competitiva para gamers que buscan disfrutar a tope los juegos por sus graficos,",
                           "precio":"649.000",
                           "imagen":"images/consolas/ps5.png"
                           },
            "mando-sega": {
                            "nombre": "Mando SEGA Genesis",
                            "stock": 2,
                            "color": "negro",
                            "Estado": "Como Nuevo",
                            "ano": "1988",
                            "pilas":"no",
                            "controles":"2",
                            "descripcion": "Consola Familiar de Sega, joya retro, pefecta si eres collecionista, 2 mandos",
                            "precio":"49.000",
                            "imagen":"images/consolas/genesis.png"
                            },
            "mando-play3": {
                            "nombre": "Mando Play Station 3 Original",
                            "stock": 4,
                            "color": "Negro",
                            "Estado": "Nuevo",
                            "ano": "2006",
                            "pilas":"no",
                            "descripcion": "mando para jugar en la play station 3, original, nuevo",
                            "precio":"19.000",
                            "imagen":"images/consolas/ps3.jpg"                            
                            },
            "xbox-classic": {
                            "nombre": "Xbox Classic",
                            "stock": 1,
                            "color": "Negro",
                            "Estado": "Como Nuevo",
                            "ano": "2001",
                            "pilas":"no",
                            "descripcion": "Consola retro, primera consola de microsoft, xbox clasica",
                            "precio":"199.000",
                            "imagen":"images/consolas/xbox_classic.png"
                            },
            }

def consolas(request):
    return render(request,"consolas/consolas.html", {"productos": data})

def detalle_consola(request, hardware_id):
    # Extraemos solo la información de la consola a la que le hicieron clic
    producto_seleccionado = data.get(hardware_id)
    
    # Mandamos esa información a un nuevo archivo HTML llamado detalle.html
    return render(request, "consolas/detalle.html", {"producto": producto_seleccionado})