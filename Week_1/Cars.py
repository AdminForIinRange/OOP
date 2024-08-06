class Cars:
    def __init__(self, make, modal, color):
        self.make = make
        self.modal = modal
        self.color = color

    def display_information(self):
        print("Make:", self.make, "\nModel:", 
              self.modal, "\nColor:", self.color)

carOne = Cars("Hyundai", "i30 N", "White")

carOne.display_information()

