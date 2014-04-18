import cla_dendrite

class neuron():
	def __init__(self,pos):
		self.active = False
		self.predicted = False
		self.position = pos
		self.dendritsegment = cla_dendrite.dendrit_segment(self.position)


class colloum():
	def __init__(self,coll_groesse,Position):
		self.overlap  = 0
		self.active   = False
		self.position = Position
		self.neurons  = []
		self.add_Neurones(coll_groesse,self.neurons)
		self.dendrit_segment = cla_dendrite.dendrit_segment(Position)
		

	def add_Neurones(self,neur_quantity,neurs):
		for x in range(0,neur_quantity):
			pos = (x,) + self.position
			neur = neuron(pos)
			self.neurons.append(neur)
	
	def get_predicted_cells(self):
		predicted_cells = []

		for neuron in self.neurons:
			if neuron.predicted == True :
				predicted_cells.append(neuron)

		return predicted_cells

	def activate_cells(self):
		neurons = self.get_predicted_cells()
		if len(predicted_cells) == 0 :
			for neuron in self.neurons:
				neuron.active = True
		else:
			for neuron in predicted_cells:
				neuron.active    = True
				neuron.predicted = False
		
