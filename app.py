import streamlit as st
import plotly.express as px
import pandas as pd
import folium
from streamlit_folium import st_folium
import math
from fpdf import FPDF
from datetime import datetime

st.set_page_config(layout="wide")
# --- FUNCIÓN PARA CALCULAR LA DISTANCIA ---
def haversine(lat1, lon1, lat2, lon2):
    """
    Calcula la distancia de la gran circunferencia entre dos puntos en la Tierra
    (especificados en coordenadas decimales).
    """
    R = 6371  # Radio de la Tierra en kilómetros
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)
    
    dlon = lon2_rad - lon1_rad
    dlat = lat2_rad - lat1_rad
    
    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    distance = R * c
    return distance
# --- FIN DE LA FUNCIÓN ---
# --- FUNCIÓN PARA GENERAR EL REPORTE EN PDF ---
def create_pdf_report(ruta, grupo, total_distance, costo_total, eficiencia_km_litro, tiempo_en_movimiento, tiempo_detenido, velocidad_movimiento_promedio):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=16)
    
    # Título del reporte
    pdf.cell(200, 10, txt=f"Reporte de Ruta: {ruta}", ln=True, align="C")
    
    pdf.set_font("Arial", size=12)
    pdf.ln(10) # Salto de línea
    
    # Resumen del viaje
    pdf.cell(200, 10, txt="Resumen del viaje:", ln=True)
    pdf.cell(200, 10, txt=f"Kilómetros Recorridos: {total_distance:.2f} km", ln=True)
    pdf.cell(200, 10, txt=f"Costo Total de Combustible: S/ {costo_total:.2f}", ln=True)
    pdf.cell(200, 10, txt=f"Eficiencia de Combustible: {eficiencia_km_litro:.2f} km/L", ln=True)
    
    pdf.ln(10)
    
    # Detalles de la ruta
    pdf.cell(200, 10, txt="Detalles de la Ruta:", ln=True)
    pdf.cell(200, 10, txt=f"Duración Total: {grupo['Fecha y Hora'].iloc[-1] - grupo['Fecha y Hora'].iloc[0]}", ln=True)
    pdf.cell(200, 10, txt=f"Tiempo en Movimiento: {tiempo_en_movimiento}", ln=True)
    pdf.cell(200, 10, txt=f"Tiempo Detenido: {tiempo_detenido}", ln=True)
    pdf.cell(200, 10, txt=f"Velocidad promedio en movimiento: {velocidad_movimiento_promedio:.2f} km/h", ln=True)
    
    return pdf.output(dest='S').encode('latin-1')

# Presentación de imágenes en columnas (tamaño reducido)
col1, col2, col3 = st.columns([1,1,1])
with col1:
    st.image("analizer.png", caption="Trucking", width=500)
with col2:
    st.image("Logo.png", caption="Imagen", width=300)
with col3:
    st.image("Phonetruck.png", caption="TruckTechnology", width=250)


# Sección de contacto
st.markdown("---")
st.header("Contacto")

# CSS para los iconos SVG (ajusta el tamaño y color)
st.markdown("""
    <style>
    .icon-social {
        width: 25px;
        height: 25px;
        margin-right: 15px;
    }
    .icon-social svg path,
    .icon-social svg circle {
        fill: #4F4F4F; /* Color de los íconos */
    }
    </style>
""", unsafe_allow_html=True)


social_col1, social_col2, social_col3, social_col4, social_col5, social_col6, social_col7 = st.columns([1,1,1,1,1,1,4])

