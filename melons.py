"""This file should have our order classes in it."""

class AbstractMelonOrder(object):
    """Base melon orders."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False


    def get_total(self):
        """Calculate price."""

        base_price = 5
        
        if self.species == "Christmas":
            base_price = base_price * 1.5

        
        if self.order_type == 'international' and self.qty < 10:
            total = (1 + self.tax) * self.qty * base_price + 3
        else: 
            total = (1 + self.tax) * self.qty * base_price
        
        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True


class GovernmentMelonOrder(AbstractMelonOrder):
    """Government order, non taxable and requires security inspection."""
    order_type = 'government'
    tax = 0

    # def __init__(self, species, qty):

    #     self.passed_inspection = False

    def mark_inspection(self, passed):
        """Set passed inspection to true."""

        self.passed_inspection = passed


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""
    order_type = 'domestic'
    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    order_type = 'international'
    tax = 0.17

    def __init__(self, country_code):
        super(InternationalMelonOrder, self).__init__(species, qty)
        """Initialize melon order attributes."""

        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code







