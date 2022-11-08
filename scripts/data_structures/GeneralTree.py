import time


# 1. Demo of the tree structure of file systems
class Node1:
    def __init__(self, item):
        self.node = item
        self.children = []
        self.parent = None
    
    # child is also an instance of this class.
    def addChild(self, child):
        child.parent = self
        self.children.append(child)
    
    def level(self):
        level = 0
        parent = self.parent
        while parent:
            level += 1
            parent = parent.parent
        return level
    
    def display(self):
        prefix = (' ' * self.level() * 3) + "|__" if self.parent else ""
        print(prefix + self.node)
        if self.children:
            for child in self.children:
                child.display()

# Implementing "1".
def ComputerDrive():
    root = Node1('   /')
    
    applications = Node1('Applications')
    applications.addChild(Node1('Anaconda-Navigator.app'))
    applications.addChild(Node1('Visual Studio Code.app'))
    applications.addChild(Node1('Postman.app'))
    applications.addChild(Node1('Spotify.app'))
    
    users = Node1('Users')
    users.addChild(Node1('shared'))
    users.addChild(Node1('ifunanyascript'))
    
    system = Node1('System')
    system.addChild(Node1('Developer'))
    system.addChild(Node1('DriverKit'))
    system.addChild(Node1('iOSSupport'))
    
    library = Node1('Library')
    library.addChild(Node1('Apple'))
    library.addChild(Node1('Application Support'))
    library.addChild(Node1('Filesystems'))
    library.addChild(Node1('GPUBundles'))
    library.addChild(Node1('OSAnalytics'))
    
    root.addChild(applications)
    root.addChild(users)
    root.addChild(system)
    root.addChild(library)
    
    return root



# 2. Demo of hierachy in the Nigerian Arm of Gov't
import time
class Node2:
    def __init__(self, item, tag):
        self.node = item
        self.tag = tag
        self.children = []
        self.parent = None
    
    # child is also an instance of this class.
    def addChild(self, child):
        child.parent = self
        self.children.append(child)
    
    def level(self):
        level = 0
        parent = self.parent
        while parent:
            level += 1
            parent = parent.parent
        return level
    
    def display(self, arg):
        if arg == "name":
            field = self.node
        elif arg == "tag":
            field = self.tag
        else:
            field = self.node + f"({self.tag})"
        
        prefix = (' ' * self.level() * 3) + "|__" if self.parent else ""
        print(prefix + field)
        if self.children:
            for child in self.children:
                time.sleep(0.5)
                child.display(arg)

# Implementing "2".
def ArmOfGovernment():
    root = Node2('Nigeria', 'Naija')
    
    executive = Node2('Executive', 'EX')
    executive.addChild(Node2('Muhammadu Buhari', 'President'))
    executive.addChild(Node2('Yemi Osinbajo', 'Vice President'))
    executive.addChild(Node2('Boss Mustapha', 'Secretary to the Govt'))
    
    legislative = Node2('Legislative', 'LG')
    legislative.addChild(Node2('Ahmed Ibrahim Lawan', 'Senate President'))
    legislative.addChild(Node2('Obarisi Ovie Omo-Agege', 'Deputy Senate President'))
    legislative.addChild(Node2('Femi Gbajabiamila', 'Speaker of House'))
    
    judicial = Node2('Judicial', 'JD')
    judicial.addChild(Node2('Olukayode Ariwoola', 'Chief Judge'))
    judicial.addChild(Node2('Musa Dattijo Muhammad', 'Justice of the Supreme Court'))
    judicial.addChild(Node2('Monica Bolna’an Dongban-Mensem', 'President, Court of Appeal'))
    
    
    root.addChild(executive)
    root.addChild(legislative)
    root.addChild(judicial)
    
    
    return root



# 3. Demo of geographic hierachy in West Africa.
class Node:
    def __init__(self, item):
        self.node = item
        self.children = []
        self.parent = None
    
    # child is also an instance of this class.
    def addChild(self, child):
        child.parent = self
        self.children.append(child)
    
    def level(self):
        level = 0
        parent = self.parent
        while parent:
            level += 1
            parent = parent.parent
        return level
    
    def display(self, level):
        if self.level() > level:
            return
        prefix = (' ' * self.level() * 3) + "|__" if self.parent else ""
        print(prefix + self.node)
        if self.children:
            for child in self.children:
                time.sleep(0.5)
                child.display(level)

