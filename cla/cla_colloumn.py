import cla_dendrite

class neuron():
	def __init__(self,pos):
		self.active = False
		self.predic = False
		self.position = pos
		self.dendritsegment = cla_dendrite.dendritsegment(self.position)


class colloum():
	def __init__(self,coll_groesse,Position):
		self.overlap  = 0
		self.active   = False
		self.position = Position
		self.neurons  = []
		self.add_Neurones(coll_groesse,self.neurons)
		self.dendrit_segment = cla_dendrite.dendritsegment(Position)
		

	def add_Neurones(self,neur_quantity,neurs):
		for x in range(0,neur_quantity):
			pos = (x,) + self.position
			neur = neuron(pos)
			self.neurons.append(neur)