with social_col1:
    st.markdown("""
        <a href="https://www.youtube.com/@TuCanalDeTransporte" target="_blank">
            <svg class="icon-social" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512"><!--! Font Awesome Pro 6.4.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. --><path d="M549.655 124.083c-6.281-23.65-24.787-42.276-48.284-48.597C458.781 64 288 64 288 64S117.22 64 74.629 75.486c-23.497 6.322-42.003 24.947-48.284 48.597-11.668 44.204-11.668 124.787 0 169.194-6.281 23.65-24.787 42.276-48.284 48.597C117.22 448 288 448 288 448s170.78 0 213.371-11.486c23.497-6.322 42.003-24.947 48.284-48.597 11.668-44.204 11.668-124.787 0-169.194zM288 368.52c-47.514 0-86.02-38.643-86.02-86.157S240.486 196.206 288 196.206c47.514 0 86.02 38.643 86.02 86.157S335.514 368.52 288 368.52zm148.455-156.634c-4.943-18.665-21.782-32.062-41.285-35.857-41.455-7.535-83.33-11.238-124.9-11.238-41.569 0-83.444 3.703-124.9 11.238-19.503 3.795-36.342 17.192-41.285 35.857-7.535 28.539-7.535 77.291 0 105.829 4.943 18.665 21.782 32.062 41.285 35.857 41.455 7.535 83.33 11.238 124.9 11.238 41.569 0 83.444-3.703 124.9-11.238 19.503-3.795 36.342-17.192 41.285-35.857 7.535-28.539 7.535-77.291 0-105.829zM288 224c-34.52 0-62.52 28.02-62.52 62.52s28.02 62.52 62.52 62.52c34.52 0 62.52-28.02 62.52-62.52s-28.02-62.52-62.52-62.52z"/></svg>
        </a>
    """, unsafe_allow_html=True)
with social_col2:
    st.markdown("""
        <a href="https://www.facebook.com/tucanaldetransporte" target="_blank">
            <svg class="icon-social" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><!--! Font Awesome Pro 6.4.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. --><path d="M504 256C504 119 393 8 256 8S8 119 8 256c0 123.78 90.69 226.37 209.25 245V327.69h-63V256h63v-54.64c0-62.15 37-96.48 93.67-96.48 27.14 0 55.52 4.84 55.52 4.84v61h-31.28c-30.8 0-40.42 19.12-40.42 38.73V256h68.78l-11 71.69h-57.78V501C413.31 482.37 504 379.78 504 256z"/></svg>
        </a>
    """, unsafe_allow_html=True)
with social_col3:
    st.markdown("""
        <a href="https://www.instagram.com/tucanaldetransporte" target="_blank">
            <svg class="icon-social" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><!--! Font Awesome Pro 6.4.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. --><path d="M224.1 140.5c-48.4 0-87.6 39.2-87.6 87.6s39.2 87.6 87.6 87.6 87.6-39.2 87.6-87.6-39.2-87.6-87.6-87.6zm0 148.1c-33.8 0-61.4-27.6-61.4-61.4s27.6-61.4 61.4-61.4 61.4 27.6 61.4 61.4-27.6 61.4-61.4 61.4zm-94.4-177.3h16.7c7.1 0 12.9-5.8 12.9-12.9v-16.7c0-7.1-5.8-12.9-12.9-12.9h-16.7c-7.1 0-12.9 5.8-12.9 12.9v16.7c0 7.1 5.8 12.9 12.9 12.9zM224 45.4c-124.9 0-193.3 4.1-220.1 10.6-21.7 5.2-34.9 11.5-44.1 20.7-9.2 9.2-15.5 22.4-20.7 44.1-6.5 26.8-10.6 95.2-10.6 220.1s4.1 193.3 10.6 220.1c5.2 21.7 11.5 34.9 20.7 44.1 9.2 9.2 22.4 15.5 20.7 44.1-6.5 26.8-10.6 95.2-10.6 220.1s4.1 193.3 10.6 220.1c5.2 21.7 11.5 34.9 20.7 44.1 9.2 9.2 22.4 15.5 44.1 20.7 26.8 6.5 95.2 10.6 220.1 10.6s193.3-4.1 220.1-10.6c21.7-5.2 34.9-11.5 44.1-20.7 9.2-9.2 15.5-22.4 20.7-44.1 6.5-26.8 10.6-95.2 10.6-220.1s-4.1-193.3-10.6-220.1c-5.2-21.7-11.5-34.9-20.7-44.1-9.2-9.2-22.4-15.5-44.1-20.7-26.8-6.5-95.2-10.6-220.1-10.6S76.1 48.6 50.4 55.1c-10.2 2.6-18.5 7.7-25.8 15-7.3 7.3-12.4 15.6-15 25.8-6.5 25.7-10.5 87.1-10.5 170.5s4 144.8 10.5 170.5z"/></svg>
        </a>
    """, unsafe_allow_html=True)
