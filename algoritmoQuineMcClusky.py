def algoritmoQuineMcClusky(cantidadVariables, minterminosUtilizados):
    todosMinterminos = formarTodosMinterminos(cantidadVariables)
    minterminos = seleccionarMinterminos(todosMinterminos, minterminosUtilizados)
    minterminosAgrupadosCantidadUnos = agruparMinterminosCantidadUnos(minterminos, cantidadVariables)
    posibleSimplificar = verificarPosibleSimplificar(minterminosAgrupadosCantidadUnos)
    while (posibleSimplificar):
        minterminosAgrupadosCantidadUnos = simplificar(minterminosAgrupadosCantidadUnos, cantidadVariables)
        posibleSimplificar = verificarPosibleSimplificar(minterminosAgrupadosCantidadUnos)
    implicantesPrimosEsenciales = encontrarImplicantesPrimosEsenciales(minterminosAgrupadosCantidadUnos) 
    return [0,0]

def formarTodosMinterminos(cantidadVariables):
    valoresBinariosVariables = []
    minterminos = []
    for variable in range(0, cantidadVariables):
        valoresBinariosVariable = []
        cantidadGruposBinarios = 2**(variable+1)
        cantidadRepeticionesBinarias = (2**cantidadVariables)//cantidadGruposBinarios
        valorBinarioActual = "0"
        for grupoBinario in range(0, cantidadGruposBinarios):
            cantidadRepeticionesBinarias = (2**cantidadVariables)//cantidadGruposBinarios
            for repeticionBinaria in range(0, cantidadRepeticionesBinarias):
                valoresBinariosVariable = valoresBinariosVariable + [valorBinarioActual]
            if valorBinarioActual == "0":
                valorBinarioActual = "1"
            else:
                valorBinarioActual = "0"
        valoresBinariosVariables = valoresBinariosVariables + [valoresBinariosVariable]
    cantidadMinterminos = 2**cantidadVariables
    for indiceValoresBinariosVariables in range(0, cantidadMinterminos):
        mintermino = []
        for valoresBinariosVariable in valoresBinariosVariables:
            mintermino = mintermino + [valoresBinariosVariable[indiceValoresBinariosVariables]]
        minterminos = minterminos + [mintermino]
    return minterminos
        
def seleccionarMinterminos(todosMinterminos, minterminosUtilizados):
    minterminos = []
    cantidadMinterminos = len(todosMinterminos)
    for indiceMintermino in range(0, cantidadMinterminos):
        if indiceMintermino in minterminosUtilizados:
            minterminos = minterminos + [[[indiceMintermino],todosMinterminos[indiceMintermino],0]]
    return minterminos

def agruparMinterminosCantidadUnos(minterminos, cantidadVariables):
    minterminosAgrupadosCantidadUnos = []
    for posibleCantidadUnos in range(0, (cantidadVariables+1)):
        minterminosAgrupadosPosibleCantidadUnos = []
        for mintermino in minterminos:
            valorBinarioMintermino = mintermino[1]
            if valorBinarioMintermino.count("1") == posibleCantidadUnos:
                minterminosAgrupadosPosibleCantidadUnos = minterminosAgrupadosPosibleCantidadUnos + [[mintermino[0],mintermino[1],posibleCantidadUnos]]
        if minterminosAgrupadosPosibleCantidadUnos != []:
            minterminosAgrupadosCantidadUnos = minterminosAgrupadosCantidadUnos + [minterminosAgrupadosPosibleCantidadUnos]
    return minterminosAgrupadosCantidadUnos
    
def verificarPosibleSimplificar(minterminosAgrupadosCantidadUnos):
    for grupoCantidadUnosComparar in minterminosAgrupadosCantidadUnos:
        cantidadUnos = grupoCantidadUnosComparar[0][2]
        for grupoCantidadUnosComparado in minterminosAgrupadosCantidadUnos:
            if cantidadUnos+1 == grupoCantidadUnosComparado[0][2]:
                for minterminoComparar in grupoCantidadUnosComparar:
                    for minterminoComparado in grupoCantidadUnosComparado:
                        diferenciasBit = 0
                        for indiceValorLogico in range(0, len(minterminoComparar[1])):
                            if minterminoComparar[1][indiceValorLogico] != minterminoComparado[1][indiceValorLogico]:
                                diferenciasBit = diferenciasBit + 1
                        if diferenciasBit == 1:
                            return True
    return False

def simplificar(minterminosAgrupadosCantidadUnos, cantidadVariables):
    nuevosMinterminos = []
    for grupoCantidadUnosComparar in minterminosAgrupadosCantidadUnos:
        cantidadUnos = grupoCantidadUnosComparar[0][2]
        for grupoCantidadUnosComparado in minterminosAgrupadosCantidadUnos:
            if cantidadUnos+1 == grupoCantidadUnosComparado[0][2]:
                for minterminoComparar in grupoCantidadUnosComparar:
                    for minterminoComparado in grupoCantidadUnosComparado:
                        diferenciasBit = 0
                        indiceValorLogicoDiferencia = 0
                        for indiceValorLogico in range(0, len(minterminoComparar[1])):
                            if minterminoComparar[1][indiceValorLogico] != minterminoComparado[1][indiceValorLogico]:
                                diferenciasBit = diferenciasBit + 1
                                indiceValorLogicoDiferencia = indiceValorLogico
                        if diferenciasBit == 1:
                            minterminosSimplificados = minterminoComparar[0] + minterminoComparado[0]
                            valorLogicoSimplificado = []
                            for indiceValorLogicoSimplificado in range(0, len(minterminoComparar[1])):
                                if indiceValorLogicoSimplificado == indiceValorLogicoDiferencia:
                                    valorLogicoSimplificado = valorLogicoSimplificado + ["-"]
                                else:
                                    valorLogicoSimplificado = valorLogicoSimplificado + [minterminoComparar[1][indiceValorLogicoSimplificado]]
                            nuevosMinterminos = nuevosMinterminos + [[minterminosSimplificados, valorLogicoSimplificado, cantidadUnos]]
    minterminosFinales = nuevosMinterminos
    for grupoCantidadUnos in minterminosAgrupadosCantidadUnos:
        for mintermino in grupoCantidadUnos:
            seSimplifico = False
            for minterminoSimplificado in nuevosMinterminos:
                cantidadCoincidencias = 0
                for minterminoUtilizado in mintermino[0]:
                    print(minterminoUtilizado)
                    cantidadCoincidencias = 0
                    for minterminoUtilizadoSimplificacion in minterminoSimplificado[0]:
                        if minterminoUtilizado == minterminoUtilizadoSimplificacion:
                            cantidadCoincidencias = cantidadCoincidencias + 1
                if cantidadCoincidencias != len(mintermino[0]):
                    minterminosFinales = minterminosFinales + [mintermino]
    minterminosFinales = agruparMinterminosCantidadUnos(minterminosFinales, cantidadVariables)
    return minterminosFinales

def encontrarImplicantesPrimosEsenciales(minterminosAgrupadosCantidadUnos):
    minterminos = []
    for grupoCantidadUnos in minterminosAgrupadosCantidadUnos:
        pass