import doctest

def areaTriangulo (base, altura):

    """Documentación: la función calcula el área de un triángulo dado.
    
        >>> areaTriangulo(3,6)
        'El área del triángulo es: 9.0'

        >>> areaTriangulo(4,6)
        'El área del triángulo es: 12.0'

    """

    return "El área del triángulo es: " + str((base*altura/2))

def comprobarMail(mail):

    """La función evalúa un mail recibido en busca de la @. Si tiene una @ es correcto, y si tiene más de una o la @ va al final es incorrecto.
    
    >>> comprobarMail('facu@gmail.com')
    True
    
    >>> comprobarMail('facugmail.com@')
    False

    >>> comprobarMail('facugmail.com')
    False

    >>> comprobarMail('facu@gmail.com@')
    False
    """

    arroba = mail.count('@')

    if(arroba!= 1 or  mail.rfind('@')==(len(mail)-1)):
        return False
    
    else: 
        return True

doctest.testmod() #Si el resultado que escribimos en la documentación es correcto, testmod no va a devolver nada. En caso contrario, nos dará una alerta
