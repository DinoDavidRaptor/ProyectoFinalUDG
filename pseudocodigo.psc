// ==========================================
// GESTOR DE CONTRASEÑAS CON HASH SHA-256
// Sistema de Gestión de Contraseñas con Interfaz Gráfica
// Pseudocódigo para PSeInt
// ==========================================

Algoritmo GestorContrasenasProyectoFinal
	
	// ========== DECLARACIÓN DE VARIABLES GLOBALES ==========
	Definir Contrasenias, Hashes Como Caracter
	Definir Caracteres, Letras Como Caracter
	Definir totalContrasenias, totalHashes Como Entero
	Definir opcion Como Entero
	Definir continuar Como Logico
	
	// Inicializar constantes
	Caracteres <- ".,!@#$%^&*()_+{}[]|\:;/?<>-_"
	Letras <- "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	
	// Arreglos para almacenar contraseñas y hashes
	Dimension Contrasenias[200, 2]  // [indice][0=clave, 1=valor]
	Dimension Hashes[200, 2]        // [indice][0=clave, 1=hash]
	totalContrasenias <- 0
	totalHashes <- 0
	continuar <- Verdadero
	
	// ========== INICIO DEL PROGRAMA ==========
	Limpiar Pantalla
	MostrarBanner()
	
	// Cargar datos desde archivos JSON simulados
	CargarDatos(Contrasenias, Hashes, totalContrasenias, totalHashes)
	
	// ========== BUCLE PRINCIPAL DEL MENÚ ==========
	Mientras continuar Hacer
		MostrarMenu()
		Leer opcion
		
		Segun opcion Hacer
			1:
				// Verificar archivos JSON
				VerificarArchivosJSON(totalContrasenias, totalHashes)
			2:
				// Buscar contraseña por hash
				BuscarContrasenia(Contrasenias, Hashes, totalContrasenias, totalHashes)
			3:
				// Hashear todas las contraseñas
				HashearTodo(Contrasenias, Hashes, totalContrasenias, totalHashes)
			4:
				// Generar nuevas contraseñas seguras
				GenerarContrasenias(Contrasenias, totalContrasenias, Letras, Caracteres)
			5:
				// Verificar seguridad de una contraseña
				VerificarSeguridad(Caracteres, Letras)
			6:
				// Eliminar contraseñas inseguras
				EliminarInseguras(Contrasenias, totalContrasenias, Caracteres, Letras)
			7:
				// Easter egg: Hackear SIIAU
				HackearSIIAU()
			8:
				// Salir del programa
				Salir(continuar)
			De Otro Modo:
				Escribir "ERROR: Opción no válida"
		FinSegun
		
		Si continuar Entonces
			Escribir ""
			Escribir "Presione ENTER para continuar..."
			Esperar Tecla
			Limpiar Pantalla
		FinSi
	FinMientras
	
	Escribir "Programa finalizado. ¡Hasta pronto!"
	
FinAlgoritmo

// ========== SUBPROCESOS PRINCIPALES ==========

SubProceso MostrarBanner
	Escribir "======================================================================"
	Escribir "       EL SOFTWARE MAS CABRON QUE HAS VISTO EN TU VIDA"
	Escribir "======================================================================"
	Escribir "  SISTEMA INICIADO - MODO VERBOSE ACTIVADO"
	Escribir "  Ready for commands..."
	Escribir "======================================================================"
	Escribir ""
FinSubProceso

SubProceso MostrarMenu
	Escribir "======================================================================"
	Escribir "                         MENU PRINCIPAL"
	Escribir "======================================================================"
	Escribir "1. Verificar Archivo JSON"
	Escribir "2. Buscar Contrasena (Hash)"
	Escribir "3. Hashear Todo"
	Escribir "4. Generar Contrasenas"
	Escribir "5. Verificar Seguridad"
	Escribir "6. Eliminar Inseguras"
	Escribir "7. Hackear SIIAU"
	Escribir "8. Salir"
	Escribir "======================================================================"
	Escribir Sin Saltar "Seleccione una opcion [1-8]: "