with social_col4:
    st.markdown("""
        <a href="https://www.linkedin.com/in/tucanaldetransporte" target="_blank">
            <svg class="icon-social" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><!--! Font Awesome Pro 6.4.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. --><path d="M416 32H31.9C14.3 32 0 46.5 0 64.3v383.4C0 465.5 14.3 480 31.9 480H416c17.6 0 32-14.5 32-32.3V64.3c0-17.8-14.4-32.3-32-32.3zM135.4 416H69V202.2h66.5V416zm-33.2-243c-21.3 0-38.5-17.3-38.5-38.5S80.9 96.2 102.2 96.2c21.2 0 38.5 17.3 38.5 38.5 0 21.3-17.2 38.5-38.5 38.5zm282.1 243h-66.4V312c0-24.8-.4-56.6-34.5-56.6-34.6 0-39.9 27-39.9 55v103.5h-66.3V202.2h63.7v29.2h.9c8.9-16.8 30.6-34.5 62.9-34.5 67.2 0 79.7 44.2 79.7 101.9V416z"/></svg>
        </a>
    """, unsafe_allow_html=True)
with social_col5:
    st.markdown("""
        <a href="https://www.tiktok.com/@tucanaldetransporte" target="_blank">
            <svg class="icon-social" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><!--! Font Awesome Pro 6.4.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. --><path d="M448 115.6c-.3-13.7-14-17.5-23.7-15.3-24.5 5.5-49.9 14.8-76.3 26.6-13.8 6.1-23.2 21.8-21.9 37.8 1.4 16 11.8 30.1 26.6 37.8 12.3 6.3 26.6 9.8 41.6 10.5 4.9 0 9.8-.2 14.7-.5 25.4-1.2 50.2-12.7 72.3-33.7 13.5-12.9 33.1-15.5 51.5-6.8 13.9 6.6 22.3 21 21.1 36.3-1.2 15.3-11.8 28.5-26.1 35.8-23.3 11.6-48.4 20-74.8 24.3-13.8 2.3-27.7 3.3-41.6 3.4-13.9 0-27.7-.8-41.6-2.4-23.7-2.6-46.7-10.4-68-23.5-12.2-7.3-22.3-17.3-29.3-29.3-7-12-10.4-25.5-10.4-39.9 0-23.1 7.6-45.7 21.7-65.4 13.6-19.3 32-33.8 53.6-43.7 21.6-9.9 44.8-14.8 68.3-14.8 25.1 0 49.6 5.8 73.1 17.5 16.5 8.3 27.2 25.9 25.4 43.6-1.8 17.7-14.6 32-31.5 38.3z"/></svg>
        </a>
    """, unsafe_allow_html=True)
