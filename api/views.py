from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Item
from .serializers import ItemSerializer
from .plot import blochSphere
import re
axisGroup = ["X","x","Y","y","Z","z"]

def error_report(error_id,error_reason):
    error_reports = {"error_id":error_id,"error_reason":error_reason}
    return error_reports

def record(circuits):
    optimized_circuit = {"X":0,"Y":0,"Z":0}
    for circuit in circuits:
        optimized_circuit[(circuit["axis"]).upper()] += circuit["amount"]
    optimized_circuit_list = []
    for key in optimized_circuit:
        if optimized_circuit[key] != 0:
            optimized_circuit_list.append({"axis":key,"amount":optimized_circuit[key]})
    result = blochSphere(optimized_circuit_list)
    output_result = {"status":"completed","optimized_circuit":str(optimized_circuit_list),"circuits":str(circuits),"result":result}
    serializer = ItemSerializer(data=output_result)
    if serializer.is_valid():
        serializer.save()
        return serializer.data
    else:
        return error_report(500,"data formatting failed")


@api_view(['GET'])
def getData(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def searchSingleJob(request,job_id):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    for item in serializer.data:
        if item["id"] == job_id:
            return Response(item)
    return Response(error_report(404,"Not found for ID:{}".format(job_id)))

@api_view(['POST'])
def addItem(request):
    userInput = request.data
    if not isinstance(userInput,dict) or "circuit" not in userInput:
        Response(error_report(400,"Invalid input"))
    if  isinstance(userInput['circuit'],list):
        check_circuits = userInput['circuit']
        for check_circuit in check_circuits:
            if isinstance(check_circuit,dict):
                if "axis" in check_circuit and "amount" in check_circuit:
                    axis = check_circuit['axis']
                    amount = check_circuit['amount']
                    if axis in axisGroup and isinstance(amount,int):
                        pass
                    elif axis not in axisGroup:
                        return Response(error_report(400,"all the axis should be X, Y or Z"))
                    else:
                        return Response(error_report(400,"all the amount should be integer"))
                else:
                    return Response(error_report(400,"all the circuit must have key 'axis' and 'amount'"))
            else:
                return Response(error_report(400,"all the element in circuits list should be in json format"))
    else:
        userInputList = userInput['circuit'].split(",")
        circuitsList = []
        for check_circuit in userInputList:
            axis = check_circuit[0]
            try:
                amount = int(check_circuit.split("(")[1].split(")")[0])
            except ValueError:
                return Response(error_report(400,"all the amount should be integer"))
            if axis in axisGroup and isinstance(amount,int):
                circuitsList.append({"axis":axis,"amount":amount})
            elif axis not in axisGroup:
                return Response(error_report(400,"all the axis should be X, Y or Z"))

        return Response(record(circuitsList))
    
    return Response(record(check_circuits))