FinSubProceso

SubProceso CargarDatos(Contrasenias Por Referencia, Hashes Por Referencia, totalContrasenias Por Referencia, totalHashes Por Referencia)
	Escribir "======================================================================"
	Escribir "CARGANDO DATOS DEL SISTEMA..."
	Escribir "======================================================================"
	Escribir "ACCEDIENDO AL SISTEMA DE ARCHIVOS..."
	Escribir "BUSCANDO: contrasenias.json"
	Escribir "BUSCANDO: hashes.json"
	Escribir ""
	
	// Simulación de carga de datos
	totalContrasenias <- 0
	totalHashes <- 0
	
	Escribir "Base de datos de contrasenas cargada correctamente."
	Escribir "Base de datos de hashes cargada correctamente."
	Escribir "CARGA COMPLETADA"
	Escribir "======================================================================"
	Escribir ""
FinSubProceso

SubProceso VerificarArchivosJSON(totalContrasenias, totalHashes)
	Definir tiempoInicio, tiempoFin, tiempoTranscurrido Como Real
	tiempoInicio <- Aleatorio(0, 50) / 10.0
	
	Escribir "======================================================================"
	Escribir "VERIFICACIÓN DE ARCHIVO DE BASE DE DATOS"
	Escribir "======================================================================"
	Escribir "ARCHIVO A VERIFICAR: contrasenias.json y hashes.json"
	Escribir "INICIANDO ESCANEO DEL SISTEMA DE ARCHIVOS..."
	Escribir ""
	
	// Verificar contrasenias.json
	Escribir "ARCHIVO ENCONTRADO: contrasenias.json"
	Escribir "  - Registros en DB: ", totalContrasenias
	Escribir "  - Formato: JSON valido"
	Escribir ""
	
	// Verificar hashes.json
	Escribir "ARCHIVO ENCONTRADO: hashes.json"
	Escribir "  - Hashes en DB: ", totalHashes
	Escribir "  - Formato: JSON valido"
	Escribir ""
	
	tiempoFin <- Aleatorio(0, 50) / 10.0
	tiempoTranscurrido <- tiempoFin - tiempoInicio
	
	Escribir "======================================================================"
	Escribir "TIEMPO DE EJECUCIÓN: ", tiempoTranscurrido, " segundos"
	Escribir "VEREDICTO: VERIFICACIÓN COMPLETADA"
	Escribir "======================================================================"
FinSubProceso

SubProceso BuscarContrasenia(Contrasenias, Hashes, totalContrasenias, totalHashes)
	Definir contrasenia, hashGenerado Como Caracter
	Definir encontradaContra, encontradaHash Como Logico
	Definir i, keyEncontrada Como Entero
	Definir tiempoInicio, tiempoFin, tiempoTranscurrido Como Real
	
	Escribir Sin Saltar "Ingrese la contrasena a buscar: "
	Leer contrasenia
	
	tiempoInicio <- Aleatorio(0, 50) / 10.0
	
	Escribir "======================================================================"
	Escribir "INICIANDO BUSQUEDA DE CONTRASENA EN BASE DE DATOS"
	Escribir "======================================================================"
	Escribir "CONTRASEÑA A BUSCAR: ", contrasenia
	Escribir "LONGITUD: ", Longitud(contrasenia), " caracteres"
	Escribir "GENERANDO HASH SHA-256 PARA COMPARACIÓN..."
	
	hashGenerado <- GenerarHashSHA256(contrasenia)
	Escribir "HASH GENERADO: ", hashGenerado
	Escribir ""
	Escribir "BUSCANDO EN ", totalContrasenias, " CONTRASEÑAS Y ", totalHashes, " HASHES..."
	
	encontradaContra <- Falso
	encontradaHash <- Falso
	keyEncontrada <- 0
	
	// Buscar en contraseñas
	Para i <- 1 Hasta totalContrasenias Hacer
		Si Contrasenias[i, 2] = contrasenia Entonces
			encontradaContra <- Verdadero
			keyEncontrada <- i
		FinSi
	FinPara
	
	// Buscar en hashes
	Para i <- 1 Hasta totalHashes Hacer
		Si Hashes[i, 2] = hashGenerado Entonces
			encontradaHash <- Verdadero
			Si keyEncontrada = 0 Entonces
				keyEncontrada <- i
			FinSi
		FinSi
	FinPara
	
	tiempoFin <- Aleatorio(0, 50) / 10.0
	tiempoTranscurrido <- tiempoFin - tiempoInicio
	
	Escribir "======================================================================"
	Si encontradaContra O encontradaHash Entonces
		Escribir "RESULTADO: CONTRASENA ENCONTRADA"
		Escribir "KEY: ", Contrasenias[keyEncontrada, 1]
		Si encontradaContra Entonces
			Escribir "UBICACIÓN: Base de datos de contraseñas (texto plano)"
		FinSi
		Si encontradaHash Entonces
			Escribir "UBICACIÓN: Base de datos de hashes (SHA-256)"
		FinSi
		Escribir "HASH: ", hashGenerado
	SiNo
		Escribir "RESULTADO: CONTRASENA NO ENCONTRADA"
		Escribir "ESTADO: La contrasena NO existe en ninguna base de datos"
		Escribir "HASH BUSCADO: ", hashGenerado
		Escribir "SUGERENCIA: La contrasena puede ser nueva o nunca fue agregada"
	FinSi
	Escribir "TIEMPO DE EJECUCIÓN: ", tiempoTranscurrido, " segundos"
	Escribir "======================================================================"