with social_col6:
    st.markdown("""
        <a href="https://wa.me/51969893045" target="_blank">
            <svg class="icon-social" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><!--! Font Awesome Pro 6.4.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. --><path d="M380.9 97.4C339.4 56.4 286.9 32 229.4 32c-128.8 0-233.1 104.2-233.1 233.1 0 40.8 10.3 80.3 29.3 115.1L2.6 448l119.8-31.4c32.9 18 69.8 27.5 109.1 27.5 128.8 0 233.1-104.2 233.1-233.1 0-57.5-24.4-110-65.9-151.6zM229.4 416c-36.9 0-72.3-10-103.5-29l-11.8-6.9-1.9 8.1-12.2 52.8 53.9-14.2 6.9-11.8c29.7 17.7 64.9 27.2 101.9 27.2 106.7 0 193.3-86.5 193.3-193.3S336.1 72 229.4 72c-55.7 0-106.7 23.3-142.9 61.1-36.2 37.8-56.7 89.9-56.7 145.9s20.5 108.1 56.7 145.9c36.2 37.8 87.2 61.1 142.9 61.1zM342.1 267.3c-2.3-3.9-14.9-7.4-17.6-8.3-2.7-.9-4.7-1.4-6.8 1.4-2.1 2.8-5.3 6.6-6.4 7.9-1.1 1.4-2.3 1.4-4.3 .5-2.1-.9-8.9-3.3-16.9-10.4-12.4-11.1-20.7-23.2-29.4-2.5-4.4-.3-6.8 1.9-9.3 1.4-1.6 3.1-3.7 4.7-5.6 1.6-1.9 2.1-3.2 2.8-5.3 .7-2.1-.4-3.9-.9-5.3-2.2-6.5-7.7-15.5-12.7-18.1-5-2.6-10.1-2.1-14.9-1.2-4.8 .9-9.1-.5-11.9-3.5-2.8-3-9.5-11-13-14.8-3.5-3.8-7.1-3.2-11.2-3.2-4.1-.1-8.7-.1-13.4-.1-9.9 0-17.7 3.7-22.9 8.7-5.2 5-21.7 20.9-21.7 50.9s22.2 59 25.3 63.1c3.1 4.1 43.8 68.3 106.2 92.5 44.5 17.1 53.6 14.4 63 13.5 9.4-.9 30.2-12.3 34.6-24.1 4.4-11.8 4.4-21.9 3.1-24.1-1.3-2.3-4.9-3.9-10.4-6.7z"/></svg>
        </a>
    """, unsafe_allow_html=True)
    
st.markdown("---")

contact_col1, contact_col2 = st.columns(2)

with contact_col1:
    st.subheader("Datos de la Empresa")
    st.markdown(f"**Nombre de la empresa:** Solucines GPS Pro SAC")
    st.markdown(f"**RUC:** 12345678901")
    st.markdown(f"**Dirección:** Av. Arequipa 123, Mirafloes, Perú")
    st.markdown(f"**Web:** [www.solucionesgpspro.com](http://www.solucionesgpspro.com)")

with contact_col2:
    st.subheader("Elaborado por")
    st.markdown(f"**Nombre:** Wilder Roy Llacchua Iman")
    st.markdown(f"**Profesión:** Ingeniero de transportes, CIP 319922")
    st.markdown(f"**Teléfono:** +51 969 893 045")
    st.markdown(f"**Correo:** roy.solucionesgpspro@gmail.com")

st.markdown("---")


st.title("Análisis de Rutas de Transporte 🚛")


uploaded_file = st.file_uploader("Carga tu archivo Excel", type=["xlsx"])

