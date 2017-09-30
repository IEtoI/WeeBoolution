from pygame.tests import image__save_gl_surface_test


class Environment:

    def __init__(self):
        self.despcription = "ParentClass of environment"


class Tree(Environment):
    """
    This is the tree class. Not sure were to actually put the img in here?
    Can we just declare them somewhere?
    """

    def __init__(self, x, y, age, hp, wood, spawn):
        self.x = x
        self.y = y
        self.age = age
        self.hp = hp
        self.wood = wood
        self.img = img
        self.spawn = spawn
        self.description = "Tree class. Tree is spawning growing and then dying."

    @age.setter
    def set_age(self, age):
        """
        Ok here the age should be updated for each tick
        I'm not sure how to implement it atm xD
        But in the end age should be updated each itereation of the game
        """
        age += FPSCLOCK.time()
        self.age = age

    @img.setter
    def set_img(self, img):
        self.img = img

    """
    should this be a seperate class ? I mean everything needs to be checked if alive
    """
    def alive(self, hp):
        if hp > 0:
            return True

    def spawn(self, x, y, age):
        """
        ok if the age is above a certain threshold the tree might spawn a new tree in its
        surroundings.
        """
        if age > ...:
        return True

    def simulation(self, ):
        alive(hp)
        set_age(age)
        set_img(img)
        if spawn:
            spawn

