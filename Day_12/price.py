def CumulativeDiscount(arr , n):

    disc_price = 100
    
    for discount in arr:
        disc_price = disc_price * (100 - discount) / 100

    disc = 100 - (disc_price * 100 / 100)

    return disc