if uploaded_file:
    sheet_name = st.text_input("Nombre de la hoja a analizar", value="Hoja1")
    try:
        df = pd.read_excel(uploaded_file, sheet_name=sheet_name)
    except Exception as e:
        st.error(f"Error al leer el archivo o la hoja: {e}")
        st.stop()

    # Procesamiento de datos
    df['Fecha y Hora'] = df['FECHA DE COMUNICACION'].astype(str) + ' ' + df['HORA DE COMUNICACION'].astype(str)
    df['Fecha y Hora'] = pd.to_datetime(df['Fecha y Hora'], errors='coerce')
    df = df.dropna(subset=['Fecha y Hora'])
    df['VELOCIDAD'] = df['VELOCIDAD'].astype(str).str.replace(' km/h', '', regex=False).astype(float)

    if 'RUTA' not in df.columns:
        st.error("El archivo debe tener una columna 'RUTA' con valores como 'Lima-Ica' e 'Ica-Lima'.")
        st.stop()
    consumo_litros_por_hora = 18.0
    costo_por_galon = 17.0

    # --- INICIO DEL CÓDIGO AÑADIDO PARA FILTRO ---
    # Sección para filtrar por rango de tiempo
    with st.expander("Filtro por rango de tiempo ⏳ (Opcional)"):
        col_start, col_end = st.columns(2)
        with col_start:
            start_date = st.date_input("Fecha de inicio", value=None)
            start_time = st.time_input("Hora de inicio", value=None)
        with col_end:
            end_date = st.date_input("Fecha de fin", value=None)
            end_time = st.time_input("Hora de fin", value=None)

    df_filtrado = df.copy()
    
    if start_date and start_time:
        start_datetime = datetime.combine(start_date, start_time)
        df_filtrado = df_filtrado[df_filtrado['Fecha y Hora'] >= start_datetime]
        st.info(f"Filtro de inicio aplicado: desde {start_datetime}")

    if end_date and end_time:
        end_datetime = datetime.combine(end_date, end_time)
        df_filtrado = df_filtrado[df_filtrado['Fecha y Hora'] <= end_datetime]
        st.info(f"Filtro de fin aplicado: hasta {end_datetime}")

    # --- FIN DEL CÓDIGO AÑADIDO PARA FILTRO ---
    
    st.markdown("---")

    # --- NUEVO FILTRO DE RUTA ---
    # Corrección para el error TypeError: '<' not supported
    # Convertir la columna 'RUTA' a tipo string para evitar errores de comparación
    df_filtrado['RUTA'] = df_filtrado['RUTA'].astype(str)
    rutas_disponibles = sorted(df_filtrado['RUTA'].unique().tolist())
    rutas_seleccionadas = st.multiselect(
        "Selecciona las rutas a analizar",
        options=rutas_disponibles,
        default=rutas_disponibles # Por defecto, todas las rutas están seleccionadas
    )

    if not rutas_seleccionadas:
        st.warning("Selecciona al menos una ruta para continuar.")
        st.stop()

    df_filtrado = df_filtrado[df_filtrado['RUTA'].isin(rutas_seleccionadas)]
    # --- FIN DEL NUEVO FILTRO DE RUTA ---

    if df_filtrado.empty:
        st.warning("Advertencia: Después de aplicar los filtros, el DataFrame está vacío. No se puede realizar el análisis.")
        st.stop()

    # --- NUEVA SECCIÓN DE RESUMEN ---
    st.header("Resumen de todas las rutas seleccionadas")
    summary_data = []

    # Se realiza el cálculo para cada ruta para llenar la tabla de resumen
    for ruta, grupo in df_filtrado.groupby('RUTA'):
        if 'DLATITUD' in grupo.columns and 'DLONGITUD' in grupo.columns:
            total_distance = 0.0
            for i in range(1, len(grupo)):
                lat1, lon1 = grupo['DLATITUD'].iloc[i-1], grupo['DLONGITUD'].iloc[i-1]
                lat2, lon2 = grupo['DLATITUD'].iloc[i], grupo['DLONGITUD'].iloc[i]
                
                if not pd.isna(lat1) and not pd.isna(lat2):
                    total_distance += haversine(lat1, lon1, lat2, lon2)
            
            duracion_td = grupo['Fecha y Hora'].iloc[-1] - grupo['Fecha y Hora'].iloc[0]
            duracion_horas = duracion_td.total_seconds() / 3600
            consumo_litros_total = duracion_horas * consumo_litros_por_hora
            costo_total = (consumo_litros_total / 3.78541) * costo_por_galon
            eficiencia_km_litro = total_distance / consumo_litros_total if consumo_litros_total > 0 else 0
            
            summary_data.append({
                'Ruta': ruta,
                'Kilómetros Recorridos (km)': f"{total_distance:.2f}",
                'Costo Total (S/)': f"{costo_total:.2f}",
                'Eficiencia (km/L)': f"{eficiencia_km_litro:.2f}",
                'Duración Total': str(duracion_td).split('.')[0]
            })

    if summary_data:
        summary_df = pd.DataFrame(summary_data)
        st.dataframe(summary_df, hide_index=True)
    else:
        st.info("No hay suficientes datos de coordenadas para generar el resumen.")
    
    st.markdown("---")
    # --- FIN DE LA SECCIÓN DE RESUMEN ---

    # Bucle original para el análisis detallado de cada ruta
    for ruta, grupo in df_filtrado.groupby('RUTA'):
        st.header(f"RUTA: {ruta}")
        inicio_fecha = grupo['Fecha y Hora'].iloc[0]
        fin_fecha = grupo['Fecha y Hora'].iloc[-1]

        # --- CÁLCULO DE LOS KILÓMETROS RECORRIDOS ---
        total_distance = 0.0
        # Revisa si hay datos de latitud/longitud
        if 'DLATITUD' in grupo.columns and 'DLONGITUD' in grupo.columns:
            for i in range(1, len(grupo)):
                lat1, lon1 = grupo['DLATITUD'].iloc[i-1], grupo['DLONGITUD'].iloc[i-1]
                lat2, lon2 = grupo['DLATITUD'].iloc[i], grupo['DLONGITUD'].iloc[i]
                
                if not pd.isna(lat1) and not pd.isna(lat2):
                    total_distance += haversine(lat1, lon1, lat2, lon2)
        # --- FIN DEL CÁLCULO ---
        # --- COLOCA EL CÓDIGO AQUÍ ABAJO ---
        # Realiza los cálculos de consumo y costo.
        duracion_td = fin_fecha - inicio_fecha
        duracion_horas = duracion_td.total_seconds() / 3600
        consumo_litros_total = duracion_horas * consumo_litros_por_hora
        consumo_galones_total = consumo_litros_total / 3.78541
        costo_total = consumo_galones_total * costo_por_galon
        # 1. Eficiencia de Combustible (km/L)
        eficiencia_km_litro = total_distance / consumo_litros_total if consumo_litros_total > 0 else 0

        # 2. Costo por Kilómetro (S/ km)
        costo_por_km = costo_total / total_distance if total_distance > 0 else 0

        # 3. y 4. Análisis de Tiempos y Velocidad en Movimiento
        grupo['time_diff'] = grupo['Fecha y Hora'].diff()
        
        tiempo_en_movimiento = grupo[grupo['VELOCIDAD'] > 0]['time_diff'].sum()
        tiempo_detenido = grupo[grupo['VELOCIDAD'] == 0]['time_diff'].sum()
        
        velocidad_movimiento_promedio = grupo[grupo['VELOCIDAD'] > 0]['VELOCIDAD'].mean()
        
        # --- FIN DE LOS CÁLCULOS ---
        # Muestra los resultados actualizados, incluyendo los kilómetros.
        st.markdown(f"""
        - **Inicio:** {inicio_fecha}
        - **Fin:** {fin_fecha}
        - **Duración Total:** {duracion_td}
        - **Tiempo en Movimiento:** {tiempo_en_movimiento}
        - **Tiempo Detenido:** {tiempo_detenido}
        - **Velocidad promedio (total):** {grupo['VELOCIDAD'].mean():.2f} km/h
        - **Velocidad promedio en movimiento:** {velocidad_movimiento_promedio:.2f} km/h
        
        - **Velocidad máxima:** {grupo['VELOCIDAD'].max():.2f} km/h
        - **Registros:** {len(grupo)}
        - **Kilómetros recorridos:** {total_distance:.2f} km
        ---
        ### Consumo y Costo de Combustible
        - **Eficiencia de combustible:** {eficiencia_km_litro:.2f} km/L
        - **Costo por kilómetro:** S/ {costo_por_km:.2f}
        - **Consumo total (Litros):** {consumo_litros_total:.2f} L
        - **Consumo total (Galones):** {consumo_galones_total:.2f} GL
        - **Costo total de combustible:** S/ {costo_total:.2f}
        """)
        # --- BOTÓN DE DESCARGA DE PDF ---
        pdf_bytes = create_pdf_report(
            ruta, 
            grupo, 
            total_distance, 
            costo_total, 
            eficiencia_km_litro, 
            tiempo_en_movimiento, 
            tiempo_detenido, 
            velocidad_movimiento_promedio
        )
        
        st.download_button(
            label="Descargar Reporte en PDF 📄",
            data=pdf_bytes,
            file_name=f"reporte_{ruta.replace(' ', '_')}.pdf",
            mime="application/pdf"
        )
        st.markdown("---") # Separador para la siguiente ruta
        
        
        # --- GRÁFICO DE VELOCIDAD CON EXCESOS Y COORDENADAS ---
        st.subheader("Velocidad vs. Tiempo")

        # Crear una columna booleana para identificar los puntos de exceso de velocidad
        grupo['Es Exceso'] = grupo['VELOCIDAD'] >= 96

        # Determinar si las columnas necesarias existen
        ubicacion_column_exists = 'UBICACION' in grupo.columns
        coordenadas_columns_exist = 'DLATITUD' in grupo.columns and 'DLONGITUD' in grupo.columns

        hover_data_list = ['Fecha y Hora', 'VELOCIDAD']
        if ubicacion_column_exists:
            hover_data_list.append('UBICACION')
        if coordenadas_columns_exist:
            hover_data_list.extend(['DLATITUD', 'DLONGITUD'])

        # Crear el gráfico de línea con Plotly
        fig = px.line(
            grupo, 
            x='Fecha y Hora', 
            y='VELOCIDAD',
            title=f"Velocidad en la ruta {ruta}",
            labels={'VELOCIDAD': 'Velocidad (km/h)', 'Fecha y Hora': 'Tiempo'},
            color_discrete_sequence=['blue'], # Color base de la línea
            hover_data=hover_data_list
        )
        
        # Añadir una traza para los puntos de exceso de velocidad
        fig.add_scatter(
            x=grupo[grupo['Es Exceso']]['Fecha y Hora'],
            y=grupo[grupo['Es Exceso']]['VELOCIDAD'],
            mode='markers', # Solo marcadores
            name='Exceso de Velocidad',
            marker=dict(
                color='red',
                size=8,  # Tamaño de la bolita roja
                symbol='circle' # Forma de círculo
            ),
        )

        # Añadir la línea de referencia para los 96 km/h
        fig.add_hline(y=96, line_dash="dash", line_color="red", annotation_text="Límite de 96 km/h", annotation_position="bottom right")

        # Personalizar el diseño del gráfico para que sea más legible
        fig.update_layout(
            xaxis_title="Fecha y Hora",
            yaxis_title="Velocidad (km/h)",
            legend_title="Leyenda",
            hovermode="x unified"
        )
        st.plotly_chart(fig, use_container_width=True)
        # --- FIN DEL GRÁFICO DE VELOCIDAD ---

        # --- NUEVA TABLA CON PUNTOS DE EXCESO DE VELOCIDAD ---
        st.subheader("Detalle de Excesos de Velocidad 🚨")

        excesos_df = grupo[grupo['Es Exceso']].copy()
        if not excesos_df.empty and coordenadas_columns_exist:
            # Crear la columna de enlace
            excesos_df['Enlace Google Maps'] = excesos_df.apply(
                lambda row: f"http://maps.google.com/?q={row['DLATITUD']},{row['DLONGITUD']}", axis=1
            )
            
            # Formatear el DataFrame para mostrarlo de forma ordenada
            cols_to_show = ['Fecha y Hora', 'VELOCIDAD']
            if ubicacion_column_exists:
                cols_to_show.append('UBICACION')
            if coordenadas_columns_exist:
                cols_to_show.extend(['DLATITUD', 'DLONGITUD'])
            cols_to_show.append('Enlace Google Maps')

            # Display the DataFrame with a custom URL renderer for the last column
            def make_clickable(val):
                return f'<a href="{val}" target="_blank">Ver en Google Maps</a>'

            # Apply the function to the 'Enlace Google Maps' column
            excesos_df['Enlace Google Maps'] = excesos_df['Enlace Google Maps'].apply(make_clickable)

            # Display the DataFrame
            st.write("Selecciona el punto de interés y haz clic en el enlace para abrir Google Maps.")
            st.markdown(excesos_df[cols_to_show].to_html(escape=False, index=False), unsafe_allow_html=True)
            
        elif not excesos_df.empty:
            st.info("No hay datos de coordenadas para generar enlaces.")
        else:
            st.info("No se registraron excesos de velocidad en esta ruta.")
        # --- FIN DE LA TABLA ---

        # Paradas prolongadas (>=4 min, velocidad 0 y coordenadas iguales)
        grupo = grupo.sort_values('Fecha y Hora')
        grupo['es_parada'] = (grupo['VELOCIDAD'] == 0)
        grupo['coord'] = list(zip(grupo['DLATITUD'].round(5), grupo['DLONGITUD'].round(5)))
        grupo['cambio_parada'] = (grupo['es_parada'] != grupo['es_parada'].shift(1)) | (grupo['coord'] != grupo['coord'].shift(1))
        grupo['id_parada'] = grupo['cambio_parada'].cumsum()

        paradas_info = []
        for parada_id, parada_df in grupo.groupby('id_parada'):
            if parada_df['es_parada'].all() and len(parada_df) > 1:
                duracion = parada_df['Fecha y Hora'].iloc[-1] - parada_df['Fecha y Hora'].iloc[0]
                if duracion >= pd.Timedelta(minutes=4):
                    lat = parada_df['DLATITUD'].iloc[0]
                    lon = parada_df['DLONGITUD'].iloc[0]
                    ubicacion = parada_df['UBICACION'].iloc[0] if 'UBICACION' in parada_df.columns else ''
                    paradas_info.append({
                        "Desde": parada_df['Fecha y Hora'].iloc[0],
                        "Hasta": parada_df['Fecha y Hora'].iloc[-1],
                        "Duración": duracion,
                        "Ubicación": ubicacion,
                        "Latitud": lat,
                        "Longitud": lon
                    })
        if paradas_info:
            st.subheader("Paradas ≥ 4 min")
            st.dataframe(pd.DataFrame(paradas_info))
        else:
            st.info("Sin paradas ≥ 4 min")

        # Mapa
        if not grupo[['DLATITUD', 'DLONGITUD']].isnull().any().any():
            puntos = [[row['DLATITUD'], row['DLONGITUD']] for index, row in grupo.iterrows()]
            color = "green" if "Lima-Ica" in ruta else "red"
            mapa = folium.Map(location=[grupo['DLATITUD'].iloc[0], grupo['DLONGITUD'].iloc[0]], zoom_start=14)
            # --- NUEVO: MARCADORES PARA PARADAS PROLONGADAS ---
            if paradas_info:
                for parada in paradas_info:
                    folium.Marker(
                        location=[parada['Latitud'], parada['Longitud']],
                        popup=f"<b>Parada Prolongada</b><br>Duración: {parada['Duración']}<br>Ubicación: {parada['Ubicación']}",
                        icon=folium.Icon(color='blue', icon='info-sign', prefix='fa')
                    ).add_to(mapa)
            folium.PolyLine(puntos, color=color, weight=2.5, opacity=1, tooltip=f"Sentido: {ruta}").add_to(mapa)
            folium.Marker(
                [grupo['DLATITUD'].iloc[0], grupo['DLONGITUD'].iloc[0]],
                popup=f'Inicio {ruta}<br>{inicio_fecha}',
                icon=folium.Icon(color='green', icon='play', prefix='fa')
            ).add_to(mapa)
            folium.Marker(
                [grupo['DLATITUD'].iloc[-1], grupo['DLONGITUD'].iloc[-1]],
                popup=f'Fin {ruta}<br>{fin_fecha}',
                icon=folium.Icon(color='red', icon='stop', prefix='fa')
            ).add_to(mapa)
            for i in range(1, len(puntos), max(1, len(puntos)//10)):
                folium.RegularPolygonMarker(
                    location=puntos[i],
                    number_of_sides=3,
                    radius=8,
                    color=color,
                    fill_color=color,
                    rotation=0
                ).add_to(mapa)
            st_folium(mapa, width=900, height=500)
        else:
            st.warning("No hay datos completos de latitud/longitud para este tramo.")
