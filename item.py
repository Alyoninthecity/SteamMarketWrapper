class Item:
    def __init__(self, name, sell_price, N_sell, order_price, N_orders, URLImg, percGuad, guadagno):
        self.name = name  # nome
        self.order_price = order_price
        self.N_sell = N_sell
        self.N_orders = N_orders
        self.sell_price = sell_price  # prezzo piu` basso
        self.URLImg = URLImg  # URL immagine
        self.guadagno = guadagno
        self.percGuad = percGuad

    def __str__(self):
        return "nome: " + self.name + " N. pezzi in vendita: " + self.sell_listings + " Prezzo piu` basso:  " + + " URL immagine" + self.URLImg

    def dump(self):
        return {
            "Item": {
                'name': self.name, 'sell_price': self.sell_price, 'N_sell': self.N_sell, 'order_price': self.order_price, 'N_orders': self.N_orders, 'URLImg': self.URLImg, 'percGuad': self.percGuad, 'guadagno': self.guadagno
            }
        }
