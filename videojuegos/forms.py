from django import forms
from .models import Videojuego


class VideojuegoForm(forms.ModelForm):
    class Meta:
        model = Videojuego
        fields = '__all__'
        labels = {
            'nombre': 'Nombre del videojuego',
            'stock': 'Stock (unidades disponibles)',
            'consola': 'Consola / Plataforma',
            'Estado': 'Estado del producto',
            'ano': 'Año de lanzamiento',
            'PEGI': 'Clasificación PEGI',
            'descripcion': 'Descripción',
            'precio': 'Precio',
            'imagen': 'Imagen',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'nombre': 'Ej: Minecraft',
            'stock': 'Ej: 15',
            'consola': 'Ej: PlayStation 5',
            'Estado': 'Ej: Nuevo',
            'ano': 'Ej: 2020',
            'PEGI': 'Ej: +13',
            'descripcion': 'Describe el videojuego aquí...',
            'precio': 'Ej: 29.000',
        }
        ayudas = {
            'nombre': 'Escribe el título del juego tal como aparece en su portada. Sirve para encontrarlo fácilmente en el catálogo.',
            'stock': 'Cantidad de unidades que hay para vender. Escribe solo números, sin puntos ni espacios.',
            'consola': 'La plataforma donde se juega. Ejemplos: PlayStation 5, Xbox Series X, Nintendo Switch, PC.',
            'Estado': 'En qué condición está el producto. Opciones: Nuevo, Como Nuevo, Poco Usado, Usado.',
            'ano': 'Año en que salió a la venta. Solo 4 números, por ejemplo: 2020.',
            'PEGI': 'Clasificación de edad recomendada. Ejemplos: +3, +7, +12, +16, +18.',
            'descripcion': 'Cuenta brevemente de qué trata el juego, su modo de juego o por qué vale la pena. Entre 1 y 3 frases está bien.',
            'precio': 'Precio de venta en pesos chilenos, con punto para separar los miles. Ejemplo: 29.000',
            'imagen': 'Opcional. Elige una imagen guardada en tu computador (JPG o PNG) y se subirá sola. Si no subes ninguna, el juego se mostrará con una imagen por defecto.',
        }
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if field_name in placeholders:
                field.widget.attrs['placeholder'] = placeholders[field_name]
            if field_name in ayudas:
                field.help_text = ayudas[field_name]