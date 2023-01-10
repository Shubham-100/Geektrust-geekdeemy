class Billing:
    ENROLLMENT_FEE = float(500.00)
    PRO_FEE = float(200.00)
    subtotal = float(0.00)
    total = float(0.00)
    coupon_discount = float(0.00)
    apply_g5 = False
    apply_g20 = False
    apply_b4g1 = False
    coupon_applied = ""
    pro_discount = float(0.00)

    programme_costs = {
            "DIPLOMA": 2500,
            "CERTIFICATION": 3000,
            "DEGREE": 5000
    }
  
    pro_discounts = {
        "DIPLOMA": 0.01,
        "CERTIFICATION": 0.02,
        "DEGREE": 0.03
    }

    def __init__(self, programmes, coupon_names, pro):
        self.programmes = programmes
        self.coupon_names = coupon_names
        self.pro = pro

    def get_best_coupon(self):
        # best autoapplied coupon
        total_programmes = sum(self.programmes.values())
        if total_programmes >= 4:
            return "B4G1"

        if "DEAL_G20" in self.coupon_names and self.subtotal >= 10000.00:
            return "DEAL_G20"

        if "DEAL_G5" in self.coupon_names and total_programmes >= 2:
            return "DEAL_G5"

        return None

    def get_subtotal(self):
        diploma = self.programmes["DIPLOMA"] * self.programme_costs["DIPLOMA"]
        certification = self.programmes["CERTIFICATION"] * self.programme_costs["CERTIFICATION"]
        degree = self.programmes["DEGREE"] * self.programme_costs["DEGREE"]
        self.subtotal = diploma + certification + degree
        if self.pro == True:
            self.apply_pro_discount()
            self.subtotal = self.subtotal + self.PRO_FEE - self.pro_discount
            self.total = self.subtotal
            return self.subtotal
        else:
            self.total = self.subtotal
            return self.subtotal

    def get_total(self):
        return self.total

    def get_pro_member_discount(self):
        return self.pro_discount

    def apply_pro_discount(self):
        for programme, quantity in self.programmes.items():
            self.pro_discount += quantity * self.programme_costs[programme] * (self.pro_discounts[programme])

    def calculate_discount(self, coupon_name):
        if coupon_name == "B4G1":
            for programme, quantity in self.programmes.items():
                if quantity > 0:
                    self.coupon_discount = self.programme_costs[programme] * (1 - self.pro_discounts[programme])
                    self.total = self.subtotal - self.coupon_discount
                    return self.coupon_discount
        
        elif coupon_name == "DEAL_G20":
            self.coupon_discount = 0.20 * self.subtotal
            self.total = self.subtotal - self.coupon_discount
            return self.coupon_discount

        elif coupon_name == "DEAL_G5":
            self.coupon_discount = 0.05 * self.subtotal
            self.total = self.subtotal - self.coupon_discount
            return self.coupon_discount

    def get_enrollment_fee(self):
        if self.total < 6666:
            self.total += self.ENROLLMENT_FEE
            return self.ENROLLMENT_FEE
        else:
            return 0.00

    def get_pro_fee(self):
        return self.PRO_FEE if self.pro_discount != 0.00 else 0.00

    def print_bill(self):
        print("SUB_TOTAL %.2f" %self.get_subtotal())
        print("COUPON_DISCOUNT %s %.2f" %(self.get_best_coupon(), self.calculate_discount(self.get_best_coupon()))) if self.get_best_coupon() != None else print("COUPON_DISCOUNT NONE 0.00")
        print("TOTAL_PRO_DISCOUNT %.2f" %self.get_pro_member_discount()) 
        print("PRO_MEMBERSHIP_FEE %.2f" %self.get_pro_fee())
        print("ENROLLMENT_FEE %.2f" %self.get_enrollment_fee()) 
        print("TOTAL %.2f" %self.get_total())


