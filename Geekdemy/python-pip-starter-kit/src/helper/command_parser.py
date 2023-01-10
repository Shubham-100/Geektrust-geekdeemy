# # Utility class to parse the entered commands
#  DIPLOMA - Rs 2500 
#  CERTIFICATION - Rs.3000 
#  DEGREE - Rs. 5000 

#subtotal = total pgm cost - pro member discount
# total = subtotal - coupon discount
#coupon discount is applied after applying pro mebership discount
# The B4G1 coupon gets auto applied when there are more than 4 programmes in the cart. 
# B4G1 coupon to be given priority
#  If 2 or more coupons are applied, the higher value coupon needs to be considered

#Pro discount
#  DIPLOMA - 1% discount 
#  CERTIFICATION - 2% discount 
#  DEGREE - 3% discount

#coupon
# B4G1 - if 4 or more pgm purchased - lowest priced program is given free
# DEAL_G20 - purchase value >= 10,000, 20% discount
# DEAL_G5 - if pgm purchaed >= 2, then 5% discount


#Enrollment fees of 500 if purchased cost < 6666, checked and applied after the discount

from src.billing import billing

class Parser:
    @staticmethod
    def commandParser(file_path):
        programmes = {
            "DIPLOMA": 0,
            "CERTIFICATION": 0,
            "DEGREE": 0
        }
        coupon_names = []
        pro = False

        f = open(file_path, 'r')
        lines = f.readlines()

        for line in lines:
            tokens = line.split()
            if tokens[0] == "ADD_PROGRAMME":
                pgm_name = tokens[1]
                pgm_qty = int(tokens[2])
                programmes[pgm_name] += pgm_qty

            elif tokens[0] == "APPLY_COUPON":
                coupon_names.append(tokens[1])

            elif tokens[0] == "ADD_PRO_MEMBERSHIP":
                pro = True
                
            elif tokens[0] == "PRINT_BILL":
                bill = billing.Billing(programmes, coupon_names, pro)
                bill.print_bill()
