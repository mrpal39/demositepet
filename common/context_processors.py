from  pet.models import *
def us_pet(request):
    return {"us_pet": Bread.objects.all(),
            "pet_objects":Pet.objects.all(),
            "pet_Cat":Category.objects.all(),

            }
