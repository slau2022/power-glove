#import data

#key1 is top key, bound1 is lower number
def chr_interval(key1, key2, key3, bound1, bound2, flex, capital):
    if capital == 0:
        if key3 == ",":
            key1 = key1.upper()
            key2 = key2.upper()
            key3 = "<"
        elif key3 == ".":
            key1 = key1.upper()
            key2 = key2.upper()
            key3 = ">"
        elif key3 == "/":
            key1 = key1.upper()
            key2 = ":"
            key3 = "?"
        else:
            key1 = key1.upper()
            key2 = key2.upper()
            key3 = key3.upper()
    if flex <= bound1:
        return ord(key1)
    elif bound1 < flex <= bound2:
        return ord(key2)
    else:
        return ord(key3)
        


def call_left_action(glove):
    #changes mode
    if glove.indexTouch == glove.middleTouch == glove.ringTouch ==\
            glove.pinkyTouch == 0:
        glove.mode = (glove.mode + 1) % 3
    elif glove.mode == 0:
        if glove.middleTouch == 0:
            pass
            #return chr("i")
        elif glove.indexTouch == 0:
            pass
            #right click
        else:
            return None
    elif glove.mode == 1:       # keyboard mode
        if glove.indexTouch == 0:
            if glove.pinkyTouch == 0:   # pinky + index keys t, g, b
                return chr_interval('t', 'g', 'b', 535, 570, 
                                    glove.index, glove.thumbTouch)
            else:
                return chr_interval('r', 'f', 'v', 535, 570, 
                                    glove.index, glove.thumbTouch)
        elif glove.middleTouch == 0:
            return chr_interval('e', 'd', 'c', 600, 620, 
                                glove.middle, glove.thumbTouch)
        elif glove.ringTouch == 0:
            return chr_interval('w', 's', 'x', 665, 695, 
                                glove.ring, glove.thumbTouch)
        elif glove.thumbTouch == 0:
            if glove.pinkyTouch == 0:
                return 10
            else:
                return 32
        elif glove.pinkyTouch == 0:
            return chr_interval('q', 'a', 'z', 620, 650, 
                                glove.pinky, glove.thumbTouch)
        else:
            return None
    elif glove.mode == 2:
        pass
        

def call_right_action(glove):
    #changes mode
    if glove.indexTouch == glove.middleTouch == glove.ringTouch ==\
            glove.pinkyTouch == 0:
        glove.mode = (glove.mode + 1) % 3       # cycles through modes
        return 100
    elif glove.mode == 0:       # mouse mode
        if glove.indexTouch == 0:
            return ord("i")
        elif glove.middleTouch == 0:
            pass
            #right click
        else:
            return None


    elif glove.mode == 1:       # keyboard mode
        if glove.indexTouch == 0:
            if glove.pinkyTouch == 0:   # pinky + index keys t, g, b
                return chr_interval('y', 'h', 'n', 645, 685, 
                                    glove.index, glove.thumbTouch)
            else:
                return chr_interval('u', 'j', 'm', 645, 685, 
                                    glove.index, glove.thumbTouch)
        elif glove.middleTouch == 0:
            return chr_interval('i', 'k', ',', 700, 745, 
                                glove.middle, glove.thumbTouch)
        elif glove.ringTouch == 0:
            return chr_interval('o', 'l', '.', 760, 767, 
                                glove.ring, glove.thumbTouch)
        elif glove.thumbTouch == 0:
            if glove.pinkyTouch == 0:
                return 10
            else:
                return 32
        elif glove.pinkyTouch == 0:
            return chr_interval('p', ';', '/', 690, 700, 
                                glove.pinky, glove.thumbTouch)
        else:
            return None

    elif glove.mode == 2:
        pass
    