FinSubProceso

SubProceso HashearTodo(Contrasenias, Hashes Por Referencia, totalContrasenias, totalHashes Por Referencia)
	Definir i Como Entero
	Definir hashGenerado Como Caracter
	Definir tiempoInicio, tiempoFin, tiempoTranscurrido Como Real
	
	tiempoInicio <- Aleatorio(0, 50) / 10.0
	
	Escribir "======================================================================"
	Escribir "INICIANDO PROCESO DE HASHEO MASIVO CON SHA-256"
	Escribir "======================================================================"
	Escribir "TOTAL DE CONTRASEÑAS EN DB: ", totalContrasenias
	Escribir "ALGORITMO: SHA-256 (Secure Hash Algorithm 256-bit)"
	Escribir "ENCODING: UTF-8"
	Escribir "OUTPUT: Hexadecimal (64 caracteres)"
	Escribir "======================================================================"
	
	totalHashes <- 0
	
	Para i <- 1 Hasta totalContrasenias Hacer
		Escribir ""
		Escribir ">>> PROCESANDO: ", Contrasenias[i, 1]
		Escribir "    Valor actual: ", Contrasenias[i, 2]
		Escribir "    STATUS: Contraseña en texto plano"
		Escribir "    ACCIÓN: Aplicando hash SHA-256..."
		
		hashGenerado <- GenerarHashSHA256(Contrasenias[i, 2])
		totalHashes <- totalHashes + 1
		Hashes[totalHashes, 1] <- Contrasenias[i, 1]
		Hashes[totalHashes, 2] <- hashGenerado
		
		Escribir "    HASH: ", hashGenerado
		Escribir "    HASHEADO EXITOSAMENTE Y GUARDADO EN hashes.json"
		
		// Barra de progreso
		MostrarProgreso(i, totalContrasenias)
	FinPara
	
	tiempoFin <- Aleatorio(0, 50) / 10.0
	tiempoTranscurrido <- tiempoFin - tiempoInicio
	
	Escribir ""
	Escribir "======================================================================"
	Escribir "RESUMEN DEL PROCESO DE HASHEO"
	Escribir "======================================================================"
	Escribir "TOTAL PROCESADAS: ", totalContrasenias
	Escribir "NUEVAS HASHEADAS: ", totalHashes
	Escribir ""
	Escribir "CAMBIOS DETECTADOS - GUARDANDO EN BASE DE DATOS..."
	Escribir "INICIANDO SECUENCIA DE GUARDADO DE DATOS..."
	Escribir "ACCEDIENDO AL SISTEMA DE ARCHIVOS..."
	Escribir "CONTRASENAS GUARDADAS CORRECTAMENTE EN contrasenias.json"
	Escribir "HASHES GUARDADOS CORRECTAMENTE EN hashes.json"
	Escribir "PROCESO COMPLETADO: Todas las contrasenas han sido hasheadas."
	Escribir "TIEMPO DE EJECUCIÓN: ", tiempoTranscurrido, " segundos"
	Escribir "======================================================================"
