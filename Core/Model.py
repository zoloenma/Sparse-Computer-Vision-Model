class Model:
    def __init__(self, grabber, counter, repository):
        self.grabber = grabber 
        self.counter = counter 
        self.repository = repository 

    def Run(self):
        image = self.grabber.GetImage()
        peopleCount = self.counter.CountPeople(image)
        self.repository.SavePeopleCount(peopleCount)