import os
from flask import Flask, render_template

app = Flask(__name__)

CATEGORIAS = [
    {
        "titulo": "Cocina y Alimentación",
        "descripcion": "Protección para motores, resistencias térmicas y sistemas electrónicos de cocina.",
        "equipos": [
            {
                "id": "neveras",
                "nombre": "Neveras y Congeladores",
                "imagen": "https://images.unsplash.com/photo-1571175443880-49e1d25b2bc5?auto=format&fit=crop&w=800&q=80",
                "alerta": "Alta sensibilidad a bajones de luz y picos de tensión.",
                "problematica": "El compresor o motor puede trancarse o quemarse si la luz regresa inmediatamente después de un corte de energía.",
                "solucion": "Desconectar de inmediato al ocurrir la falla eléctrica. Esperar de 5 a 10 minutos tras el retorno del servicio.",
                "sintoma_clave": "calienta-mucho, no-enciende, humo-olor"
            },
            {
                "id": "cafeteras",
                "nombre": "Cafeteras",
                "imagen": "https://images.unsplash.com/photo-1565452344518-47faca79dc69?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8Y2FmZXRlcmF8ZW58MHx8MHx8fDA%3D",
                "alerta": "Sensibilidad en la resistencia de calentamiento y bombas de agua.",
                "problematica": "Las variaciones bruscas de energía dañan las tarjetas de control y queman el elemento calefactor.",
                "solucion": "Desenchufar cuando esté fuera de uso o no haya energía eléctrica.",
                "sintoma_clave": "no-enciende, humo-olor"
            },
            {
                "id": "tostadoras",
                "nombre": "Tostadoras de Pan",
                "imagen": "https://plus.unsplash.com/premium_photo-1719452894874-3da9fa3b882c?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3",
                "alerta": "Alto consumo instantáneo y desgaste del electroimán.",
                "problematica": "Los bajones de luz impiden que el electroimán retenga la palanca hacia abajo y desgastan las resistencias.",
                "solucion": "Evitar usarla durante variaciones bruscas de energía. Desenchufar cuando esté fuera de uso.",
                "sintoma_clave": "no-enciende, humo-olor"
            },
            {
                "id": "freidoras_aire",
                "nombre": "Freidoras de Aire (Air Fryers)",
                "imagen": "https://plus.unsplash.com/premium_photo-1711684803379-f45ffd226412?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTd8fGZyZWlkb3JhcyUyMGRlJTIwYWlyZXxlbnwwfHwwfHx8MA%3D%3D",
                "alerta": "Consumo elevado de energía y vulnerabilidad en paneles táctiles.",
                "problematica": "Requieren alto amperaje constante; los cortes repentinos desprograman la tarjeta digital de control y queman térmicos.",
                "solucion": "Evitar encenderla al mismo tiempo que otros aparatos de alta potencia (como la plancha). Desconectar apenas termine.",
                "sintoma_clave": "no-enciende, humo-olor"
            },
            {
                "id": "procesadores",
                "nombre": "Procesadores de Alimentos y Picadoras",
                "imagen": "https://images.unsplash.com/photo-1570222094114-d054a817e56b?auto=format&fit=crop&w=800&q=80",
                "alerta": "Vulnerabilidad en fusibles térmicos del motor.",
                "problematica": "Las caídas de voltaje reducen las revoluciones del motor al procesar cargas pesadas, activando o quemando protecciones.",
                "solucion": "Trabajar en pulsos cortos y no saturar el tazón. Desconectar inmediatamente ante un bajón de electricidad.",
                "sintoma_clave": "no-enciende"
            },
            {
                "id": "ollas_arroceras",
                "nombre": "Ollas Arroceras y Multiusos",
                "imagen": "https://images.unsplash.com/photo-1599182345361-9542815e73f6?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0",
                "alerta": "Riesgo de interrupción en ciclos de presión.",
                "problematica": "Un corte de luz durante la cocción a presión interrumpe los sensores de temperatura y los picos de voltaje queman tarjetas.",
                "solucion": "Conectarlas a tomas de corriente estables o supresores de picos. Si ocurre un apagón, esperar a que regrese la luz.",
                "sintoma_clave": "calienta-mucho, no-enciende"
            },
            {
                "id": "hornos_microondas",
                "nombre": "Hornos Microondas",
                "imagen": "https://media.istockphoto.com/id/182915079/es/foto/horno-de-microondas.webp?a=1&b=1&s=612x612&w=0&k=20&c=_KRg0on4EaHw7RBgnETyOkSanyT3Rh2xlwm3bF4Qjpc=",
                "alerta": "Vulnerabilidad en fusibles de alto voltaje, magnetrón y tarjetas digitales.",
                "problematica": "Las fluctuaciones bruscas de energía pueden quemar el fusible interno de alto voltaje o alterar la tarjeta electrónica, dejando el equipo inoperativo o impidiendo que genere calor.",
                "solucion": "Desconectar de inmediato tras un corte de luz. Usar un protector de voltaje especial para grandes electrodomésticos antes de volver a encenderlo.",
                "sintoma_clave": "enciende-pero-no-calienta, no-enciende, chispas, olor-a-quemado"
            },
            {
                "id": "waffleras",
                "nombre": "Waffleras y Sanducheras",
                "imagen": "https://images.unsplash.com/photo-1713164394509-79e8c579c860?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0",
                "alerta": "Consumo térmico continuo sin botón de apagado.",
                "problematica": "Al no tener interruptor de encendido/apagado directo, la reconexión súbita del servicio sobrecalienta las placas.",
                "solucion": "Desconectar del tomacorriente una vez finalizada su utilización o ante cualquier fallo del suministro.",
                "sintoma_clave": "calienta-mucho, no-enciende, chispas"
            },
            {
                "id": "cocinas_electricas",
                "nombre": "Cocinas y Hornos Eléctricos",
                "imagen": "https://images.unsplash.com/photo-1556911220-e15b29be8c8f?auto=format&fit=crop&w=800&q=80",
                "alerta": "Alto consumo de energía y riesgo de cortocircuito.",
                "problematica": "Las hornillas y resistencias reciben arcos eléctricos al restablecerse la luz, dañando selectores de potencia.",
                "solucion": "Girar todas las perillas a la posición de apagado ('Off') mientras no haya servicio eléctrico. Conectar únicamente al usarse.",
                "sintoma_clave": "no-enciende, humo-olor"
            },
            {
                "id": "licuadoras",
                "nombre": "Licuadoras y Pequeños Electrodomésticos",
                "imagen": "https://plus.unsplash.com/premium_photo-1718043036199-d98bef36af46?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8bGljdWFkb3Jhc3xlbnwwfHwwfHx8MA%3D%3D",
                "alerta": "Sensibilidad en botones y carbones del motor.",
                "problematica": "Arranques involuntarios si quedaron encendidas o choques de corriente en el rotor.",
                "solucion": "Mantener siempre desenchufadas mientras no estén en uso directo. Revisar que los botones estén en posición nula.",
                "sintoma_clave": "no-enciende, ruido"
            },
            {
                "id": "batidoras",
                "nombre": "Batidoras (de Vaso y Mano)",
                "imagen": "https://media.istockphoto.com/id/1792891860/es/foto/mujer-sosteniendo-de-la-mano-y-mostrando-una-nueva-licuadora-de-inmersi%C3%B3n-fondo-de-mesa-azul.webp?a=1&b=1&s=612x612&w=0&k=20&c=04xudbOzcrYPmfQq3pwRHgwK45n-EqMeoKBOv0aaLzc=",
                "alerta": "Riesgo de sobrecalentamiento del motor por bajo voltaje.",
                "problematica": "Si el voltaje baja, el motor realiza más esfuerzo técnico elevando la temperatura de los bobinados.",
                "solucion": "Desconectar al detectar fluctuaciones y evitar usos prolongados en mezclas densas.",
                "sintoma_clave": "calienta-mucho, no-enciende, ruido"
            }
        ]
    },
    {
        "titulo": "Entretenimiento y Tecnología",
        "descripcion": "Cuidado de tarjetas madres, chips de video, conectividad y sistemas de almacenamiento.",
        "equipos": [
            {
                "id": "consolas_ps",
                "nombre": "Consolas PlayStation (PS3, PS4, PS5)",
                "imagen": "https://images.unsplash.com/photo-1606813907291-d86efa9b94db?auto=format&fit=crop&w=800&q=80",
                "alerta": "Alto riesgo de corrupción del sistema de archivos y daño en la fuente interna.",
                "problematica": "Un apagón repentino durante la lectura/escritura de datos altera el almacenamiento (disco duro/SSD) y la fuente.",
                "solucion": "Conectar siempre a un regulador de voltaje o UPS (que dé tiempo de apagar la consola desde el menú). Nunca desenchufar bruscamente.",
                "sintoma_clave": "calienta-mucho, no-enciende, ruido"
            },
            {
                "id": "cargadores_telefono",
                "nombre": "Cargadores de Teléfono y Adaptadores USB",
                "imagen": "https://images.unsplash.com/photo-1583863788434-e58a36330cf0?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0",
                "alerta": "Daño directo en transformadores internos de corriente continua.",
                "problematica": "Los sobrevoltajes repentinos destruyen los condensadores y circuitos integrados miniaturizados del cargador, pudiendo afectar la batería del teléfono conectado.",
                "solucion": "Desenchufar los cargadores de la pared cuando no estén en uso o mientras la energía eléctrica permanezca inestable.",
                "sintoma_clave": "no-carga, calienta-demasiado, chispas, olor-a-plástico-quemado"
            },
            {
                "id": "camaras_seguridad",
                "nombre": "Cámaras de Seguridad e IP",
                "imagen": "https://images.unsplash.com/photo-1549109926-58f039549485?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8Y2FtYXJhcyUyMGRlJTIwc2VndXJpZGFkfGVufDB8fDB8fHww",
                "alerta": "Sensibilidad extrema en fuentes de alimentación y tarjetas lógicas.",
                "problematica": "Los cortes repentinos de energía y retornos bruscos desconfiguran el firmware del dispositivo o queman los adaptadores de corriente de 12V.",
                "solucion": "Alimentar el sistema mediante un sistema UPS o reguladores de voltaje para garantizar un flujo eléctrico continuo y limpio.",
                "sintoma_clave": "pierde-conexion, no-enciende, visión-nocturna-falla, reinicios-constantes"
            },    
            {
                "id": "nintendo_switch",
                "nombre": "Nintendo Switch y Consolas Portátiles",
                "imagen": "https://images.unsplash.com/photo-1578303512597-81e6cc155b3e?auto=format&fit=crop&w=800&q=80",
                "alerta": "Sensibilidad en el Dock de carga y adaptadores de corriente alternativos.",
                "problematica": "La consola en modo Dock recibe variaciones de voltaje directas que queman el chip M92T36 (encargado del encendido).",
                "solucion": "Utilizar únicamente el cargador original. Desconectar la base Dock del tomacorriente durante tormentas o variaciones.",
                "sintoma_clave": "calienta-mucho, no-enciende, ruido"
            },
            {
                "id": "modems",
                "nombre": "Módems, Routers y Decodificadores",
                "imagen": "https://images.unsplash.com/photo-1606904825846-647eb07f5be2?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0",
                "alerta": "Vulnerabilidad continua por estar conectados las 24 horas.",
                "problematica": "Cortes de energía continuos desconfiguran las memorias Flash de los firmware e inician sobretensiones por transformadores.",
                "solucion": "Conectar la fuente de alimentación a una toma con supresor de picos o adquirir un Mini UPS de 12V especializado.",
                "sintoma_clave": "calienta-mucho, no retiene carga"
            },
            {
                "id": "televisores",
                "nombre": "Televisores y Equipos Smart",
                "imagen": "https://images.unsplash.com/photo-1593784991095-a205069470b6?auto=format&fit=crop&w=800&q=80",
                "alerta": "Sensibilidad extrema en tarjetas lógicas y paneles LED/OLED.",
                "problematica": "Picos de voltaje y variaciones bruscas queman la tarjeta principal (MainBoard) y la fuente de poder.",
                "solucion": "Conectar a un regulador de voltaje. En tormentas eléctricas, desconectar también el cable de antena o red.",
                "sintoma_clave": "no-enciende"
            },
            {
                "id": "sonido",
                "nombre": "Equipos de Sonido y Amplificadores",
                "imagen": "https://images.unsplash.com/photo-1545454675-3531b543be5d?auto=format&fit=crop&w=800&q=80",
                "alerta": "Daño en transformadores de entrada y salidas de audio.",
                "problematica": "Sobretensiones que queman los fusibles internos o destruyen los transistores de potencia.",
                "solucion": "Usar regletas con supresor de picos certificado. Desconectar los cables de la toma de pared tras la interrupción.",
                "sintoma_clave": "calienta-mucho, no-enciende, ruido"
            },
            {
                "id": "computadoras",
                "nombre": "Computadoras de Mesa y Laptops",
                "imagen": "https://images.unsplash.com/photo-1566647387313-9fda80664848?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTZ8fGNvbXB1dGFkb3Jhc3xlbnwwfHwwfHx8MA%3D%3D",
                "alerta": "Pérdida de datos, daño en la fuente de poder y tarjeta madre.",
                "problematica": "Cortes repentinos corrompen el sistema operativo y sobretensiones queman la fuente de alimentación (PSU).",
                "solucion": "Usar un regulador de voltaje o un sistema UPS. Para laptops, desenchufar el cargador cuando esté apagada.",
                "sintoma_clave": "calienta-mucho, no-enciende, ruido"
            },
            {
                "id": "telefonos",
                "nombre": "Teléfonos Celulares y Tablets",
                "imagen": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?auto=format&fit=crop&w=800&q=80",
                "alerta": "Degradación del cargador y la batería.",
                "problematica": "Flujos de voltaje inestables destruyen los circuitos integrados de carga del dispositivo o el adaptador.",
                "solucion": "No dejar los celulares cargando durante tormentas o cortes eléctricos. Utilizar cargadores originales y protectores.",
                "sintoma_clave": "calienta-mucho, no-enciende, no retiene carga"
            },
            {
                "id": "impresoras",
                "nombre": "Impresoras y Multifuncionales",
                "imagen": "https://images.unsplash.com/photo-1612815154858-60aa4c59eaa6?auto=format&fit=crop&w=800&q=80",
                "alerta": "Riesgo en la fuente de alimentación externa/interna y cabezales.",
                "problematica": "Los cortes repentinos interrumpen el ciclo de reposo del cabezal secando la tinta. Los picos de tensión dañan la placa.",
                "solucion": "Conectar a un multicontacto con supresor de picos o regulador. Al apagarla, usar siempre el botón de encendido.",
                "sintoma_clave": "no-enciende"
            }
        ]
    },
    {
        "titulo": "Climatización, Lavado y Hogar",
        "descripcion": "Protección para motores inductivos de alto consumo y sistemas de agua.",
        "equipos": [
            {
                "id": "ventiladores",
                "nombre": "Ventiladores",
                "imagen": "https://images.unsplash.com/photo-1618941716939-553df3c6c278?auto=format&fit=crop&w=800&q=80",
                "alerta": "Riesgo de sobrecalentamiento del bobinado.",
                "problematica": "Si el suministro eléctrico regresa con bajo voltaje, el motor intenta girar pero no obtiene suficiente fuerza, quemándose.",
                "solucion": "Apagar o desenchufar el equipo durante los cortes de energía. Al retornar la electricidad, verificar que la fuerza sea regular.",
                "sintoma_clave": "no-enciende, ruido"
            },
            {
                "id": "calentadores_agua",
                "nombre": "Calentadores de Agua (Termotanques y Calentadores Eléctricos)",
                "imagen": "https://media.istockphoto.com/id/1294344007/es/foto/la-mano-femenina-pone-el-termostato-del-calentador-de-agua-el%C3%A9ctrico-en-modo-econ%C3%B3mico.webp?a=1&b=1&s=612x612&w=0&k=20&c=HMQorGXfaXrsp1ItduTm9rBoeslGLFP3lv-LlGgqL5w=",
                "alerta": "Alto consumo de potencia y sobrecalentamiento en resistencias térmicas.",
                "problematica": "Los picos o bajas de tensión al restablecerse el servicio eléctrico pueden fundir las resistencias eléctricas internas o averiar los termostatos de control.",
                "solucion": "Mantenerlos apagados o desconectados durante interrupciones eléctricas. Volver a conectar únicamente cuando la red eléctrica esté estable.",
                "sintoma_clave": "no-calienta, agua-sale-tibia, dispara-breaker, olor-a-quemado"
            },
            {
                "id": "hidroyets",
                "nombre": "Hidroyets (Hidrolavadoras de Alta Presión)",
                "imagen": "https://images.unsplash.com/photo-1520340356584-f9917d1eea6f?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0",
                "alerta": "Sensibilidad en el motor eléctrico de alta demanda y sellos de presión.",
                "problematica": "Operar con baja tensión o caídas de voltaje reduce la fuerza del motor, haciendo que se recaliente rápidamente hasta quemar los devanados del motor.",
                "solucion": "Evitar su uso cuando se detecten bajones de luz y desconectarla del tomacorriente inmediatamente al cortar la corriente.",
                "sintoma_clave": "pierde-fuerza, huele-a-quemado, no-enciende, ruidos-extraños"
            },
            {
                "id": "aires_acondicionados",
                "nombre": "Aires Acondicionados",
                "imagen": "https://media.istockphoto.com/id/2233478240/es/foto/aire-acondicionado-moderno-montado-en-la-pared-para-la-refrigeraci%C3%B3n-y-el-confort-del-hogar.webp?a=1&b=1&s=612x612&w=0&k=20&c=SFNHQVXJcYw1dhDHwiV_P7vl-8QPeAAoe9B-CgKgl34=",
                "alerta": "Daño crítico en la tarjeta electrónica y el compresor.",
                "problematica": "Las variaciones bruscas de corriente destruyen los capacitores de arranque y la placa lógica de control.",
                "solucion": "Instalar protectores integrados o breques diferenciales. Apagar el interruptor de energía durante apagones prolongados.",
                "sintoma_clave": "calienta-mucho, no-enciende, humo-olor, ruido"
            },
            {
                "id": "lavadoras",
                "nombre": "Lavadoras y Secadoras",
                "imagen": "https://images.unsplash.com/photo-1610557892470-55d9e80c0bce?auto=format&fit=crop&w=800&q=80",
                "alerta": "Pérdida de ciclo de programación y fallas de placa.",
                "problematica": "Los picos eléctricos reinician repentinamente las placas digitales durante ciclos de centrifugado o llenado.",
                "solucion": "Desconectar la toma principal al interrumpirse el servicio. Dejar drenar el agua si quedó detenida para evitar esfuerzo de bomba.",
                "sintoma_clave": "no-enciende, ruido"
            },
            {
                "id": "quitapelusas",
                "nombre": "Quitapelusas Eléctricos",
                "imagen": "https://media.istockphoto.com/id/2290647694/es/foto/manos-usando-quitapelusas-de-bater%C3%ADa-en-el-jersey-marr%C3%B3n-afeitando-el-vello-y-las-bolitas-para.webp?a=1&b=1&s=612x612&w=0&k=20&c=6O9WdfsOcpQJKKG2ugN9m1ziiN1BO7PtLEQqCEuNbmQ=",
                "alerta": "Sensibilidad en motorcitos de DC y circuitos de carga.",
                "problematica": "Una baja tensión durante la recarga de batería o el uso directo conectado causa sobrecalentamiento del pequeño motor de corte.",
                "solucion": "No mantenerlos conectados a la toma de corriente si hay variaciones de energía y cargarlos utilizando reguladores.",
                "sintoma_clave": "pierde-velocidad, no-enciende, no-retiene-carga, calienta-al-usar, no retiene carga"
            },
            {
                "id": "humidificadores",
                "nombre": "Humidificadores Ultrasónicos",
            "imagen": "https://images.unsplash.com/photo-1768471569643-717e823b5f9a?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8aHVtaWZpY2Fkb3Jlc3xlbnwwfHwwfHx8MA%3D%3D",
            "alerta": "Vulnerabilidad en la placa ultrasónica y placa electrónica principal.",
            "problematica": "Los picos eléctricos queman el transductor piezoeléctrico o la fuente interna de alimentación, haciendo que el equipo encienda pero no genere vapor.",
            "solucion": "Desconectar la unidad cuando no esté en uso o ante fluctuaciones en el fluido eléctrico.",
            "sintoma_clave": "no-sale-vapor, no-enciende, ruido-extraño, luz-parpadea, no retiene carga"
            },
            {
            "id": "lamparas_hogar",
            "nombre": "Lámparas Eléctricas y Bombillos LED",
            "imagen": "https://images.unsplash.com/photo-1507473885765-e6ed057f782c?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0",
            "alerta": "Alta sensibilidad en transformadores y controladores LED (drivers).",
            "problematica": "Las variaciones continuas de voltaje degradan los microchips de los bombillos LED y queman los balastros o drivers internos de las lámparas.",
            "solucion": "Apagar los interruptores de luz durante los cortes de corriente y utilizar regletas con protección contra sobretensiones para lámparas de mesa.",
            "sintoma_clave": "parpadea, baja-intensidad, no-enciende, chispas"
            }
        ]
    },
    {
        "titulo": "Cuidado Personal",
        "descripcion": "Prevención en herramientas eléctricas de uso personal.",
        "equipos": [
            {
                "id": "planchas_ropa",
                "nombre": "Planchas de Ropa (Vapor y Secas)",
                "imagen": "https://plus.unsplash.com/premium_photo-1678218591263-e9f4126efe9c?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0",
                "alerta": "Alto consumo eléctrico y riesgo en la resistencia térmica.",
                "problematica": "Al ser aparatos de altísimo consumo, encenderlas durante caídas de voltaje puede disparar los breakers principales.",
                "solucion": "Desconectar inmediatamente ante cualquier bajón o corte de energía. Evitar usarlas al mismo tiempo que otros artefactos altos.",
                "sintoma_clave": "calienta-mucho, no-enciende, humo-olor"
            },
            {
                "id": "secadores_cabello",
                "nombre": "Secadores y Planchas de Cabello",
                "imagen": "https://media.istockphoto.com/id/1199272696/es/foto/diferentes-herramientas-electr%C3%B3nicas-para-el-peinado-del-cabello.webp?a=1&b=1&s=612x612&w=0&k=20&c=EDHLgeFxLvcSljZagjwGpVIwiHDVDnJjLfL-6T0DALw=",
                "alerta": "Vulnerabilidad en fusibles térmicos y resistencia eléctrica.",
                "problematica": "Un bajón de luz reduce la velocidad del motor del ventilador interno mientras la resistencia sigue encendida, derritiendo el plástico.",
                "solucion": "Apagar y desenchufar al detectar variaciones de luz. Esperar estabilidad antes de moldear el cabello.",
                "sintoma_clave": "calienta-mucho, no-enciende, chispas"
            },
            {
                "id": "afeitadoras",
                "nombre": "Afeitadoras y Cortadoras de Cabello",
                "imagen": "https://images.unsplash.com/photo-1599351431613-18ef1fdd27e1?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0",
                "alerta": "Sensibilidad en transformadores de carga y baterías de litio.",
                "problematica": "Picos de voltaje dañan el cargador externo o sobrecalientan las celdas de litio durante la carga.",
                "solucion": "Cargar preferiblemente mediante un regulador de voltaje o desconectar de la toma cuando no estén cargando.",
                "sintoma_clave": "no-enciende, chispas"
            },
            {
                "id": "maquinas_coser",
                "nombre": "Máquinas de Coser (Mecánicas y Electrónicas)",
                "imagen": "https://plus.unsplash.com/premium_photo-1664195857816-ec8f3ed30e36?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0",
                "alerta": "Sensibilidad en placas digitales de bordado y motores de pedal.",
                "problematica": "Las bajones de luz descalibran la velocidad del motor en máquinas tradicionales. En modelos digitales, bloquean la memoria.",
                "solucion": "Usar protector de voltaje o regulador. Desconectar el pedal y el cable de corriente inmediatamente al interrumpirse la luz.",
                "sintoma_clave": "no-enciende, ruido"
            }
        ]
    }
]

@app.route('/')
def inicio():
    return render_template('index.html', categorias=CATEGORIAS)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
