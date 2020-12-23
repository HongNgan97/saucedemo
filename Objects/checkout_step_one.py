class CheckoutStepOne:
    def __init__(self, firstname, lastname, postalcode):
        self.firstname = firstname
        self.lastname = lastname
        self.postalcode = postalcode

    def __str__(self):
        return '{"firstname":"%s", "lastname": "%s","postalcode":"%s"' % (self.firstname, self.lastname, self.postalcode)
