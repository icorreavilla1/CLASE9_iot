import paho.mqtt.client as paho
import time
import streamlit as st
import json

values = 0.0
act1 = "OFF"

def on_publish(client, userdata, result):  # create function for callback
    print("¡El dato ha sido publicado! 🎉\n")
    pass

def on_message(client, userdata, message):
    global message_received
    time.sleep(2)
    message_received = str(message.payload.decode("utf-8"))
    st.markdown(f"<h3 style='color: green;'>{message_received}</h3>", unsafe_allow_html=True)

broker = "broker.mqttdashboard.com"
port = 1883
client1 = paho.Client("GIT-HUB")
client1.on_message = on_message

# Título de la aplicación
st.markdown("<h1 style='text-align: center; color: orange;'>🌟 MQTT Control 🌟</h1>", unsafe_allow_html=True)

# Botones para encender/apagar
if st.button('💡 Encender'):
    act1 = "ON"
    client1 = paho.Client("icorreava")
    client1.on_publish = on_publish
    client1.connect(broker, port)
    message = json.dumps({"Act1": act1})
    ret = client1.publish("datosicov1", message)
    st.markdown("<h3 style='color: blue;'>¡La luz está encendida! 🔆</h3>", unsafe_allow_html=True)

if st.button('🔌 Apagar'):
    act1 = "OFF"
    client1 = paho.Client("icorreava")
    client1.on_publish = on_publish
    client1.connect(broker, port)
    message = json.dumps({"Act1": act1})
    ret = client1.publish("datosicov1", message)
    st.markdown("<h3 style='color: red;'>¡La luz está apagada! 🌑</h3>", unsafe_allow_html=True)

# Control deslizante para valores
values = st.slider('🔢 Selecciona el rango de valores', 0.0, 100.0)
st.markdown(f"<h3 style='color: purple;'>Valores: {values}</h3>", unsafe_allow_html=True)

# Botón para enviar valor analógico
if st.button('📤 Enviar valor analógico'):
    client1 = paho.Client("icorreava")
    client1.on_publish = on_publish
    client1.connect(broker, port)
    message = json.dumps({"Analog": float(values)})
    ret = client1.publish("datosicov2", message)
    st.markdown("<h3 style='color: green;'>¡Valor enviado exitosamente! ✅</h3>", unsafe_allow_html=True)





