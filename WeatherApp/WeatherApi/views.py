from django.shortcuts import render

# Create your views here.
def index(request):

    # appoint_list = Appointment.objects.filter(
    #         description__icontains = "D"
    #     )
    # appt_dict = {
    #     'appointment_records': appoint_list,
    # }

    return render(request,'WeatherApi/index.html')


### API function ####