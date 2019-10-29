from tkinter import *


root = Tk()
root.title("Registro de Trabajos")
root.config(bg = "#1F1F1F")

miFrame = Frame(root)
miFrame.pack()
miFrame.config(bg = "#1F1F1F")

# Titulo
labelSubTitulo = Label(miFrame, text = "REGISTRO DE TRABAJOS PM03", bg = "#1F1F1F", fg = "#03f943")
labelSubTitulo.grid(row = 0,column = 0,columnspan = 4, padx = 10, pady = 10)


labelDescripcionUT = Label(miFrame, text = "Descripcion UT", bg = "#1F1F1F", fg = "#03f943")
labelDescripcionUT.grid(row = 1, column = 0, padx = 10, pady = 10)

cuadroTableroMartillo = Entry(miFrame, justify=CENTER)
cuadroTableroMartillo.grid(row = 1, column = 1, padx = 10, pady = 10)
cuadroTableroMartillo.focus()


labelUbicacionTecnica = Label(miFrame, text = "Ubicacion Tecnica", bg = "#1F1F1F", fg = "#03f943")
labelUbicacionTecnica.grid(row = 1, column = 2, padx = 10, pady = 10)

cuadroUbicacionTecnica = Entry(miFrame, justify=CENTER)
cuadroUbicacionTecnica.grid(row = 1, column = 3, padx = 10, pady = 10)

miFrame1 = Frame(root)
miFrame1.pack()
miFrame1.config(bg = "#1F1F1F")

labelOrden = Label(miFrame1, text = "Orden", bg = "#1F1F1F", fg = "#03f943")
labelOrden.grid(row = 0, column = 0, padx = 10, pady = 10)

cuadroOrden = Entry(miFrame1, justify=CENTER)
cuadroOrden.grid(row = 1, column = 0, padx = 10, pady = 10)

labelFechaInicioAveria = Label(miFrame1, text = "Fecha Inicio Averia", bg = "#1F1F1F", fg = "#03f943")
labelFechaInicioAveria.grid(row = 0, column = 1, padx = 10, pady = 10)

cuadroInicioAveria = Entry(miFrame1, justify=CENTER)
cuadroInicioAveria.grid(row = 1, column = 1, padx = 10, pady = 10)

labelFechaFinAveria = Label(miFrame1, text = "Fecha Fin Averia", bg = "#1F1F1F", fg = "#03f943")
labelFechaFinAveria.grid(row = 0, column = 2, padx = 10, pady = 10)

cuadroFinAveria = Entry(miFrame1, justify=CENTER)
cuadroFinAveria.grid(row = 1, column = 2, padx = 10, pady = 10)

labelDetencionEquipo = Label(miFrame1, text = "Detencion Equipo", bg = "#1F1F1F", fg = "#03f943")
labelDetencionEquipo.grid(row = 0, column = 3, padx = 10, pady = 10)

cuadroDetencionEquipo = Entry(miFrame1, justify=CENTER)
cuadroDetencionEquipo.grid(row = 1, column = 3, padx = 10, pady = 10)

labelFechaAviso = Label(miFrame1, text = "Fecha del Aviso", bg = "#1F1F1F", fg = "#03f943")
labelFechaAviso.grid(row = 0, column = 4, padx = 10, pady = 10)

cuadroFechaAviso = Entry(miFrame1, justify=CENTER)
cuadroFechaAviso.grid(row = 1, column = 4, padx = 10, pady = 10)

labelDetencion = Label(miFrame1, text = "Detencion", bg = "#1F1F1F", fg = "#03f943")
labelDetencion.grid(row = 0, column = 5, padx = 10, pady = 10)

cuadroDetencion = Entry(miFrame1, justify=CENTER)
cuadroDetencion.grid(row = 1, column = 5, padx = 10, pady = 10)

labelNumTecnicos = Label(miFrame1, text = "Numeros de Tecnicos", bg = "#1F1F1F", fg = "#03f943")
labelNumTecnicos.grid(row = 0, column = 6, padx = 10, pady = 10)

cuadroNumTecnicos = Entry(miFrame1, justify=CENTER)
cuadroNumTecnicos.grid(row = 1, column = 6, padx = 10, pady = 10)

labelNumAviso = Label(miFrame1, text = "Numero de Aviso", bg = "#1F1F1F", fg = "#03f943")
labelNumAviso.grid(row = 2, column = 0, padx = 10, pady = 10)

cuadroNumAviso = Entry(miFrame1, justify=CENTER)
cuadroNumAviso.grid(row = 3, column = 0, padx = 10, pady = 10)