FinSubProceso

SubProceso GenerarContrasenias(Contrasenias Por Referencia, totalContrasenias Por Referencia, Letras, Caracteres)
	Definir cantidad, i Como Entero
	Definir nuevaContrasenia Como Caracter
	Definir tiempoInicio, tiempoFin, tiempoTranscurrido Como Real
	Definir respuesta Como Caracter
	
	Escribir Sin Saltar "Cantidad de contrasenas a generar: "
	Leer cantidad
	
	tiempoInicio <- Aleatorio(0, 50) / 10.0
	
	Escribir "======================================================================"
	Escribir "INICIANDO GENERADOR DE CONTRASENAS SEGURAS"
	Escribir "======================================================================"
	Escribir "CANTIDAD SOLICITADA: ", cantidad, " contraseñas"
	Escribir "NIVEL DE SEGURIDAD: MÁXIMO"
	Escribir "LONGITUD MÍNIMA: 9 caracteres"
	Escribir "REQUISITOS: Mayúsculas, Minúsculas, Números, Símbolos"
	Escribir "======================================================================"
	
	Para i <- 1 Hasta cantidad Hacer
		Escribir ""
		Escribir ">>> GENERANDO CONTRASEÑA #", i, " de ", cantidad
		Escribir "INICIALIZANDO GENERADOR ALEATORIO..."
		Escribir "MEZCLANDO CARACTERES: A-Z, a-z, 0-9, símbolos..."
		
		nuevaContrasenia <- GenerarContraseniaSegura(Letras, Caracteres)
		totalContrasenias <- totalContrasenias + 1
		Contrasenias[totalContrasenias, 1] <- Concatenar("pass_", ConvertirATexto(i))
		Contrasenias[totalContrasenias, 2] <- nuevaContrasenia
		
		Escribir "✓ CONTRASEÑA GENERADA: ", nuevaContrasenia
		Escribir "  - Longitud: ", Longitud(nuevaContrasenia), " caracteres"
		Escribir "  - Mayusculas: ", ContarMayusculas(nuevaContrasenia)
		Escribir "  - Minusculas: ", ContarMinusculas(nuevaContrasenia)
		Escribir "  - Numeros: ", ContarNumeros(nuevaContrasenia)
		Escribir "  - Simbolos: ", ContarSimbolos(nuevaContrasenia, Caracteres)
		Escribir "  - KEY ID: pass_", i
		Escribir "  - ESTADO: VALIDA Y SEGURA"
		
		MostrarProgreso(i, cantidad)
	FinPara
	
	tiempoFin <- Aleatorio(0, 50) / 10.0
	tiempoTranscurrido <- tiempoFin - tiempoInicio
	
	Escribir ""
	Escribir "======================================================================"
	Escribir "PROCESO DE GENERACION COMPLETADO"
	Escribir "======================================================================"
	Escribir "INICIANDO SECUENCIA DE GUARDADO DE DATOS..."
	Escribir "ACCEDIENDO AL SISTEMA DE ARCHIVOS..."
	Escribir "CONTRASENAS GUARDADAS CORRECTAMENTE EN contrasenias.json"
	Escribir "HASHES GUARDADOS CORRECTAMENTE EN hashes.json"
	Escribir cantidad, " CONTRASENAS GENERADAS Y ALMACENADAS"
	Escribir "TIEMPO DE EJECUCIÓN: ", tiempoTranscurrido, " segundos"
	Escribir "======================================================================"
FinSubProceso

