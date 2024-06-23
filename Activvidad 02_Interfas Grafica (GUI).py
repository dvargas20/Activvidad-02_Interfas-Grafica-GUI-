# -*- coding: utf-8 -*-
"""
Created Mon Jun 17 21:52:43 2024

@author: Diana Angelica
"""



import tkinter as tk
from tkinter import ttk

#Incluye  métodos que permiten convertir coordenadas de Grados Decimales (DD) a Grados, Minutos y Segundos (DMS), y viceversa.
class Coordenadas:
   
    def dd_a_dms(dd):
        grados = int(dd)
        minutos_completos = abs((dd - grados) * 60)
        minutos = int(minutos_completos)
        segundos = (minutos_completos - minutos) * 60
        return grados, minutos, segundos


    def dms_a_dd(grados, minutos, segundos):
        dd = abs(grados) + minutos / 60 + segundos / 3600
        return dd if grados >= 0 else -dd

# Conversión de DD a DMS
def convertir_dd_a_dms():
    try:
        lat_dd = float(entry_lat_dd.get())
        lon_dd = float(entry_lon_dd.get())

        lat_grados, lat_minutos, lat_segundos = Coordenadas.dd_a_dms(lat_dd)
        lon_grados, lon_minutos, lon_segundos = Coordenadas.dd_a_dms(lon_dd)

        lat_hemisferio = 'N' if lat_dd >= 0 else 'S'
        lon_hemisferio = 'E' if lon_dd >= 0 else 'O'

        label_resultado_dd_a_dms.config(text=f"Latitud: {abs(lat_grados)}° {lat_minutos}' {lat_segundos:.4f}'' {lat_hemisferio}\n"
                                             f"Longitud: {abs(lon_grados)}° {lon_minutos}' {lon_segundos:.4f}'' {lon_hemisferio}")
    except ValueError:
        ventana.showerror("Error", "Por favor, ingrese valores válidos para las coordenadas en DD.")

# Conversión de DMS a DD
def convertir_dms_a_dd():
    try:
        lat_grados = int(entry_lat_grados.get())
        lat_minutos = int(entry_lat_minutos.get())
        lat_segundos = float(entry_lat_segundos.get())
        lon_grados = int(entry_lon_grados.get())
        lon_minutos = int(entry_lon_minutos.get())
        lon_segundos = float(entry_lon_segundos.get())

        lat_dd = Coordenadas.dms_a_dd(lat_grados, lat_minutos, lat_segundos)
        lon_dd = Coordenadas.dms_a_dd(lon_grados, lon_minutos, lon_segundos)

        label_resultado_dms_a_dd.config(text=f"Latitud DD: {lat_dd}\nLongitud DD: {lon_dd}")
    except ValueError:
        ventana.showerror("Error", "Por favor, ingrese valores válidos para las coordenadas en DMS.")


# crea una instancia en tinker

ventana = tk.Tk()
ventana.title("Conversión de Coordenadas")
ventana.geometry("600x700")

notebook = ttk.Notebook(ventana)

# añadir color al fondo
# ventana.config(bg='black')
ventana ['bg'] = 'green'

# agregar etiqueta
etiqueta = tk.Label(
    ventana, text='CONVERSION DE COORDENADAS', bg='black', fg='white')
etiqueta.pack (expand= 100)


# Pestaña DD a DMS

tab_dd_a_dms = ttk.Frame(notebook)
notebook.add(tab_dd_a_dms, text="GRADOS DECIMALES")

ttk.Label(tab_dd_a_dms, text="Latitud DD:").grid(row=0, column=0, padx=5, pady=5)
entry_lat_dd = ttk.Entry(tab_dd_a_dms)
entry_lat_dd.grid(row=0, column=1, padx=6, pady=6)

ttk.Label(tab_dd_a_dms, text="Longitud DD:").grid(row=1, column=0, padx=5, pady=5)
entry_lon_dd = ttk.Entry(tab_dd_a_dms)
entry_lon_dd.grid(row=1, column=1, padx=5, pady=5)

ttk.Button(tab_dd_a_dms, text="Convertir DD a DMS", command=convertir_dd_a_dms).grid(row=2, columnspan=2, pady=10)

label_resultado_dd_a_dms = ttk.Label(tab_dd_a_dms)
label_resultado_dd_a_dms.grid(row=3, columnspan=2)



