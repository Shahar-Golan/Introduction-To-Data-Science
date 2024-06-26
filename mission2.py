class X:
    pass


class Y(X):
    pass


# section A
def isInstancePPL(object1, classinfo):
    # check type
    if not (type(classinfo) is type):
        raise TypeError("Classinfo must be a class")
    # check if instance
    return type(object1) is classinfo


# section B
def numInstancePPL(object1, classinfo):
    # check type
    if not (type(classinfo) is type):
        raise TypeError("Classinfo must be a class")

    level = 0
    object_class = type(object1)

    # if not check the hierarchy level
    while object_class is not object:
        # check if the class of the object is classinfo
        if object_class is classinfo:
            return level + 1
        # checking other bases
        if object_class.__bases__ != ():
            object_class = object_class.__bases__[0]
            level += 1
        else:
            break
    # checking if object_class is classinfo itself
    if object_class is classinfo:
        return level + 1

    # no inheritance found
    return 0


# section C
def subClassPPL(subclass, classinfo):
    # check type
    if not (type(subclass) is type and type(classinfo) is type):
        raise TypeError("Both arguments must be classes")

    current = subclass

    # checking ancestors
    while current is not object:
        # checking if current is classinfo
        if current is classinfo:
            return True
        if current.__bases__ != ():
            current = current.__bases__[0]
        else:
            break

    # no inheritance
    return False


# section D
def numSubClassPPL(subclass, classinfo):
    # check types
    if not (type(subclass) is type and type(classinfo) is type):
        raise TypeError("Both arguments must be classes")

    level = 0
    current = subclass

    # self inheritance
    if subclass is classinfo:
        return 1

    # if not self inheritance check level of hierarchy
    while subclass is not object:
        # checking if current is classinfo
        if current is classinfo:
            return level + 1

        # Next bases
        if current.__bases__ != ():
            current = current.__bases__[0]
            level += 1
        else:
            break

    # incase there is no inheritance
    return 0