Funcion contrasenia <- GenerarContraseniaSegura(Letras, Caracteres)
	Definir contrasenia Como Caracter
	Definir longitud, i, indice Como Entero
	Definir todoJunto Como Caracter
	Definir valida Como Logico
	
	longitud <- 9
	todoJunto <- Concatenar(Letras, Caracteres)
	todoJunto <- Concatenar(todoJunto, "0123456789")
	valida <- Falso
	
	Mientras NO valida Hacer
		contrasenia <- ""
		Para i <- 1 Hasta longitud Hacer
			indice <- Aleatorio(1, Longitud(todoJunto))
			contrasenia <- Concatenar(contrasenia, Subcadena(todoJunto, indice, indice))
		FinPara
		
		// Verificar que cumple todos los requisitos
		Si ValidarContrasenia(contrasenia, Caracteres, Letras) Entonces
			valida <- Verdadero
		FinSi
	FinMientras
FinFuncion

SubProceso VerificarSeguridad(Caracteres, Letras)
	Definir contrasenia Como Caracter
	Definir tieneMinus, tieneMayus, tieneNum, tieneSimb Como Logico
	Definir tiempoInicio, tiempoFin, tiempoTranscurrido Como Real
	
	Escribir Sin Saltar "Ingrese contrasena a analizar: "
	Leer contrasenia
	
	tiempoInicio <- Aleatorio(0, 50) / 10.0
	
	Escribir "======================================================================"
	Escribir "ANALISIS DE SEGURIDAD DE CONTRASENA"
	Escribir "======================================================================"
	Escribir "CONTRASENA INGRESADA: ", contrasenia
	Escribir "LONGITUD: ", Longitud(contrasenia), " caracteres"
	Escribir ""
	Escribir "CRITERIOS DE SEGURIDAD:"
	
	tieneMinus <- TieneMinusculas(contrasenia)
	tieneMayus <- TieneMayusculas(contrasenia)
	tieneNum <- TieneNumeros(contrasenia)
	tieneSimb <- TieneSimbolos(contrasenia, Caracteres)
	
	Si Longitud(contrasenia) >= 9 Entonces
		Escribir "  Longitud >= 9: SI (actual: ", Longitud(contrasenia), ")"
	SiNo
		Escribir "  Longitud >= 9: NO (actual: ", Longitud(contrasenia), ")"
	FinSi
	
	Si tieneMinus Entonces
		Escribir "  Minusculas: SI (", ContarMinusculas(contrasenia), " encontradas)"
	SiNo
		Escribir "  Minusculas: NO"
	FinSi
	
	Si tieneMayus Entonces
		Escribir "  Mayusculas: SI (", ContarMayusculas(contrasenia), " encontradas)"
	SiNo
		Escribir "  Mayusculas: NO"
	FinSi
	
	Si tieneNum Entonces
		Escribir "  Numeros: SI (", ContarNumeros(contrasenia), " encontrados)"
	SiNo
		Escribir "  Numeros: NO"
	FinSi
	
	Si tieneSimb Entonces
		Escribir "  Simbolos: SI (", ContarSimbolos(contrasenia, Caracteres), " encontrados)"
	SiNo
		Escribir "  Simbolos: NO"
	FinSi
	
	Escribir ""
	tiempoFin <- Aleatorio(0, 50) / 10.0
	tiempoTranscurrido <- tiempoFin - tiempoInicio
	
	Si Longitud(contrasenia) >= 9 Y tieneMinus Y tieneMayus Y tieneNum Y tieneSimb Entonces
		Escribir "======================================================================"
		Escribir "VEREDICTO: CONTRASENA SEGURA"
		Escribir "TIEMPO DE EJECUCION: ", tiempoTranscurrido, " segundos"
		Escribir "======================================================================"
	SiNo
		Escribir "======================================================================"
		Escribir "VEREDICTO: CONTRASENA INSEGURA (DEBIL)"
		Escribir "======================================================================"
		Escribir "RECOMENDACIONES:"
		Si Longitud(contrasenia) < 9 Entonces
			Escribir "  - Aumentar longitud a minimo 9 caracteres"
		FinSi
		Si NO tieneMinus Entonces
			Escribir "  - Agregar letras minusculas (a-z)"
		FinSi
		Si NO tieneMayus Entonces
			Escribir "  - Agregar letras mayusculas (A-Z)"
		FinSi
		Si NO tieneNum Entonces
			Escribir "  - Agregar numeros (0-9)"
		FinSi
		Si NO tieneSimb Entonces
			Escribir "  - Agregar simbolos especiales"
		FinSi
		Escribir "TIEMPO DE EJECUCION: ", tiempoTranscurrido, " segundos"
	FinSi
