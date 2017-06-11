from __future__ import print_function

class LogicGate(object):
    def __init__(self, label):
        self.label = label
        self.output = None

    def get_label(self):
        return self.label

    def get_output(self):
        # Powerful idea in OOP.
        self.output = self.perform_gate_logic()
        return self.output


class BinaryGate(LogicGate):
    def __init__(self, label):
        super(BinaryGate, self).__init__(label)
        self.pinA = None
        self.pinB = None

    def get_pinA(self):
        if self.pinA == None:
            return int(input(
                'Enter Pin A input for gate {}: '
                .format(self.get_label())))
        else:
            return self.pinA.get_from().get_output()

    def get_pinB(self):
        if self.pinB == None:
            return int(input(
                'Enter Pin B input for gate {}: '
                .format(self.get_label())))
        else:
            return self.pinB.get_from().get_output()

    def set_next_pin(self, source):
        if self.pinA == None:
            self.pinA = source
        elif self.pinB == None:
            self.pinB = source
        else:
            raise RunTimeError('No empty pins.')


class UnaryGate(LogicGate):
    def __init__(self, label):
        super(UnaryGate, self).__init__(label)
        self.pin = None

    def get_pin(self):
        if self.pin == None:
            return int(input(
                'Enter Pin input for gate {}: '
                .format(self.get_label())))
        else:
            return self.pin.get_from().get_output()

    def set_next_pin(self, source):
        if self.pin == None:
            self.pin = source
        else:
            raise RunTimeError('Not empty pin.')


class AndGate(BinaryGate):
    def __init__(self, label):
        super(AndGate, self).__init__(label)

    def perform_gate_logic(self):
        a = self.get_pinA()
        b = self.get_pinB()
        if (a == 1) and (b == 1):
            return 1
        else:
            return 0


class OrGate(BinaryGate):
    def __init__(self, label):
        super(OrGate, self).__init__(label)

    def perform_gate_logic(self):
        a = self.get_pinA()
        b = self.get_pinB()
        if (a == 1) or (b == 1):
            return 1
        else:
            return 0


class NotGate(UnaryGate):
    def __init__(self, label):
        super(NotGate, self).__init__(label)

    def perform_gate_logic(self):
        p = self.get_pin()
        if p == 1:
            return 0
        else:
            return 1


class Connector():
    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate
        tgate.set_next_pin(self)

    def get_from(self):
        return self.fromgate

    def get_to(self):
        return self.togate