labelHoraInicioAveria = Label(miFrame1, text = "Hora Inicio Averia", bg = "#1F1F1F", fg = "#03f943")
labelHoraInicioAveria.grid(row = 2, column = 1, padx = 10, pady = 10)

cuadroHoraInicioAveria = Entry(miFrame1, justify=CENTER)
cuadroHoraInicioAveria.grid(row = 3, column = 1, padx = 10, pady = 10)

labelHoraFinAveria = Label(miFrame1, text = "Hora Fin Averia", bg = "#1F1F1F", fg = "#03f943")
labelHoraFinAveria.grid(row = 2, column = 2, padx = 10, pady = 10)

cuadroHoraFinAveria = Entry(miFrame1, justify=CENTER)
cuadroHoraFinAveria.grid(row = 3, column = 2, padx = 10, pady = 10)

labelTiempoDetencion = Label(miFrame1, text = "Tiempo Detencion", bg = "#1F1F1F", fg = "#03f943")
labelTiempoDetencion.grid(row = 2, column = 3, padx = 10, pady = 10)

cuadroTiempoDetencion = Entry(miFrame1, justify=CENTER)
cuadroTiempoDetencion.grid(row = 3, column = 3, padx = 10, pady = 10)

labelHoraInicioTrabajos = Label(miFrame1, text = "Hora Inicio Trabajos", bg = "#1F1F1F", fg = "#03f943")
labelHoraInicioTrabajos.grid(row = 2, column = 4, padx = 10, pady = 10)

cuadroHoraInicioTrabajos = Entry(miFrame1, justify=CENTER)
cuadroHoraInicioTrabajos.grid(row = 3, column = 4, padx = 10, pady = 10)

labelTipoActividad = Label(miFrame1, text = "Tipo Actividad", bg = "#1F1F1F", fg = "#03f943")
labelTipoActividad.grid(row = 2, column = 5, padx = 10, pady = 10)

cuadroTipoActividad = Entry(miFrame1, justify=CENTER)
cuadroTipoActividad.grid(row = 3, column = 5, padx = 10, pady = 10)

labelHH = Label(miFrame1, text = "HH", bg = "#1F1F1F", fg = "#03f943")
labelHH.grid(row = 2, column = 6, padx = 10, pady = 10)

cuadroHH = Entry(miFrame1, justify=CENTER)
cuadroHH.grid(row = 3, column = 6, padx = 10, pady = 10)

miFrame2 = Frame(root)
miFrame2.pack()
miFrame2.config(bg = "#1F1F1F")

labelParteObjeto = Label(miFrame2, text = "Parte Objeto", bg = "#1F1F1F", fg = "#03f943")
labelParteObjeto.grid(row = 0, column = 0, padx = 10, pady = 10)

cuadroParteObjeto = Entry(miFrame2)
cuadroParteObjeto.grid(row = 0, column = 1, padx = 10, pady = 10)

labelCodigoObjeto = Label(miFrame2, text = "Codigo", bg = "#1F1F1F", fg = "#03f943")
labelCodigoObjeto.grid(row = 0, column = 2, padx = 10, pady = 10)

cuadroCodigoObjeto = Entry(miFrame2)
cuadroCodigoObjeto.grid(row = 0, column = 3, padx = 10, pady = 10)

labelSintoma = Label(miFrame2, text = "Sintoma Anomalia", bg = "#1F1F1F", fg = "#03f943")
labelSintoma.grid(row = 1, column = 0, padx = 10, pady = 10)

cuadroSintoma = Entry(miFrame2)
cuadroSintoma.grid(row = 1, column = 1, padx = 10, pady = 10)

labelCodigoObjeto = Label(miFrame2, text = "Codigo", bg = "#1F1F1F", fg = "#03f943")
labelCodigoObjeto.grid(row = 1, column = 2, padx = 10, pady = 10)

cuadroCodigoSintoma = Entry(miFrame2)
cuadroCodigoSintoma.grid(row = 1, column = 3, padx = 10, pady = 10)

labelCausa = Label(miFrame2, text = "Causa Anomalia", bg = "#1F1F1F", fg = "#03f943")
labelCausa.grid(row = 2, column = 0, padx = 10, pady = 10)

cuadroCausa = Entry(miFrame2)
cuadroCausa.grid(row = 2, column = 1, padx = 10, pady = 10)

labelCodigoObjeto = Label(miFrame2, text = "Codigo", bg = "#1F1F1F", fg = "#03f943")
labelCodigoObjeto.grid(row = 2, column = 2, padx = 10, pady = 10)

cuadroCodigoSintoma = Entry(miFrame2)
cuadroCodigoSintoma.grid(row = 2, column = 3, padx = 10, pady = 10)


root.mainloop()
