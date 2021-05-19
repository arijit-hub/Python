class item:
    def __init__(self , qty , price , dis):
        self.qty = qty
        self.price = price
        self.dis = dis


def MoneySaved(list):

    disc_price = 0.0
    for each_item in list:
        disc_price = disc_price + (each_item.qty * each_item.price * each_item.dis / 100)

    return disc_price


a = item(10 , 50.00  , 25.50)
b = item(8 , 23.15 , 36.00)
c = item(1 , 90.50 , 45.12)

print(MoneySaved([a , b , c]))