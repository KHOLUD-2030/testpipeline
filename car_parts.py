class CarParts:
    def __init__(self):
        self.parts = ['engine', 'wheels', 'brakes', 'seats', 'steering wheel']

    def get_parts(self):
        return self.parts

    def add_part(self, part):
        if part not in self.parts:
            self.parts.append(part)
            return True
        return False

    def remove_part(self, part):
        if part in self.parts:
            self.parts.remove(part)
            return True
        return False

if __name__ == "__main__":
    car = CarParts()
    print(car.get_parts())
