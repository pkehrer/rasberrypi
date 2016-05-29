from rest_framework.decorators import api_view
from rest_framework.response import Response
from subprocess import call


@api_view(http_method_names=['PUT'])
def turn_on_tv(request):
    send_vol_command("tvpower")
    return Response("tv turned on")

@api_view(http_method_names=['PUT'])
def volume_up(request):
    send_vol_command("KEY_VOLUMEUP")
    return Response("volume up")

@api_view(http_method_names=['PUT'])
def volume_down(request):
    send_vol_command("KEY_VOLUMEDOWN")
    return Response("volume down")

@api_view(http_method_names=['PUT'])
def mute(request):
    send_vol_command("KEY_MUTE")
    return Response("muted")

@api_view(http_method_names=['PUT'])
def set_channel(request):
    channel = str(request.data["channel"])
    for n in channel:
        send_command("KEY_" + n)
    return Response("set channel to " + channel)
    

def send_command(command):
    call(["irsend", "SEND_ONCE", "Sasha", command])

def send_vol_command(command):
    call(["irsend", "SEND_ONCE", "SashaVol", command])


