import sys

from ipyxact.ipyxact import Component

def get_businterfaces(busInterfaces):
    ifs = []
    for busInterface in busInterfaces.busInterface:
        print('='*20)
        print('name    : ' + busInterface.name)
        _vendor  = busInterface.busType.vendor
        _library = busInterface.busType.library
        _name    = busInterface.busType.name
        _version = busInterface.busType.version
        print(busInterface.busType.name)
        print('busType         : {}/{}/{}/{}'.format(_vendor,
                                                     _library,
                                                     _name,
                                                     _version))
        print('abstractionType : {}/{}/{}/{}'.format(_vendor,
                                                     _library,
                                                     _name,
                                                     _version))
        for portMap in busInterface.portMaps.portMap:
            print("{}[{}:{}] => {}[{}:{}]".format(portMap.logicalPort.name,
                                           portMap.logicalPort.vector.left,
                                           portMap.logicalPort.vector.right,
                                           portMap.physicalPort.name,
                                           portMap.physicalPort.vector.left,
                                           portMap.physicalPort.vector.right))
    return ifs
    
if __name__ == "__main__":
    f = open(sys.argv[1])

    component = Component()
    component.load(f)

    if component.busInterfaces is not None:
        ifs = get_businterfaces(component.busInterfaces)
        print(ifs)
    else:
        print("No bus interfaces found in file")
    f.close()
