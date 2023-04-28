from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Sum
from .models import *


import time

start = time.time()

end = time.time()

############################################################################################################

@api_view(['GET'])
def get_veh_org(request):
    start = time.time()
    org_obj = Organisation.objects.all()
    end = time.time()
    print(end - start)
    total_vehicle_record_obj = Organisation.objects.aggregate(total_vehicle_processed =Sum("vehicle_processed"),total_wanted_matches_identified =  Sum("wanted_matches_identified"),total_ticketed_matches_identified = Sum("ticketed_matches_identified"),total_percentage_ticketed_matches = Sum("percentage_ticketed_matches"), total_percentage_operations_processed = Sum("percentage_operations_processed"))
    if org_obj:
        id = [data.id for data in org_obj]
        organistaion_name = [data.name for data in org_obj]
        vehicle_processed = [data.vehicle_processed for data in org_obj]
        wanted_matches_identified = [data.wanted_matches_identified for data in org_obj]
        ticketed_matches_identified = [data.ticketed_matches_identified for data in org_obj]
        percentage_ticketed_matches = [data.percentage_ticketed_matches for data in org_obj]
        percentage_operations_processed = [data.percentage_operations_processed for data in org_obj]

        data = [{
            "Organisation_id": id,
            "wanted_matches_identified": wanted_matches_identified,
            "ticketed_matches_identified": ticketed_matches_identified,
            "percentage_ticketed_matches": percentage_ticketed_matches,
            "percentage_operations_processed": percentage_operations_processed,
            "x": organistaion_name,
            "y": vehicle_processed,
            "total_vehicle_record":total_vehicle_record_obj
        }]
    else:
        data = []
    return Response(data)

##########################################################################################################

# @api_view(['GET'])
# def get_vehicles_org_sub(request, id):
#     sub_obj = SubOrganisation.objects.filter(org_name__id=id).all()
#     if sub_obj:
#         id = [ data.id for data in sub_obj]
#         sub_organistaion_name = [data.sub_name for data in sub_obj]
#         sub_organistaion_vehicle_processed = [data.vehicle_processed for data in sub_obj]
#         wanted_matches_identified = [data.wanted_matches_identified for data in sub_obj]
#         ticketed_matches_identified = [data.ticketed_matches_identified for data in sub_obj]
#         percentage_ticketed_matches = [data.percentage_ticketed_matches for data in sub_obj]
#         percentage_operations_processed = [data.percentage_operations_processed for data in sub_obj]

#         data = [{
#             "sub_organisation_id": id,
#             "wanted_matches_identified": wanted_matches_identified,
#             "ticketed_matches_identified": ticketed_matches_identified,
#             "percentage_ticketed_matches": percentage_ticketed_matches,
#             "percentage_operations_processed": percentage_operations_processed,
#             "x": sub_organistaion_name,
#             "y": sub_organistaion_vehicle_processed
#         }]
#     else:
#         data = []
#     return Response(data)

############################################################################################################

@api_view(['GET'])
def get_vehicles_sub_data(request, id):
    sub_data_obj = SubOrganisationData.objects.filter(
        sub_org_name__id=id).all()
    if sub_data_obj:
        org_list = []
        for data in sub_data_obj:
            response  = {}
            response["id"] = data.id
            response["org_sub_cat_name"] = data.sub_name
            response["vehicle_processed"] = data.vehicle_processed
            response["wanted_matches_identified"] = data.wanted_matches_identified
            response["ticketed_matches_identified"] = data.ticketed_matches_identified
            response["percentage_ticketed_matches"] = data.percentage_ticketed_matches
            response["percentage_operations_processed"] = data.percentage_operations_processed
            org_list.append(response)
    else:
        org_list = []
    return Response(org_list)


#######################################################################################################
#######################################################################################################


@api_view(['GET'])
def fetch_veh_org(request):
   
    org_obj = Organisation.objects.all()
    
    total_vehicle_record_obj = Organisation.objects.aggregate(total_vehicle_processed =Sum("vehicle_processed"),total_wanted_matches_identified =  Sum("wanted_matches_identified"),total_ticketed_matches_identified = Sum("ticketed_matches_identified"),total_percentage_ticketed_matches = Sum("percentage_ticketed_matches"), total_percentage_operations_processed = Sum("percentage_operations_processed"))
    if org_obj:
        org_list = []
        for data in org_obj:
            response  = {}
            response["id"] = data.id
            response["organistaion_name"] = data.name
            response["vehicle_processed"] = data.vehicle_processed
            response["wanted_matches_identified"] = data.wanted_matches_identified
            response["ticketed_matches_identified"] = data.ticketed_matches_identified
            response["percentage_ticketed_matches"] = data.percentage_ticketed_matches
            response["percentage_operations_processed"] = data.percentage_operations_processed
            org_list.append(response)
        total_vehicle_data = {}
        total_vehicle_data["total_vehicle_record"] = total_vehicle_record_obj
        org_list.append(total_vehicle_data)
    else:
        org_list = []
    return Response(org_list)

@api_view(['GET'])
def get_vehicles_org_sub(request, id):
    start = time.time()
    sub_obj = SubOrganisation.objects.filter(org_name__id=id).all()
    end = time.time()
    print(end - start)
    total_sub_vehicle_record_obj = SubOrganisation.objects.filter(org_name__id = id).aggregate(total_vehicle_processed =Sum("vehicle_processed"),total_wanted_matches_identified =  Sum("wanted_matches_identified"),total_ticketed_matches_identified = Sum("ticketed_matches_identified"),total_percentage_ticketed_matches = Sum("percentage_ticketed_matches"), total_percentage_operations_processed = Sum("percentage_operations_processed"))
    if sub_obj:
        org_list = []
        for data in sub_obj:
            response  = {}
            response["id"] = data.id
            response["sub_organistaion_category"] = data.sub_name
            response["vehicle_processed"] = data.vehicle_processed
            response["wanted_matches_identified"] = data.wanted_matches_identified
            response["ticketed_matches_identified"] = data.ticketed_matches_identified
            response["percentage_ticketed_matches"] = data.percentage_ticketed_matches
            response["percentage_operations_processed"] = data.percentage_operations_processed
            org_list.append(response)
        total_sub_vehicle_data = {}
        total_sub_vehicle_data["total_vehicle_record"] = total_sub_vehicle_record_obj
        org_list.append(total_sub_vehicle_data)
    else:
        org_list = []
    return Response(org_list)