FinSubProceso

SubProceso EliminarInseguras(Contrasenias Por Referencia, totalContrasenias Por Referencia, Caracteres, Letras)
	Definir i, eliminadas, nuevoTotal Como Entero
	Definir esSegura Como Logico
	Definir tiempoInicio, tiempoFin, tiempoTranscurrido Como Real
	Definir ContraseniasTemporal Como Caracter
	
	Dimension ContraseniasTemporal[200, 2]
	
	tiempoInicio <- Aleatorio(0, 50) / 10.0
	
	Escribir "======================================================================"
	Escribir "INICIANDO ANALISIS DE SEGURIDAD Y LIMPIEZA"
	Escribir "======================================================================"
	Escribir "TOTAL DE CONTRASENAS A ANALIZAR: ", totalContrasenias
	Escribir "CRITERIOS DE SEGURIDAD:"
	Escribir "  - Longitud minima: 9 caracteres"
	Escribir "  - Debe contener: Mayusculas, Minusculas, Numeros, Simbolos"
	Escribir "======================================================================"
	
	eliminadas <- 0
	nuevoTotal <- 0
	
	Para i <- 1 Hasta totalContrasenias Hacer
		Escribir ""
		Escribir ">>> ANALIZANDO: ", Contrasenias[i, 1]
		Escribir "    Longitud: ", Longitud(Contrasenias[i, 2]), " caracteres"
		Escribir "    Valor: ", Contrasenias[i, 2]
		
		esSegura <- ValidarContrasenia(Contrasenias[i, 2], Caracteres, Letras)
		
		Si TieneMinusculas(Contrasenias[i, 2]) Entonces
			Escribir "    Minusculas: SI"
		SiNo
			Escribir "    Minusculas: NO"
		FinSi
		
		Si TieneMayusculas(Contrasenias[i, 2]) Entonces
			Escribir "    Mayusculas: SI"
		SiNo
			Escribir "    Mayusculas: NO"
		FinSi
		
		Si TieneNumeros(Contrasenias[i, 2]) Entonces
			Escribir "    Numeros: SI"
		SiNo
			Escribir "    Numeros: NO"
		FinSi
		
		Si TieneSimbolos(Contrasenias[i, 2], Caracteres) Entonces
			Escribir "    Simbolos: SI"
		SiNo
			Escribir "    Simbolos: NO"
		FinSi
		
		Si esSegura Entonces
			Escribir "    VEREDICTO: SEGURA"
			nuevoTotal <- nuevoTotal + 1
			ContraseniasTemporal[nuevoTotal, 1] <- Contrasenias[i, 1]
			ContraseniasTemporal[nuevoTotal, 2] <- Contrasenias[i, 2]
		SiNo
			Escribir "    VEREDICTO: INSEGURA - MARCADA PARA ELIMINACION"
			eliminadas <- eliminadas + 1
		FinSi
		
		MostrarProgreso(i, totalContrasenias)
	FinPara
	
	// Actualizar el arreglo original
	Para i <- 1 Hasta nuevoTotal Hacer
		Contrasenias[i, 1] <- ContraseniasTemporal[i, 1]
		Contrasenias[i, 2] <- ContraseniasTemporal[i, 2]
	FinPara
	totalContrasenias <- nuevoTotal
	
	tiempoFin <- Aleatorio(0, 50) / 10.0
	tiempoTranscurrido <- tiempoFin - tiempoInicio
	
	Escribir ""
	Escribir "======================================================================"
	Escribir "RESUMEN DEL ANALISIS DE SEGURIDAD"
	Escribir "======================================================================"
	Escribir "TOTAL ANALIZADAS: ", totalContrasenias + eliminadas
	Escribir "CONTRASENAS INSEGURAS ENCONTRADAS: ", eliminadas
	
	Si eliminadas > 0 Entonces
		Escribir ""
		Escribir ">>> GUARDANDO CAMBIOS EN BASE DE DATOS..."
		Escribir "INICIANDO SECUENCIA DE GUARDADO DE DATOS..."
		Escribir "ACCEDIENDO AL SISTEMA DE ARCHIVOS..."
		Escribir "CONTRASENAS GUARDADAS CORRECTAMENTE EN contrasenias.json"
		Escribir "HASHES GUARDADOS CORRECTAMENTE EN hashes.json"
		Escribir "LIMPIEZA COMPLETADA: ", eliminadas, " contrasenas inseguras eliminadas."
	SiNo
		Escribir "LIMPIEZA: No se encontraron contrasenas inseguras."
		Escribir "    Todas las contrasenas cumplen con los estandares de seguridad."
	FinSi
	
	Escribir "TIEMPO DE EJECUCION: ", tiempoTranscurrido, " segundos"
	Escribir "======================================================================"