# Implementing "3"
def WestAfrica():
    root = Node('West Africa')
    
    benin = Node('Benin')
    benin.addChild(Node('Porto-Novo'))
    benin.addChild(Node('Cotonou'))
    
    burkina_faso = Node('Burkina Faso')
    burkina_faso.addChild(Node('Ouagadougou'))
    burkina_faso.addChild(Node('Bodo-Dioulasso'))
    
    cape_verde = Node('Cape Verde')
    cape_verde.addChild(Node('Praia'))
    cape_verde.addChild(Node('Mindelo'))
    
    ivory_coast = Node("Côte D'Ivoire")
    ivory_coast.addChild(Node('Yamoussoukro'))
    ivory_coast.addChild(Node('Abidjan'))
    
    gambia = Node('Gambia')
    gambia.addChild(Node('Banjul'))
    gambia.addChild(Node('Bakau'))
    
    ghana = Node('Ghana')
    ghana.addChild(Node('Accra'))
    ghana.addChild(Node('Kumasi'))
    
    guinea = Node('Guinea')
    guinea.addChild(Node('Conakry'))
    guinea.addChild(Node('Nzérékoré'))
    
    guinea_bissau = Node('Guinea-Bissau')
    guinea_bissau.addChild(Node('Bissau'))
    guinea_bissau.addChild(Node('Bafata'))
    
    liberia = Node('Liberia')
    liberia.addChild(Node('Monrovia'))
    liberia.addChild(Node('Buchanan'))
    
    mali = Node('Mali')
    mali.addChild(Node('Bamako'))
    mali.addChild(Node('Ségou'))
    
    mauritania = Node('Mauritania')
    mauritania.addChild(Node('Nouakchott'))
    mauritania.addChild(Node('Nouadhibou'))
    
    niger = Node('Niger')
    niger.addChild(Node('Niamey'))
    niger.addChild(Node('Maradi'))
    
    nigeria = Node('Nigeria')
    nigeria.addChild(Node('Abuja'))
    nigeria.addChild(Node('Lagos'))
    
    senegal = Node('Senegal')
    senegal.addChild(Node('Dakar'))
    senegal.addChild(Node('Touba'))
    
    sierra_leone = Node('Sierra Leone')
    sierra_leone.addChild(Node('Freetown'))
    sierra_leone.addChild(Node('Bo'))
    
    togo = Node('Togo')
    togo.addChild(Node('Lomé'))
    togo.addChild(Node('Sokodé'))
    
    # Tree building.
    root.addChild(benin)
    root.addChild(burkina_faso)
    root.addChild(cape_verde)
    root.addChild(ivory_coast)
    root.addChild(gambia)
    root.addChild(ghana)
    root.addChild(guinea)
    root.addChild(guinea_bissau)
    root.addChild(liberia)
    root.addChild(mali)
    root.addChild(mauritania)
    root.addChild(niger)
    root.addChild(nigeria)
    root.addChild(senegal)
    root.addChild(sierra_leone)
    root.addChild(togo)
    
    # Return the tree.
    return root



# NB: The time.sleep() is just spice display().
# Running the entire program.
if __name__ == "__main__":
    # "1".
    print("File system Structure:")
    root1 = ComputerDrive()
    root1.display()

    print("\n")
    print("_________________________________________________")
    print("\n")

    # "2".
    print("Nigerian Arm of government hierachy:")
    root2 = ArmOfGovernment()
    root2.display("tag")
    print("\n")
    root2.display("name")
    print("\n")
    root2.display("both")

    print("\n")
    print("_________________________________________________")
    print("\n")

    # "3".
    print("West Africa Geo:")
    root3 = WestAfrica()
    root3.display(0)
    print('\n')
    root3.display(1)
    print('\n')
    root3.display(2)


# ifunanyaScript