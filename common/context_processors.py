from  pet.models import Bread, Pet

def us_pet(request):
    return {"us_pet": Bread.objects.all(),
            "pet_objects":Pet.objects.all(),
            }
