from django.shortcuts import render, redirect
from . models import AddCustomer, AddRoom, RoomBooking, LoundryBooking, Cleaning


def home(request):
    return render(request, 'home.html')


def after(request):
    return render(request, 'main.html')


def add(request):
    return render(request, 'AddCustomer.html')


def add_submission(request):
    print('Hello form is submitted')
    first = request.POST["first"]
    sur = request.POST["sur"]
    last = request.POST["last"]
    email = request.POST["email"]
    phone = request.POST["phone"]
    gender = request.POST["gender"]
    date = request.POST["date"]
    address = request.POST["address"]

    add_info = AddCustomer(first=first, sur=sur, last=last, email=email, phone=phone, gender=gender, date=date,
                           address=address)
    add_info.save()
    return redirect('main')


def customer_report(request):
    context = {
        'shows': AddCustomer.objects.all()
    }
    return render(request, 'add_customer_report.html', context)


def add_room(request):
    return render(request, 'add_room.html')


def add_room_submission(request):
    r_number = request.POST["r_number"]
    r_cost = request.POST["r_cost"]
    r_type = request.POST["r_type"]
    r_description = request.POST["r_description"]
    date = request.POST["date"]

    add_room_info = AddRoom(r_number=r_number, r_cost=r_cost, r_type=r_type, r_description=r_description, date=date)
    add_room_info.save()
    return redirect('main')


def add_room_report(request):
    context = {
        'shows': AddRoom.objects.all()
    }
    return render(request, 'add_room_report.html', context)


def add_room_booking(request):
    return render(request, 'add_room_booking.html')


def add_room_booking_submission(request):
    name = request.POST["name"]
    r_number = request.POST["r_number"]
    phone = request.POST["phone"]
    from_date = request.POST["from_date"]
    to_date = request.POST["to_date"]
    amount = request.POST["amount"]
    description = request.POST["description"]

    add_room_booking_info = RoomBooking(name=name, r_number=r_number, phone=phone, from_date=from_date, to_date=to_date,
                                        amount=amount,  description=description)
    add_room_booking_info.save()
    return redirect('main')


def add_room_booking_report(request):
    context = {
        'shows': RoomBooking.objects.all()
    }
    return render(request, 'add_room_booking_report.html', context)


def add_room_billing(request):
    return render(request, 'add_room_billing.html')


def room_billing_submission(request):
    r_number = request.POST["r_number"]
    r_cost = request.POST["r_cost"]
    r_type = request.POST["r_type"]
    r_description = request.POST["r_description"]
    date = request.POST["date"]

    add_room_billing_info = AddRoom(r_number=r_number, r_cost=r_cost, r_type=r_type, r_description=r_description, date=date)
    add_room_billing_info.save()
    return redirect('main')


def room_billing_report(request):
    context = {
        'show': AddRoom.objects.all()
    }
    return render(request, 'room_billing_report.html', context)


def add_cleaning(request):
    return render(request, 'add_cleaning.html')


def add_cleaning_submission(request):
    r_number = request.POST["r_number"]
    r_description = request.POST["r_description"]
    date = request.POST["date"]

    add_cleaning_info = Cleaning(r_number=r_number, r_description=r_description, date=date)
    add_cleaning_info.save()
    return redirect('main')


def add_cleaning_report(request):
    context = {
        'shows': Cleaning.objects.all
    }
    return render(request, 'add_cleaning_report.html', context)


def add_loundry(request):
    return render(request, 'add_loundry.html')


def loundry_submission(request):
    r_number = request.POST["r_number"]
    date = request.POST["date"]
    r_cost = request.POST["r_cost"]
    r_description = request.POST["r_description"]

    add_loundry_info = LoundryBooking(r_number=r_number, date=date, r_cost=r_cost, r_description=r_description)
    add_loundry_info.save()
    return redirect('main')


def add_loundry_report(request):
    context = {
        'show': LoundryBooking.objects.all
    }
    return render(request, 'add_loundry_report.html', context)










