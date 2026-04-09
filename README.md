# Asistene Turistico Inteligente
1. ¿Que APIs se usaron?  
Nuetra aplicacion consume 3 APIs diferentes. Para el clima se ocupo la api de `OPENWEATHER`, esta require loguearse en la pagina para poder obtener una API Key. En el caso de las imagenes se hizo uso de la API de `UNSPLASH`, de igual forma requiere una API Key. La API que se uso para obtener los datos fincaniceron no requiere de ninguna API key, su implementacion es mas facil. 

2. ¿Que datos obtuvieron?  
En todas las APIs las respuestas que nos devolvian son Json, lo cual es facil manipular.  
Cabe decir que no todos los datos se ocupan para la aplicacion, necesitamos solo ciertos datos, por lo cual 
se hizo que retornara lo necesario, por ejemplo para el clima devolvemos un diccionario con claves como
**ciudad, pais, temperatura, sensacion, etc**

3. ¿Como integraron la informacion?  
Relacionamos todas las APIs mediante el estado ingresada por el usuario y generamos una recomendación basada en clima y tipo de cambio

4. ¿Que dificultades encontraron?
Las dificultades que se encontraron fueron en consumir las APIs y saber que metodos ocupara para hacer las
consultas

5. ¿Como utilizaron la ia para el desarrollo?
Se utilizo la ia para saber como consultas las APIs, para hacer el archivo integrador y para genera el
index.html