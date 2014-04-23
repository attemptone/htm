import cla_dendrite
import cla_region

class neuron():
    def __init__(self, pos):
        self.active = False
        self.predicted = False
        self.position = pos
        self.dendrit_segment = cla_dendrite.dendrit_segment(self.position)
        self.activate_dendrite_segment()

    def check_overlap(self, Input):
        self.dendrit_segment.get_overlap(Input)

    def is_active(self):
        if self.active == True:
            return True
        else:
            return False

    def activate_dendrite_segment(self):
        region_max = cla_region.region.max_groesse
        anzahl_neuronen = cla_region.region.coll_groesse
        self.dendrit_segment.initialize_distrale_dendriten(region_max,anzahl_neuronen)

class colloum():
    def __init__(self, coll_groesse, Position):
        self.active = False
        self.position = Position
        self.neurons = []
        self.add_Neurones(coll_groesse, self.neurons)
        self.dendrit_segment = cla_dendrite.dendrit_segment(Position)

    # add neurones and gives them a position
    def add_Neurones(self, neur_quantity, neurs):
        for x in range(0, neur_quantity):
            pos = (x,) + self.position
            neur = neuron(pos)
            self.neurons.append(neur)

    # returns a list of the cells which are in the "predicted"-state
    def get_predicted_cells(self):
        predicted_cells = []
        for neuron in self.neurons:
            if neuron.predicted == True:
                predicted_cells.append(neuron)
        return predicted_cells

    # activates cells based on ther prediction-state
    def activate_cells(self):
        predicted_cells = self.get_predicted_cells()
        if len(predicted_cells) == 0:
            for neuron in self.neurons:
                neuron.active = True
        else:
            for neuron in predicted_cells:
                neuron.active = True
                neuron.predicted = False
		