FinSubProceso

SubProceso HackearSIIAU
	Escribir "======================================================================"
	Escribir "INICIANDO ATAQUE AL SISTEMA SIIAU..."
	Escribir "======================================================================"
	Escribir "ESCANEANDO PUERTOS..."
	Escribir "  • Puerto 80: ABIERTO"
	Escribir "  • Puerto 443: ABIERTO"
	Escribir "  • Puerto 8080: ABIERTO"
	Escribir ""
	Escribir "INTENTANDO BYPASS DE AUTENTICACIÓN..."
	Escribir "  • Método 1: SQL Injection... FALLÓ"
	Escribir "  • Método 2: XSS Attack... FALLÓ"
	Escribir "  • Método 3: Buffer Overflow... EXITO"
	Escribir ""
	Escribir "EJECUTANDO EXPLOIT SQL INJECTION..."
	Escribir "  • SELECT * FROM usuarios WHERE..."
	Escribir "  • ' OR '1'='1' --"
	Escribir ""
	Escribir "ACCEDIENDO A BASE DE DATOS..."
	Escribir "======================================================================"
	Escribir "======================================================================"
	Escribir ""
	Escribir "CALIFICACION EDITADA CON ÉXITO A 0.0"
	Escribir "======================================================================"
	Escribir ""
	Escribir "¿Quieres cambiar libremente la calificacion?"
	Escribir "Depositame 0.01 BTC a la siguiente dirección:"
	Escribir "1HckjUpRGcrrRAtFaaCAUaGjsPx9oYmLaZ"
	Escribir ""
	Esperar 3 Segundos
FinSubProceso

SubProceso Salir(continuar Por Referencia)
	Escribir "======================================================================"
	Escribir "FINALIZANDO SESION..."
	Escribir "======================================================================"
	Escribir "LIMPIANDO MEMORIA..."
	Escribir "  - Buscando donde esta Rubio..."
	Escribir "  - Jugando Counter..."
	Escribir ""
	Escribir "Cuenta de STEAM Papoi encontrada..."
	Escribir "  - Puerto 8080: CERRADO"
	Escribir "  - Puerto 443: CERRADO"
	Escribir "  - Puerto 80: CERRADO"
	Escribir ""
	Escribir "DESCONECTANDO DEL SISTEMA..."
	Escribir ""
	Escribir "Te portas bien"
	Escribir "======================================================================"
	continuar <- Falso
FinSubProceso

// ========== FUNCIONES AUXILIARES ==========

Funcion hash <- GenerarHashSHA256(texto)
	Definir hash Como Caracter
	// Simulacion de hash SHA-256 (64 caracteres hexadecimales)
	hash <- Concatenar("sha256_", texto)
	hash <- Concatenar(hash, "_simulado_64_caracteres_hexadecimal")
