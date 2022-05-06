"""
12. Now extend that circuit and implement an 8-bit full adder.
"""

class LogicGate:

    def __init__(self,n):
        self.name = n
        self.output = None

    def get_label(self):
        return self.name

    def get_output(self):
        self.output = self.perform_gate_logic()
        return self.output


class BinaryGate(LogicGate):

    def __init__(self,n):
        LogicGate.__init__(self,n)

        self.pin_a = None
        self.pin_b = None

    def get_pin_a(self):
        if self.pin_a == None:
            return int(input("Enter Pin A input for gate "+self.get_label()+"-->"))
        else:
            return self.pin_a.get_from().get_output()

    def get_pin_b(self):
        if self.pin_b == None:
            return int(input("Enter Pin B input for gate "+self.get_label()+"-->"))
        else:
            return self.pin_b.get_from().get_output()

    def set_next_pin(self,source):
        if self.pin_a == None:
            self.pin_a = source
        else:
            if self.pin_b == None:
                self.pin_b = source
            else:
                print("Cannot Connect: NO EMPTY PINS on this gate")


class AndGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def perform_gate_logic(self):

        a = self.get_pin_a()
        b = self.get_pin_b()
        if a==1 and b==1:
            return 1
        else:
            return 0

class OrGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def perform_gate_logic(self):

        a = self.get_pin_a()
        b = self.get_pin_b()
        if a ==1 or b==1:
            return 1
        else:
            return 0

class UnaryGate(LogicGate):

    def __init__(self,n):
        LogicGate.__init__(self,n)

        self.pin = None

    def get_pin(self):
        if self.pin == None:
            return int(input("Enter Pin input for gate "+self.get_label()+"-->"))
        else:
            return self.pin.get_from().get_output()

    def set_next_pin(self,source):
        if self.pin == None:
            self.pin = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")


class NotGate(UnaryGate):

    def __init__(self,n):
        UnaryGate.__init__(self,n)

    def perform_gate_logic(self):
        if self.get_pin():
            return 0
        else:
            return 1


class NorGate(OrGate):
        
    def perform_gate_logic(self):
        output = super().perform_gate_logic()
        if output == 1:
            return 0
        else:
            return 1
            
            
class NandGate(AndGate):
        
    def perform_gate_logic(self):
        output = super().perform_gate_logic()
        if output == 1:
            return 0
        else:
            return 1   

class XorGate(BinaryGate):

    def __init__(self, n):
        BinaryGate.__init__(self, n)
        
    def perform_gate_logic(self):
        
        a = self.get_pin_a()
        b = self.get_pin_b()

        if (a == 1 and b == 1) or (a == 0 and b == 0):
            return 0
        else:
            return 1    
        

class Connector:

    def __init__(self, fgate, tgate):
        self.from_gate = fgate
        self.to_gate = tgate

        tgate.set_next_pin(self)

    def get_from(self):
        return self.from_gate

    def get_to(self):
        return self.to_gate



def main():
    
    # Implement Half Adder Circuit
    x1 = XorGate("X1")
    g1 = AndGate("G1")

    sum_output = x1.get_output()
    carry_output = g1.get_output()

    print(f"S: {sum_output}")
    print(f"C: {carry_output}")


main()