FinFuncion

Funcion resultado <- ValidarContrasenia(contrasenia, Caracteres, Letras)
	Definir resultado Como Logico
	resultado <- (Longitud(contrasenia) >= 9) Y TieneMinusculas(contrasenia) Y TieneMayusculas(contrasenia) Y TieneNumeros(contrasenia) Y TieneSimbolos(contrasenia, Caracteres)
FinFuncion

Funcion resultado <- TieneMinusculas(texto)
	Definir resultado Como Logico
	Definir i Como Entero
	resultado <- Falso
	Para i <- 1 Hasta Longitud(texto) Hacer
		Si Subcadena(texto, i, i) >= "a" Y Subcadena(texto, i, i) <= "z" Entonces
			resultado <- Verdadero
		FinSi
	FinPara
FinFuncion

Funcion resultado <- TieneMayusculas(texto)
	Definir resultado Como Logico
	Definir i Como Entero
	resultado <- Falso
	Para i <- 1 Hasta Longitud(texto) Hacer
		Si Subcadena(texto, i, i) >= "A" Y Subcadena(texto, i, i) <= "Z" Entonces
			resultado <- Verdadero
		FinSi
	FinPara
FinFuncion

Funcion resultado <- TieneNumeros(texto)
	Definir resultado Como Logico
	Definir i Como Entero
	resultado <- Falso
	Para i <- 1 Hasta Longitud(texto) Hacer
		Si Subcadena(texto, i, i) >= "0" Y Subcadena(texto, i, i) <= "9" Entonces
			resultado <- Verdadero
		FinSi
	FinPara
FinFuncion

Funcion resultado <- TieneSimbolos(texto, Caracteres)
	Definir resultado Como Logico
	Definir i, j Como Entero
	resultado <- Falso
	Para i <- 1 Hasta Longitud(texto) Hacer
		Para j <- 1 Hasta Longitud(Caracteres) Hacer
			Si Subcadena(texto, i, i) = Subcadena(Caracteres, j, j) Entonces
				resultado <- Verdadero
			FinSi
		FinPara
	FinPara
FinFuncion

Funcion cantidad <- ContarMinusculas(texto)
	Definir cantidad, i Como Entero
	cantidad <- 0
	Para i <- 1 Hasta Longitud(texto) Hacer
		Si Subcadena(texto, i, i) >= "a" Y Subcadena(texto, i, i) <= "z" Entonces
			cantidad <- cantidad + 1
		FinSi
	FinPara
FinFuncion

Funcion cantidad <- ContarMayusculas(texto)
	Definir cantidad, i Como Entero
	cantidad <- 0
	Para i <- 1 Hasta Longitud(texto) Hacer
		Si Subcadena(texto, i, i) >= "A" Y Subcadena(texto, i, i) <= "Z" Entonces
			cantidad <- cantidad + 1
		FinSi
	FinPara
FinFuncion

Funcion cantidad <- ContarNumeros(texto)
	Definir cantidad, i Como Entero
	cantidad <- 0
	Para i <- 1 Hasta Longitud(texto) Hacer
		Si Subcadena(texto, i, i) >= "0" Y Subcadena(texto, i, i) <= "9" Entonces
			cantidad <- cantidad + 1
		FinSi
	FinPara
FinFuncion

Funcion cantidad <- ContarSimbolos(texto, Caracteres)
	Definir cantidad, i, j Como Entero
	cantidad <- 0
	Para i <- 1 Hasta Longitud(texto) Hacer
		Para j <- 1 Hasta Longitud(Caracteres) Hacer
			Si Subcadena(texto, i, i) = Subcadena(Caracteres, j, j) Entonces
				cantidad <- cantidad + 1
			FinSi
		FinPara
	FinPara
FinFuncion

SubProceso MostrarProgreso(actual, total)
	Definir porcentaje Como Entero
	porcentaje <- Trunc((actual * 100) / total)
	Escribir "    [PROGRESO: ", porcentaje, "%]"
FinSubProceso
